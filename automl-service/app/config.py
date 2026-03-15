"""Configuration management using Pydantic settings."""

import os
import re
from typing import Optional

from pydantic_settings import BaseSettings


def sanitize_project_name(value: Optional[str]) -> str:
    """Normalize project name into a filesystem-safe segment."""
    raw = (value or "").strip()
    if not raw:
        return "default_project"
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", raw).strip("._-")
    return safe or "default_project"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    app_name: str = "AutoML Service"
    app_version: str = "1.0.0"
    debug: bool = False
    debug_logging: bool = False  # AUTOML_DEBUG_LOGGING - verbose request/response logging

    # Database
    database_url: str = ""

    # Paths - project-scoped under /mnt/data in Domino, ./local_data for local dev
    models_path: str = ""
    temp_path: str = ""
    datasets_path: str = ""
    uploads_path: str = ""
    eda_results_path: str = ""

    def _is_domino_runtime(self) -> bool:
        """Detect Domino runtime based on mounted paths or run metadata."""
        return os.path.isdir("/mnt/data") or bool(os.environ.get("DOMINO_RUN_ID"))

    @property
    def resolved_project_name(self) -> str:
        """Resolve project name with env-first fallback for path scoping."""
        return sanitize_project_name(
            self.domino_project_name
            or os.environ.get("DOMINO_PROJECT_NAME")
            or "default_project"
        )

    @property
    def project_storage_root(self) -> str:
        """Project-scoped writable root path."""
        if self._is_domino_runtime():
            return f"/mnt/data/{self.resolved_project_name}"
        return "./local_data"

    def model_post_init(self, __context):
        """Set path defaults based on environment (Domino vs local)."""
        is_domino = self._is_domino_runtime()
        project_root = self.project_storage_root
        defaults = {
            "database_url": f"sqlite:////{project_root.lstrip('/')}/automl.db" if is_domino else "sqlite:///./automl.db",
            "models_path": f"{project_root}/models" if is_domino else "./local_data/models",
            "temp_path": f"{project_root}/temp" if is_domino else "./local_data/temp",
            "datasets_path": f"{project_root}/datasets" if is_domino else "./local_data/datasets",
            "uploads_path": f"{project_root}/uploads" if is_domino else "./local_data/uploads",
            "eda_results_path": f"{project_root}/eda_results" if is_domino else "./local_data/eda_results",
        }
        domino_local_placeholders = {
            "database_url": {"sqlite:///./automl.db"},
            "models_path": {"./local_data/models"},
            "temp_path": {"./local_data/temp"},
            "datasets_path": {"./local_data/datasets"},
            "uploads_path": {"./local_data/uploads"},
            "eda_results_path": {"./local_data/eda_results"},
        }
        for field, default in defaults.items():
            current_value = getattr(self, field)
            should_override = not current_value or (
                is_domino and current_value in domino_local_placeholders.get(field, set())
            )
            if should_override:
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
        if self.domino_api_key:
            return self.domino_api_key
        if self.domino_user_api_key:
            return self.domino_user_api_key

        token_file = os.environ.get("DOMINO_TOKEN_FILE")
        if not token_file:
            return None

        try:
            with open(token_file, "r", encoding="utf-8") as handle:
                token = handle.read().strip()
            return token or None
        except OSError:
            return None

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
    max_local_queue_size: int = 10
    max_domino_queue_size: int = 20

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

    @property
    def standalone_mode(self) -> bool:
        """True when Domino platform services are unavailable.

        Honors explicit AUTOML_STANDALONE_MODE env var if set.
        Otherwise, standalone when Domino environment is not detected.
        """
        explicit = os.environ.get("AUTOML_STANDALONE_MODE")
        if explicit is not None:
            return explicit.strip().lower() in {"1", "true", "yes"}
        return not self.is_domino_environment


_settings_instance: Optional[Settings] = None

def get_settings() -> Settings:
    """Get settings instance (not cached to ensure fresh values after restart)."""
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance
