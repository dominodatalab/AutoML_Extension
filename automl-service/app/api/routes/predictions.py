"""Prediction and inference endpoints."""

import inspect
import logging
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.prediction_service import get_prediction_service
from app.core.model_diagnostics import get_model_diagnostics
from app.core.domino_registry import get_domino_registry
from app.db import crud
from app.dependencies import get_db
from app.api.utils import get_job_paths
from app.api.error_handler import handle_errors

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

    First checks the job's pre-computed ``diagnostics_data`` (populated during
    training while the model was on disk inside the Domino Job).  Falls back to
    loading the model from disk only when stored diagnostics are unavailable.
    """
    # Try pre-computed diagnostics first
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job not found: {job_id}")

    stored = getattr(job, "diagnostics_data", None) or {}
    if diagnostics_method in stored:
        logger.debug("Serving %s for job %s from stored diagnostics", diagnostics_method, job_id)
        return stored[diagnostics_method]

    # Fall back to live computation (model must be on disk)
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


class PredictRequest(BaseModel):
    """Request for single/batch predictions."""
    model_id: str = Field(..., description="ID/path of the trained model")
    model_type: str = Field(..., description="Type: tabular, timeseries")
    data: Optional[List[Dict[str, Any]]] = Field(None, description="Data rows for prediction")
    file_path: Optional[str] = Field(None, description="Path to data file")
    return_probabilities: bool = Field(False, description="Return class probabilities")
    prediction_length: Optional[int] = Field(None, description="Prediction horizon for time series")


class PredictResponse(BaseModel):
    """Response from prediction."""
    model_id: str
    model_type: str
    num_rows: int
    predictions: List[Any]
    probabilities: Optional[List[Dict[str, float]]] = None
    problem_type: Optional[str] = None
    label: Optional[str] = None


class BatchPredictRequest(BaseModel):
    """Request for batch predictions to file."""
    model_id: str
    model_type: str
    input_file: str
    output_file: str
    return_probabilities: bool = False


class BatchPredictResponse(BaseModel):
    """Response from batch prediction."""
    model_id: str
    output_file: str
    output_rows: int
    success: bool


class ModelInfoResponse(BaseModel):
    """Response with model information."""
    model_id: str
    model_type: str
    problem_type: Optional[str] = None
    label: Optional[str] = None
    features: Optional[List[str]] = None
    model_names: Optional[List[str]] = None
    best_model: Optional[str] = None
    leaderboard: Optional[List[Dict]] = None


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


@router.post("/predict", response_model=PredictResponse)
@handle_errors("Prediction error")
async def predict(request: PredictRequest):
    """Run predictions on data using a trained model."""
    service = get_prediction_service()

    # For time series, allow forecasting without input data
    if request.model_type == "timeseries" and not request.data and not request.file_path:
        result = service.forecast(
            model_id=request.model_id,
            prediction_length=request.prediction_length
        )
    elif request.data:
        result = service.predict(
            model_id=request.model_id,
            model_type=request.model_type,
            data=request.data,
            return_probabilities=request.return_probabilities
        )
    elif request.file_path:
        result = service.predict_from_file(
            model_id=request.model_id,
            model_type=request.model_type,
            file_path=request.file_path,
            return_probabilities=request.return_probabilities
        )
    else:
        raise HTTPException(status_code=400, detail="Either data or file_path is required")

    return PredictResponse(**result)


@router.post("/predict/batch", response_model=BatchPredictResponse)
@handle_errors("Batch prediction error")
async def batch_predict(request: BatchPredictRequest):
    """Run batch predictions and save to file."""
    service = get_prediction_service()

    result = service.batch_predict(
        model_id=request.model_id,
        model_type=request.model_type,
        input_file=request.input_file,
        output_file=request.output_file,
        return_probabilities=request.return_probabilities
    )

    return BatchPredictResponse(
        model_id=request.model_id,
        output_file=result["output_file"],
        output_rows=result["output_rows"],
        success=True
    )


@router.get("/model/{model_id}/info", response_model=ModelInfoResponse)
@handle_errors("Error getting model info")
async def get_model_info(model_id: str, model_type: str):
    """Get information about a trained model."""
    service = get_prediction_service()

    try:
        info = service.get_model_info(model_id, model_type)
        return ModelInfoResponse(**info)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Model not found: {model_id}")


@router.post("/model/feature-importance", response_model=FeatureImportanceResponse)
async def get_feature_importance(
    request: FeatureImportanceRequest,
    db: AsyncSession = Depends(get_db)
):
    """Get feature importance for a trained model (identified by job_id)."""
    result = await _run_diagnostics(
        db,
        job_id=request.job_id,
        diagnostics_method="get_feature_importance",
        model_type_override=request.model_type,
        data_path_override=request.data_path,
        require_data_path=False,
    )

    # Replace model_path with job_id in response
    result["job_id"] = request.job_id
    result.pop("model_path", None)

    return FeatureImportanceResponse(**result)


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


@router.delete("/model/{model_id}/unload")
async def unload_model(model_id: str):
    """Unload a model from memory."""
    service = get_prediction_service()
    success = service.unload_model(model_id)

    return {"success": success, "model_id": model_id}


@router.get("/models/loaded")
async def get_loaded_models():
    """Get list of currently loaded models."""
    service = get_prediction_service()
    return {"models": service.get_loaded_models()}
