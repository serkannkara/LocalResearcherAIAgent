"""Configuration management."""

from pathlib import Path
from typing import Any
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    
    # Ollama
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen2.5:latest"
    ollama_embedding_model: str = "nomic-embed-text:latest"
    
    # Optional API Keys
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    
    # Paths
    database_path: Path = Path("./localresearcher.db")
    vector_store_path: Path = Path("./chroma_db")
    reports_path: Path = Path("./reports")
    
    # Logging
    log_level: str = "INFO"
    
    # RAG
    chunk_size: int = 1000
    chunk_overlap: int = 200
    top_k_retrieval: int = 5
    
    def model_post_init(self, __context: Any) -> None:
        """Ensure directories exist."""
        self.reports_path.mkdir(exist_ok=True, parents=True)
        self.vector_store_path.mkdir(exist_ok=True, parents=True)


# Global settings instance
settings = Settings()