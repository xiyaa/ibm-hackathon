"""
Configuration management for DevOnboard AI backend.
Loads environment variables and provides application settings.
"""

import os
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # watsonx.ai Configuration
    watsonx_api_key: str = ""
    watsonx_project_id: str = ""
    watsonx_url: str = "https://us-south.ml.cloud.ibm.com"
    watsonx_model_id: str = "ibm/granite-13b-chat-v2"
    
    # Cloudant Configuration (for future use)
    cloudant_url: str = ""
    cloudant_api_key: str = ""
    cloudant_database: str = "devonboard_cache"
    
    # Application Settings
    repo_clone_dir: str = "/tmp/repos"
    max_repo_size_mb: int = 500
    cache_ttl_days: int = 7
    session_timeout_hours: int = 24
    
    # API Settings
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    cors_origins: str = "http://localhost:3000,http://localhost:5173"
    
    # Logging
    log_level: str = "INFO"
    
    # Model inference parameters
    max_new_tokens: int = 2048
    temperature: float = 0.7
    top_p: float = 0.9
    top_k: int = 50
    repetition_penalty: float = 1.1
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    def get_repo_path(self, repo_name: str) -> str:
        """Get the full path for a cloned repository."""
        return os.path.join(self.repo_clone_dir, repo_name)
    
    def ensure_repo_dir_exists(self) -> None:
        """Ensure the repository clone directory exists."""
        os.makedirs(self.repo_clone_dir, exist_ok=True)
    
    def get_cors_origins_list(self) -> List[str]:
        """Get CORS origins as a list."""
        return [origin.strip() for origin in self.cors_origins.split(",")]


# Global settings instance
settings = Settings()

# Made with Bob
