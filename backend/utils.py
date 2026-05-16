"""
Utility functions for DevPilot backend.
"""

import hashlib
import logging
from datetime import datetime, timedelta
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def generate_session_id() -> str:
    """
    Generate a unique session identifier.
    
    Returns:
        UUID-like session ID
    """
    import uuid
    return str(uuid.uuid4())


def hash_repo_url(repo_url: str, branch: str) -> str:
    """
    Generate a hash for a repository URL and branch combination.
    
    Args:
        repo_url: Repository URL
        branch: Branch name
        
    Returns:
        MD5 hash string
    """
    combined = f"{repo_url}:{branch}"
    return hashlib.md5(combined.encode()).hexdigest()


def calculate_expiry_time(days: int) -> datetime:
    """
    Calculate expiry datetime from current time.
    
    Args:
        days: Number of days until expiry
        
    Returns:
        Expiry datetime
    """
    return datetime.utcnow() + timedelta(days=days)


def is_expired(expiry_time: datetime) -> bool:
    """
    Check if a datetime has expired.
    
    Args:
        expiry_time: Expiry datetime to check
        
    Returns:
        True if expired, False otherwise
    """
    return datetime.utcnow() > expiry_time


def truncate_text(text: str, max_length: int = 500, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to append if truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def extract_code_snippet(content: str, start_line: int, end_line: int) -> str:
    """
    Extract a code snippet from content by line numbers.
    
    Args:
        content: Full file content
        start_line: Starting line number (1-based)
        end_line: Ending line number (1-based, inclusive)
        
    Returns:
        Code snippet
    """
    lines = content.splitlines()
    # Convert to 0-based indexing
    start_idx = max(0, start_line - 1)
    end_idx = min(len(lines), end_line)
    
    return '\n'.join(lines[start_idx:end_idx])


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format.
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string (e.g., "1.5 MB")
    """
    size = float(size_bytes)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"


def sanitize_path(path: str) -> str:
    """
    Sanitize a file path to prevent directory traversal attacks.
    
    Args:
        path: File path to sanitize
        
    Returns:
        Sanitized path
    """
    # Remove leading slashes and parent directory references
    path = path.lstrip('/')
    path = path.replace('..', '')
    return path


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the specified name.
    
    Args:
        name: Logger name
        
    Returns:
        Logger instance
    """
    return logging.getLogger(name)

# Made with Bob
