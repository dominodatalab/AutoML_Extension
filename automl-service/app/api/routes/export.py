"""Model export and deployment endpoints."""

import io
import logging
import json
import os
import zipfile
from pathlib import PurePosixPath
from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import Response, StreamingResponse
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Job
from app.core.model_export import get_model_exporter
from app.core.model_diagnostics import get_model_diagnostics
from app.core.dataset_manager import DominoDatasetManager
from app.core.domino_project_type import DominoProjectType, detect_project_type
from app.core.notebook_generator import generate_tabular_notebook, generate_timeseries_notebook
from app.dependencies import get_db
from app.api.utils import get_job_paths
from app.api.error_handler import handle_errors
from app.services.job_service import get_job_or_404

logger = logging.getLogger(__name__)
router = APIRouter()


class DeploymentPackageRequest(BaseModel):
    """Request for deployment package export."""
    job_id: str = Field(..., description="ID of the completed training job")
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries (optional)")
    output_dir: str = Field(..., description="Output directory for deployment package")


class DeploymentPackageResponse(BaseModel):
    """Response from deployment package export."""
    success: bool
    output_dir: Optional[str] = None
    files: list = []
    error: Optional[str] = None


class LearningCurvesRequest(BaseModel):
    """Request for learning curves."""
    job_id: str = Field(..., description="ID of the completed training job")
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries (optional)")


class LearningCurvesResponse(BaseModel):
    """Response with learning curves."""
    models: Optional[list] = None  # List of model training data for charts
    fit_summary: Optional[str] = None
    fit_summary_raw: Optional[Dict[str, Any]] = None
    training_history: Optional[Dict[str, Any]] = None  # Legacy support
    chart: Optional[str] = None  # base64 encoded (deprecated)
    error: Optional[str] = None



def _normalize_model_type(raw_model_type: Any) -> Optional[str]:
    """Normalize enum/legacy model_type values to canonical API keys."""
    if raw_model_type is None:
        return None

    value = raw_model_type.value if hasattr(raw_model_type, "value") else str(raw_model_type)
    normalized = str(value).strip().lower()

    if normalized.startswith("modeltype."):
        normalized = normalized.split(".", 1)[1]

    compact = normalized.replace("_", "").replace("-", "").replace(" ", "")
    if compact == "tabular":
        return "tabular"
    if compact == "timeseries":
        return "timeseries"

    return normalized or None


async def _resolve_notebook_data_path(job: Job) -> Optional[str]:
    """Resolve concrete data path for notebook export."""
    file_path = job.file_path
    dataset_id = job.dataset_id
    project_id = job.project_id
    if not dataset_id or not file_path or not project_id:
        return None

    dataset_manager = DominoDatasetManager()
    dataset_path = await dataset_manager.get_dataset_path(str(dataset_id))

    return f"{dataset_path}/{file_path}"

@router.post("/deployment", response_model=DeploymentPackageResponse)
async def export_deployment_package(
    request: DeploymentPackageRequest,
    db: AsyncSession = Depends(get_db)
):
    """Export model as deployment package with all necessary files (identified by job_id)."""
    # Look up job to get model_path
    model_path, model_type, _, _ = await get_job_paths(db, request.job_id)
    actual_model_type = request.model_type or model_type

    exporter = get_model_exporter()
    result = exporter.export_for_deployment(
        model_path=model_path,
        model_type=actual_model_type,
        output_dir=request.output_dir,
    )

    return DeploymentPackageResponse(**result)


class DeploymentDownloadRequest(BaseModel):
    """Request for downloading a deployment package as a zip."""
    output_dir: str = Field(..., description="Path to the deployment package directory")


@router.post("/deployment/download")
async def download_deployment_package(request: DeploymentDownloadRequest):
    """Download a previously exported deployment package as a zip file."""
    target_dir = request.output_dir
    if not os.path.isdir(target_dir):
        raise HTTPException(status_code=404, detail=f"Deployment package not found at: {target_dir}")

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _dirs, files in os.walk(target_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                arcname = os.path.relpath(file_path, target_dir)
                zf.write(file_path, arcname)
    buf.seek(0)

    basename = os.path.basename(target_dir.rstrip("/"))
    zip_filename = f"{basename}.zip" if basename else "deployment_package.zip"

    return StreamingResponse(
        buf,
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="{zip_filename}"'},
    )


@router.post("/learning-curves", response_model=LearningCurvesResponse)
async def get_learning_curves(
    request: LearningCurvesRequest,
    db: AsyncSession = Depends(get_db)
):
    """Get learning curves for a trained model (identified by job_id)."""
    # Look up job to get model_path
    model_path, model_type, _, _ = await get_job_paths(db, request.job_id)
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
        raise HTTPException(status_code=500, detail=f"Failed to generate learning curves: {e}")



@router.get("/formats")
async def get_supported_formats():
    """Get list of supported export formats by model type."""
    return {
        "tabular": {
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
        "timeseries": {
            "deployment_package": {
                "supported": True,
                "description": "Complete deployment package with inference script"
            },
            "shap_analysis": {
                "supported": False,
                "description": "SHAP not yet supported for time series models"
            },
            "notebook": {
                "supported": True,
                "description": "Jupyter notebook with time series training and forecasting code"
            }
        }
    }


class ExportNotebookRequest(BaseModel):
    """Request for notebook export."""
    job_id: str = Field(..., description="ID of the completed training job")


@router.post("/notebook")
@handle_errors("Error generating notebook")
async def export_notebook(
    request: ExportNotebookRequest,
    db: AsyncSession = Depends(get_db)
):
    """Export job configuration as a Jupyter notebook."""
    job = await get_job_or_404(db, request.job_id)

    model_type = _normalize_model_type(job.model_type)
    resolved_data_path = await _resolve_notebook_data_path(job)

    if job.data_source == "domino_dataset" and not resolved_data_path:
        raise HTTPException(
            status_code=400,
            detail=f"Could not resolve a mounted file path for dataset_id={job.dataset_id}",
        )

    if model_type == "tabular":
        notebook_content = generate_tabular_notebook(job, data_path=resolved_data_path)
    elif model_type == "timeseries":
        notebook_content = generate_timeseries_notebook(job, data_path=resolved_data_path)
    else:
        raise HTTPException(
            status_code=400,
            detail=(
                "Notebook export is supported for tabular and timeseries models only. "
                f"Received model_type={model_type!r}"
            ),
        )

    filename = f"{job.name.replace(' ', '_')}_automl.ipynb"

    # Return as JSON for frontend to handle download
    return {
        "success": True,
        "filename": filename,
        "notebook": notebook_content
    }
