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
    # keep
    project_id: Optional[str] = None
    # keep
    project_name: Optional[str] = None
    project_owner: Optional[str] = None
    execution_target: str = "local"
    # keep
    domino_job_id: Optional[str] = None
    model_type: ModelType
    # keep
    problem_type: Optional[ProblemType] = None
    data_source: str
    # keep
    dataset_id: Optional[str] = None
    # keep
    file_path: Optional[str] = None
    target_column: str
    # keep
    time_column: Optional[str] = None
    # keep
    id_column: Optional[str] = None
    # keep
    prediction_length: Optional[int] = None
    #keep
    preset: str = "medium_quality_faster_train"
    # keep
    time_limit: Optional[int] = None
    # keep
    eval_metric: Optional[str] = None
    autogluon_config: Optional[dict[str, Any]] = None
    metrics: Optional[dict[str, Any]] = None
    leaderboard: Optional[dict[str, Any] | list[dict[str, Any]]] = None
    # keep
    model_path: Optional[str] = None
    experiment_name: Optional[str] = None
    experiment_run_id: Optional[str] = None
    enable_mlflow: bool = False
    auto_register: bool = False
    # keep
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
