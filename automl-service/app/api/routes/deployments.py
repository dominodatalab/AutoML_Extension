"""Model Deployment endpoints for Domino Model Serving integration.

Provides API endpoints to:
- Deploy trained models as REST endpoints
- Start/stop model deployments
- Manage deployment versions and scaling
- View deployment logs and status
"""

from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from app.core.domino_model_api import get_domino_model_api
from app.dependencies import get_request_project_id
from app.services.deployment_service import (
    list_deployments_safe,
    list_model_apis_safe,
)

router = APIRouter()


# ========== Request/Response Models ==========

class CreateModelApiRequest(BaseModel):
    """Request to create a Model API definition."""
    name: str = Field(..., description="Name for the model API")
    description: str = Field("", description="Description of the model")
    project_id: Optional[str] = Field(None, description="Domino project ID (auto-detected if not provided)")


class CreateVersionRequest(BaseModel):
    """Request to create a new Model API version."""
    model_file: str = Field(..., description="Path to the model file (e.g., model.py)")
    function_name: str = Field(..., description="Name of the predict function")
    environment_id: Optional[str] = Field(None, description="Environment ID to use")
    description: str = Field("", description="Version description")


class CreateDeploymentRequest(BaseModel):
    """Request to create a Model Deployment."""
    model_api_id: str = Field(..., description="ID of the Model API to deploy")
    model_api_version_id: str = Field(..., description="ID of the version to deploy")
    name: Optional[str] = Field(None, description="Deployment name")
    description: str = Field("", description="Deployment description")
    environment_id: Optional[str] = Field(None, description="Environment ID")
    hardware_tier_id: Optional[str] = Field(None, description="Hardware tier ID")
    min_replicas: int = Field(1, ge=0, description="Minimum number of replicas")
    max_replicas: int = Field(1, ge=1, description="Maximum number of replicas")


class QuickDeployRequest(BaseModel):
    """Request for quick end-to-end model deployment."""
    model_name: str = Field(..., description="Name for the deployed model")
    model_file: str = Field(..., description="Path to the model file")
    function_name: str = Field("predict", description="Name of the predict function")
    description: str = Field("", description="Model description")
    environment_id: Optional[str] = Field(None, description="Environment ID")
    hardware_tier_id: Optional[str] = Field(None, description="Hardware tier ID")
    min_replicas: int = Field(1, ge=0, description="Minimum replicas")
    max_replicas: int = Field(1, ge=1, description="Maximum replicas")
    auto_start: bool = Field(True, description="Start deployment immediately")


class UpdateDeploymentRequest(BaseModel):
    """Request to update a Model Deployment."""
    min_replicas: Optional[int] = Field(None, ge=0, description="Minimum replicas")
    max_replicas: Optional[int] = Field(None, ge=1, description="Maximum replicas")
    model_api_version_id: Optional[str] = Field(None, description="New version to deploy")


class DeploymentResponse(BaseModel):
    """Response containing deployment information."""
    success: bool
    deployment_id: Optional[str] = None
    status: Optional[str] = None
    message: Optional[str] = None
    url: Optional[str] = None
    error: Optional[str] = None
    data: Optional[Dict[str, Any]] = None


# ========== Model APIs Endpoints ==========

@router.get("/model-apis")
async def list_model_apis(
    project_id: Optional[str] = Query(None, description="Filter by project ID")
):
    """List all Model API definitions."""
    return await list_model_apis_safe(project_id=project_id)


@router.post("/model-apis")
async def create_model_api(request: CreateModelApiRequest):
    """Create a new Model API definition."""
    api = get_domino_model_api()
    result = await api.create_model_api(
        name=request.name,
        description=request.description,
        project_id=request.project_id,
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    return result


@router.get("/model-apis/{model_api_id}")
async def get_model_api(model_api_id: str):
    """Get a specific Model API definition."""
    api = get_domino_model_api()
    result = await api.get_model_api(model_api_id)

    if not result["success"]:
        raise HTTPException(status_code=404, detail=result.get("error"))

    return result


@router.delete("/model-apis/{model_api_id}")
async def delete_model_api(model_api_id: str):
    """Delete a Model API and all its versions."""
    api = get_domino_model_api()
    result = await api.delete_model_api(model_api_id)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    return result


# ========== Model API Versions Endpoints ==========

@router.get("/model-apis/{model_api_id}/versions")
async def list_model_api_versions(model_api_id: str):
    """List all versions of a Model API."""
    api = get_domino_model_api()
    result = await api.list_model_api_versions(model_api_id)

    if not result["success"]:
        raise HTTPException(status_code=500, detail=result.get("error"))

    return result


@router.post("/model-apis/{model_api_id}/versions")
async def create_model_api_version(model_api_id: str, request: CreateVersionRequest):
    """Create a new version of a Model API."""
    api = get_domino_model_api()
    result = await api.create_model_api_version(
        model_api_id=model_api_id,
        model_file=request.model_file,
        function_name=request.function_name,
        environment_id=request.environment_id,
        description=request.description,
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    return result


@router.get("/model-apis/{model_api_id}/versions/{version_id}")
async def get_model_api_version(model_api_id: str, version_id: str):
    """Get a specific version of a Model API."""
    api = get_domino_model_api()
    result = await api.get_model_api_version(model_api_id, version_id)

    if not result["success"]:
        raise HTTPException(status_code=404, detail=result.get("error"))

    return result


@router.get("/model-apis/{model_api_id}/versions/{version_id}/logs")
async def get_version_build_logs(model_api_id: str, version_id: str):
    """Get build logs for a Model API version."""
    api = get_domino_model_api()
    result = await api.get_version_build_logs(model_api_id, version_id)

    if not result["success"]:
        raise HTTPException(status_code=500, detail=result.get("error"))

    return result


# ========== Deployments Endpoints ==========

@router.get("/deployments")
async def list_deployments(
    project_id: Optional[str] = Query(None, description="Filter by project ID"),
    model_api_id: Optional[str] = Query(None, description="Filter by Model API ID"),
):
    """List all Model Deployments."""
    return await list_deployments_safe(
        project_id=project_id,
        model_api_id=model_api_id,
    )


@router.post("/deployments")
async def create_deployment(request: CreateDeploymentRequest):
    """Create a new Model Deployment."""
    api = get_domino_model_api()
    result = await api.create_deployment(
        model_api_id=request.model_api_id,
        model_api_version_id=request.model_api_version_id,
        name=request.name,
        description=request.description,
        environment_id=request.environment_id,
        hardware_tier_id=request.hardware_tier_id,
        min_replicas=request.min_replicas,
        max_replicas=request.max_replicas,
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    return result


@router.get("/deployments/{deployment_id}")
async def get_deployment(deployment_id: str):
    """Get a specific Model Deployment."""
    api = get_domino_model_api()
    result = await api.get_deployment(deployment_id)

    if not result["success"]:
        raise HTTPException(status_code=404, detail=result.get("error"))

    return result


@router.patch("/deployments/{deployment_id}")
async def update_deployment(deployment_id: str, request: UpdateDeploymentRequest):
    """Update a Model Deployment (scaling, version)."""
    api = get_domino_model_api()
    result = await api.update_deployment(
        deployment_id=deployment_id,
        min_replicas=request.min_replicas,
        max_replicas=request.max_replicas,
        model_api_version_id=request.model_api_version_id,
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    return result


@router.delete("/deployments/{deployment_id}")
async def delete_deployment(deployment_id: str):
    """Delete a Model Deployment."""
    api = get_domino_model_api()
    result = await api.delete_deployment(deployment_id)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    return result


@router.post("/deployments/{deployment_id}/start", response_model=DeploymentResponse)
async def start_deployment(deployment_id: str):
    """Start a stopped Model Deployment."""
    api = get_domino_model_api()
    result = await api.start_deployment(deployment_id)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    return DeploymentResponse(
        success=True,
        deployment_id=deployment_id,
        status="starting",
        message="Deployment start initiated",
    )


@router.post("/deployments/{deployment_id}/stop", response_model=DeploymentResponse)
async def stop_deployment(deployment_id: str):
    """Stop a running Model Deployment."""
    api = get_domino_model_api()
    result = await api.stop_deployment(deployment_id)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    return DeploymentResponse(
        success=True,
        deployment_id=deployment_id,
        status="stopping",
        message="Deployment stop initiated",
    )


@router.get("/deployments/{deployment_id}/status")
async def get_deployment_status(deployment_id: str):
    """Get the current status of a Model Deployment."""
    api = get_domino_model_api()
    result = await api.get_deployment_status(deployment_id)

    if not result["success"]:
        raise HTTPException(status_code=404, detail=result.get("error"))

    return result


@router.get("/deployments/{deployment_id}/logs/{log_type}")
async def get_deployment_logs(
    deployment_id: str,
    log_type: str = "stdout"
):
    """Get logs for a Model Deployment.

    log_type can be 'stdout' or 'stderr'.
    """
    api = get_domino_model_api()
    result = await api.get_deployment_logs(deployment_id, log_type)

    if not result["success"]:
        raise HTTPException(status_code=500, detail=result.get("error"))

    return result


@router.get("/deployments/{deployment_id}/versions")
async def get_deployment_versions(deployment_id: str):
    """Get all versions of a Model Deployment."""
    api = get_domino_model_api()
    result = await api.get_deployment_versions(deployment_id)

    if not result["success"]:
        raise HTTPException(status_code=500, detail=result.get("error"))

    return result


@router.get("/deployments/{deployment_id}/credentials")
async def get_deployment_credentials(
    deployment_id: str,
    operation_type: Optional[str] = Query(None, description="Specific operation type")
):
    """Get temporary credentials for a Model Deployment."""
    api = get_domino_model_api()
    result = await api.get_deployment_credentials(deployment_id, operation_type)

    if not result["success"]:
        raise HTTPException(status_code=500, detail=result.get("error"))

    return result


# ========== Quick Deploy Endpoint ==========

@router.post("/quick-deploy", response_model=DeploymentResponse)
async def quick_deploy(request: QuickDeployRequest):
    """Deploy a model end-to-end in a single request.

    This creates a Model API, version, and deployment automatically.
    Ideal for deploying trained AutoML models.
    """
    api = get_domino_model_api()

    result = await api.deploy_model(
        model_name=request.model_name,
        model_file=request.model_file,
        function_name=request.function_name,
        description=request.description,
        environment_id=request.environment_id,
        hardware_tier_id=request.hardware_tier_id,
        min_replicas=request.min_replicas,
        max_replicas=request.max_replicas,
        auto_start=request.auto_start,
    )

    if not result["success"]:
        raise HTTPException(
            status_code=400,
            detail={
                "error": result.get("error"),
                "steps_completed": result.get("steps_completed", []),
            }
        )

    return DeploymentResponse(
        success=True,
        deployment_id=result.get("deployment_id"),
        status="starting" if request.auto_start else "created",
        message=result.get("message"),
        url=result.get("endpoint_url"),
        data={
            "model_api_id": result.get("model_api_id"),
            "version_id": result.get("version_id"),
            "steps_completed": result.get("steps_completed", []),
        }
    )


# ========== Deployment from Job Endpoint ==========

@router.post("/deploy-from-job/{job_id}")
async def deploy_from_job(
    job_id: str,
    model_name: Optional[str] = None,
    function_name: str = "predict",
    min_replicas: int = 1,
    max_replicas: int = 1,
    project_id: str = Depends(get_request_project_id),
):
    """Deploy a trained model from an AutoML job.

    This creates the deployment files and deploys the model.
    """
    from app.services.deployment_service import deploy_from_job as deploy_from_job_service

    return await deploy_from_job_service(
        job_id=job_id,
        model_name=model_name,
        function_name=function_name,
        min_replicas=min_replicas,
        max_replicas=max_replicas,
        project_id=project_id,
    )
