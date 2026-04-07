"""Model Registry endpoints for Domino integration."""

import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.domino_http import domino_request
from app.db import crud
from app.dependencies import get_db
from app.api.error_handler import handle_errors

logger = logging.getLogger(__name__)
router = APIRouter()


class RegisterModelRequest(BaseModel):
    """Request to register a model."""
    job_id: str = Field(..., description="Job ID that created this model")
    model_name: str = Field(..., description="Name for the registered model")
    description: str = Field("", description="Model description")


class RegisterModelResponse(BaseModel):
    """Response from model registration."""
    success: bool
    model_name: str
    model_version: Optional[str] = None
    error: Optional[str] = None


@router.post("/register", response_model=RegisterModelResponse)
@handle_errors("Error registering model")
async def register_model(request: RegisterModelRequest, db: AsyncSession = Depends(get_db)):
    """Register a trained model to the Domino Model Registry via the Domino REST API."""
    job = await crud.get_job(db, request.job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job not found: {request.job_id}")
    if not job.experiment_run_id:
        raise HTTPException(status_code=400, detail="Job has no MLflow experiment run to register from")

    resp = await domino_request("POST", "/api/registeredmodels/v2", json={
        "modelName": request.model_name,
        "description": request.description,
        "modelSource": {
            "sourceType": "mlflow",
            "mlflowSource": {
                "experimentRunId": job.experiment_run_id,
                "artifactPath": "autogluon_model",
            },
        },
        "create": True,
        "discoverable": False,
    })

    data = resp.json()
    model_version = str(data["modelVersion"]["modelVersion"])

    try:
        job.is_registered = True
        job.registered_model_name = request.model_name
        job.registered_model_version = model_version
        await db.commit()
    except Exception as db_error:
        logger.warning(f"Could not update job registration status: {db_error}")

    return RegisterModelResponse(
        success=True,
        model_name=request.model_name,
        model_version=model_version,
    )
