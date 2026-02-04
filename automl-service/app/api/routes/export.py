"""Model export and deployment endpoints."""

import logging
import json
from typing import Any, Dict, Optional, Tuple

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import Response
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.model_export import get_model_exporter
from app.core.model_diagnostics import get_model_diagnostics
from app.core.notebook_generator import generate_binary_classification_notebook
from app.dependencies import get_db
from app.db import crud

logger = logging.getLogger(__name__)
router = APIRouter()


async def get_job_paths(db: AsyncSession, job_id: str) -> Tuple[str, str, Optional[str]]:
    """
    Look up a job and return (model_path, model_type, file_path).
    Raises HTTPException if job not found or model_path not available.
    """
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job not found: {job_id}")

    if not job.model_path:
        raise HTTPException(
            status_code=400,
            detail=f"Job {job_id} has no trained model. Status: {job.status.value}"
        )

    return job.model_path, job.model_type.value, job.file_path


class ExportONNXRequest(BaseModel):
    """Request for ONNX export."""
    job_id: str = Field(..., description="ID of the completed training job")
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries, multimodal (optional)")
    output_path: Optional[str] = Field(None, description="Optional output path")


class ExportONNXResponse(BaseModel):
    """Response from ONNX export."""
    success: bool
    output_path: Optional[str] = None
    format: str = "onnx"
    model_used: Optional[str] = None
    features: Optional[list] = None
    error: Optional[str] = None


class DeploymentPackageRequest(BaseModel):
    """Request for deployment package export."""
    job_id: str = Field(..., description="ID of the completed training job")
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries, multimodal (optional)")
    output_dir: str = Field(..., description="Output directory for deployment package")
    optimize_for_inference: bool = Field(True, description="Optimize model for inference")


class DeploymentPackageResponse(BaseModel):
    """Response from deployment package export."""
    success: bool
    output_dir: Optional[str] = None
    files: list = []
    error: Optional[str] = None


class LearningCurvesRequest(BaseModel):
    """Request for learning curves."""
    job_id: str = Field(..., description="ID of the completed training job")
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries, multimodal (optional)")


class LearningCurvesResponse(BaseModel):
    """Response with learning curves."""
    models: Optional[list] = None  # List of model training data for charts
    fit_summary: Optional[str] = None
    fit_summary_raw: Optional[Dict[str, Any]] = None
    training_history: Optional[Dict[str, Any]] = None  # Legacy support
    chart: Optional[str] = None  # base64 encoded (deprecated)
    error: Optional[str] = None


class ModelComparisonRequest(BaseModel):
    """Request for model comparison."""
    model_paths: list = Field(..., description="List of model paths to compare")
    model_type: str = Field(..., description="Type: tabular, timeseries, multimodal")
    data_path: Optional[str] = Field(None, description="Path to test data")


class ModelComparisonResponse(BaseModel):
    """Response with model comparison."""
    models: list = []
    metrics_comparison: Optional[Dict[str, Any]] = None
    chart: Optional[str] = None  # base64 encoded
    best_model: Optional[str] = None
    error: Optional[str] = None


@router.post("/export/onnx", response_model=ExportONNXResponse)
async def export_to_onnx(
    request: ExportONNXRequest,
    db: AsyncSession = Depends(get_db)
):
    """Export model to ONNX format (identified by job_id)."""
    # Look up job to get model_path
    model_path, model_type, _ = await get_job_paths(db, request.job_id)
    actual_model_type = request.model_type or model_type

    exporter = get_model_exporter()
    result = exporter.export_to_onnx(
        model_path=model_path,
        model_type=actual_model_type,
        output_path=request.output_path
    )

    return ExportONNXResponse(**result)


@router.post("/export/deployment", response_model=DeploymentPackageResponse)
async def export_deployment_package(
    request: DeploymentPackageRequest,
    db: AsyncSession = Depends(get_db)
):
    """Export model as deployment package with all necessary files (identified by job_id)."""
    # Look up job to get model_path
    model_path, model_type, _ = await get_job_paths(db, request.job_id)
    actual_model_type = request.model_type or model_type

    exporter = get_model_exporter()
    result = exporter.export_for_deployment(
        model_path=model_path,
        model_type=actual_model_type,
        output_dir=request.output_dir,
        optimize_for_inference=request.optimize_for_inference
    )

    return DeploymentPackageResponse(**result)


@router.post("/learning-curves", response_model=LearningCurvesResponse)
async def get_learning_curves(
    request: LearningCurvesRequest,
    db: AsyncSession = Depends(get_db)
):
    """Get learning curves for a trained model (identified by job_id)."""
    # Look up job to get model_path
    model_path, model_type, _ = await get_job_paths(db, request.job_id)
    actual_model_type = request.model_type or model_type

    diagnostics = get_model_diagnostics()

    try:
        result = diagnostics.get_learning_curves(
            model_path=model_path,
            model_type=actual_model_type
        )
        return LearningCurvesResponse(**result)
    except Exception as e:
        logger.error(f"Error getting learning curves: {e}")
        return LearningCurvesResponse(error=str(e))


@router.post("/compare-models", response_model=ModelComparisonResponse)
async def compare_models(request: ModelComparisonRequest):
    """Compare multiple trained models."""
    diagnostics = get_model_diagnostics()

    try:
        result = diagnostics.compare_models(
            model_paths=request.model_paths,
            model_type=request.model_type,
            data_path=request.data_path
        )
        return ModelComparisonResponse(**result)
    except Exception as e:
        logger.error(f"Error comparing models: {e}")
        return ModelComparisonResponse(error=str(e))


@router.get("/export/formats")
async def get_supported_formats():
    """Get list of supported export formats by model type."""
    return {
        "tabular": {
            "onnx": {
                "supported": True,
                "description": "ONNX format for sklearn-compatible models",
                "requirements": ["skl2onnx"]
            },
            "deployment_package": {
                "supported": True,
                "description": "Complete deployment package with inference script"
            },
            "shap_analysis": {
                "supported": True,
                "description": "SHAP-based feature importance analysis",
                "requirements": ["shap"]
            },
            "notebook": {
                "supported": True,
                "description": "Jupyter notebook with training code",
                "requirements": []
            }
        },
        "multimodal": {
            "onnx": {
                "supported": True,
                "description": "ONNX format for neural network models",
                "requirements": []
            },
            "deployment_package": {
                "supported": True,
                "description": "Complete deployment package with inference script"
            },
            "shap_analysis": {
                "supported": False,
                "description": "SHAP not yet supported for multimodal models"
            },
            "notebook": {
                "supported": False,
                "description": "Notebook export not yet supported for multimodal"
            }
        },
        "timeseries": {
            "onnx": {
                "supported": False,
                "description": "ONNX export not yet supported for time series"
            },
            "deployment_package": {
                "supported": True,
                "description": "Complete deployment package with inference script"
            },
            "shap_analysis": {
                "supported": False,
                "description": "SHAP not yet supported for time series models"
            },
            "notebook": {
                "supported": False,
                "description": "Notebook export not yet supported for time series"
            }
        }
    }


class ExportNotebookRequest(BaseModel):
    """Request for notebook export."""
    job_id: str = Field(..., description="ID of the completed training job")


@router.post("/export/notebook")
async def export_notebook(
    request: ExportNotebookRequest,
    db: AsyncSession = Depends(get_db)
):
    """Export job configuration as a Jupyter notebook."""
    # Get job details
    job = await crud.get_job(db, request.job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job not found: {request.job_id}")

    # Validate model type
    if job.model_type.value != "tabular":
        raise HTTPException(
            status_code=400,
            detail="Notebook export is only supported for tabular models"
        )

    # Validate problem type
    if job.problem_type and job.problem_type.value != "binary":
        raise HTTPException(
            status_code=400,
            detail="Notebook export is not yet supported for this problem type"
        )

    try:
        # Generate the notebook
        notebook_content = generate_binary_classification_notebook(job)
        filename = f"{job.name.replace(' ', '_')}_automl.ipynb"

        # Return as JSON for frontend to handle download
        return {
            "success": True,
            "filename": filename,
            "notebook": notebook_content
        }

    except Exception as e:
        logger.error(f"Error generating notebook: {e}")
        raise HTTPException(status_code=500, detail=str(e))
