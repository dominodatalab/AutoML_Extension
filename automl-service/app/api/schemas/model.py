"""Model-related Pydantic schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class RegisteredModelResponse(BaseModel):
    """Response schema for a registered model."""

    id: str
    name: str
    description: Optional[str] = None
    job_id: str
    version: int
    mlflow_model_uri: Optional[str] = None
    domino_model_id: Optional[str] = None
    deployed: bool = False
    created_at: datetime

    class Config:
        from_attributes = True


class ModelVersionResponse(BaseModel):
    """Response schema for model version."""

    version: int
    created_at: datetime
    run_id: Optional[str] = None
    status: str = "ready"


class DeployModelRequest(BaseModel):
    """Request schema for deploying a model."""

    model_version: int = Field(1, ge=1, description="Model version to deploy")
    environment_id: Optional[str] = Field(
        None, description="Domino environment ID"
    )
    hardware_tier_id: Optional[str] = Field(
        None, description="Domino hardware tier ID"
    )
    description: Optional[str] = Field(
        None, description="Deployment description"
    )


class DeploymentResponse(BaseModel):
    """Response schema for deployment."""

    success: bool
    model_name: str
    model_version: int
    deployment_id: Optional[str] = None
    endpoint_url: Optional[str] = None
    status: str = "pending"
    message: Optional[str] = None
