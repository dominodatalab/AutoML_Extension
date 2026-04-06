"""Model Deployment endpoints for Domino Model Serving integration."""

from typing import Optional

from fastapi import APIRouter, Query
from pydantic import BaseModel, Field

from app.services.deployment_service import (
    list_deployments_safe,
    deploy_from_job as deploy_from_job_service,
)

router = APIRouter()


@router.get("/deployments")
async def list_deployments(
    model_api_id: str = Query(..., description="Model API ID to fetch deployments for"),
):
    """List deployments for a Model API."""
    return await list_deployments_safe(model_api_id=model_api_id)


class DeployFromJobBody(BaseModel):
    """Request body for deploying a model from a job."""
    model_name: Optional[str] = Field(None, description="Name for the Model API")
    replicas: int = Field(1, ge=1, description="Number of replicas")


@router.post("/deploy-from-job/{job_id}")
async def deploy_from_job(job_id: str, body: DeployFromJobBody):
    """Create a Domino Model API from a job's registered model."""
    return await deploy_from_job_service(
        job_id=job_id,
        model_name=body.model_name,
        replicas=body.replicas,
    )
