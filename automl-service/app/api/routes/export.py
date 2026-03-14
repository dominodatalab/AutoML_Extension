"""Model export and deployment endpoints."""

import io
import logging
import json
import os
import tempfile
import zipfile
from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import Response, StreamingResponse
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_settings
from app.core.model_export import get_model_exporter
from app.core.model_diagnostics import get_model_diagnostics
from app.core.dataset_manager import DominoDatasetManager
from app.core.notebook_generator import generate_tabular_notebook, generate_timeseries_notebook
from app.dependencies import get_db
from app.db import crud
from app.api.utils import get_job_paths
from app.api.error_handler import handle_errors

logger = logging.getLogger(__name__)
router = APIRouter()


class DeploymentPackageRequest(BaseModel):
    """Request for deployment package export."""
    job_id: str = Field(..., description="ID of the completed training job")
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries (optional)")
    output_dir: Optional[str] = Field(None, description="Output directory (server resolves when omitted)")


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


class ModelComparisonRequest(BaseModel):
    """Request for model comparison."""
    model_paths: list = Field(..., description="List of model paths to compare")
    model_type: str = Field(..., description="Type: tabular, timeseries")
    data_path: Optional[str] = Field(None, description="Path to test data")


class ModelComparisonResponse(BaseModel):
    """Response with model comparison."""
    models: list = []
    metrics_comparison: Optional[Dict[str, Any]] = None
    chart: Optional[str] = None  # base64 encoded
    best_model: Optional[str] = None
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


async def _resolve_notebook_data_path(job: Any) -> Optional[str]:
    """Resolve concrete data path for notebook export."""
    if getattr(job, "file_path", None):
        return str(job.file_path)

    dataset_id = getattr(job, "dataset_id", None)
    if not dataset_id:
        return None

    try:
        dataset_manager = DominoDatasetManager()
        return await dataset_manager.get_dataset_file_path(str(dataset_id))
    except Exception as exc:
        logger.warning(
            "Failed to resolve notebook dataset path for job %s (dataset_id=%s): %s",
            getattr(job, "id", "unknown"),
            dataset_id,
            exc,
        )
        return None


@router.post("/export/deployment", response_model=DeploymentPackageResponse)
async def export_deployment_package(
    request: DeploymentPackageRequest,
    db: AsyncSession = Depends(get_db)
):
    """Export model as deployment package with all necessary files (identified by job_id)."""
    # Look up job to get model_path
    model_path, model_type, _, _ = await get_job_paths(db, request.job_id)
    actual_model_type = request.model_type or model_type

    # Resolve output_dir server-side when not provided
    output_dir = request.output_dir
    if not output_dir:
        output_dir = tempfile.mkdtemp(
            prefix="automl_export_", dir=get_settings().temp_path
        )

    exporter = get_model_exporter()
    result = exporter.export_for_deployment(
        model_path=model_path,
        model_type=actual_model_type,
        output_dir=output_dir,
    )

    return DeploymentPackageResponse(**result)


class DeploymentDownloadRequest(BaseModel):
    """Request for downloading a deployment package as a zip."""
    output_dir: str = Field(..., description="Path to the deployment package directory")


@router.post("/export/deployment/download")
async def download_deployment_package(request: DeploymentDownloadRequest):
    """Download a previously exported deployment package as a zip file."""
    target_dir = request.output_dir
    if not os.path.isdir(target_dir):
        raise HTTPException(status_code=404, detail=f"Deployment package not found at: {target_dir}")

    basename = os.path.basename(target_dir.rstrip("/"))
    zip_filename = f"{basename}.zip" if basename else "deployment_package.zip"

    spooled = _zip_directory_to_spooled(target_dir)
    return StreamingResponse(
        _iter_spooled(spooled),
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="{zip_filename}"'},
    )


_ZIP_CHUNK_SIZE = 8 * 1024 * 1024  # 8 MB read chunks
_SPOOLED_MAX = 50 * 1024 * 1024   # 50 MB before spilling to disk


def _zip_directory_to_spooled(
    target_dir: str,
) -> tempfile.SpooledTemporaryFile:
    """Zip a directory into a SpooledTemporaryFile (spills to disk >50 MB)."""
    spooled = tempfile.SpooledTemporaryFile(max_size=_SPOOLED_MAX)
    with zipfile.ZipFile(spooled, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _dirs, files in os.walk(target_dir):
            for fname in files:
                fpath = os.path.join(root, fname)
                arcname = os.path.relpath(fpath, target_dir)
                zf.write(fpath, arcname)
    spooled.seek(0)
    return spooled


def _zip_model_and_files(
    model_path: str,
    text_files: Dict[str, str],
) -> tempfile.SpooledTemporaryFile:
    """Build a zip with model files from disk + generated text files, no intermediate copy."""
    spooled = tempfile.SpooledTemporaryFile(max_size=_SPOOLED_MAX)
    with zipfile.ZipFile(spooled, "w", zipfile.ZIP_DEFLATED) as zf:
        # Add generated text files
        for name, content in text_files.items():
            zf.writestr(name, content)

        # Stream model files directly from source — no shutil.copytree
        if os.path.isdir(model_path):
            for root, _dirs, files in os.walk(model_path):
                for fname in files:
                    fpath = os.path.join(root, fname)
                    arcname = os.path.join(
                        "model", os.path.relpath(fpath, model_path)
                    )
                    zf.write(fpath, arcname)
        elif os.path.isfile(model_path):
            zf.write(model_path, os.path.join("model", os.path.basename(model_path)))

    spooled.seek(0)
    return spooled


def _iter_spooled(
    spooled: tempfile.SpooledTemporaryFile,
    chunk_size: int = _ZIP_CHUNK_SIZE,
):
    """Yield chunks from a SpooledTemporaryFile, then close it."""
    try:
        while True:
            chunk = spooled.read(chunk_size)
            if not chunk:
                break
            yield chunk
    finally:
        spooled.close()


class DeploymentZipRequest(BaseModel):
    """Request for combined build-and-download zip."""
    job_id: str = Field(..., description="ID of the completed training job")
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries (optional)")


@router.post("/export/deployment/zip")
async def export_deployment_zip(
    request: DeploymentZipRequest,
    db: AsyncSession = Depends(get_db),
):
    """Build and stream a deployment zip directly from the model's dataset mount.

    Combines build + download into a single request. No intermediate copy
    of model files — they are read directly from the dataset mount and
    streamed into the zip.
    """
    model_path, model_type, _, _ = await get_job_paths(db, request.job_id)
    actual_model_type = request.model_type or model_type

    if not os.path.exists(model_path):
        raise HTTPException(
            status_code=404,
            detail=f"Model artifacts not found at: {model_path}",
        )

    exporter = get_model_exporter()
    text_files = exporter.generate_deployment_files(actual_model_type)
    spooled = _zip_model_and_files(model_path, text_files)

    zip_filename = f"deployment_{request.job_id}.zip"
    return StreamingResponse(
        _iter_spooled(spooled),
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
        raise HTTPException(status_code=500, detail=f"Failed to compare models: {e}")


@router.get("/export/formats")
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


@router.post("/export/notebook")
@handle_errors("Error generating notebook")
async def export_notebook(
    request: ExportNotebookRequest,
    db: AsyncSession = Depends(get_db)
):
    """Export job configuration as a Jupyter notebook."""
    # Get job details
    job = await crud.get_job(db, request.job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job not found: {request.job_id}")

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
