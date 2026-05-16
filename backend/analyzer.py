"""
Code analyzer module that orchestrates repository analysis.
Combines repository management, watsonx.ai inference, and result formatting.
"""

from typing import Dict, List, Optional
from datetime import datetime

from models import (
    CodeAnalysis, FileNode, KeyFile, DependencyInfo,
    RepositoryInfo, AnalyzeResponse
)
from repo_manager import RepositoryManager
from watsonx_client import WatsonXClient
from config import settings
from utils import get_logger, generate_session_id, calculate_expiry_time

logger = get_logger(__name__)


class CodebaseAnalyzer:
    """Orchestrates the analysis of a codebase."""
    
    def __init__(self):
        """Initialize the analyzer with required components."""
        self.repo_manager = RepositoryManager()
        self.watsonx_client = WatsonXClient()
    
    def _format_file_tree(self, node: FileNode, indent: int = 0) -> str:
        """
        Format file tree as a string for AI prompt.
        
        Args:
            node: Root file node
            indent: Current indentation level
            
        Returns:
            Formatted file tree string
        """
        result = "  " * indent + f"{'📁' if node.type == 'directory' else '📄'} {node.name}"
        
        if node.type == "file" and node.language:
            result += f" ({node.language})"
        
        result += "\n"
        
        if node.children:
            for child in node.children:
                result += self._format_file_tree(child, indent + 1)
        
        return result
    
    def _extract_languages(self, file_tree: FileNode) -> List[str]:
        """
        Extract unique programming languages from file tree.
        
        Args:
            file_tree: Root file node
            
        Returns:
            List of unique languages
        """
        languages = set()
        
        def traverse(node: FileNode):
            if node.language:
                languages.add(node.language)
            if node.children:
                for child in node.children:
                    traverse(child)
        
        traverse(file_tree)
        return sorted(list(languages))
    
    def _format_key_files(self, key_files: List[KeyFile]) -> str:
        """
        Format key files information for AI prompt.
        
        Args:
            key_files: List of key files
            
        Returns:
            Formatted string
        """
        result = ""
        for kf in key_files:
            result += f"\n### {kf.path} ({kf.type})\n"
            if kf.language:
                result += f"Language: {kf.language}\n"
            result += f"Lines: {kf.lines}\n"
            if kf.snippet:
                result += f"```\n{kf.snippet}\n```\n"
        return result
    
    def _format_dependencies(self, dependencies: List[DependencyInfo]) -> str:
        """
        Format dependencies for AI prompt.
        
        Args:
            dependencies: List of dependency info
            
        Returns:
            Formatted string
        """
        result = ""
        for dep_info in dependencies:
            result += f"\n### {dep_info.file}\n"
            for name, version in list(dep_info.dependencies.items())[:20]:  # Limit to 20
                result += f"- {name}: {version}\n"
        return result
    
    def _extract_tech_stack(
        self,
        languages: List[str],
        dependencies: List[DependencyInfo]
    ) -> List[str]:
        """
        Extract technology stack from languages and dependencies.
        
        Args:
            languages: Programming languages
            dependencies: Dependency information
            
        Returns:
            List of technologies
        """
        tech_stack = set(languages)
        
        # Add frameworks based on dependencies
        for dep_info in dependencies:
            if dep_info.file == "requirements.txt":
                if "fastapi" in dep_info.dependencies:
                    tech_stack.add("FastAPI")
                if "django" in dep_info.dependencies:
                    tech_stack.add("Django")
                if "flask" in dep_info.dependencies:
                    tech_stack.add("Flask")
            elif dep_info.file == "package.json":
                if "react" in dep_info.dependencies:
                    tech_stack.add("React")
                if "vue" in dep_info.dependencies:
                    tech_stack.add("Vue.js")
                if "angular" in dep_info.dependencies:
                    tech_stack.add("Angular")
                if "express" in dep_info.dependencies:
                    tech_stack.add("Express.js")
        
        return sorted(list(tech_stack))
    
    def _get_readme_content(self, key_files: List[KeyFile]) -> Optional[str]:
        """
        Extract README content from key files.
        
        Args:
            key_files: List of key files
            
        Returns:
            README content or None
        """
        for kf in key_files:
            if kf.type == "readme":
                return kf.snippet
        return None
    
    async def analyze_repository(
        self,
        repo_url: str,
        branch: str = "main"
    ) -> AnalyzeResponse:
        """
        Perform comprehensive repository analysis.
        
        Args:
            repo_url: GitHub repository URL
            branch: Branch to analyze
            
        Returns:
            Complete analysis response
        """
        logger.info(f"Starting analysis of {repo_url} (branch: {branch})")
        
        try:
            # Clone repository
            repo_path, repo_info = self.repo_manager.clone_repository(repo_url, branch)
            logger.info(f"Repository cloned to {repo_path}")
            
            # Build file tree
            file_tree = self.repo_manager.build_file_tree(repo_path)
            logger.info("File tree built")
            
            # Identify key files
            key_files = self.repo_manager.identify_key_files(repo_path)
            logger.info(f"Identified {len(key_files)} key files")
            
            # Extract dependencies
            dependencies = self.repo_manager.extract_dependencies(repo_path)
            logger.info(f"Extracted {len(dependencies)} dependency files")
            
            # Extract languages and tech stack
            languages = self._extract_languages(file_tree)
            tech_stack = self._extract_tech_stack(languages, dependencies)
            
            # Format data for AI
            file_tree_str = self._format_file_tree(file_tree)
            key_files_str = self._format_key_files(key_files)
            dependencies_str = self._format_dependencies(dependencies)
            
            # Count files
            def count_files(node: FileNode) -> int:
                count = 1 if node.type == "file" else 0
                if node.children:
                    for child in node.children:
                        count += count_files(child)
                return count
            
            file_count = count_files(file_tree)
            
            # Generate AI analysis
            logger.info("Generating AI analysis...")
            overview = self.watsonx_client.generate_repository_analysis(
                repo_name=repo_info.name,
                file_count=file_count,
                languages=languages,
                file_tree=file_tree_str,
                key_files_content=key_files_str,
                dependencies=dependencies_str
            )
            
            # Generate architecture insights
            architecture_insights = self.watsonx_client.extract_architecture_insights(
                file_structure=file_tree_str,
                key_files=key_files_str,
                tech_stack=tech_stack
            )
            
            # Generate setup instructions
            readme_content = self._get_readme_content(key_files)
            setup_instructions = self.watsonx_client.generate_setup_instructions(
                dependencies=dependencies_str,
                readme_content=readme_content,
                tech_stack=tech_stack
            )
            
            # Build analysis result
            analysis = CodeAnalysis(
                overview=overview,
                tech_stack=tech_stack,
                file_structure=file_tree,
                key_files=key_files,
                dependencies=dependencies,
                setup_instructions=setup_instructions,
                architecture_insights=architecture_insights
            )
            
            # Generate session ID
            session_id = generate_session_id()
            
            # Create response
            response = AnalyzeResponse(
                session_id=session_id,
                repository=repo_info,
                analysis=analysis,
                cached=False,
                analyzed_at=datetime.utcnow()
            )
            
            logger.info(f"Analysis complete for {repo_url}")
            return response
            
        except Exception as e:
            logger.error(f"Error analyzing repository: {str(e)}")
            raise
    
    def get_file_content(
        self,
        repo_path: str,
        file_path: str
    ) -> tuple[str, Optional[str], int]:
        """
        Get content of a specific file.
        
        Args:
            repo_path: Path to cloned repository
            file_path: Relative path to file
            
        Returns:
            Tuple of (content, language, line_count)
        """
        return self.repo_manager.get_file_content(repo_path, file_path)

# Made with Bob
