"""
IBM watsonx.ai client for code analysis and chat functionality.
Handles interactions with the Granite model for generating insights.
"""

from typing import List, Dict, Any, Optional
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

from config import settings
from utils import get_logger

logger = get_logger(__name__)


class WatsonXClient:
    """Client for interacting with IBM watsonx.ai Granite models."""
    
    def __init__(self):
        """Initialize the watsonx.ai client."""
        # Validate required settings
        if not settings.watsonx_api_key:
            raise ValueError("WATSONX_API_KEY is not set in environment variables")
        if not settings.watsonx_project_id:
            raise ValueError("WATSONX_PROJECT_ID is not set in environment variables")
        
        # Initialize credentials dictionary
        self.credentials = {
            "url": settings.watsonx_url,
            "apikey": settings.watsonx_api_key
        }
        
        self.model_id = settings.watsonx_model_id
        self.project_id = settings.watsonx_project_id
        
        # Model parameters
        self.parameters = {
            GenParams.MAX_NEW_TOKENS: settings.max_new_tokens,
            GenParams.TEMPERATURE: settings.temperature,
            GenParams.TOP_P: settings.top_p,
            GenParams.TOP_K: settings.top_k,
            GenParams.REPETITION_PENALTY: settings.repetition_penalty,
        }
        
        logger.info(f"Initialized WatsonX client with model: {self.model_id}")
        logger.info(f"Using project ID: {self.project_id}")
        logger.info(f"API URL: {settings.watsonx_url}")
    
    def _create_model(self) -> Model:
        """Create a model instance for inference."""
        try:
            model = Model(
                model_id=self.model_id,
                params=self.parameters,
                credentials=self.credentials,
                project_id=self.project_id
            )
            logger.debug(f"Model created successfully with ID: {self.model_id}")
            return model
        except Exception as e:
            logger.error(f"Error creating model: {str(e)}")
            raise RuntimeError(f"Failed to initialize watsonx.ai model: {str(e)}")
    
    def generate_repository_analysis(
        self,
        repo_name: str,
        file_count: int,
        languages: List[str],
        file_tree: str,
        key_files_content: str,
        dependencies: str
    ) -> str:
        """
        Generate comprehensive repository analysis using Granite model.
        
        Args:
            repo_name: Repository name
            file_count: Number of files analyzed
            languages: List of programming languages
            file_tree: String representation of file structure
            key_files_content: Content of key files
            dependencies: Dependency information
            
        Returns:
            AI-generated analysis in markdown format
        """
        prompt = f"""You are an expert software architect analyzing a codebase for developer onboarding.

Repository: {repo_name}
Files analyzed: {file_count}
Primary languages: {', '.join(languages)}

File structure:
{file_tree}

Key files content:
{key_files_content}

Dependencies:
{dependencies}

Generate a comprehensive onboarding guide including:
1. Project overview and purpose
2. Technology stack explanation
3. Architecture overview
4. Setup instructions
5. Key components and their interactions
6. Development workflow
7. Important files and their purposes

Format the response in markdown with clear sections and code examples where appropriate."""

        try:
            logger.debug(f"Creating model for repository analysis...")
            model = self._create_model()
            
            logger.debug(f"Sending prompt to watsonx.ai (length: {len(prompt)} chars)")
            response = model.generate_text(prompt=prompt)
            
            logger.info(f"Generated repository analysis for {repo_name}")
            logger.debug(f"Response type: {type(response)}")
            
            # Handle different response types from watsonx.ai
            if isinstance(response, dict):
                logger.debug(f"Response keys: {response.keys()}")
                # Response is a dictionary with results
                if 'results' in response and len(response['results']) > 0:
                    return response['results'][0].get('generated_text', str(response))
                return str(response)
            elif isinstance(response, str):
                return response
            else:
                # Handle list or other types
                logger.debug(f"Converting response to string: {type(response)}")
                return str(response)
        except Exception as e:
            logger.error(f"Error generating repository analysis: {str(e)}")
            logger.error(f"Error type: {type(e).__name__}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            raise RuntimeError(f"Failed to generate analysis: {str(e)}")
    
    def generate_chat_response(
        self,
        repository_overview: str,
        file_context: Optional[str],
        chat_history: List[Dict[str, str]],
        user_message: str
    ) -> str:
        """
        Generate a chat response about the codebase.
        
        Args:
            repository_overview: Summary of the repository
            file_context: Optional context about specific files
            chat_history: Previous chat messages
            user_message: Current user question
            
        Returns:
            AI-generated response
        """
        # Build chat history string
        history_str = ""
        for msg in chat_history[-5:]:  # Last 5 messages for context
            role = msg.get("role", "user")
            content = msg.get("content", "")
            history_str += f"{role.capitalize()}: {content}\n\n"
        
        # Build file context string
        context_str = ""
        if file_context:
            context_str = f"\nCurrent file context:\n{file_context}\n"
        
        prompt = f"""You are a helpful AI assistant helping a developer understand a codebase.

Repository context:
{repository_overview}
{context_str}

Chat history:
{history_str}

User question: {user_message}

Provide a clear, concise answer. If referencing specific code, include file paths and line numbers. Format code snippets with proper markdown syntax."""

        try:
            model = self._create_model()
            response = model.generate_text(prompt=prompt)
            logger.info("Generated chat response")
            
            # Handle different response types from watsonx.ai
            if isinstance(response, dict):
                # Response is a dictionary with results
                if 'results' in response and len(response['results']) > 0:
                    return response['results'][0].get('generated_text', str(response))
                return str(response)
            elif isinstance(response, str):
                return response
            else:
                # Handle list or other types
                return str(response)
        except Exception as e:
            logger.error(f"Error generating chat response: {str(e)}")
            raise RuntimeError(f"Failed to generate response: {str(e)}")
    
    def extract_architecture_insights(
        self,
        file_structure: str,
        key_files: str,
        tech_stack: List[str]
    ) -> str:
        """
        Extract architecture insights from codebase structure.
        
        Args:
            file_structure: Repository file structure
            key_files: Information about key files
            tech_stack: Technologies used
            
        Returns:
            Architecture insights
        """
        prompt = f"""Analyze the following codebase structure and provide architecture insights.

Technology Stack: {', '.join(tech_stack)}

File Structure:
{file_structure}

Key Files:
{key_files}

Provide insights about:
1. Overall architecture pattern (MVC, microservices, etc.)
2. Code organization and modularity
3. Design patterns identified
4. Potential areas for improvement
5. Best practices observed

Keep the response concise and actionable."""

        try:
            model = self._create_model()
            response = model.generate_text(prompt=prompt)
            logger.info("Generated architecture insights")
            
            # Handle different response types from watsonx.ai
            if isinstance(response, dict):
                # Response is a dictionary with results
                if 'results' in response and len(response['results']) > 0:
                    return response['results'][0].get('generated_text', str(response))
                return str(response)
            elif isinstance(response, str):
                return response
            else:
                # Handle list or other types
                return str(response)
        except Exception as e:
            logger.error(f"Error generating architecture insights: {str(e)}")
            return "Unable to generate architecture insights at this time."
    
    def generate_architecture_diagram(
        self,
        file_structure: str,
        tech_stack: List[str],
        key_files: str
    ) -> str:
        """
        Generate a Mermaid architecture diagram.
        
        Args:
            file_structure: Repository file structure
            tech_stack: Technologies used
            key_files: Information about key files
            
        Returns:
            Mermaid diagram code
        """
        prompt = f"""Generate a Mermaid diagram showing the architecture of this codebase.

Technology Stack: {', '.join(tech_stack)}

File Structure:
{file_structure}

Key Files:
{key_files}

Create a Mermaid graph diagram that shows:
1. Main components/modules
2. Their relationships and dependencies
3. Data flow between components
4. External services or APIs if any

IMPORTANT: Return ONLY the Mermaid diagram code starting with ```mermaid and ending with ```. 
Use graph TD or graph LR format. Keep it clear and not too complex.

Example format:
```mermaid
graph TD
    A[Frontend] --> B[API]
    B --> C[Database]
    B --> D[External Service]
```"""

        try:
            model = self._create_model()
            response = model.generate_text(prompt=prompt)
            logger.info("Generated architecture diagram")
            
            # Handle different response types
            if isinstance(response, dict):
                if 'results' in response and len(response['results']) > 0:
                    text = response['results'][0].get('generated_text', str(response))
                else:
                    text = str(response)
            elif isinstance(response, str):
                text = response
            else:
                text = str(response)
            
            # Extract mermaid code if wrapped in markdown
            if '```mermaid' in text:
                start = text.find('```mermaid') + 10
                end = text.find('```', start)
                if end > start:
                    return text[start:end].strip()
            
            return text
        except Exception as e:
            logger.error(f"Error generating architecture diagram: {str(e)}")
            # Return a default diagram on error
            return """graph TD
    A[Application] --> B[Components]
    B --> C[Services]
    C --> D[Data Layer]"""
    
    def generate_flow_diagram(
        self,
        repo_name: str,
        tech_stack: List[str],
        key_files: str,
        entry_points: str
    ) -> str:
        """
        Generate a Mermaid flow diagram showing application flow.
        
        Args:
            repo_name: Repository name
            tech_stack: Technologies used
            key_files: Information about key files
            entry_points: Main entry point files
            
        Returns:
            Mermaid flowchart code
        """
        prompt = f"""Generate a Mermaid flowchart showing the application flow for {repo_name}.

Technology Stack: {', '.join(tech_stack)}

Key Files:
{key_files}

Entry Points:
{entry_points}

Create a Mermaid flowchart that shows:
1. User/client interaction
2. Request flow through the application
3. Main processing steps
4. Response flow back to user
5. Key decision points

IMPORTANT: Return ONLY the Mermaid diagram code starting with ```mermaid and ending with ```.
Use flowchart TD or flowchart LR format. Keep it focused on the main flow.

Example format:
```mermaid
flowchart TD
    Start[User Request] --> Auth{{Authenticated?}}
    Auth -->|Yes| Process[Process Request]
    Auth -->|No| Login[Login Page]
    Process --> DB[(Database)]
    DB --> Response[Send Response]
```"""

        try:
            model = self._create_model()
            response = model.generate_text(prompt=prompt)
            logger.info("Generated flow diagram")
            
            # Handle different response types
            if isinstance(response, dict):
                if 'results' in response and len(response['results']) > 0:
                    text = response['results'][0].get('generated_text', str(response))
                else:
                    text = str(response)
            elif isinstance(response, str):
                text = response
            else:
                text = str(response)
            
            # Extract mermaid code if wrapped in markdown
            if '```mermaid' in text:
                start = text.find('```mermaid') + 10
                end = text.find('```', start)
                if end > start:
                    return text[start:end].strip()
            
            return text
        except Exception as e:
            logger.error(f"Error generating flow diagram: {str(e)}")
            # Return a default diagram on error
            return """flowchart TD
    Start[Start] --> Process[Process]
    Process --> End[End]"""
    
    def generate_setup_instructions(
        self,
        dependencies: str,
        readme_content: Optional[str],
        tech_stack: List[str]
    ) -> str:
        """
        Generate setup and installation instructions.
        
        Args:
            dependencies: Dependency information
            readme_content: Content from README if available
            tech_stack: Technologies used
            
        Returns:
            Setup instructions
        """
        readme_section = ""
        if readme_content:
            readme_section = f"\nREADME content:\n{readme_content[:1000]}\n"
        
        prompt = f"""Generate clear setup and installation instructions for this project.

Technology Stack: {', '.join(tech_stack)}

Dependencies:
{dependencies}
{readme_section}

Provide step-by-step instructions including:
1. Prerequisites and system requirements
2. Installation steps
3. Configuration needed
4. How to run the project
5. Common troubleshooting tips

Format as a clear, numbered list."""

        try:
            model = self._create_model()
            response = model.generate_text(prompt=prompt)
            logger.info("Generated setup instructions")
            
            # Handle different response types from watsonx.ai
            if isinstance(response, dict):
                # Response is a dictionary with results
                if 'results' in response and len(response['results']) > 0:
                    return response['results'][0].get('generated_text', str(response))
                return str(response)
            elif isinstance(response, str):
                return response
            else:
                # Handle list or other types
                return str(response)
        except Exception as e:
            logger.error(f"Error generating setup instructions: {str(e)}")
            return "Please refer to the project's README for setup instructions."

# Made with Bob
