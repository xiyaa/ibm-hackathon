"""
FastAPI application for DevOnboard AI backend.
Provides REST API endpoints for repository analysis and chat functionality.
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List, Optional
from datetime import datetime
import asyncio

from models import (
    AnalyzeRequest, AnalyzeResponse, ChatRequest, ChatResponse,
    ChatHistoryResponse, ChatMessage, FileTreeResponse,
    FileContentRequest, FileContentResponse, ErrorResponse,
    CodeReference, CachedAnalysis, ChatSession
)
from analyzer import CodebaseAnalyzer
from watsonx_client import WatsonXClient
from config import settings
from utils import (
    get_logger, generate_session_id, hash_repo_url,
    calculate_expiry_time, is_expired, extract_code_snippet,
    sanitize_path
)

logger = get_logger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="DevOnboard AI API",
    description="AI-powered developer onboarding assistant",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_cors_origins_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
analyzer = CodebaseAnalyzer()
watsonx_client = WatsonXClient()

# In-memory cache (temporary, will be replaced with Cloudant)
analysis_cache: Dict[str, CachedAnalysis] = {}
chat_sessions: Dict[str, ChatSession] = {}
repo_paths: Dict[str, str] = {}  # session_id -> repo_path mapping
session_to_cache_key: Dict[str, str] = {}  # session_id -> cache_key mapping for recovery


@app.on_event("startup")
async def startup_event():
    """Initialize application on startup."""
    logger.info("Starting DevOnboard AI API")
    settings.ensure_repo_dir_exists()


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("Shutting down DevOnboard AI API")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "DevOnboard AI API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}


@app.post("/api/analyze", response_model=AnalyzeResponse)
async def analyze_repository(request: AnalyzeRequest):
    """
    Analyze a GitHub repository and generate onboarding guide.
    
    Args:
        request: Analysis request with repo URL and options
        
    Returns:
        Complete analysis results
    """
    try:
        repo_url = str(request.repo_url)
        branch = request.branch
        force_refresh = request.force_refresh
        
        logger.info(f"Received analysis request for {repo_url} (branch: {branch})")
        
        # Check cache unless force refresh
        cache_key = hash_repo_url(repo_url, branch)
        
        if not force_refresh and cache_key in analysis_cache:
            cached = analysis_cache[cache_key]
            
            # Check if cache is still valid
            if not is_expired(cached.expires_at):
                logger.info(f"Returning cached analysis for {repo_url}")
                
                # Create new session for cached result
                session_id = generate_session_id()
                
                # Store repo path and cache key for this session
                repo_paths[session_id] = settings.get_repo_path(cache_key)
                session_to_cache_key[session_id] = cache_key
                
                # Initialize chat session if not exists
                if session_id not in chat_sessions:
                    chat_sessions[session_id] = ChatSession(
                        session_id=session_id,
                        repo_url=repo_url,
                        messages=[],
                        created_at=datetime.utcnow(),
                        last_activity=datetime.utcnow()
                    )
                
                return AnalyzeResponse(
                    session_id=session_id,
                    repository=cached.repository,
                    analysis=cached.analysis,
                    cached=True,
                    analyzed_at=cached.created_at
                )
        
        # Perform analysis
        result = await analyzer.analyze_repository(repo_url, branch)
        
        # Cache the result
        analysis_cache[cache_key] = CachedAnalysis(
            repo_url=repo_url,
            branch=branch,
            analysis=result.analysis,
            repository=result.repository,
            created_at=result.analyzed_at,
            expires_at=calculate_expiry_time(settings.cache_ttl_days)
        )
        
        # Store repo path and cache key for this session
        repo_paths[result.session_id] = settings.get_repo_path(cache_key)
        session_to_cache_key[result.session_id] = cache_key
        
        # Initialize chat session
        chat_sessions[result.session_id] = ChatSession(
            session_id=result.session_id,
            repo_url=repo_url,
            messages=[],
            created_at=datetime.utcnow(),
            last_activity=datetime.utcnow()
        )
        
        logger.info(f"Analysis complete for {repo_url}, session: {result.session_id}")
        return result
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error analyzing repository: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a message and get AI-powered response about the codebase.
    
    Args:
        request: Chat request with session ID and message
        
    Returns:
        AI-generated response with code references
    """
    try:
        session_id = request.session_id
        user_message = request.message
        
        # Validate session - try to recover if not found
        if session_id not in chat_sessions:
            logger.warning(f"Session not found in chat_sessions: {session_id}")
            
            # Try to recover session from cache
            if session_id in session_to_cache_key:
                cache_key = session_to_cache_key[session_id]
                if cache_key in analysis_cache:
                    cached = analysis_cache[cache_key]
                    logger.info(f"Recovering session {session_id} from cache")
                    
                    # Recreate chat session
                    chat_sessions[session_id] = ChatSession(
                        session_id=session_id,
                        repo_url=cached.repo_url,
                        messages=[],
                        created_at=datetime.utcnow(),
                        last_activity=datetime.utcnow()
                    )
                    
                    # Ensure repo_path is set
                    if session_id not in repo_paths:
                        repo_paths[session_id] = settings.get_repo_path(cache_key)
                else:
                    logger.error(f"Cache key {cache_key} not found in analysis_cache")
                    raise HTTPException(
                        status_code=404,
                        detail=f"Session expired or not found. Please analyze the repository again. Session ID: {session_id}"
                    )
            else:
                logger.error(f"Session {session_id} not found in session_to_cache_key")
                logger.debug(f"Available sessions: {list(chat_sessions.keys())}")
                logger.debug(f"Total sessions in memory: {len(chat_sessions)}")
                raise HTTPException(
                    status_code=404,
                    detail=f"Session not found. Please analyze a repository first to create a session. Session ID: {session_id}"
                )
        
        session = chat_sessions[session_id]
        
        # Get repository context - try to find the cached analysis
        # First, try to find the cache key by iterating through cache
        cached = None
        cache_key = None
        for key, value in analysis_cache.items():
            if value.repo_url == session.repo_url:
                cached = value
                cache_key = key
                break
        
        if not cached:
            logger.error(f"Repository analysis not found for session {session_id}")
            logger.debug(f"Session repo_url: {session.repo_url}")
            logger.debug(f"Available cache keys: {list(analysis_cache.keys())}")
            raise HTTPException(status_code=404, detail="Repository analysis not found")
        repository_overview = cached.analysis.overview[:2000]  # Limit context size
        
        # Build file context if provided
        file_context = None
        if request.context:
            repo_path = repo_paths.get(session_id)
            if repo_path:
                try:
                    file_path = sanitize_path(request.context.file_path)
                    content, language, lines = analyzer.get_file_content(repo_path, file_path)
                    
                    # Extract specific line range if provided
                    if request.context.line_range and len(request.context.line_range) == 2:
                        start, end = request.context.line_range
                        snippet = extract_code_snippet(content, start, end)
                        file_context = f"File: {file_path}\nLines {start}-{end}:\n```{language or ''}\n{snippet}\n```"
                    else:
                        # Use first 50 lines as context
                        snippet = extract_code_snippet(content, 1, 50)
                        file_context = f"File: {file_path}\n```{language or ''}\n{snippet}\n```"
                except Exception as e:
                    logger.warning(f"Could not load file context: {str(e)}")
        
        # Prepare chat history
        chat_history = [
            {"role": msg.role, "content": msg.content}
            for msg in session.messages[-5:]  # Last 5 messages
        ]
        
        # Generate response
        logger.info(f"Generating chat response for session {session_id}")
        response_text = watsonx_client.generate_chat_response(
            repository_overview=repository_overview,
            file_context=file_context,
            chat_history=chat_history,
            user_message=user_message
        )
        
        # Extract code references from response (simplified)
        references = []
        # TODO: Implement proper code reference extraction
        
        # Create response
        timestamp = datetime.utcnow()
        response = ChatResponse(
            response=response_text,
            references=references,
            timestamp=timestamp
        )
        
        # Update chat history
        session.messages.append(ChatMessage(
            role="user",
            content=user_message,
            references=None,
            timestamp=timestamp
        ))
        session.messages.append(ChatMessage(
            role="assistant",
            content=response_text,
            references=references if references else None,
            timestamp=timestamp
        ))
        session.last_activity = timestamp
        
        logger.info(f"Chat response generated for session {session_id}")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating chat response: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Chat failed: {str(e)}")


@app.get("/api/chat/history/{session_id}", response_model=ChatHistoryResponse)
async def get_chat_history(session_id: str):
    """
    Retrieve chat history for a session.
    
    Args:
        session_id: Session identifier
        
    Returns:
        Chat message history
    """
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = chat_sessions[session_id]
    
    return ChatHistoryResponse(
        session_id=session_id,
        messages=session.messages
    )


@app.get("/api/files/{session_id}", response_model=FileTreeResponse)
async def get_file_tree(session_id: str):
    """
    Get file tree for analyzed repository.
    
    Args:
        session_id: Session identifier
        
    Returns:
        Repository file tree
    """
    # Validate session - try to recover if not found
    if session_id not in chat_sessions:
        logger.warning(f"Session not found in chat_sessions: {session_id}")
        
        # Try to recover session from cache
        if session_id in session_to_cache_key:
            cache_key = session_to_cache_key[session_id]
            if cache_key in analysis_cache:
                cached = analysis_cache[cache_key]
                logger.info(f"Recovering session {session_id} from cache for file tree")
                
                # Recreate chat session
                chat_sessions[session_id] = ChatSession(
                    session_id=session_id,
                    repo_url=cached.repo_url,
                    messages=[],
                    created_at=datetime.utcnow(),
                    last_activity=datetime.utcnow()
                )
                
                # Ensure repo_path is set
                if session_id not in repo_paths:
                    repo_paths[session_id] = settings.get_repo_path(cache_key)
            else:
                logger.error(f"Cache key {cache_key} not found in analysis_cache")
                raise HTTPException(
                    status_code=404,
                    detail=f"Session expired or not found. Please analyze the repository again. Session ID: {session_id}"
                )
        else:
            logger.error(f"Session {session_id} not found in session_to_cache_key")
            logger.debug(f"Available sessions: {list(chat_sessions.keys())}")
            logger.debug(f"Total sessions in memory: {len(chat_sessions)}")
            raise HTTPException(
                status_code=404,
                detail=f"Session not found. Please analyze a repository first to create a session. Session ID: {session_id}"
            )
    
    session = chat_sessions[session_id]
    
    # Find the cached analysis for this repository
    cached = None
    for key, value in analysis_cache.items():
        if value.repo_url == session.repo_url:
            cached = value
            break
    
    if not cached:
        raise HTTPException(status_code=404, detail="Repository analysis not found")
    
    return FileTreeResponse(
        session_id=session_id,
        file_tree=cached.analysis.file_structure
    )


@app.get("/api/files/{session_id}/content", response_model=FileContentResponse)
async def get_file_content(
    session_id: str,
    path: str = Query(..., description="File path relative to repository root")
):
    """
    Get content of a specific file.
    
    Args:
        session_id: Session identifier
        path: File path
        
    Returns:
        File content and metadata
    """
    if session_id not in repo_paths:
        logger.error(f"Session not found in repo_paths: {session_id}")
        logger.debug(f"Available repo_paths: {list(repo_paths.keys())}")
        raise HTTPException(
            status_code=404,
            detail=f"Session not found. Please analyze a repository first to create a session. Session ID: {session_id}"
        )
    
    repo_path = repo_paths[session_id]
    safe_path = sanitize_path(path)
    
    try:
        content, language, lines = analyzer.get_file_content(repo_path, safe_path)
        
        return FileContentResponse(
            path=safe_path,
            content=content,
            language=language,
            lines=lines
        )
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"File not found: {path}")
    except Exception as e:
        logger.error(f"Error reading file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to read file: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    import multiprocessing
    
    # Fix for Windows multiprocessing issue
    multiprocessing.freeze_support()
    
    uvicorn.run(
        app,  # Pass app object directly instead of string to avoid reimport issues
        host=settings.api_host,
        port=settings.api_port,
        reload=False,  # Disable reload on Windows to prevent multiprocessing issues
        log_level=settings.log_level.lower()
    )

# Made with Bob
