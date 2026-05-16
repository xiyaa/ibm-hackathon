"""
Repository management module for cloning and analyzing GitHub repositories.
Handles Git operations, file structure extraction, and code sample collection.
"""

import os
import shutil
import hashlib
import json
import stat
import time
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import git
from git import Repo
from git.exc import GitCommandError
from pygments.lexers import guess_lexer_for_filename, ClassNotFound
from pygments.util import ClassNotFound as PygmentsClassNotFound

from models import FileNode, KeyFile, DependencyInfo, RepositoryInfo
from config import settings
from utils import get_logger

logger = get_logger(__name__)


class RepositoryManager:
    """Manages GitHub repository operations."""
    
    # File extensions to skip during analysis
    SKIP_EXTENSIONS = {
        '.pyc', '.pyo', '.so', '.dll', '.dylib', '.exe', '.bin',
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ico', '.svg',
        '.mp3', '.mp4', '.avi', '.mov', '.wav',
        '.zip', '.tar', '.gz', '.rar', '.7z',
        '.pdf', '.doc', '.docx', '.xls', '.xlsx',
        '.lock', '.log', '.cache'
    }
    
    # Directories to skip during analysis
    SKIP_DIRS = {
        '.git', '__pycache__', 'node_modules', 'venv', 'env',
        '.venv', 'dist', 'build', '.next', '.nuxt',
        'coverage', '.pytest_cache', '.mypy_cache',
        'vendor', 'target', 'bin', 'obj'
    }
    
    # Key file patterns to identify
    KEY_FILE_PATTERNS = {
        'readme': ['README.md', 'README.rst', 'README.txt', 'README'],
        'config': [
            'config.py', 'config.js', 'config.json', 'config.yaml', 'config.yml',
            'settings.py', 'settings.json', '.env.example', 'app.config'
        ],
        'entry_point': [
            'main.py', 'app.py', 'index.js', 'index.ts', 'server.js',
            'main.go', 'main.java', 'Program.cs', 'main.cpp'
        ],
        'dependency': [
            'requirements.txt', 'package.json', 'Pipfile', 'poetry.lock',
            'go.mod', 'pom.xml', 'build.gradle', 'Cargo.toml', 'composer.json'
        ]
    }
    
    def __init__(self):
        """Initialize the repository manager."""
        settings.ensure_repo_dir_exists()
    
    def _remove_readonly(self, func, path, excinfo):
        """
        Error handler for Windows readonly file removal.
        Used with shutil.rmtree to handle Git files on Windows.
        """
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except Exception as e:
            logger.warning(f"Could not remove {path}: {str(e)}")
    
    def _safe_remove_directory(self, path: str, max_retries: int = 3) -> None:
        """
        Safely remove a directory, handling Windows file locks.
        
        Args:
            path: Directory path to remove
            max_retries: Maximum number of retry attempts
        """
        if not os.path.exists(path):
            return
        
        for attempt in range(max_retries):
            try:
                # On Windows, use onerror callback to handle readonly files
                if os.name == 'nt':  # Windows
                    shutil.rmtree(path, onerror=self._remove_readonly)
                else:
                    shutil.rmtree(path)
                logger.debug(f"Successfully removed directory: {path}")
                return
            except PermissionError as e:
                if attempt < max_retries - 1:
                    logger.warning(f"Attempt {attempt + 1} failed to remove {path}, retrying...")
                    time.sleep(0.5)  # Wait before retry
                else:
                    logger.error(f"Failed to remove directory after {max_retries} attempts: {path}")
                    raise
            except Exception as e:
                logger.error(f"Error removing directory {path}: {str(e)}")
                raise
    
    def _generate_repo_id(self, repo_url: str, branch: str) -> str:
        """Generate a unique identifier for a repository and branch."""
        combined = f"{repo_url}:{branch}"
        return hashlib.md5(combined.encode()).hexdigest()
    
    def _parse_github_url(self, repo_url: str) -> Tuple[str, str]:
        """
        Parse GitHub URL to extract owner and repository name.
        
        Args:
            repo_url: GitHub repository URL
            
        Returns:
            Tuple of (owner, repo_name)
        """
        # Remove .git suffix if present
        url = repo_url.rstrip('/').replace('.git', '')
        
        # Extract from various GitHub URL formats
        if 'github.com' in url:
            parts = url.split('github.com/')[-1].split('/')
            if len(parts) >= 2:
                return parts[0], parts[1]
        
        raise ValueError(f"Invalid GitHub URL format: {repo_url}")
    
    def clone_repository(self, repo_url: str, branch: str = "main") -> Tuple[str, RepositoryInfo]:
        """
        Clone a GitHub repository to local storage.
        
        Args:
            repo_url: GitHub repository URL
            branch: Branch to clone (default: main)
            
        Returns:
            Tuple of (local_path, repository_info)
        """
        owner, repo_name = self._parse_github_url(repo_url)
        repo_id = self._generate_repo_id(repo_url, branch)
        local_path = settings.get_repo_path(repo_id)
        
        # Remove existing directory if it exists
        if os.path.exists(local_path):
            logger.info(f"Removing existing directory: {local_path}")
            self._safe_remove_directory(local_path)
        
        # Try to clone with specified branch, fallback to alternative branches
        branches_to_try = [branch]
        if branch == "main":
            branches_to_try.append("master")
        elif branch == "master":
            branches_to_try.append("main")
        
        last_error = None
        for try_branch in branches_to_try:
            try:
                # Clone the repository
                repo = Repo.clone_from(
                    repo_url,
                    local_path,
                    branch=try_branch,
                    depth=1  # Shallow clone for faster cloning
                )
                
                # Get last commit info
                last_commit = repo.head.commit.hexsha[:7]
                
                repo_info = RepositoryInfo(
                    name=repo_name,
                    owner=owner,
                    url=repo_url,
                    branch=try_branch,  # Use the actual branch that worked
                    last_commit=last_commit
                )
                
                return local_path, repo_info
                
            except GitCommandError as e:
                last_error = e
                logger.warning(f"Failed to clone with branch '{try_branch}': {str(e)}")
                # Clean up failed attempt
                if os.path.exists(local_path):
                    self._safe_remove_directory(local_path)
                # Continue to next branch
                continue
        
        # If we get here, all branches failed
        error_msg = f"Branch '{branch}' not found in repository"
        if branch in ["main", "master"] and len(branches_to_try) > 1:
            error_msg += f". Tried branches: {', '.join(branches_to_try)}"
        raise ValueError(error_msg)
    
    def _should_skip_file(self, file_path: Path) -> bool:
        """Check if a file should be skipped during analysis."""
        return file_path.suffix.lower() in self.SKIP_EXTENSIONS
    
    def _should_skip_dir(self, dir_name: str) -> bool:
        """Check if a directory should be skipped during analysis."""
        return dir_name in self.SKIP_DIRS
    
    def _detect_language(self, file_path: Path) -> Optional[str]:
        """
        Detect the programming language of a file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Language name or None
        """
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(1024)  # Read first 1KB
                lexer = guess_lexer_for_filename(file_path.name, content)
                return lexer.name
        except (ClassNotFound, PygmentsClassNotFound, UnicodeDecodeError, IOError):
            return None
    
    def build_file_tree(self, repo_path: str) -> FileNode:
        """
        Build a hierarchical file tree structure.
        
        Args:
            repo_path: Path to the cloned repository
            
        Returns:
            Root FileNode representing the repository structure
        """
        root_path = Path(repo_path)
        
        def build_node(path: Path, relative_to: Path) -> FileNode:
            """Recursively build file tree nodes."""
            rel_path = str(path.relative_to(relative_to))
            
            if path.is_file():
                size = path.stat().st_size if not self._should_skip_file(path) else None
                language = self._detect_language(path) if size else None
                
                return FileNode(
                    name=path.name,
                    path=rel_path,
                    type="file",
                    size=size,
                    language=language,
                    children=None
                )
            else:
                # Directory
                children = []
                try:
                    for child in sorted(path.iterdir()):
                        if child.is_dir() and self._should_skip_dir(child.name):
                            continue
                        if child.is_file() and self._should_skip_file(child):
                            continue
                        children.append(build_node(child, relative_to))
                except PermissionError:
                    pass  # Skip directories we can't read
                
                return FileNode(
                    name=path.name,
                    path=rel_path,
                    type="directory",
                    size=None,
                    language=None,
                    children=children if children else None
                )
        
        return build_node(root_path, root_path)
    
    def identify_key_files(self, repo_path: str) -> List[KeyFile]:
        """
        Identify important files in the repository.
        
        Args:
            repo_path: Path to the cloned repository
            
        Returns:
            List of KeyFile objects
        """
        key_files = []
        root_path = Path(repo_path)
        
        for file_type, patterns in self.KEY_FILE_PATTERNS.items():
            for pattern in patterns:
                # Search in root and immediate subdirectories
                for file_path in root_path.rglob(pattern):
                    if file_path.is_file() and not any(
                        skip_dir in file_path.parts for skip_dir in self.SKIP_DIRS
                    ):
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read()
                                lines = len(content.splitlines())
                                
                                # Get snippet (first 20 lines or 500 chars)
                                snippet_lines = content.splitlines()[:20]
                                snippet = '\n'.join(snippet_lines)
                                if len(snippet) > 500:
                                    snippet = snippet[:500] + '...'
                                
                                language = self._detect_language(file_path)
                                
                                key_files.append(KeyFile(
                                    path=str(file_path.relative_to(root_path)),
                                    type=file_type,
                                    language=language,
                                    lines=lines,
                                    snippet=snippet
                                ))
                                break  # Only take first match per pattern
                        except (IOError, UnicodeDecodeError):
                            continue
        
        return key_files
    
    def extract_dependencies(self, repo_path: str) -> List[DependencyInfo]:
        """
        Extract dependency information from package files.
        
        Args:
            repo_path: Path to the cloned repository
            
        Returns:
            List of DependencyInfo objects
        """
        dependencies = []
        root_path = Path(repo_path)
        
        # Python - requirements.txt
        req_file = root_path / 'requirements.txt'
        if req_file.exists():
            try:
                with open(req_file, 'r', encoding='utf-8') as f:
                    deps = {}
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            # Parse package==version or package>=version
                            if '==' in line:
                                pkg, ver = line.split('==', 1)
                                deps[pkg.strip()] = ver.strip()
                            elif '>=' in line:
                                pkg, ver = line.split('>=', 1)
                                deps[pkg.strip()] = f">={ver.strip()}"
                            else:
                                deps[line] = "latest"
                    
                    if deps:
                        dependencies.append(DependencyInfo(
                            file="requirements.txt",
                            dependencies=deps
                        ))
            except IOError:
                pass
        
        # Node.js - package.json
        pkg_file = root_path / 'package.json'
        if pkg_file.exists():
            try:
                with open(pkg_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    deps = {}
                    
                    if 'dependencies' in data:
                        deps.update(data['dependencies'])
                    if 'devDependencies' in data:
                        deps.update(data['devDependencies'])
                    
                    if deps:
                        dependencies.append(DependencyInfo(
                            file="package.json",
                            dependencies=deps
                        ))
            except (IOError, json.JSONDecodeError):
                pass
        
        return dependencies
    
    def cleanup_repository(self, repo_path: str) -> None:
        """
        Remove a cloned repository from local storage.
        
        Args:
            repo_path: Path to the repository to remove
        """
        if os.path.exists(repo_path):
            logger.info(f"Cleaning up repository: {repo_path}")
            self._safe_remove_directory(repo_path)
    
    def get_file_content(self, repo_path: str, file_path: str) -> Tuple[str, Optional[str], int]:
        """
        Get the content of a specific file.
        
        Args:
            repo_path: Path to the cloned repository
            file_path: Relative path to the file within the repository
            
        Returns:
            Tuple of (content, language, line_count)
        """
        full_path = Path(repo_path) / file_path
        
        if not full_path.exists() or not full_path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = len(content.splitlines())
                language = self._detect_language(full_path)
                
                return content, language, lines
        except IOError as e:
            raise IOError(f"Failed to read file: {str(e)}")

# Made with Bob
