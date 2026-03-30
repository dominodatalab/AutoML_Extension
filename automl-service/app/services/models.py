"""Service-layer models that should not depend on database persistence."""

import uuid
from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict
from pydantic_core import PydanticUndefined

from app.core.utils import utc_now
from app.db.models import Job, JobStatus, ModelType, ProblemType


class JobConfig(BaseModel):
    """Serializable training job state for worker handoff and background runners."""

    model_config = ConfigDict(from_attributes=True, extra="ignore")

    id: str
    name: str
    description: Optional[str] = None
    owner: Optional[str] = None
    project_id: Optional[str] = None
    project_name: Optional[str] = None
    project_owner: Optional[str] = None
    execution_target: str = "local"
    domino_job_id: Optional[str] = None
    model_type: ModelType
    problem_type: Optional[ProblemType] = None
    data_source: str
    dataset_id: Optional[str] = None
    file_path: Optional[str] = None
    target_column: str
    time_column: Optional[str] = None
    id_column: Optional[str] = None
    prediction_length: Optional[int] = None
    preset: str = "medium_quality_faster_train"
    time_limit: Optional[int] = None
    eval_metric: Optional[str] = None
    autogluon_config: Optional[dict[str, Any]] = None
    metrics: Optional[dict[str, Any]] = None
    leaderboard: Optional[dict[str, Any] | list[dict[str, Any]]] = None
    model_path: Optional[str] = None
    experiment_name: Optional[str] = None
    experiment_run_id: Optional[str] = None
    enable_mlflow: bool = False
    auto_register: bool = False
    register_name: Optional[str] = None
    registered_model_name: Optional[str] = None
    registered_model_version: Optional[str] = None
    created_at: datetime

    @classmethod
    def from_job(cls, job: Job, **overrides: Any) -> "JobConfig":
        """Create a transport-safe config from a persisted job."""
        payload: dict[str, Any] = {}

        for field_name, field_info in cls.model_fields.items():
            value = getattr(job, field_name, PydanticUndefined)
            if value is PydanticUndefined:
                continue

            if value is None:
                if field_info.default_factory is not None:
                    value = field_info.default_factory()
                elif field_info.default is not PydanticUndefined:
                    value = field_info.default

            payload[field_name] = value

        payload.update(overrides)
        return cls.model_validate(payload)
