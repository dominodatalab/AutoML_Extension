"""Model Registry endpoints for Domino integration."""

import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.domino_registry import get_domino_registry
from app.core.utils import remap_shared_path
from app.db import crud
from app.db.models import RegisteredModel as DBRegisteredModel
from app.dependencies import get_db
from app.api.error_handler import handle_errors

logger = logging.getLogger(__name__)
router = APIRouter()


class RegisterModelRequest(BaseModel):
    """Request to register a model."""
    model_path: str = Field(..., description="Path to the trained model")
    model_name: str = Field(..., description="Name for the registered model")
    model_type: str = Field(..., description="Type: tabular, timeseries")
    description: str = Field("", description="Model description")
    job_id: Optional[str] = Field(None, description="Job ID that created this model")
    tags: Optional[Dict[str, str]] = Field(None, description="Custom tags")
    metrics: Optional[Dict[str, float]] = Field(None, description="Model metrics")
    params: Optional[Dict[str, Any]] = Field(None, description="Training parameters")
    experiment_name: Optional[str] = Field(None, description="MLflow experiment name from training")


class RegisterModelResponse(BaseModel):
    """Response from model registration."""
    success: bool
    model_name: str
    model_version: Optional[str] = None
    run_id: Optional[str] = None
    artifact_uri: Optional[str] = None
    error: Optional[str] = None


class TransitionStageRequest(BaseModel):
    """Request to transition model stage."""
    model_name: str
    version: str
    stage: str = Field(..., description="Stage: None, Staging, Production, Archived")
    archive_existing: bool = Field(False, description="Archive other versions in this stage")


class UpdateDescriptionRequest(BaseModel):
    """Request to update model description."""
    model_name: str
    description: str
    version: Optional[str] = None


class ModelVersionInfo(BaseModel):
    """Information about a model version."""
    version: str
    name: str
    status: str
    stage: str
    description: Optional[str] = None
    creation_timestamp: Optional[int] = None
    last_updated_timestamp: Optional[int] = None
    run_id: Optional[str] = None
    source: Optional[str] = None
    tags: Dict[str, str] = {}


class RegisteredModelInfo(BaseModel):
    """Information about a registered model from MLflow."""
    name: str
    description: Optional[str] = None
    creation_timestamp: Optional[int] = None
    last_updated_timestamp: Optional[int] = None
    tags: Dict[str, str] = {}
    latest_versions: List[Dict[str, Any]] = []


class LocalModelInfo(BaseModel):
    """Information about a model registered in local database."""
    id: str
    name: str
    description: Optional[str] = None
    job_id: Optional[str] = None
    version: int = 1
    mlflow_model_uri: Optional[str] = None
    domino_model_id: Optional[str] = None
    deployed: bool = False
    created_at: Optional[datetime] = None
    # Additional fields for frontend compatibility
    model_path: Optional[str] = None
    model_type: Optional[str] = None
    metrics: Optional[Dict[str, float]] = None

    class Config:
        from_attributes = True


class ModelCardRequest(BaseModel):
    """Request to generate a model card."""
    model_name: str
    version: str
    job_info: Dict[str, Any]
    metrics: Dict[str, Any]
    feature_importance: Optional[List[Dict]] = None


@router.post("/register", response_model=RegisterModelResponse)
@handle_errors("Error registering model")
async def register_model(request: RegisterModelRequest, db: AsyncSession = Depends(get_db)):
    """Register a trained model to the Domino Model Registry and local database."""
    registry = get_domino_registry()

    # Build tags and metrics from job info if job_id provided
    tags = request.tags or {}
    metrics = request.metrics or {}
    params = request.params or {}

    if request.job_id:
        job = await crud.get_job(db, request.job_id)
        if job:
            # Add default tags
            tags["source"] = "automl"
            tags["model_type"] = request.model_type
            if job.problem_type:
                tags["problem_type"] = job.problem_type.value if hasattr(job.problem_type, 'value') else str(job.problem_type)
            if job.target_column:
                tags["target_column"] = job.target_column
            if job.preset:
                tags["preset"] = job.preset.value if hasattr(job.preset, 'value') else str(job.preset)

            # Add params from job config
            params["model_type"] = request.model_type
            if job.time_limit:
                params["time_limit"] = job.time_limit
            if job.eval_metric:
                params["eval_metric"] = job.eval_metric

            # Extract numeric metrics from job.metrics
            if job.metrics:
                for key, value in job.metrics.items():
                    if isinstance(value, (int, float)) and not isinstance(value, bool):
                        metrics[key] = float(value)

            logger.info(f"Built tags={tags}, metrics={metrics} from job {request.job_id}")

    # Use request-provided experiment name if given; otherwise let the
    # registry create a new experiment scoped to *this* project.
    # Do NOT reuse the training job's experiment_name because it may
    # belong to a different Domino project (cross-project permission error).
    experiment_name = request.experiment_name

    result = registry.register_model(
        model_path=remap_shared_path(request.model_path),
        model_name=request.model_name,
        model_type=request.model_type,
        description=request.description,
        tags=tags if tags else None,
        metrics=metrics if metrics else None,
        params=params if params else None,
        experiment_name=experiment_name,
    )

    # Also save to local database for persistence
    if result.get("success"):
        try:
            # Check if model already exists
            existing = await crud.get_registered_model(db, request.model_name)
            if existing:
                # Update version
                existing.version += 1
                existing.mlflow_model_uri = result.get("artifact_uri")
                await db.commit()
            else:
                # Create new entry
                local_model = DBRegisteredModel(
                    name=request.model_name,
                    description=request.description,
                    job_id=request.job_id,
                    mlflow_model_uri=result.get("artifact_uri"),
                )
                await crud.create_registered_model(db, local_model)
            logger.info(f"Saved model {request.model_name} to local database")

            # Update job's registration status
            if request.job_id:
                job = await crud.get_job(db, request.job_id)
                if job:
                    job.is_registered = True
                    job.registered_model_name = request.model_name
                    job.registered_model_version = result.get("model_version")
                    await db.commit()
                    logger.info(f"Updated job {request.job_id} with registration status")
        except Exception as db_error:
            logger.warning(f"Could not save to local DB: {db_error}")

    return RegisterModelResponse(**result)


@router.get("/models", response_model=List[LocalModelInfo])
@handle_errors("Error listing models")
async def list_registered_models(db: AsyncSession = Depends(get_db), *, project_id: Optional[str] = None, owner: Optional[str] = None):
    """List all registered models from local database."""
    models = await crud.get_registered_models(db, project_id=project_id, owner=owner)
    result = []
    for m in models:
        # Get job info to add model_path and model_type
        job = await crud.get_job(db, m.job_id) if m.job_id else None
        # Filter metrics to numeric values only — job.metrics may contain
        # strings like best_model, problem_type, eval_metric.
        numeric_metrics = None
        if job and job.metrics:
            numeric_metrics = {
                k: float(v) for k, v in job.metrics.items()
                if isinstance(v, (int, float)) and not isinstance(v, bool)
            }

        result.append(LocalModelInfo(
            id=m.id,
            name=m.name,
            description=m.description,
            job_id=m.job_id,
            version=m.version,
            mlflow_model_uri=m.mlflow_model_uri,
            domino_model_id=m.domino_model_id,
            deployed=m.deployed,
            created_at=m.created_at,
            model_path=remap_shared_path(job.model_path) if job and job.model_path else None,
            model_type=job.model_type.value if job else None,
            metrics=numeric_metrics,
        ))
    return result


@router.get("/models/mlflow", response_model=List[RegisteredModelInfo])
@handle_errors("Error listing MLflow models")
async def list_mlflow_models():
    """List all registered models from MLflow registry."""
    registry = get_domino_registry()

    models = registry.list_registered_models()
    return [RegisteredModelInfo(**m) for m in models]


@router.get("/models/{model_name}/versions", response_model=List[ModelVersionInfo])
@handle_errors("Error getting model versions")
async def get_model_versions(model_name: str):
    """Get all versions of a registered model."""
    registry = get_domino_registry()

    versions = registry.get_model_versions(model_name)
    if not versions:
        raise HTTPException(status_code=404, detail=f"Model not found: {model_name}")
    return [ModelVersionInfo(**v) for v in versions]


@router.post("/models/transition-stage")
async def transition_model_stage(request: TransitionStageRequest):
    """Transition a model version to a new stage."""
    registry = get_domino_registry()

    result = registry.transition_model_stage(
        model_name=request.model_name,
        version=request.version,
        stage=request.stage,
        archive_existing=request.archive_existing
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error", "Unknown error"))

    return result


@router.post("/models/update-description")
async def update_model_description(request: UpdateDescriptionRequest):
    """Update model or version description."""
    registry = get_domino_registry()

    result = registry.update_model_description(
        model_name=request.model_name,
        description=request.description,
        version=request.version
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error", "Unknown error"))

    return result


@router.delete("/models/{model_name}/versions/{version}")
async def delete_model_version(model_name: str, version: str):
    """Delete a specific model version."""
    registry = get_domino_registry()

    result = registry.delete_model_version(model_name, version)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error", "Unknown error"))

    return result


@router.delete("/models/{model_name}")
async def delete_registered_model(model_name: str):
    """Delete a registered model and all its versions."""
    registry = get_domino_registry()

    result = registry.delete_registered_model(model_name)

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error", "Unknown error"))

    return result


@router.get("/models/{model_name}/versions/{version}/uri")
async def get_model_uri(model_name: str, version: str):
    """Get the download URI for a model version."""
    registry = get_domino_registry()

    uri = registry.get_model_download_uri(model_name, version)

    if not uri:
        raise HTTPException(status_code=404, detail="Model URI not found")

    return {"model_name": model_name, "version": version, "uri": uri}


@router.post("/models/{model_name}/versions/{version}/download")
@handle_errors("Error downloading model")
async def download_model(model_name: str, version: str):
    """Download a model from the registry to local storage."""
    registry = get_domino_registry()

    local_path = registry.load_model_from_registry(model_name, version=version)

    if not local_path:
        raise HTTPException(status_code=404, detail="Model not found or download failed")

    return {
        "success": True,
        "model_name": model_name,
        "version": version,
        "local_path": local_path
    }


@router.post("/models/card")
@handle_errors("Error generating model card")
async def generate_model_card(request: ModelCardRequest):
    """Generate a model card markdown document."""
    registry = get_domino_registry()

    card = registry.create_model_card(
        model_name=request.model_name,
        version=request.version,
        job_info=request.job_info,
        metrics=request.metrics,
        feature_importance=request.feature_importance
    )

    return {
        "model_name": request.model_name,
        "version": request.version,
        "card": card
    }


@router.get("/models/{model_name}/stages")
@handle_errors("Error getting model stages")
async def get_model_by_stage(model_name: str):
    """Get model versions organized by stage."""
    registry = get_domino_registry()

    versions = registry.get_model_versions(model_name)

    by_stage = {
        "None": [],
        "Staging": [],
        "Production": [],
        "Archived": []
    }

    for v in versions:
        stage = v.get("stage", "None")
        if stage in by_stage:
            by_stage[stage].append(v)

    return {
        "model_name": model_name,
        "stages": by_stage
    }
