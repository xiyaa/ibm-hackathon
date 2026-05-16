"""
Pydantic models for request/response validation.
Defines all data structures used in the DevOnboard AI API.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl


# ============================================================================
# Repository Analysis Models
# ============================================================================

class AnalyzeRequest(BaseModel):
    """Request model for repository analysis."""
    repo_url: HttpUrl = Field(..., description="GitHub repository URL")
    branch: str = Field(default="main", description="Branch to analyze")
    force_refresh: bool = Field(default=False, description="Force re-analysis ignoring cache")


class RepositoryInfo(BaseModel):
    """Repository metadata."""
    name: str = Field(..., description="Repository name")
    owner: str = Field(..., description="Repository owner")
    url: str = Field(..., description="Repository URL")
    branch: str = Field(..., description="Analyzed branch")
    last_commit: Optional[str] = Field(None, description="Last commit hash")


class FileNode(BaseModel):
    """Represents a file or directory in the repository structure."""
    name: str = Field(..., description="File or directory name")
    path: str = Field(..., description="Full path relative to repository root")
    type: str = Field(..., description="'file' or 'directory'")
    size: Optional[int] = Field(None, description="File size in bytes")
    language: Optional[str] = Field(None, description="Programming language")
    children: Optional[List['FileNode']] = Field(None, description="Child nodes for directories")


class KeyFile(BaseModel):
    """Information about a key file in the repository."""
    path: str = Field(..., description="File path")
    type: str = Field(..., description="File type (e.g., 'readme', 'config', 'entry_point')")
    language: Optional[str] = Field(None, description="Programming language")
    lines: int = Field(..., description="Number of lines")
    snippet: Optional[str] = Field(None, description="Code snippet or excerpt")


class DependencyInfo(BaseModel):
    """Dependency information extracted from package files."""
    file: str = Field(..., description="Package file (e.g., requirements.txt, package.json)")
    dependencies: Dict[str, str] = Field(..., description="Dependency name to version mapping")


class CodeAnalysis(BaseModel):
    """Comprehensive code analysis results."""
    overview: str = Field(..., description="AI-generated project overview")
    tech_stack: List[str] = Field(..., description="Technologies and frameworks used")
    file_structure: FileNode = Field(..., description="Repository file tree")
    key_files: List[KeyFile] = Field(..., description="Important files identified")
    dependencies: List[DependencyInfo] = Field(..., description="Project dependencies")
    setup_instructions: str = Field(..., description="Setup and installation guide")
    architecture_insights: str = Field(..., description="Architecture and design patterns")
    architecture_diagram: Optional[str] = Field(None, description="Mermaid diagram of architecture")
    flow_diagram: Optional[str] = Field(None, description="Mermaid diagram of application flow")
    file_structure_diagram: Optional[str] = Field(None, description="Mermaid diagram of file/folder structure")


class AnalyzeResponse(BaseModel):
    """Response model for repository analysis."""
    session_id: str = Field(..., description="Unique session identifier")
    repository: RepositoryInfo = Field(..., description="Repository metadata")
    analysis: CodeAnalysis = Field(..., description="Analysis results")
    cached: bool = Field(..., description="Whether results were retrieved from cache")
    analyzed_at: datetime = Field(..., description="Analysis timestamp")


# ============================================================================
# Chat Models
# ============================================================================

class FileContext(BaseModel):
    """Context about a specific file for chat."""
    file_path: str = Field(..., description="Path to the file")
    line_range: Optional[List[int]] = Field(None, description="[start_line, end_line] range")


class ChatRequest(BaseModel):
    """Request model for chat interaction."""
    session_id: str = Field(..., description="Session identifier from analysis")
    message: str = Field(..., description="User's question or message")
    context: Optional[FileContext] = Field(None, description="Optional file context")


class CodeReference(BaseModel):
    """Reference to specific code in the repository."""
    file: str = Field(..., description="File path")
    lines: List[int] = Field(..., description="Referenced line numbers")
    snippet: str = Field(..., description="Code snippet")


class ChatMessage(BaseModel):
    """A single chat message."""
    role: str = Field(..., description="'user' or 'assistant'")
    content: str = Field(..., description="Message content")
    references: Optional[List[CodeReference]] = Field(None, description="Code references in response")
    timestamp: datetime = Field(..., description="Message timestamp")


class ChatResponse(BaseModel):
    """Response model for chat interaction."""
    response: str = Field(..., description="AI-generated response")
    references: List[CodeReference] = Field(default_factory=list, description="Code references")
    timestamp: datetime = Field(..., description="Response timestamp")


class ChatHistoryResponse(BaseModel):
    """Response model for chat history retrieval."""
    session_id: str = Field(..., description="Session identifier")
    messages: List[ChatMessage] = Field(..., description="Chat message history")


# ============================================================================
# File Operations Models
# ============================================================================

class FileTreeResponse(BaseModel):
    """Response model for file tree retrieval."""
    session_id: str = Field(..., description="Session identifier")
    file_tree: FileNode = Field(..., description="Repository file tree")


class FileContentRequest(BaseModel):
    """Request model for file content retrieval."""
    path: str = Field(..., description="File path relative to repository root")


class FileContentResponse(BaseModel):
    """Response model for file content retrieval."""
    path: str = Field(..., description="File path")
    content: str = Field(..., description="File content")
    language: Optional[str] = Field(None, description="Programming language")
    lines: int = Field(..., description="Number of lines")


# ============================================================================
# Error Models
# ============================================================================

class ErrorResponse(BaseModel):
    """Standard error response."""
    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Error message")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")


# ============================================================================
# Cache Models (for internal use)
# ============================================================================

class CachedAnalysis(BaseModel):
    """Cached analysis data structure."""
    repo_url: str
    branch: str
    analysis: CodeAnalysis
    repository: RepositoryInfo
    created_at: datetime
    expires_at: datetime


class ChatSession(BaseModel):
    """Chat session data structure."""
    session_id: str
    repo_url: str
    messages: List[ChatMessage]
    created_at: datetime
    last_activity: datetime


# Update forward references for recursive models (Pydantic v1)
FileNode.update_forward_refs()

# Made with Bob
