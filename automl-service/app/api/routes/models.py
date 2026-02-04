"""Model registry endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.db import crud
from app.core.model_registry import ModelRegistry
from app.api.schemas.model import (
    RegisteredModelResponse,
    ModelVersionResponse,
    DeployModelRequest,
    DeploymentResponse,
)

router = APIRouter()


def get_model_registry() -> ModelRegistry:
    """Get model registry instance."""
    return ModelRegistry()


@router.get("", response_model=list[RegisteredModelResponse])
async def list_models(db: AsyncSession = Depends(get_db)):
    """List all registered models."""
    models = await crud.get_registered_models(db)
    return [RegisteredModelResponse.model_validate(m) for m in models]


@router.get("/{model_name}", response_model=RegisteredModelResponse)
async def get_model(model_name: str, db: AsyncSession = Depends(get_db)):
    """Get a registered model by name."""
    model = await crud.get_registered_model(db, model_name)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return model


@router.get("/{model_name}/versions", response_model=list[ModelVersionResponse])
async def list_model_versions(
    model_name: str,
    registry: ModelRegistry = Depends(get_model_registry),
):
    """List all versions of a model."""
    try:
        versions = await registry.list_versions(model_name)
        return versions
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to list model versions: {str(e)}",
        )


@router.post("/{model_name}/deploy", response_model=DeploymentResponse)
async def deploy_model(
    model_name: str,
    request: DeployModelRequest,
    db: AsyncSession = Depends(get_db),
    registry: ModelRegistry = Depends(get_model_registry),
):
    """Deploy a model to Domino Model API."""
    # Check if model exists
    model = await crud.get_registered_model(db, model_name)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")

    try:
        deployment = await registry.deploy_model(
            model_name=model_name,
            model_version=request.model_version,
            environment_id=request.environment_id,
            hardware_tier_id=request.hardware_tier_id,
            description=request.description,
        )
        return deployment
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to deploy model: {str(e)}",
        )


@router.get("/{model_name}/deployments")
async def list_deployments(
    model_name: str,
    registry: ModelRegistry = Depends(get_model_registry),
):
    """List active deployments for a model."""
    try:
        deployments = await registry.list_deployments(model_name)
        return {"model_name": model_name, "deployments": deployments}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to list deployments: {str(e)}",
        )
