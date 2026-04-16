"""Model Registry endpoints for Domino integration."""

import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.generated.domino_public_api_client.api.registered_models import register_model_v2
from app.api.generated.domino_public_api_client.models.domino_registered_models_api_mlflow_model_source_v1 import DominoRegisteredModelsApiMlflowModelSourceV1
from app.api.generated.domino_public_api_client.models.domino_registered_models_api_model_source_v1 import DominoRegisteredModelsApiModelSourceV1
from app.api.generated.domino_public_api_client.models.domino_registered_models_api_model_source_v1_source_type import DominoRegisteredModelsApiModelSourceV1SourceType
from app.api.generated.domino_public_api_client.models.new_registered_model_v2 import NewRegisteredModelV2
from app.api.generated.domino_public_api_client.models.register_model_response_v2 import RegisterModelResponseV2
from app.core.domino_http import get_domino_public_api_client_sync
from app.dependencies import get_db
from app.api.error_handler import handle_errors
from app.services.job_service import get_job_or_404

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


@router.post("/register", response_model=RegisterModelResponse)
@handle_errors("Error registering model")
async def register_model(request: RegisterModelRequest, db: AsyncSession = Depends(get_db)):
    """Register a trained model to the Domino Model Registry via the Domino REST API."""
    job = await get_job_or_404(db, request.job_id)
    if not job.experiment_run_id:
        raise HTTPException(status_code=400, detail="Job has no MLflow experiment run to register from")

    body = NewRegisteredModelV2(
        model_name=request.model_name,
        description=request.description,
        model_source=DominoRegisteredModelsApiModelSourceV1(
            source_type=DominoRegisteredModelsApiModelSourceV1SourceType.MLFLOW,
            mlflow_source=DominoRegisteredModelsApiMlflowModelSourceV1(
                experiment_run_id=job.experiment_run_id,
                artifact_path="autogluon_model",
            ),
        ),
        create=True,
        discoverable=False,
    )

    response = register_model_v2.sync_detailed(client=get_domino_public_api_client_sync(), body=body)

    if not isinstance(response.parsed, RegisterModelResponseV2):
        raise HTTPException(status_code=response.status_code, detail=f"Model registration failed: {response.status_code}")

    model_version = str(response.parsed.model_version.model_version)

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
