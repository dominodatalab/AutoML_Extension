"""AutoGluon training orchestrator - delegates to specialized trainers."""

import logging
import os
import json
from datetime import datetime
from typing import Any, Callable, Optional, Dict, List

import pandas as pd
import numpy as np
import mlflow

from app.config import get_settings
from app.db.models import ModelType, ProblemType
from app.core.trainers import (
    AdvancedConfig,
    TrainingProgressCallback,
    TabularTrainer,
    TimeSeriesTrainer,
)

logger = logging.getLogger(__name__)


class AutoGluonRunner:
    """Orchestrates AutoGluon training by delegating to specialized trainers."""

    def __init__(self):
        self.settings = get_settings()
        self._active_progress: Dict[str, TrainingProgressCallback] = {}
        self.tabular_trainer = TabularTrainer()
        self.timeseries_trainer = TimeSeriesTrainer()

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

            # Delegate to appropriate trainer
            if model_type == ModelType.TABULAR:
                result = await self.tabular_trainer.train(
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
                result = await self.timeseries_trainer.train(
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
