"""Configuration management using Pydantic settings."""

import os
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    app_name: str = "AutoML Service"
    app_version: str = "1.0.0"
    debug: bool = False

    # Database
    database_url: str = "sqlite:///./automl.db"

    # Paths - use persistent /mnt paths that survive container restarts
    models_path: str = "/mnt/data/models"
    temp_path: str = "/mnt/automl-service/uploads"  # Changed from /tmp/automl
    datasets_path: str = "/mnt/data/datasets"
    uploads_path: str = "/mnt/automl-service/uploads"

    # Domino environment (auto-populated in Domino)
    domino_api_key: Optional[str] = None  # DOMINO_API_KEY for REST API access
    domino_user_api_key: Optional[str] = None  # Legacy - DOMINO_USER_API_KEY
    domino_api_host: Optional[str] = None  # e.g., https://se-demo.domino.tech
    domino_project_id: Optional[str] = None
    domino_project_name: Optional[str] = None
    domino_project_owner: Optional[str] = None
    domino_starting_username: Optional[str] = None
    domino_run_id: Optional[str] = None

    @property
    def effective_api_key(self) -> Optional[str]:
        """Get the effective API key (prefer DOMINO_API_KEY over DOMINO_USER_API_KEY)."""
        import os
        # Check multiple possible env var names
        return (
            self.domino_api_key or
            self.domino_user_api_key or
            os.environ.get("DOMINO_TOKEN_FILE") and open(os.environ.get("DOMINO_TOKEN_FILE")).read().strip() or
            None
        )

    # MLflow - auto-populated in Domino workspaces
    mlflow_tracking_uri: Optional[str] = None
    mlflow_tracking_token: Optional[str] = None  # MLFLOW_TRACKING_TOKEN

    # Training defaults
    default_time_limit: int = 3600
    default_job_list_limit: int = 100
    default_preview_rows: int = 10
    max_shap_samples: int = 100
    max_scatter_points: int = 500

    # CORS
    cors_origins: list[str] = ["*"]

    class Config:
        env_file = ("../.env", ".env")
        env_file_encoding = "utf-8"
        extra = "ignore"

    @property
    def is_domino_environment(self) -> bool:
        """Check if running in Domino environment."""
        return self.domino_api_host is not None and self.effective_api_key is not None


_settings_instance: Optional[Settings] = None

def get_settings() -> Settings:
    """Get settings instance (not cached to ensure fresh values after restart)."""
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance
