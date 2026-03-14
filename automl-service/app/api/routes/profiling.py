"""Data profiling endpoints."""

import logging
from typing import Any, Dict, List, Literal, Optional
from uuid import uuid4

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

from app.core.data_profiler import get_data_profiler
from app.core.domino_job_launcher import get_domino_job_launcher
from app.core.eda_job_store import get_eda_job_store
from app.core.ts_profiler import get_ts_profiler
from app.api.error_handler import handle_errors
from app.config import get_settings
from app.core.utils import ensure_local_file

logger = logging.getLogger(__name__)
router = APIRouter()


class ProfileRequest(BaseModel):
    """Request for data profiling."""
    file_path: str = Field(..., description="Path to the data file")
    sample_size: int = Field(50000, description="Max rows to sample for profiling")
    sampling_strategy: str = Field("random", description="Sampling strategy: random, stratified, head, full")
    stratify_column: Optional[str] = Field(None, description="Column for stratified sampling")


class ColumnProfile(BaseModel):
    """Profile of a single column."""
    name: str
    dtype: str
    missing_count: int
    missing_percentage: float
    unique_count: int
    unique_percentage: float
    semantic_type: str
    statistics: Optional[Dict[str, Any]] = None
    histogram: Optional[Dict[str, Any]] = None
    value_counts: Optional[List[Dict[str, Any]]] = None
    issues: List[str] = []


class DataSummary(BaseModel):
    """Summary statistics of the dataset."""
    total_rows: int
    total_columns: int
    sampled: bool
    sample_size: int
    sampling_strategy: str = "random"
    memory_usage_mb: float
    duplicate_rows: int
    duplicate_percentage: float


class Recommendation(BaseModel):
    """A data recommendation."""
    type: str
    message: str
    priority: str


class Warning(BaseModel):
    """A data warning."""
    type: str
    message: str
    severity: str


class ProfileResponse(BaseModel):
    """Complete data profile response."""
    summary: DataSummary
    columns: List[ColumnProfile]
    correlations: Dict[str, Any] = {}
    recommendations: List[Recommendation] = []
    warnings: List[Warning] = []


class TargetSuggestion(BaseModel):
    """A target column suggestion."""
    column: str
    score: int
    reasons: List[str]
    problem_type: str


class TargetSuggestionsResponse(BaseModel):
    """Response with target column suggestions."""
    suggestions: List[TargetSuggestion]


@router.post("/profile", response_model=ProfileResponse)
@handle_errors("Profiling error")
async def profile_data(request: ProfileRequest, http_request: Request):
    """Generate a comprehensive profile of a data file."""
    project_id = http_request.headers.get("X-Project-Id")
    resolved_path = await ensure_local_file(request.file_path, project_id)

    profiler = get_data_profiler()

    try:
        profile = profiler.profile_file(
            file_path=resolved_path,
            sample_size=request.sample_size,
            sampling_strategy=request.sampling_strategy,
            stratify_column=request.stratify_column,
        )

        return ProfileResponse(
            summary=DataSummary(**profile["summary"]),
            columns=[ColumnProfile(**col) for col in profile["columns"]],
            correlations=profile.get("correlations", {}),
            recommendations=[Recommendation(**r) for r in profile.get("recommendations", [])],
            warnings=[Warning(**w) for w in profile.get("warnings", [])]
        )

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"File not found: {request.file_path}")


@router.post("/profile/suggest-target", response_model=TargetSuggestionsResponse)
@handle_errors("Error suggesting targets")
async def suggest_target_column(request: ProfileRequest, http_request: Request):
    """Suggest potential target columns based on data profile."""
    project_id = http_request.headers.get("X-Project-Id")
    resolved_path = await ensure_local_file(request.file_path, project_id)

    profiler = get_data_profiler()

    try:
        profile = profiler.profile_file(
            file_path=resolved_path,
            sample_size=request.sample_size,
            sampling_strategy=request.sampling_strategy,
            stratify_column=request.stratify_column,
        )

        suggestions = profiler.suggest_target_column(profile)

        return TargetSuggestionsResponse(
            suggestions=[TargetSuggestion(**s) for s in suggestions]
        )

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"File not found: {request.file_path}")


@router.post("/profile/quick")
@handle_errors("Quick profile error")
async def quick_profile(file_path: str, http_request: Request):
    """Get a quick profile summary (faster than full profile)."""
    project_id = http_request.headers.get("X-Project-Id")
    resolved_path = await ensure_local_file(file_path, project_id)

    profiler = get_data_profiler()

    profile = profiler.profile_file(resolved_path, sample_size=1000)

    # Return simplified summary
    return {
        "rows": profile["summary"]["total_rows"],
        "columns": profile["summary"]["total_columns"],
        "memory_mb": round(profile["summary"]["memory_usage_mb"], 2),
        "column_types": {
            col["name"]: col["semantic_type"]
            for col in profile["columns"]
        },
        "missing_columns": [
            col["name"]
            for col in profile["columns"]
            if col["missing_percentage"] > 0
        ],
        "potential_targets": [
            r["message"]
            for r in profile.get("recommendations", [])
            if r["type"] == "target"
        ][:3]
    }


@router.post("/profile/column/{column_name}")
@handle_errors("Column profile error")
async def profile_column(file_path: str, column_name: str, http_request: Request):
    """Get detailed profile for a specific column."""
    project_id = http_request.headers.get("X-Project-Id")
    resolved_path = await ensure_local_file(file_path, project_id)

    profiler = get_data_profiler()

    try:
        profile = profiler.profile_file(resolved_path, sample_size=10000)

        for col in profile["columns"]:
            if col["name"] == column_name:
                return col

        raise HTTPException(status_code=404, detail=f"Column not found: {column_name}")

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"File not found: {file_path}")


@router.get("/profile/metrics")
async def get_available_metrics():
    """Get list of available evaluation metrics by problem type."""
    return {
        "binary": [
            {"value": "accuracy", "label": "Accuracy", "description": "Fraction of correct predictions"},
            {"value": "balanced_accuracy", "label": "Balanced Accuracy", "description": "Accuracy for imbalanced datasets"},
            {"value": "f1", "label": "F1 Score", "description": "Harmonic mean of precision and recall"},
            {"value": "f1_macro", "label": "F1 Macro", "description": "Macro-averaged F1 score"},
            {"value": "f1_micro", "label": "F1 Micro", "description": "Micro-averaged F1 score"},
            {"value": "f1_weighted", "label": "F1 Weighted", "description": "Weighted F1 score"},
            {"value": "roc_auc", "label": "ROC AUC", "description": "Area under ROC curve"},
            {"value": "average_precision", "label": "Average Precision", "description": "Area under PR curve"},
            {"value": "precision", "label": "Precision", "description": "Positive predictive value"},
            {"value": "recall", "label": "Recall", "description": "True positive rate"},
            {"value": "log_loss", "label": "Log Loss", "description": "Negative log-likelihood"},
            {"value": "pac_score", "label": "PAC Score", "description": "Probabilistic accuracy"},
        ],
        "multiclass": [
            {"value": "accuracy", "label": "Accuracy", "description": "Fraction of correct predictions"},
            {"value": "balanced_accuracy", "label": "Balanced Accuracy", "description": "Accuracy for imbalanced datasets"},
            {"value": "f1_macro", "label": "F1 Macro", "description": "Macro-averaged F1 score"},
            {"value": "f1_micro", "label": "F1 Micro", "description": "Micro-averaged F1 score"},
            {"value": "f1_weighted", "label": "F1 Weighted", "description": "Weighted F1 score"},
            {"value": "log_loss", "label": "Log Loss", "description": "Negative log-likelihood"},
            {"value": "pac_score", "label": "PAC Score", "description": "Probabilistic accuracy"},
            {"value": "quadratic_kappa", "label": "Quadratic Kappa", "description": "Cohen's kappa with quadratic weights"},
        ],
        "regression": [
            {"value": "root_mean_squared_error", "label": "RMSE", "description": "Root mean squared error"},
            {"value": "mean_squared_error", "label": "MSE", "description": "Mean squared error"},
            {"value": "mean_absolute_error", "label": "MAE", "description": "Mean absolute error"},
            {"value": "r2", "label": "R-squared", "description": "Coefficient of determination"},
            {"value": "median_absolute_error", "label": "Median AE", "description": "Median absolute error"},
            {"value": "mean_absolute_percentage_error", "label": "MAPE", "description": "Mean absolute percentage error"},
            {"value": "spearmanr", "label": "Spearman", "description": "Spearman correlation coefficient"},
            {"value": "pearsonr", "label": "Pearson", "description": "Pearson correlation coefficient"},
        ],
        "timeseries": [
            {"value": "MASE", "label": "MASE", "description": "Mean absolute scaled error"},
            {"value": "MAPE", "label": "MAPE", "description": "Mean absolute percentage error"},
            {"value": "sMAPE", "label": "sMAPE", "description": "Symmetric mean absolute percentage error"},
            {"value": "RMSE", "label": "RMSE", "description": "Root mean squared error"},
            {"value": "MAE", "label": "MAE", "description": "Mean absolute error"},
            {"value": "WAPE", "label": "WAPE", "description": "Weighted absolute percentage error"},
            {"value": "SQL", "label": "SQL", "description": "Scaled quantile loss"},
        ]
    }


@router.get("/profile/presets")
async def get_available_presets():
    """Get list of available training presets."""
    return {
        "tabular": [
            {
                "value": "best_quality",
                "label": "Best Quality",
                "description": "Maximum accuracy, slowest training. Uses stacking and extensive HPO.",
                "time_multiplier": 10
            },
            {
                "value": "high_quality",
                "label": "High Quality",
                "description": "Very good accuracy with reasonable training time.",
                "time_multiplier": 5
            },
            {
                "value": "good_quality",
                "label": "Good Quality",
                "description": "Good balance of accuracy and speed.",
                "time_multiplier": 2
            },
            {
                "value": "medium_quality_faster_train",
                "label": "Medium Quality (Faster)",
                "description": "Fast training with decent accuracy. Good for prototyping.",
                "time_multiplier": 1
            },
            {
                "value": "optimize_for_deployment",
                "label": "Optimize for Deployment",
                "description": "Fastest inference, smallest model size.",
                "time_multiplier": 0.5
            }
        ],
        "timeseries": [
            {
                "value": "best_quality",
                "label": "Best Quality",
                "description": "Includes Chronos foundation model and extensive ensembling.",
                "time_multiplier": 10
            },
            {
                "value": "high_quality",
                "label": "High Quality",
                "description": "Good accuracy with multiple model types.",
                "time_multiplier": 5
            },
            {
                "value": "medium_quality",
                "label": "Medium Quality",
                "description": "Balanced speed and accuracy.",
                "time_multiplier": 2
            },
            {
                "value": "fast_training",
                "label": "Fast Training",
                "description": "Quick training for prototyping.",
                "time_multiplier": 1
            },
            {
                "value": "chronos",
                "label": "Chronos (Zero-shot)",
                "description": "Uses pretrained Chronos model. No training required.",
                "time_multiplier": 0.1
            }
        ]
    }


# ── Time Series Profiling ──────────────────────────────────────────────


class TimeSeriesProfileRequest(BaseModel):
    """Request for time series profiling."""
    file_path: str = Field(..., description="Path to the data file")
    time_column: str = Field(..., description="Name of the datetime column")
    target_column: str = Field(..., description="Name of the numeric target column")
    id_column: Optional[str] = Field(None, description="Name of the series identifier column")
    sample_size: int = Field(100000, description="Max rows to sample for profiling")
    sampling_strategy: str = Field("recent", description="Sampling strategy: recent, oldest, uniform, full")
    rolling_window: Optional[int] = Field(None, description="Rolling window size (auto if omitted)")


class TimeSeriesProfileResponse(BaseModel):
    """Complete time series profile response."""
    temporal_summary: Dict[str, Any] = {}
    gap_analysis: Dict[str, Any] = {}
    stationarity: Optional[Dict[str, Any]] = None
    trend_analysis: Optional[Dict[str, Any]] = None
    seasonality: Optional[Dict[str, Any]] = None
    autocorrelation: Optional[Dict[str, Any]] = None
    target_statistics: Dict[str, Any] = {}
    rolling_statistics: Optional[Dict[str, Any]] = None
    per_series_summary: Optional[List[Dict[str, Any]]] = None
    recommendations: List[Recommendation] = []
    warnings: List[Warning] = []


class AsyncProfileStartRequest(BaseModel):
    """Request to start async EDA profiling in a Domino Job."""

    mode: Literal["tabular", "timeseries"] = Field("tabular")
    file_path: str = Field(..., description="Path to the data file")
    sample_size: int = Field(50000, description="Max rows to sample for profiling")
    sampling_strategy: str = Field(
        "random",
        description="Sampling strategy (tabular: random/stratified/head/full; TS: recent/oldest/uniform/full)",
    )
    stratify_column: Optional[str] = Field(None, description="Column for stratified tabular sampling")
    time_column: Optional[str] = Field(None, description="Datetime column for timeseries profiling")
    target_column: Optional[str] = Field(None, description="Target column for timeseries profiling")
    id_column: Optional[str] = Field(None, description="Series id column for timeseries profiling")
    rolling_window: Optional[int] = Field(None, description="Rolling window for timeseries profiling")
    domino_hardware_tier_name: Optional[str] = Field(
        None,
        description="Optional Domino hardware tier name",
    )
    domino_environment_id: Optional[str] = Field(
        None,
        description="Optional Domino environment ID",
    )


class AsyncProfileStartResponse(BaseModel):
    """Response for async profile start."""

    request_id: str
    status: str
    mode: str
    domino_job_id: Optional[str] = None
    domino_job_status: Optional[str] = None
    domino_job_url: Optional[str] = None


class AsyncProfileStatusRequest(BaseModel):
    """Request for async profile status polling."""

    request_id: str = Field(..., description="EDA async request id")


class AsyncProfileStatusResponse(BaseModel):
    """Response for async profile status polling."""

    request_id: str
    status: str
    mode: Optional[str] = None
    domino_job_id: Optional[str] = None
    domino_job_status: Optional[str] = None
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


@router.post("/profile/timeseries", response_model=TimeSeriesProfileResponse)
@handle_errors("Time series profiling error")
async def profile_timeseries(request: TimeSeriesProfileRequest, http_request: Request):
    """Generate a comprehensive time series profile."""
    project_id = http_request.headers.get("X-Project-Id")
    resolved_path = await ensure_local_file(request.file_path, project_id)

    profiler = get_ts_profiler()

    try:
        result = profiler.profile_timeseries_file(
            file_path=resolved_path,
            time_column=request.time_column,
            target_column=request.target_column,
            id_column=request.id_column,
            sample_size=request.sample_size,
            sampling_strategy=request.sampling_strategy,
            rolling_window=request.rolling_window,
        )

        return TimeSeriesProfileResponse(
            temporal_summary=result.get("temporal_summary", {}),
            gap_analysis=result.get("gap_analysis", {}),
            stationarity=result.get("stationarity"),
            trend_analysis=result.get("trend_analysis"),
            seasonality=result.get("seasonality"),
            autocorrelation=result.get("autocorrelation"),
            target_statistics=result.get("target_statistics", {}),
            rolling_statistics=result.get("rolling_statistics"),
            per_series_summary=result.get("per_series_summary"),
            recommendations=[Recommendation(**r) for r in result.get("recommendations", [])],
            warnings=[Warning(**w) for w in result.get("warnings", [])],
        )

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"File not found: {request.file_path}")


@router.post("/profile/async/start", response_model=AsyncProfileStartResponse)
@handle_errors("Async profiling start error")
async def start_profile_async(request: AsyncProfileStartRequest, http_request: Request):
    """Start async EDA profiling as an external Domino Job."""
    import asyncio

    if request.mode == "timeseries":
        if not request.time_column or not request.target_column:
            raise HTTPException(
                status_code=400,
                detail="time_column and target_column are required for timeseries profiling",
            )

    store = get_eda_job_store()
    settings = get_settings()
    request_id = str(uuid4())
    store.create_request(
        request_id=request_id,
        mode=request.mode,
        request_payload=request.model_dump(exclude_none=True),
    )

    # Resolve project context for dataset pre-creation and job launch
    project_id = http_request.headers.get("X-Project-Id") if http_request else None

    # Pre-create the automl-extension dataset so the EDA Domino Job
    # boots with the mount already available for writing results.
    if project_id and not settings.standalone_mode:
        try:
            from app.services.storage_resolver import get_storage_resolver

            await asyncio.wait_for(
                get_storage_resolver().ensure_dataset_exists(project_id),
                timeout=30.0,
            )
        except (asyncio.TimeoutError, Exception):
            logger.warning(
                "Pre-launch dataset creation failed for EDA job in project %s; job proceeds anyway",
                project_id,
            )

    launcher = get_domino_job_launcher()
    launch_result = await launcher.start_eda_job(
        request_id=request_id,
        mode=request.mode,
        file_path=request.file_path,
        sample_size=request.sample_size,
        sampling_strategy=request.sampling_strategy,
        stratify_column=request.stratify_column,
        time_column=request.time_column,
        target_column=request.target_column,
        id_column=request.id_column,
        rolling_window=request.rolling_window,
        hardware_tier_name=request.domino_hardware_tier_name or settings.domino_eda_hardware_tier_name,
        environment_id=request.domino_environment_id or settings.domino_eda_environment_id,
        project_id=project_id,
    )
    if not launch_result.get("success"):
        error_message = launch_result.get("error", "Failed to launch async profiling job")
        store.update_request(request_id, status="failed", error=error_message)
        raise HTTPException(status_code=502, detail=error_message)

    store.update_request(
        request_id,
        status="running",
        domino_job_id=launch_result.get("domino_job_id"),
        domino_job_status=launch_result.get("domino_job_status", "Submitted"),
        domino_job_url=launch_result.get("domino_job_url"),
        error=None,
    )
    return AsyncProfileStartResponse(
        request_id=request_id,
        status="running",
        mode=request.mode,
        domino_job_id=launch_result.get("domino_job_id"),
        domino_job_status=launch_result.get("domino_job_status", "Submitted"),
        domino_job_url=launch_result.get("domino_job_url"),
    )


async def _build_async_status_response(request_id: str) -> AsyncProfileStatusResponse:
    """Load async EDA status from file-backed metadata/results."""
    store = get_eda_job_store()
    launcher = get_domino_job_launcher()

    metadata = store.get_request(request_id)
    if metadata is None:
        raise HTTPException(status_code=404, detail=f"Async profile request not found: {request_id}")

    result_payload = store.get_result(request_id)
    if result_payload and metadata.get("status") != "completed":
        metadata = store.update_request(request_id, status="completed", error=None) or metadata

    if result_payload:
        return AsyncProfileStatusResponse(
            request_id=request_id,
            status="completed",
            mode=result_payload.get("mode"),
            domino_job_id=metadata.get("domino_job_id"),
            domino_job_status=metadata.get("domino_job_status"),
            result=result_payload.get("result"),
        )

    status = metadata.get("status", "pending")
    domino_job_id = metadata.get("domino_job_id")
    domino_job_status = metadata.get("domino_job_status")

    if status in {"running", "pending"} and domino_job_id:
        domino_status_result = await launcher.get_job_status(domino_job_id)
        if domino_status_result.get("success"):
            latest_domino_status = domino_status_result.get("domino_job_status")
            if latest_domino_status and latest_domino_status != domino_job_status:
                metadata = store.update_request(
                    request_id,
                    domino_job_status=latest_domino_status,
                ) or metadata
                domino_job_status = latest_domino_status

            if latest_domino_status and latest_domino_status.lower() in {
                "failed",
                "error",
                "killed",
                "stopped",
                "cancelled",
            }:
                error_message = f"Domino profiling job ended with status: {latest_domino_status}"
                metadata = store.update_request(
                    request_id,
                    status="failed",
                    error=error_message,
                ) or metadata
                status = "failed"

    if status == "failed":
        return AsyncProfileStatusResponse(
            request_id=request_id,
            status="failed",
            mode=metadata.get("mode"),
            domino_job_id=metadata.get("domino_job_id"),
            domino_job_status=metadata.get("domino_job_status"),
            error=metadata.get("error") or store.get_error(request_id) or "Async profiling failed",
        )

    return AsyncProfileStatusResponse(
        request_id=request_id,
        status=status,
        mode=metadata.get("mode"),
        domino_job_id=metadata.get("domino_job_id"),
        domino_job_status=metadata.get("domino_job_status"),
    )


@router.post("/profile/async/status", response_model=AsyncProfileStatusResponse)
@handle_errors("Async profiling status error")
async def get_profile_async_status(request: AsyncProfileStatusRequest):
    """Poll async EDA job status/result."""
    return await _build_async_status_response(request.request_id)


@router.get("/profile/async/{request_id}", response_model=AsyncProfileStatusResponse)
@handle_errors("Async profiling status error")
async def get_profile_async_status_get(request_id: str):
    """GET variant for async EDA status polling."""
    return await _build_async_status_response(request_id)
