"""Prediction and inference endpoints."""

import inspect
import logging
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.model_diagnostics import get_model_diagnostics
from app.dependencies import get_db
from app.api.utils import get_job_paths
from app.api.error_handler import handle_errors
from app.services.job_service import _ensure_mlflow_results, get_job_or_404

logger = logging.getLogger(__name__)
router = APIRouter()


async def _run_diagnostics(
    db: AsyncSession,
    job_id: str,
    diagnostics_method: str,
    model_type_override: Optional[str] = None,
    data_path_override: Optional[str] = None,
    require_data_path: bool = True,
    extra_kwargs: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Shared helper that handles the common diagnostics flow.

    1. Resolve job paths from the database
    2. Apply any request-level overrides for model_type / data_path
    3. Optionally enforce that a data_path is available
    4. Delegate to the named method on ModelDiagnostics
    5. Return the raw result dict

    Args:
        db: Async database session.
        job_id: The training job ID to look up.
        diagnostics_method: Name of the method to call on ModelDiagnostics
            (e.g. "get_confusion_matrix").
        model_type_override: Optional model_type from the request body.
        data_path_override: Optional data_path from the request body.
        require_data_path: If True, raise 400 when no data path is available.
        extra_kwargs: Any additional keyword arguments forwarded to the
            diagnostics method.

    Returns:
        The dict returned by the diagnostics method.
    """
    model_path, model_type, file_path, _ = await get_job_paths(db, job_id)

    actual_model_type = model_type_override or model_type
    actual_data_path = data_path_override or file_path

    if require_data_path and not actual_data_path:
        raise HTTPException(status_code=400, detail="No data path available for this job")

    diagnostics = get_model_diagnostics()
    method = getattr(diagnostics, diagnostics_method)

    # Build kwargs, only including data_path if the method accepts it
    kwargs: Dict[str, Any] = {
        "model_path": model_path,
        "model_type": actual_model_type,
    }
    method_params = inspect.signature(method).parameters
    if "data_path" in method_params and actual_data_path is not None:
        kwargs["data_path"] = actual_data_path
    if extra_kwargs:
        kwargs.update(extra_kwargs)

    return method(**kwargs)



class FeatureImportanceRequest(BaseModel):
    """Request for feature importance."""
    job_id: str = Field(..., description="ID of the completed training job")
    # model_type is optional - will be looked up from job if not provided
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries (optional)")
    # data_path is optional - will use job's file_path if not provided
    data_path: Optional[str] = Field(None, description="Optional path to data for permutation importance")


class FeatureImportanceResponse(BaseModel):
    """Feature importance response."""
    job_id: str
    model_type: str
    method: str
    features: List[Dict[str, Any]]
    chart: Optional[str] = None
    error: Optional[str] = None


class DiagnosticsRequest(BaseModel):
    """Request for model diagnostics (uses job_id to look up paths)."""
    job_id: str = Field(..., description="ID of the completed training job")
    # Optional overrides - will use job's values if not provided
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries (optional)")
    data_path: Optional[str] = Field(None, description="Path to data file (optional, uses job's file_path)")


class ConfusionMatrixResponse(BaseModel):
    """Confusion matrix response."""
    matrix: Optional[List[List[int]]] = None
    labels: List[str] = []
    chart: Optional[str] = None
    metrics: Dict[str, Any] = {}
    error: Optional[str] = None


class ROCCurveResponse(BaseModel):
    """ROC curve response."""
    auc: Optional[float] = None
    fpr: List[float] = []
    tpr: List[float] = []
    chart: Optional[str] = None
    error: Optional[str] = None


class RegressionDiagnosticsResponse(BaseModel):
    """Regression diagnostics response."""
    metrics: Dict[str, float] = {}
    predicted_vs_actual_chart: Optional[str] = None
    residuals_chart: Optional[str] = None
    residuals_histogram_chart: Optional[str] = None
    error: Optional[str] = None



@router.post("/model/feature-importance", response_model=FeatureImportanceResponse)
async def get_feature_importance(
    request: FeatureImportanceRequest,
    db: AsyncSession = Depends(get_db)
):
    """Get feature importance for a trained model (identified by job_id)."""
    job = await get_job_or_404(db, request.job_id)

    # do not call _sync_domino_job_state here — only do that in job endpoints, not prediction endpoints. 
    # _ensure_mlflow_results handles the case where the job is already COMPLETED in the DB but results were never fetched.
    job = await _ensure_mlflow_results(db, job)
    model_type = request.model_type or (job.model_type.value if job.model_type else "tabular")

    if not job.feature_importance:
        raise HTTPException(status_code=404, detail="Feature importance not available for this job")

    return FeatureImportanceResponse(
        job_id=request.job_id,
        model_type=model_type,
        method="mlflow",
        features=job.feature_importance,
    )


class LeaderboardRequest(BaseModel):
    """Request for model leaderboard (shows all models trained in a job)."""
    job_id: str = Field(..., description="ID of the completed training job")
    model_type: Optional[str] = Field(None, description="Type: tabular, timeseries (optional)")


@router.post("/model/leaderboard")
async def get_leaderboard(
    request: LeaderboardRequest,
    db: AsyncSession = Depends(get_db)
):
    """Get model leaderboard with comparison chart (identified by job_id)."""
    result = await _run_diagnostics(
        db,
        job_id=request.job_id,
        diagnostics_method="get_leaderboard",
        model_type_override=request.model_type,
        require_data_path=False,
    )
    result["job_id"] = request.job_id
    return result


@router.post("/model/confusion-matrix", response_model=ConfusionMatrixResponse)
async def get_confusion_matrix(
    request: DiagnosticsRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate confusion matrix for classification models (identified by job_id)."""
    result = await _run_diagnostics(
        db,
        job_id=request.job_id,
        diagnostics_method="get_confusion_matrix",
        model_type_override=request.model_type,
        data_path_override=request.data_path,
    )
    return ConfusionMatrixResponse(**result)


@router.post("/model/roc-curve", response_model=ROCCurveResponse)
async def get_roc_curve(
    request: DiagnosticsRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate ROC curve for binary classification (identified by job_id)."""
    result = await _run_diagnostics(
        db,
        job_id=request.job_id,
        diagnostics_method="get_roc_curve",
        model_type_override=request.model_type,
        data_path_override=request.data_path,
    )
    return ROCCurveResponse(**result)


@router.post("/model/precision-recall")
async def get_precision_recall_curve(
    request: DiagnosticsRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate Precision-Recall curve for binary classification (identified by job_id)."""
    return await _run_diagnostics(
        db,
        job_id=request.job_id,
        diagnostics_method="get_precision_recall_curve",
        model_type_override=request.model_type,
        data_path_override=request.data_path,
    )


@router.post("/model/regression-diagnostics", response_model=RegressionDiagnosticsResponse)
async def get_regression_diagnostics(
    request: DiagnosticsRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate diagnostic plots for regression models (identified by job_id)."""
    result = await _run_diagnostics(
        db,
        job_id=request.job_id,
        diagnostics_method="get_regression_diagnostics",
        model_type_override=request.model_type,
        data_path_override=request.data_path,
    )
    return RegressionDiagnosticsResponse(**result)
