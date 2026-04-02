"""Job-related Pydantic schemas."""

from datetime import datetime
from typing import Optional, Literal, Any, List, Dict

from pydantic import BaseModel, Field


class HyperparameterTuningConfig(BaseModel):
    """Configuration for hyperparameter optimization (HPO)."""

    enabled: bool = Field(False, description="Enable hyperparameter tuning")
    scheduler: str = Field(
        "local",
        description="HPO scheduler: 'local', 'ray'"
    )
    searcher: str = Field(
        "auto",
        description="HPO search algorithm: 'auto', 'random', 'bayes', 'grid'"
    )
    num_trials: int = Field(
        10, ge=1, le=100,
        description="Number of HPO trials per model"
    )
    max_t: Optional[int] = Field(
        None, ge=1,
        description="Maximum training iterations per trial"
    )
    grace_period: Optional[int] = Field(
        None, ge=1,
        description="Minimum iterations before early stopping"
    )
    reduction_factor: Optional[float] = Field(
        None, ge=1.0,
        description="Early stopping reduction factor"
    )


class PerModelHyperparameters(BaseModel):
    """Per-model hyperparameter configuration."""

    # LightGBM
    lightgbm: Optional[Dict[str, Any]] = Field(
        None,
        description="LightGBM hyperparameters (e.g., {'num_leaves': 31, 'learning_rate': 0.05})"
    )

    # CatBoost
    catboost: Optional[Dict[str, Any]] = Field(
        None,
        description="CatBoost hyperparameters (e.g., {'depth': 6, 'learning_rate': 0.03})"
    )

    # XGBoost
    xgboost: Optional[Dict[str, Any]] = Field(
        None,
        description="XGBoost hyperparameters (e.g., {'max_depth': 6, 'eta': 0.3})"
    )

    # Random Forest
    random_forest: Optional[Dict[str, Any]] = Field(
        None,
        description="Random Forest hyperparameters (e.g., {'n_estimators': 300})"
    )

    # Neural Network (Torch)
    neural_network: Optional[Dict[str, Any]] = Field(
        None,
        description="Neural Network hyperparameters (e.g., {'num_epochs': 50, 'learning_rate': 1e-3})"
    )

    # TabPFN (foundation model)
    tabpfn: Optional[Dict[str, Any]] = Field(
        None,
        description="TabPFN hyperparameters"
    )


class DecisionThresholdConfig(BaseModel):
    """Configuration for decision threshold calibration (binary classification)."""

    enabled: bool = Field(False, description="Enable threshold calibration")
    metric: str = Field(
        "balanced_accuracy",
        description="Metric to optimize: 'f1', 'balanced_accuracy', 'precision', 'recall', 'mcc'"
    )
    thresholds_to_try: int = Field(
        100, ge=10, le=1000,
        description="Number of thresholds to evaluate"
    )


class AdvancedAutoGluonConfig(BaseModel):
    """Advanced AutoGluon configuration options."""

    model_config = {"extra": "ignore"}

    # Resource allocation
    num_gpus: int = Field(0, ge=0, description="Number of GPUs to use")
    num_cpus: Optional[int] = Field(None, ge=1, description="Number of CPUs (auto if None)")

    # Bagging and stacking
    num_bag_folds: Optional[int] = Field(None, ge=2, le=10, description="Number of bagging folds")
    num_bag_sets: Optional[int] = Field(None, ge=1, description="Number of bagging sets")
    num_stack_levels: Optional[int] = Field(None, ge=0, le=3, description="Number of stacking levels")
    auto_stack: bool = Field(False, description="Automatically determine stacking config")
    dynamic_stacking: bool = Field(False, description="Use dynamic stacking for adaptive ensembles")

    # Model selection
    excluded_model_types: List[str] = Field(
        default_factory=list,
        description="Model types to exclude (e.g., ['NN_TORCH', 'CAT'])"
    )
    included_model_types: List[str] = Field(
        default_factory=list,
        description="Only include these model types"
    )

    # Hyperparameters
    hyperparameters: Optional[Dict[str, Any]] = Field(
        None,
        description="Custom hyperparameters for specific models"
    )
    hyperparameter_tune_kwargs: Optional[Dict[str, Any]] = Field(
        None,
        description="Hyperparameter tuning configuration"
    )

    # NEW: Hyperparameter tuning (HPO) configuration
    hpo_config: Optional[HyperparameterTuningConfig] = Field(
        None,
        description="Hyperparameter optimization configuration"
    )

    # NEW: Per-model hyperparameters
    per_model_hyperparameters: Optional[PerModelHyperparameters] = Field(
        None,
        description="Model-specific hyperparameter overrides"
    )

    # Early stopping / ag_args_fit
    ag_args_fit: Optional[Dict[str, Any]] = Field(
        None,
        description="Extra arguments passed to model .fit() (e.g., early stopping)"
    )

    # Feature engineering
    feature_generator: Optional[str] = Field(
        None,
        description="Feature generator type override"
    )
    feature_prune: bool = Field(False, description="Enable feature pruning")

    # Post-training
    calibrate: bool = Field(False, description="Calibrate model probabilities")
    refit_full: bool = Field(False, description="Refit on full data after training")
    set_best_to_refit_full: bool = Field(False, description="Use refit model as best")

    # NEW: Decision threshold calibration
    threshold_config: Optional[DecisionThresholdConfig] = Field(
        None,
        description="Decision threshold calibration for binary classification"
    )

    # Training behavior
    holdout_frac: Optional[float] = Field(
        None, ge=0.01, le=0.5,
        description="Fraction of data to hold out for validation"
    )
    use_bag_holdout: bool = Field(False, description="Use bag holdout for validation")

    # NEW: Pseudo-labeling for semi-supervised learning
    pseudo_labeling: bool = Field(False, description="Enable pseudo-labeling with unlabeled data")
    unlabeled_data_path: Optional[str] = Field(
        None,
        description="Path to unlabeled data for pseudo-labeling"
    )

    # Feature engineering
    feature_generator_kwargs: Optional[Dict[str, Any]] = Field(
        None,
        description="Custom feature generator configuration"
    )

    # NEW: Feature metadata for custom column types
    feature_metadata: Optional[Dict[str, str]] = Field(
        None,
        description="Custom feature types: {'col1': 'category', 'col2': 'numeric'}"
    )

    # NEW: Drop unique/high-cardinality features
    drop_unique: bool = Field(False, description="Automatically drop high-cardinality features")

    # Memory optimization
    cache_data: bool = Field(True, description="Cache data in memory")
    infer_limit: Optional[float] = Field(
        None, ge=0.001,
        description="Inference time limit per row in seconds"
    )

    # Verbosity
    verbosity: int = Field(2, ge=0, le=4, description="Logging verbosity (0-4)")

    # Class imbalance handling
    class_imbalance_strategy: Optional[str] = Field(
        None,
        description="Strategy for handling class imbalance: 'oversample', 'undersample', 'smote', 'focal_loss'"
    )
    sample_weight_column: Optional[str] = Field(
        None,
        description="Column containing sample weights"
    )

    # Distillation (knowledge transfer from ensemble to single model)
    distill: bool = Field(False, description="Enable knowledge distillation")
    distill_time_limit: Optional[int] = Field(
        None, ge=60,
        description="Time limit for distillation in seconds"
    )

    # Feature pruning
    feature_prune_kwargs: Optional[Dict[str, Any]] = Field(
        None,
        description="Feature pruning configuration"
    )

    # NEW: Foundation model options (2025 presets)
    use_tabular_foundation_models: bool = Field(
        False,
        description="Use foundation models like TabPFN for tabular data"
    )
    foundation_model_preset: Optional[str] = Field(
        None,
        description="Foundation model preset: 'zeroshot', 'zeroshot_hpo'"
    )


class TimeSeriesAdvancedConfig(BaseModel):
    """Advanced configuration for time series models."""

    # Forecasting
    freq: Optional[str] = Field(
        None,
        description="Time series frequency (e.g., 'D', 'H', 'M')"
    )
    known_covariates_names: List[str] = Field(
        default_factory=list,
        description="Known future covariates"
    )
    static_features_names: List[str] = Field(
        default_factory=list,
        description="Static features for each time series"
    )

    # Quantile prediction
    quantile_levels: List[float] = Field(
        default_factory=lambda: [0.1, 0.5, 0.9],
        description="Quantile levels for probabilistic forecasting"
    )

    # Preprocessing
    target_scaler: Optional[str] = Field(
        None,
        description="Target scaling: 'mean_abs', 'standard', 'min_max', 'identity'"
    )

    # Model selection
    enable_ensemble: bool = Field(True, description="Enable ensemble of models")
    skip_model_selection: bool = Field(False, description="Skip model selection")

    # Chronos options (foundation model)
    use_chronos: bool = Field(False, description="Include Chronos foundation model")
    chronos_model_size: str = Field(
        "tiny",
        description="Chronos model size: 'tiny', 'mini', 'small', 'base', 'large'"
    )


class JobCreateRequest(BaseModel):
    """Request schema for creating a training job."""

    name: str = Field(..., min_length=1, max_length=255, description="Job name")
    description: Optional[str] = Field(None, description="Job description")

    # Model type
    model_type: Literal["tabular", "timeseries"] = Field(
        ..., description="AutoGluon model type"
    )
    problem_type: Optional[Literal["binary", "multiclass", "regression", "quantile"]] = Field(
        None, description="Problem type (auto-detected if not specified)"
    )

    # Data source
    data_source: Literal["upload", "domino_dataset", "mounted"] = Field(
        ..., description="Data source type"
    )
    dataset_id: Optional[str] = Field(
        None, description="Domino dataset ID (if data_source is 'domino_dataset')"
    )
    file_path: Optional[str] = Field(
        None, description="File path (if data_source is 'upload' or 'mounted')"
    )

    # Training configuration
    target_column: str = Field(..., description="Target column name")
    time_column: Optional[str] = Field(
        None, description="Time column (required for timeseries)"
    )
    id_column: Optional[str] = Field(
        None, description="ID column for timeseries (entity identifier)"
    )
    prediction_length: Optional[int] = Field(
        None, ge=1, description="Prediction horizon for timeseries"
    )
    feature_columns: Optional[List[str]] = Field(
        None, description="Specific features to use (all if None)"
    )

    # AutoGluon settings
    preset: Literal[
        "best_quality",
        "high_quality",
        "good_quality",
        "medium_quality_faster_train",
        "optimize_for_deployment",
        "chronos",
        "fast_training",
        # 2025 presets with foundation models
        "zeroshot",
        "zeroshot_hpo",
        "experimental_tabfm",
    ] = Field(
        "medium_quality_faster_train", description="AutoGluon preset"
    )
    time_limit: Optional[int] = Field(
        3600, ge=60, description="Time limit in seconds"
    )
    eval_metric: Optional[str] = Field(
        None, description="Evaluation metric (auto-detected if not specified)"
    )

    # Advanced configuration
    advanced_config: Optional[AdvancedAutoGluonConfig] = Field(
        None, description="Advanced AutoGluon configuration"
    )
    timeseries_config: Optional[TimeSeriesAdvancedConfig] = Field(
        None, description="Time series specific configuration"
    )

    # Experiment tracking
    experiment_name: Optional[str] = Field(
        None, description="MLflow experiment name"
    )

    # Model registration
    auto_register: bool = Field(
        False, description="Automatically register model to Domino registry"
    )
    register_name: Optional[str] = Field(
        None, description="Name for registered model"
    )

    domino_hardware_tier_name: Optional[str] = Field(
        None,
        description="Optional Domino hardware tier name for external training jobs",
    )
    domino_environment_id: Optional[str] = Field(
        None,
        description="Optional Domino environment ID for external training jobs",
    )
    enable_mlflow: bool = Field(
        False,
        description="Enable MLflow experiment tracking for this job",
    )


class JobResponse(BaseModel):
    """Response schema for a job."""

    id: str
    name: str
    description: Optional[str] = None
    owner: Optional[str] = None
    project_id: Optional[str] = None
    project_name: Optional[str] = None
    model_type: str
    problem_type: Optional[str] = None
    status: str
    domino_job_id: Optional[str] = None
    domino_job_url: Optional[str] = None
    domino_job_status: Optional[str] = None
    progress: Optional[int] = None
    current_step: Optional[str] = None
    data_source: str
    dataset_id: Optional[str] = None
    file_path: Optional[str] = None
    target_column: str
    time_column: Optional[str] = None
    id_column: Optional[str] = None
    prediction_length: Optional[int] = None
    feature_columns: Optional[List[str]] = None
    preset: str
    time_limit: Optional[int] = None
    eval_metric: Optional[str] = None
    metrics: Optional[Dict[str, Any]] = None
    leaderboard: Optional[List[Dict[str, Any]]] = None
    model_path: Optional[str] = None
    experiment_name: Optional[str] = None
    experiment_id: Optional[str] = None
    experiment_run_id: Optional[str] = None
    experiment_run_url: Optional[str] = None
    enable_mlflow: bool = False
    error_message: Optional[str] = None
    advanced_config: Optional[Dict[str, Any]] = None
    timeseries_config: Optional[Dict[str, Any]] = None
    is_registered: bool = False
    registered_model_name: Optional[str] = None
    registered_model_version: Optional[str] = None
    model_registry_url: Optional[str] = None
    created_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class JobStatusResponse(BaseModel):
    """Response schema for job status."""

    id: str
    status: str
    domino_job_status: Optional[str] = None
    error_message: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class JobMetricsResponse(BaseModel):
    """Response schema for job metrics."""

    id: str
    metrics: Optional[dict[str, Any]] = None
    leaderboard: Optional[list[dict[str, Any]]] = None


class JobLogResponse(BaseModel):
    """Response schema for job logs."""

    id: int
    job_id: str
    level: str
    message: str
    timestamp: datetime

    class Config:
        from_attributes = True


class JobListRequest(BaseModel):
    """Request schema for listing jobs."""

    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(100, ge=1, le=1000, description="Maximum records to return")
    status: Optional[str] = Field(None, description="Filter by status")
    model_type: Optional[str] = Field(None, description="Filter by model type")
    owner: Optional[str] = Field(None, description="Filter by owner username (from domino-username header)")
    project_id: Optional[str] = Field(None, description="Filter by project ID")
    project_name: Optional[str] = Field(None, description="Filter by project name")


class CleanupRequest(BaseModel):
    """Request schema for bulk job cleanup."""

    statuses: List[str] = Field(
        default_factory=lambda: ["failed", "cancelled"],
        description="Job statuses to clean up",
    )
    older_than_days: Optional[int] = Field(
        None,
        description="Only include jobs older than this many days",
    )
    include_orphans: bool = Field(
        False,
        description="Also clean orphaned artifacts",
    )


class BulkDeleteJobsRequest(BaseModel):
    """Request schema for bulk job deletion."""

    job_ids: List[str] = Field(
        ..., min_length=1,
        description="List of job IDs to delete",
    )


class BulkDeleteJobsResponse(BaseModel):
    """Response schema for bulk job deletion."""

    deleted_job_ids: List[str] = Field(
        default_factory=list,
        description="IDs of successfully deleted jobs",
    )
    failed: List[Dict[str, str]] = Field(
        default_factory=list,
        description="Jobs that failed to delete, with job_id and error",
    )


class JobListResponse(BaseModel):
    """Response schema for job list."""

    jobs: List[JobResponse]
    total: int
    skip: int
    limit: int


class JobProgressResponse(BaseModel):
    """Response schema for job progress."""

    id: str
    status: str
    progress: int = Field(0, ge=0, le=100, description="Progress percentage")
    current_step: Optional[str] = None
    models_trained: int = 0
    current_model: Optional[str] = None
    eta_seconds: Optional[int] = None
    started_at: Optional[datetime] = None


class RegisterModelRequest(BaseModel):
    """Request schema for registering a trained model."""

    job_id: str = Field(..., description="ID of the completed job")
    model_name: str = Field(..., min_length=1, max_length=255, description="Name for registered model")
    description: Optional[str] = Field(None, description="Model description")
    stage: Optional[Literal["None", "Staging", "Production"]] = Field(
        None, description="Initial stage for the model"
    )


class RegisterModelResponse(BaseModel):
    """Response schema for model registration."""

    success: bool
    model_name: str
    version: Optional[str] = None
    run_id: Optional[str] = None
    artifact_uri: Optional[str] = None
    stage: Optional[str] = None
    error: Optional[str] = None
