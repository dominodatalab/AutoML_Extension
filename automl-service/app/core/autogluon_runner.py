"""AutoGluon training execution logic with advanced parameters and experiment tracking."""

import logging
import os
import json
import asyncio
from datetime import datetime
from typing import Any, Callable, Optional, Dict, List
from dataclasses import dataclass, field

import pandas as pd
import numpy as np
import mlflow

from app.config import get_settings
from app.db.models import ModelType, ProblemType

logger = logging.getLogger(__name__)


@dataclass
class HpoConfig:
    """Hyperparameter optimization configuration."""
    enabled: bool = False
    scheduler: str = "local"
    searcher: str = "auto"
    num_trials: int = 10
    max_t: Optional[int] = None
    grace_period: Optional[int] = None
    reduction_factor: Optional[float] = None


@dataclass
class ThresholdConfig:
    """Decision threshold calibration configuration."""
    enabled: bool = False
    metric: str = "balanced_accuracy"
    thresholds_to_try: int = 100


@dataclass
class AdvancedConfig:
    """Advanced AutoGluon configuration options."""
    # General
    num_gpus: int = 0
    num_cpus: Optional[int] = None
    verbosity: int = 2

    # Training
    num_bag_folds: Optional[int] = None
    num_bag_sets: Optional[int] = None
    num_stack_levels: Optional[int] = None
    holdout_frac: Optional[float] = None
    auto_stack: bool = False
    dynamic_stacking: bool = False

    # Model selection
    excluded_model_types: List[str] = field(default_factory=list)
    included_model_types: List[str] = field(default_factory=list)

    # Hyperparameters
    hyperparameters: Optional[Dict[str, Any]] = None
    hyperparameter_tune_kwargs: Optional[Dict[str, Any]] = None

    # NEW: Hyperparameter tuning (HPO)
    hpo_config: Optional[HpoConfig] = None

    # NEW: Per-model hyperparameters
    per_model_hyperparameters: Optional[Dict[str, Dict[str, Any]]] = None

    # Early stopping
    ag_args_fit: Optional[Dict[str, Any]] = None

    # Feature engineering
    feature_generator: Optional[str] = None
    feature_generator_kwargs: Optional[Dict[str, Any]] = None
    feature_prune: bool = False
    feature_prune_kwargs: Optional[Dict[str, Any]] = None
    feature_metadata: Optional[Dict[str, str]] = None
    drop_unique: bool = False

    # Calibration
    calibrate: bool = False

    # NEW: Decision threshold calibration
    threshold_config: Optional[ThresholdConfig] = None

    # Ensemble
    refit_full: bool = False
    set_best_to_refit_full: bool = False

    # NEW: Pseudo-labeling
    pseudo_labeling: bool = False
    unlabeled_data_path: Optional[str] = None

    # NEW: Foundation models (2025)
    use_tabular_foundation_models: bool = False
    foundation_model_preset: Optional[str] = None

    # Class imbalance
    class_imbalance_strategy: Optional[str] = None
    sample_weight_column: Optional[str] = None

    # Distillation
    distill: bool = False
    distill_time_limit: Optional[int] = None

    # Use bag holdout
    use_bag_holdout: bool = False

    # Inference limit
    infer_limit: Optional[float] = None

    # Cache data
    cache_data: bool = True


class TrainingProgressCallback:
    """Callback for tracking training progress."""

    def __init__(self, job_id: str, log_callback: Optional[Callable] = None):
        self.job_id = job_id
        self.log_callback = log_callback
        self.start_time = datetime.now()
        self.models_trained = 0
        self.current_model = None
        self.progress_percent = 0
        self.metrics_history: List[Dict] = []

    def on_model_trained(self, model_name: str, score: float):
        """Called when a model finishes training."""
        self.models_trained += 1
        self.current_model = model_name

        entry = {
            "timestamp": datetime.now().isoformat(),
            "model": model_name,
            "score": score,
            "models_trained": self.models_trained
        }
        self.metrics_history.append(entry)

        if self.log_callback:
            asyncio.create_task(
                self.log_callback(f"Trained model: {model_name} (score: {score:.4f})")
            )

    def on_progress(self, percent: float, message: str):
        """Called to update progress percentage."""
        self.progress_percent = percent
        if self.log_callback:
            asyncio.create_task(self.log_callback(f"[{percent:.0f}%] {message}"))

    def get_elapsed_time(self) -> float:
        """Get elapsed time in seconds."""
        return (datetime.now() - self.start_time).total_seconds()

    def to_dict(self) -> Dict[str, Any]:
        """Export progress info as dictionary."""
        return {
            "job_id": self.job_id,
            "models_trained": self.models_trained,
            "current_model": self.current_model,
            "progress_percent": self.progress_percent,
            "elapsed_seconds": self.get_elapsed_time(),
            "metrics_history": self.metrics_history
        }


class AutoGluonRunner:
    """Runs AutoGluon training for different model types with advanced configuration."""

    def __init__(self):
        self.settings = get_settings()
        self._active_progress: Dict[str, TrainingProgressCallback] = {}

    def get_progress(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Get training progress for a job."""
        if job_id in self._active_progress:
            return self._active_progress[job_id].to_dict()
        return None

    async def run_training(
        self,
        job_id: str,
        model_type: ModelType,
        data_path: str,
        target_column: str,
        time_column: Optional[str] = None,
        id_column: Optional[str] = None,
        prediction_length: Optional[int] = None,
        problem_type: Optional[ProblemType] = None,
        preset: str = "medium_quality_faster_train",
        time_limit: Optional[int] = None,
        eval_metric: Optional[str] = None,
        advanced_config: Optional[AdvancedConfig] = None,
        timeseries_config: Optional[Dict[str, Any]] = None,
        multimodal_config: Optional[Dict[str, Any]] = None,
        log_callback: Optional[Callable] = None,
    ) -> dict[str, Any]:
        """
        Run AutoGluon training based on model type with advanced options.

        Returns:
            dict with keys: metrics, leaderboard, model_path, predictor, feature_importance
        """
        # Initialize progress tracking
        progress = TrainingProgressCallback(job_id, log_callback)
        self._active_progress[job_id] = progress

        try:
            # Load data
            logger.info(f"Loading data from {data_path}")
            df = self._load_data(data_path)
            logger.info(f"Loaded {len(df)} rows with columns: {list(df.columns)}")

            # Create model save path
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            model_path = os.path.join(
                self.settings.models_path,
                f"job_{job_id}_{timestamp}",
            )
            os.makedirs(model_path, exist_ok=True)

            # Use default advanced config if not provided
            if advanced_config is None:
                advanced_config = AdvancedConfig()

            # Log to MLflow
            self._log_training_start(job_id, model_type, df, advanced_config)

            if model_type == ModelType.TABULAR:
                result = await self._run_tabular_training(
                    df=df,
                    target_column=target_column,
                    model_path=model_path,
                    problem_type=problem_type,
                    preset=preset,
                    time_limit=time_limit,
                    eval_metric=eval_metric,
                    advanced_config=advanced_config,
                    progress=progress,
                )
            elif model_type == ModelType.TIMESERIES:
                result = await self._run_timeseries_training(
                    df=df,
                    target_column=target_column,
                    time_column=time_column,
                    id_column=id_column,
                    prediction_length=prediction_length,
                    model_path=model_path,
                    preset=preset,
                    time_limit=time_limit,
                    eval_metric=eval_metric,
                    advanced_config=advanced_config,
                    timeseries_config=timeseries_config,
                    progress=progress,
                )
            elif model_type == ModelType.MULTIMODAL:
                result = await self._run_multimodal_training(
                    df=df,
                    target_column=target_column,
                    model_path=model_path,
                    problem_type=problem_type,
                    preset=preset,
                    time_limit=time_limit,
                    eval_metric=eval_metric,
                    advanced_config=advanced_config,
                    multimodal_config=multimodal_config,
                    progress=progress,
                )
            else:
                raise ValueError(f"Unsupported model type: {model_type}")

            # Log final metrics to MLflow
            self._log_training_end(result)

            return result

        finally:
            # Clean up progress tracking
            if job_id in self._active_progress:
                del self._active_progress[job_id]

    def _load_data(self, data_path: str) -> pd.DataFrame:
        """Load data from file with format detection."""
        if data_path.endswith(".csv"):
            return pd.read_csv(data_path)
        elif data_path.endswith((".parquet", ".pq")):
            return pd.read_parquet(data_path)
        elif data_path.endswith(".json"):
            return pd.read_json(data_path)
        elif data_path.endswith((".xlsx", ".xls")):
            return pd.read_excel(data_path)
        else:
            # Try CSV as default
            try:
                return pd.read_csv(data_path)
            except Exception:
                raise ValueError(f"Unsupported file format: {data_path}")

    def _log_training_start(
        self,
        job_id: str,
        model_type: ModelType,
        df: pd.DataFrame,
        config: AdvancedConfig
    ):
        """Log training start to MLflow."""
        try:
            mlflow.log_param("job_id", job_id)
            mlflow.log_param("model_type", model_type.value)
            mlflow.log_param("num_rows", len(df))
            mlflow.log_param("num_columns", len(df.columns))
            mlflow.log_param("num_gpus", config.num_gpus)

            if config.num_bag_folds:
                mlflow.log_param("num_bag_folds", config.num_bag_folds)
            if config.holdout_frac:
                mlflow.log_param("holdout_frac", config.holdout_frac)

            # Log column info
            mlflow.log_param("columns", json.dumps(list(df.columns)[:50]))  # Limit to 50
        except Exception as e:
            logger.warning(f"Could not log to MLflow: {e}")

    def _log_training_end(self, result: Dict[str, Any]):
        """Log training results to MLflow."""
        try:
            metrics = result.get("metrics", {})
            for key, value in metrics.items():
                if isinstance(value, (int, float)) and not np.isnan(value):
                    mlflow.log_metric(key, value)

            # Log leaderboard as artifact
            leaderboard = result.get("leaderboard", {})
            if leaderboard:
                leaderboard_path = "/tmp/leaderboard.json"
                with open(leaderboard_path, "w") as f:
                    json.dump(leaderboard, f, indent=2, default=str)
                mlflow.log_artifact(leaderboard_path)

            # Log feature importance if available
            if "feature_importance" in result:
                fi_path = "/tmp/feature_importance.json"
                with open(fi_path, "w") as f:
                    json.dump(result["feature_importance"], f, indent=2)
                mlflow.log_artifact(fi_path)

        except Exception as e:
            logger.warning(f"Could not log results to MLflow: {e}")

    async def _run_tabular_training(
        self,
        df: pd.DataFrame,
        target_column: str,
        model_path: str,
        problem_type: Optional[ProblemType] = None,
        preset: str = "medium_quality_faster_train",
        time_limit: Optional[int] = None,
        eval_metric: Optional[str] = None,
        advanced_config: AdvancedConfig = None,
        progress: TrainingProgressCallback = None,
    ) -> dict[str, Any]:
        """Run tabular prediction training with advanced options."""
        from autogluon.tabular import TabularPredictor

        logger.info("Starting TabularPredictor training")
        if progress:
            progress.on_progress(5, "Initializing TabularPredictor")

        # Configure predictor
        predictor_kwargs = {
            "label": target_column,
            "path": model_path,
            "verbosity": advanced_config.verbosity if advanced_config else 2,
        }

        if problem_type:
            predictor_kwargs["problem_type"] = problem_type.value

        if eval_metric:
            predictor_kwargs["eval_metric"] = eval_metric

        # Create predictor
        predictor = TabularPredictor(**predictor_kwargs)

        # Configure fit parameters
        fit_kwargs = {
            "train_data": df,
            "presets": preset,
        }

        if time_limit:
            fit_kwargs["time_limit"] = time_limit

        # Apply advanced configuration
        if advanced_config:
            if advanced_config.num_gpus > 0:
                fit_kwargs["num_gpus"] = advanced_config.num_gpus

            if advanced_config.num_cpus:
                fit_kwargs["num_cpus"] = advanced_config.num_cpus

            if advanced_config.num_bag_folds:
                fit_kwargs["num_bag_folds"] = advanced_config.num_bag_folds

            if advanced_config.num_bag_sets:
                fit_kwargs["num_bag_sets"] = advanced_config.num_bag_sets

            if advanced_config.num_stack_levels:
                fit_kwargs["num_stack_levels"] = advanced_config.num_stack_levels

            if advanced_config.holdout_frac:
                fit_kwargs["holdout_frac"] = advanced_config.holdout_frac

            if advanced_config.auto_stack:
                fit_kwargs["auto_stack"] = True

            if advanced_config.excluded_model_types:
                fit_kwargs["excluded_model_types"] = advanced_config.excluded_model_types

            if advanced_config.included_model_types:
                fit_kwargs["included_model_types"] = advanced_config.included_model_types

            if advanced_config.hyperparameters:
                fit_kwargs["hyperparameters"] = advanced_config.hyperparameters

            if advanced_config.hyperparameter_tune_kwargs:
                fit_kwargs["hyperparameter_tune_kwargs"] = advanced_config.hyperparameter_tune_kwargs

            if advanced_config.ag_args_fit:
                # Merge with existing ag_args_fit if present
                if "ag_args_fit" in fit_kwargs:
                    fit_kwargs["ag_args_fit"].update(advanced_config.ag_args_fit)
                else:
                    fit_kwargs["ag_args_fit"] = dict(advanced_config.ag_args_fit)

            if advanced_config.calibrate:
                fit_kwargs["calibrate"] = True

            if advanced_config.feature_prune:
                fit_kwargs["feature_prune"] = True

            # Feature generator kwargs
            if advanced_config.feature_generator_kwargs:
                fit_kwargs["feature_generator_kwargs"] = advanced_config.feature_generator_kwargs

            # Feature prune kwargs
            if advanced_config.feature_prune_kwargs:
                fit_kwargs["feature_prune_kwargs"] = advanced_config.feature_prune_kwargs

            # NEW: Dynamic stacking
            if advanced_config.dynamic_stacking:
                fit_kwargs["dynamic_stacking"] = True

            # NEW: Use bag holdout
            if advanced_config.use_bag_holdout:
                fit_kwargs["use_bag_holdout"] = True

            # NEW: Refit full
            if advanced_config.refit_full:
                fit_kwargs["refit_full"] = True

            # NEW: Set best to refit full
            if advanced_config.set_best_to_refit_full:
                fit_kwargs["set_best_to_refit_full"] = True

            # NEW: Inference limit
            if advanced_config.infer_limit:
                fit_kwargs["infer_limit"] = advanced_config.infer_limit

            # NEW: HPO configuration
            if advanced_config.hpo_config and advanced_config.hpo_config.enabled:
                hpo = advanced_config.hpo_config
                hpo_kwargs = {
                    "scheduler": hpo.scheduler,
                    "searcher": hpo.searcher,
                    "num_trials": hpo.num_trials,
                }
                if hpo.max_t:
                    hpo_kwargs["max_t"] = hpo.max_t
                if hpo.grace_period:
                    hpo_kwargs["grace_period"] = hpo.grace_period
                if hpo.reduction_factor:
                    hpo_kwargs["reduction_factor"] = hpo.reduction_factor
                fit_kwargs["hyperparameter_tune_kwargs"] = hpo_kwargs

            # NEW: Per-model hyperparameters
            if advanced_config.per_model_hyperparameters:
                model_hps = {}
                hp_map = {
                    "lightgbm": "GBM",
                    "catboost": "CAT",
                    "xgboost": "XGB",
                    "random_forest": "RF",
                    "neural_network": "NN_TORCH",
                    "tabpfn": "TABPFN",
                }
                for model_key, hps in advanced_config.per_model_hyperparameters.items():
                    if hps and model_key in hp_map:
                        model_hps[hp_map[model_key]] = hps
                if model_hps:
                    fit_kwargs["hyperparameters"] = model_hps

            # NEW: Class imbalance handling
            if advanced_config.class_imbalance_strategy:
                strategy = advanced_config.class_imbalance_strategy
                # Ensure ag_args_fit exists
                if "ag_args_fit" not in fit_kwargs:
                    fit_kwargs["ag_args_fit"] = {}

                if strategy == "focal_loss":
                    # Use focal loss for neural networks
                    fit_kwargs["ag_args_fit"]["use_focal_loss"] = True
                    logger.info("Using focal loss for class imbalance")
                elif strategy == "oversample":
                    fit_kwargs["ag_args_fit"]["class_weight"] = "balanced"
                    logger.info("Using oversampling via balanced class weights")
                elif strategy == "undersample":
                    fit_kwargs["ag_args_fit"]["class_weight"] = "balanced"
                    logger.info("Using undersampling via balanced class weights")
                elif strategy == "smote":
                    # SMOTE requires imblearn, log a warning if not available
                    try:
                        from imblearn.over_sampling import SMOTE
                        fit_kwargs["ag_args_fit"]["use_smote"] = True
                        logger.info("SMOTE enabled for class imbalance")
                    except ImportError:
                        logger.warning("SMOTE requires imblearn. Install with: pip install imbalanced-learn")
                        fit_kwargs["ag_args_fit"]["class_weight"] = "balanced"

            # NEW: Sample weight column
            if advanced_config.sample_weight_column:
                fit_kwargs["sample_weight"] = advanced_config.sample_weight_column

            # NEW: Drop unique/high-cardinality features
            if advanced_config.drop_unique:
                fit_kwargs["drop_unique"] = True

            # NEW: Cache data in memory
            if advanced_config.cache_data is False:
                fit_kwargs["cache_data"] = False

            # NEW: Feature metadata for custom column types
            if advanced_config.feature_metadata:
                from autogluon.common.features.types import R_CATEGORY, R_INT, R_FLOAT
                feature_metadata = {}
                type_map = {
                    "category": R_CATEGORY,
                    "int": R_INT,
                    "float": R_FLOAT,
                }
                for col, col_type in advanced_config.feature_metadata.items():
                    if col_type in type_map:
                        feature_metadata[col] = type_map[col_type]
                if feature_metadata:
                    fit_kwargs["feature_metadata"] = feature_metadata

            # NEW: Foundation models (TabPFN, etc.)
            if advanced_config.use_tabular_foundation_models:
                if "hyperparameters" not in fit_kwargs:
                    fit_kwargs["hyperparameters"] = {}
                # Add TabPFN to the hyperparameters
                fit_kwargs["hyperparameters"]["TABPFN"] = {}
                logger.info("Added TabPFN foundation model to training")

                # If using zeroshot preset, configure accordingly
                if advanced_config.foundation_model_preset:
                    if advanced_config.foundation_model_preset == "zeroshot":
                        # Use only TabPFN for zero-shot
                        fit_kwargs["hyperparameters"] = {"TABPFN": {}}
                        fit_kwargs["num_bag_folds"] = 0
                        fit_kwargs["num_stack_levels"] = 0
                        logger.info("Using zero-shot foundation model preset")
                    elif advanced_config.foundation_model_preset == "zeroshot_hpo":
                        fit_kwargs["hyperparameters"] = {"TABPFN": {}}
                        if "hyperparameter_tune_kwargs" not in fit_kwargs:
                            fit_kwargs["hyperparameter_tune_kwargs"] = {
                                "scheduler": "local",
                                "searcher": "auto",
                                "num_trials": 5,
                            }
                        logger.info("Using zero-shot + HPO foundation model preset")

            # NEW: Pseudo-labeling for semi-supervised learning
            if advanced_config.pseudo_labeling and advanced_config.unlabeled_data_path:
                try:
                    unlabeled_df = self._load_data(advanced_config.unlabeled_data_path)
                    fit_kwargs["unlabeled_data"] = unlabeled_df
                    logger.info(f"Loaded {len(unlabeled_df)} rows of unlabeled data for pseudo-labeling")
                except Exception as e:
                    logger.warning(f"Could not load unlabeled data: {e}")

            # NEW: Distillation
            if advanced_config.distill:
                fit_kwargs["ds_args"] = {"distill": True}
                if advanced_config.distill_time_limit:
                    fit_kwargs["ds_args"]["time_limit"] = advanced_config.distill_time_limit

        if progress:
            progress.on_progress(10, "Starting model training")

        # Train
        predictor.fit(**fit_kwargs)

        # NEW: Post-training decision threshold calibration
        if (advanced_config and
            advanced_config.threshold_config and
            advanced_config.threshold_config.enabled and
            problem_type and problem_type.value == "binary"):
            try:
                if progress:
                    progress.on_progress(85, "Calibrating decision threshold")
                threshold_config = advanced_config.threshold_config
                predictor.calibrate_decision_threshold(
                    metric=threshold_config.metric,
                    thresholds_to_try=threshold_config.thresholds_to_try,
                )
                logger.info(f"Decision threshold calibrated for {threshold_config.metric}")
            except Exception as e:
                logger.warning(f"Could not calibrate decision threshold: {e}")

        if progress:
            progress.on_progress(80, "Training complete, computing metrics")

        # Get results
        leaderboard = predictor.leaderboard(silent=True)
        best_model = leaderboard.iloc[0] if len(leaderboard) > 0 else None

        # Get feature importance
        feature_importance = None
        try:
            fi = predictor.feature_importance(silent=True)
            if fi is not None and len(fi) > 0:
                feature_importance = [
                    {"feature": idx, "importance": float(row.iloc[0]) if hasattr(row, 'iloc') else float(row)}
                    for idx, row in fi.iterrows()
                ]
                feature_importance.sort(key=lambda x: abs(x["importance"]), reverse=True)
        except Exception as e:
            logger.warning(f"Could not compute feature importance: {e}")

        metrics = {
            "best_model": best_model["model"] if best_model is not None else None,
            "best_score": float(best_model["score_val"]) if best_model is not None else None,
            "problem_type": predictor.problem_type,
            "eval_metric": str(predictor.eval_metric) if hasattr(predictor.eval_metric, '__str__') else predictor.eval_metric,
            "num_models": len(leaderboard),
            "num_features": len(predictor.feature_metadata.get_features()) if predictor.feature_metadata else 0,
        }

        # Note: Per-model scores are logged by experiment_tracker.log_training_results
        # Each model gets its own MLflow run with score_val (matching notebook pattern)

        # Return leaderboard as list (schema expects List[Dict])
        leaderboard_list = leaderboard.to_dict(orient="records")

        if progress:
            progress.on_progress(100, "Training completed successfully")

        logger.info(f"Training completed. Best model: {metrics['best_model']}")

        # Refit on full data if requested
        if advanced_config and advanced_config.refit_full:
            logger.info("Refitting best model on full dataset")
            predictor.refit_full()

        return {
            "metrics": metrics,
            "leaderboard": leaderboard_list,
            "model_path": model_path,
            "predictor": predictor,
            "feature_importance": feature_importance,
        }

    async def _run_timeseries_training(
        self,
        df: pd.DataFrame,
        target_column: str,
        time_column: Optional[str],
        id_column: Optional[str],
        prediction_length: Optional[int],
        model_path: str,
        preset: str = "medium_quality",
        time_limit: Optional[int] = None,
        eval_metric: Optional[str] = None,
        advanced_config: AdvancedConfig = None,
        timeseries_config: Optional[Dict[str, Any]] = None,
        progress: TrainingProgressCallback = None,
    ) -> dict[str, Any]:
        """Run time series prediction training."""
        from autogluon.timeseries import TimeSeriesPredictor, TimeSeriesDataFrame

        logger.info("Starting TimeSeriesPredictor training")
        if progress:
            progress.on_progress(5, "Initializing TimeSeriesPredictor")

        if not time_column:
            raise ValueError("time_column is required for timeseries models")
        if not prediction_length:
            raise ValueError("prediction_length is required for timeseries models")

        # Convert to TimeSeriesDataFrame
        ts_df = TimeSeriesDataFrame.from_data_frame(
            df,
            id_column=id_column,
            timestamp_column=time_column,
        )

        # Configure predictor
        predictor_kwargs = {
            "target": target_column,
            "prediction_length": prediction_length,
            "path": model_path,
            "verbosity": advanced_config.verbosity if advanced_config else 2,
        }

        if eval_metric:
            predictor_kwargs["eval_metric"] = eval_metric

        # Apply timeseries-specific config to predictor
        if timeseries_config:
            if timeseries_config.get("freq"):
                predictor_kwargs["freq"] = timeseries_config["freq"]
            if timeseries_config.get("quantile_levels"):
                predictor_kwargs["quantile_levels"] = timeseries_config["quantile_levels"]

        # Create predictor
        predictor = TimeSeriesPredictor(**predictor_kwargs)

        # Configure fit parameters
        fit_kwargs = {
            "train_data": ts_df,
            "presets": preset,
        }

        if time_limit:
            fit_kwargs["time_limit"] = time_limit

        # Apply advanced configuration
        if advanced_config:
            if advanced_config.num_gpus > 0:
                fit_kwargs["num_gpus"] = advanced_config.num_gpus

            if advanced_config.excluded_model_types:
                fit_kwargs["excluded_model_types"] = advanced_config.excluded_model_types

            if advanced_config.hyperparameters:
                fit_kwargs["hyperparameters"] = advanced_config.hyperparameters

        # Apply timeseries-specific config to fit
        if timeseries_config:
            # Known covariates
            if timeseries_config.get("known_covariates_names"):
                fit_kwargs["known_covariates_names"] = timeseries_config["known_covariates_names"]

            # Static features
            if timeseries_config.get("static_features_names"):
                fit_kwargs["static_features_names"] = timeseries_config["static_features_names"]

            # Target scaler
            if timeseries_config.get("target_scaler"):
                fit_kwargs["target_scaler"] = timeseries_config["target_scaler"]

            # Enable ensemble
            if timeseries_config.get("enable_ensemble") is False:
                fit_kwargs["enable_ensemble"] = False

            # Skip model selection
            if timeseries_config.get("skip_model_selection"):
                fit_kwargs["skip_model_selection"] = True

            # Chronos foundation model
            if timeseries_config.get("use_chronos"):
                chronos_size = timeseries_config.get("chronos_model_size", "tiny")
                # Add Chronos to hyperparameters
                if "hyperparameters" not in fit_kwargs:
                    fit_kwargs["hyperparameters"] = {}
                fit_kwargs["hyperparameters"]["Chronos"] = {
                    "model_path": f"amazon/chronos-t5-{chronos_size}"
                }
                logger.info(f"Added Chronos model: amazon/chronos-t5-{chronos_size}")

        if progress:
            progress.on_progress(10, "Starting model training")

        # Train
        predictor.fit(**fit_kwargs)

        if progress:
            progress.on_progress(90, "Training complete, computing metrics")

        # Get results
        leaderboard = predictor.leaderboard(silent=True)
        best_model = leaderboard.iloc[0] if len(leaderboard) > 0 else None

        metrics = {
            "best_model": best_model["model"] if best_model is not None else None,
            "best_score": float(best_model["score_val"]) if best_model is not None else None,
            "prediction_length": prediction_length,
            "eval_metric": str(predictor.eval_metric),
            "num_models": len(leaderboard),
        }

        # Return leaderboard as list (schema expects List[Dict])
        leaderboard_list = leaderboard.to_dict(orient="records")

        if progress:
            progress.on_progress(100, "Training completed successfully")

        logger.info(f"Training completed. Best model: {metrics['best_model']}")

        return {
            "metrics": metrics,
            "leaderboard": leaderboard_list,
            "model_path": model_path,
            "predictor": predictor,
        }

    async def _run_multimodal_training(
        self,
        df: pd.DataFrame,
        target_column: str,
        model_path: str,
        problem_type: Optional[ProblemType] = None,
        preset: str = "medium_quality",
        time_limit: Optional[int] = None,
        eval_metric: Optional[str] = None,
        advanced_config: AdvancedConfig = None,
        multimodal_config: Optional[Dict[str, Any]] = None,
        progress: TrainingProgressCallback = None,
    ) -> dict[str, Any]:
        """Run multimodal prediction training."""
        from autogluon.multimodal import MultiModalPredictor

        logger.info("Starting MultiModalPredictor training")
        if progress:
            progress.on_progress(5, "Initializing MultiModalPredictor")

        # Configure predictor
        predictor_kwargs = {
            "label": target_column,
            "path": model_path,
            "verbosity": advanced_config.verbosity if advanced_config else 2,
        }

        if problem_type:
            predictor_kwargs["problem_type"] = problem_type.value

        if eval_metric:
            predictor_kwargs["eval_metric"] = eval_metric

        # Create predictor
        predictor = MultiModalPredictor(**predictor_kwargs)

        # Configure fit parameters
        fit_kwargs = {
            "train_data": df,
            "presets": preset,
        }

        if time_limit:
            fit_kwargs["time_limit"] = time_limit

        # Apply advanced configuration
        if advanced_config:
            if advanced_config.num_gpus > 0:
                fit_kwargs["num_gpus"] = advanced_config.num_gpus

            if advanced_config.hyperparameters:
                fit_kwargs["hyperparameters"] = advanced_config.hyperparameters

        # Apply multimodal-specific config
        if multimodal_config:
            # Build hyperparameters for multimodal
            hyperparameters = fit_kwargs.get("hyperparameters", {})

            # Text model configuration
            if multimodal_config.get("text_backbone"):
                hyperparameters["model.hf_text.checkpoint_name"] = multimodal_config["text_backbone"]
            if multimodal_config.get("text_max_length"):
                hyperparameters["data.text.max_len"] = multimodal_config["text_max_length"]

            # Image model configuration
            if multimodal_config.get("image_backbone"):
                hyperparameters["model.timm_image.checkpoint_name"] = multimodal_config["image_backbone"]
            if multimodal_config.get("image_size"):
                hyperparameters["data.image.image_size"] = multimodal_config["image_size"]

            # Training configuration
            if multimodal_config.get("learning_rate"):
                hyperparameters["optimization.learning_rate"] = multimodal_config["learning_rate"]
            if multimodal_config.get("batch_size"):
                hyperparameters["env.per_gpu_batch_size"] = multimodal_config["batch_size"]
            if multimodal_config.get("max_epochs"):
                hyperparameters["optimization.max_epochs"] = multimodal_config["max_epochs"]
            if multimodal_config.get("warmup_steps"):
                hyperparameters["optimization.warmup_steps"] = multimodal_config["warmup_steps"]
            if multimodal_config.get("weight_decay"):
                hyperparameters["optimization.weight_decay"] = multimodal_config["weight_decay"]
            if multimodal_config.get("gradient_clip_val"):
                hyperparameters["optimization.gradient_clip_val"] = multimodal_config["gradient_clip_val"]

            # Fusion method
            if multimodal_config.get("fusion_method"):
                if multimodal_config["fusion_method"] == "early":
                    hyperparameters["model.fusion.strategy"] = "early"
                else:
                    hyperparameters["model.fusion.strategy"] = "late"

            if hyperparameters:
                fit_kwargs["hyperparameters"] = hyperparameters
                logger.info(f"Multimodal hyperparameters: {hyperparameters}")

        if progress:
            progress.on_progress(10, "Starting model training")

        # Train
        predictor.fit(**fit_kwargs)

        if progress:
            progress.on_progress(90, "Training complete")

        # Get results
        metrics = {
            "problem_type": getattr(predictor, 'problem_type', None),
            "eval_metric": getattr(predictor, 'eval_metric', None),
        }

        # Try to get additional model info
        try:
            model_info = predictor.get_model_info() if hasattr(predictor, 'get_model_info') else {}
            metrics.update(model_info)
        except Exception:
            pass

        # Return leaderboard as list (schema expects List[Dict])
        leaderboard_list = [{"model": "MultiModalPredictor", "info": "Single model predictor"}]

        if progress:
            progress.on_progress(100, "Training completed successfully")

        logger.info("Multimodal training completed")

        return {
            "metrics": metrics,
            "leaderboard": leaderboard_list,
            "model_path": model_path,
            "predictor": predictor,
        }
