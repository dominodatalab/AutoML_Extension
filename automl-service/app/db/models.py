"""SQLAlchemy ORM models for the AutoML service."""

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text, DateTime, Integer, Float, JSON, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
import enum

from app.core.utils import utc_now
from app.db.database import Base


# TODO map domino jaob statuses to this
class JobStatus(str, enum.Enum):
    """Training job status."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    # TODO remove
    CANCELLED = "cancelled"


class ModelType(str, enum.Enum):
    """AutoGluon model type."""
    TABULAR = "tabular"
    TIMESERIES = "timeseries"


class ProblemType(str, enum.Enum):
    """Problem type for tabular models."""
    BINARY = "binary"
    MULTICLASS = "multiclass"
    REGRESSION = "regression"


class Job(Base):
    """Training job model."""
    __tablename__ = "jobs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Owner and project (for user/project filtering)
    owner: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, index=True)
    project_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, index=True)
    project_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    project_owner: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # Status
    status: Mapped[JobStatus] = mapped_column(SQLEnum(JobStatus), default=JobStatus.PENDING)
    domino_job_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, index=True)
    domino_job_status: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    progress: Mapped[int] = mapped_column(Integer, default=0)
    current_step: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    models_trained: Mapped[int] = mapped_column(Integer, default=0)
    current_model: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    eta_seconds: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    # Model configuration
    model_type: Mapped[ModelType] = mapped_column(SQLEnum(ModelType), nullable=False)
    problem_type: Mapped[Optional[ProblemType]] = mapped_column(SQLEnum(ProblemType), nullable=True)

    # Data source
    data_source: Mapped[str] = mapped_column(String(50), nullable=False)  # e.g. "domino_dataset"
    dataset_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    file_path: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Training configuration
    target_column: Mapped[str] = mapped_column(String(255), nullable=False)
    time_column: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    id_column: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    prediction_length: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    preset: Mapped[str] = mapped_column(String(100), default="medium_quality_faster_train")
    time_limit: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    eval_metric: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # AutoGluon configuration (stored as JSON)
    autogluon_config: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)

    # Results
    metrics: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    leaderboard: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    feature_importance: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    model_path: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Experiment tracking
    experiment_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    experiment_run_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # MLflow gating
    enable_mlflow: Mapped[bool] = mapped_column(default=False)

    # Auto-register to Domino Model Registry after training
    auto_register: Mapped[bool] = mapped_column(default=False)
    register_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # Registration status
    is_registered: Mapped[bool] = mapped_column(default=False)
    registered_model_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    registered_model_version: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utc_now)
    started_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class JobLog(Base):
    """Job execution logs."""
    __tablename__ = "job_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    level: Mapped[str] = mapped_column(String(20), default="INFO")
    message: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=utc_now)


class RegisteredModel(Base):
    """Registered models for tracking deployments."""
    __tablename__ = "registered_models"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    job_id: Mapped[str] = mapped_column(String(36), nullable=False)
    version: Mapped[int] = mapped_column(Integer, default=1)
    mlflow_model_uri: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    domino_model_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    deployed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=utc_now)
