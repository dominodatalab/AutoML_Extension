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
    database_url: str = ""

    # Paths - /mnt paths for Domino, ./local_data for local dev
    models_path: str = ""
    temp_path: str = ""
    datasets_path: str = ""
    uploads_path: str = ""
    eda_results_path: str = ""

    def model_post_init(self, __context):
        """Set path defaults based on environment (Domino vs local)."""
        is_domino = os.path.isdir("/mnt/data") or os.environ.get("DOMINO_RUN_ID")
        defaults = {
            "database_url": "sqlite:////mnt/data/automl.db" if is_domino else "sqlite:///./automl.db",
            "models_path": "/mnt/data/models" if is_domino else "./local_data/models",
            "temp_path": "/mnt/automl-service/uploads" if is_domino else "./local_data/temp",
            "datasets_path": "/mnt/data/datasets" if is_domino else "./local_data/datasets",
            "uploads_path": "/mnt/automl-service/uploads" if is_domino else "./local_data/uploads",
            "eda_results_path": "/mnt/data/automl/eda_results" if is_domino else "./local_data/eda_results",
        }
        for field, default in defaults.items():
            if not getattr(self, field):
                object.__setattr__(self, field, default)

    # Domino environment (auto-populated in Domino)
    domino_api_key: Optional[str] = None  # DOMINO_API_KEY for REST API access
    domino_user_api_key: Optional[str] = None  # Legacy - DOMINO_USER_API_KEY
    domino_api_host: Optional[str] = None  # e.g., https://se-demo.domino.tech
    domino_project_id: Optional[str] = None
    domino_project_name: Optional[str] = None
    domino_project_owner: Optional[str] = None
    domino_starting_username: Optional[str] = None
    domino_run_id: Optional[str] = None
    domino_training_hardware_tier_name: Optional[str] = None
    domino_training_environment_id: Optional[str] = None
    domino_eda_hardware_tier_name: Optional[str] = None
    domino_eda_environment_id: Optional[str] = None

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
    max_concurrent_jobs: int = 2

    # CORS
    cors_origins: list[str] = ["*"]

    class Config:
        env_file = ("../.env", ".env")
        env_file_encoding = "utf-8"
        extra = "ignore"

    @property
    def is_domino_environment(self) -> bool:
        """Check if Domino runtime config exists for API calls/job launches.

        Domino Apps/Runs can authenticate through DOMINO_API_PROXY without an
        explicit API key environment variable.
        """
        has_proxy_auth = bool(os.environ.get("DOMINO_API_PROXY"))
        has_key_auth = self.effective_api_key is not None
        return self.domino_api_host is not None and (has_proxy_auth or has_key_auth)


_settings_instance: Optional[Settings] = None

def get_settings() -> Settings:
    """Get settings instance (not cached to ensure fresh values after restart)."""
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance
