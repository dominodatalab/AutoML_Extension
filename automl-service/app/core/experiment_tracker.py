"""MLflow experiment tracking integration for Domino."""

import logging
import os
from datetime import datetime
from functools import lru_cache
from typing import Any, Optional

from app.config import get_settings

logger = logging.getLogger(__name__)


class ExperimentTracker:
    """Tracks experiments using MLflow with Domino integration."""

    def __init__(self):
        self.settings = get_settings()
        self._setup_mlflow()

    def _setup_mlflow(self):
        """Set up MLflow with Domino tracking URI."""
        import mlflow

        # Use Domino's MLflow tracking URI if available
        tracking_uri = self.settings.mlflow_tracking_uri
        if tracking_uri:
            mlflow.set_tracking_uri(tracking_uri)
            logger.info(f"MLflow tracking URI set to: {tracking_uri}")
        else:
            logger.warning("MLflow tracking URI not set, using default")

    def create_experiment(self, experiment_name: Optional[str] = None) -> str:
        """Create or get an MLflow experiment."""
        import mlflow

        if not experiment_name:
            experiment_name = f"AutoML__{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        mlflow.set_experiment(experiment_name)
        logger.info(f"Using experiment: {experiment_name}")

        return experiment_name

    def start_run(
        self,
        run_name: Optional[str] = None,
        tags: Optional[dict[str, str]] = None,
        project_id: Optional[str] = None,
        project_name: Optional[str] = None,
    ) -> str:
        """Start a new MLflow run."""
        import mlflow

        # Add Domino-specific tags, preferring caller-provided context over env
        run_tags = {
            "domino.project_id": project_id or self.settings.domino_project_id or "",
            "domino.project_name": project_name or self.settings.domino_project_name or "",
            "domino.user": self.settings.domino_starting_username or "",
            "domino.run_id": self.settings.domino_run_id or "",
            "source": "automl-service",
        }

        if tags:
            run_tags.update(tags)

        run = mlflow.start_run(run_name=run_name, tags=run_tags)
        logger.info(f"Started MLflow run: {run.info.run_id}")

        return run.info.run_id

    def log_params(self, params: dict[str, Any]):
        """Log parameters to MLflow."""
        import mlflow

        # Convert non-string values to strings
        clean_params = {}
        for key, value in params.items():
            if value is not None:
                clean_params[key] = str(value)

        mlflow.log_params(clean_params)
        logger.debug(f"Logged params: {clean_params}")

    def log_metrics(self, metrics: dict[str, float], step: Optional[int] = None):
        """Log metrics to MLflow."""
        import mlflow

        # Filter to only numeric values
        clean_metrics = {}
        for key, value in metrics.items():
            if isinstance(value, (int, float)) and value is not None:
                clean_metrics[key] = float(value)

        mlflow.log_metrics(clean_metrics, step=step)
        logger.debug(f"Logged metrics: {clean_metrics}")

    def log_metric(self, key: str, value: float, step: Optional[int] = None):
        """Log a single metric to MLflow."""
        import mlflow

        if isinstance(value, (int, float)) and value is not None:
            mlflow.log_metric(key, float(value), step=step)
            logger.debug(f"Logged metric: {key}={value}")

    def log_artifact(self, local_path: str, artifact_path: Optional[str] = None):
        """Log an artifact to MLflow."""
        import mlflow

        mlflow.log_artifact(local_path, artifact_path)
        logger.debug(f"Logged artifact: {local_path}")

    def log_artifacts(self, local_dir: str, artifact_path: Optional[str] = None):
        """Log a directory of artifacts to MLflow."""
        import mlflow

        mlflow.log_artifacts(local_dir, artifact_path)
        logger.debug(f"Logged artifacts from directory: {local_dir}")

    def log_artifact_dict(self, data: dict, filename: str):
        """Log a dictionary as a JSON artifact to MLflow."""
        import json
        import tempfile
        import mlflow

        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                json.dump(data, f, indent=2, default=str)
                temp_path = f.name

            mlflow.log_artifact(temp_path, artifact_path=None)
            os.unlink(temp_path)
            logger.debug(f"Logged dict artifact: {filename}")
        except Exception as e:
            logger.warning(f"Failed to log artifact dict {filename}: {e}")

    def log_text(self, text: str, filename: str):
        """Log text content as an artifact to MLflow."""
        import tempfile
        import mlflow

        try:
            suffix = os.path.splitext(filename)[1] or '.txt'
            with tempfile.NamedTemporaryFile(mode='w', suffix=suffix, delete=False) as f:
                f.write(text)
                temp_path = f.name

            mlflow.log_artifact(temp_path, artifact_path=None)
            os.unlink(temp_path)
            logger.debug(f"Logged text artifact: {filename}")
        except Exception as e:
            logger.warning(f"Failed to log text {filename}: {e}")

    def log_model(
        self,
        model_path: str,
        artifact_path: str = "model",
        registered_model_name: Optional[str] = None,
    ):
        """Log a model directory to MLflow."""
        import mlflow

        # Log the model directory as artifacts
        mlflow.log_artifacts(model_path, artifact_path)
        logger.info(f"Logged model artifacts from: {model_path}")

        if registered_model_name:
            # Register the model
            run_id = mlflow.active_run().info.run_id
            model_uri = f"runs:/{run_id}/{artifact_path}"

            try:
                mlflow.register_model(model_uri, registered_model_name)
                logger.info(f"Registered model: {registered_model_name}")
            except Exception as e:
                logger.warning(f"Failed to register model: {e}")

    def log_individual_model_run(
        self,
        model_name: str,
        model_info: dict[str, Any],
        rank: int,
        job_config: dict[str, Any],
        predictor: Any = None,
        test_data: Any = None,
    ):
        """Log an individual model from the AutoGluon leaderboard as a SEPARATE MLflow run.

        This mimics the notebook logging pattern where each trained model gets its own
        top-level run for better experiment tracking and comparison in Domino.

        IMPORTANT: This creates a separate run (not nested) like notebooks do.

        Like notebooks, this logs:
        - Training configuration
        - Model-specific parameters
        - ACTUAL hyperparameters from bagged_info['child_hyperparameters']
        - Early-stopped values from bagged_info['child_hyperparameters_fit']
        - Detailed per-model metrics (precision, recall, F1 for classification; RMSE, MAE, R² for regression)
        """
        import mlflow

        try:
            # Determine algorithm and model family
            algorithm = self._extract_algorithm(model_name)
            model_family = self._get_model_family(model_name)
            stack_level = self._extract_stack_level(model_name)
            is_bagged = "_BAG_" in model_name
            is_stacked = stack_level > 1

            # Create a SEPARATE run for this model (like notebooks do)
            with mlflow.start_run(run_name=model_name) as model_run:
                # === LOG TRAINING CONFIGURATION ===
                mlflow.log_params({
                    "experiment_type": job_config.get("name", "automl_training"),
                    "problem_type": str(job_config.get("problem_type", "auto")),
                    "target_column": str(job_config.get("target_column", "")),
                    "preset": str(job_config.get("preset", "medium_quality")),
                    "eval_metric": str(job_config.get("eval_metric", "auto")),
                    "model_type": str(job_config.get("model_type", "tabular")),
                    "time_limit": str(job_config.get("time_limit", "")),
                    "n_train_samples": str(job_config.get("n_train_samples", "")),
                    "n_features": str(job_config.get("n_features", "")),
                })

                # === LOG MODEL-SPECIFIC PARAMETERS ===
                mlflow.log_params({
                    "model_name": model_name,
                    "algorithm": algorithm,
                    "model_family": model_family,
                    "stack_level": str(stack_level),
                    "is_bagged": str(is_bagged),
                    "is_stacked": str(is_stacked),
                    "fit_order": str(model_info.get("fit_order", rank)),
                })

                # === GET ACTUAL HYPERPARAMETERS FROM THE MODEL (like notebooks) ===
                if predictor is not None:
                    self._log_model_hyperparameters(predictor, model_name)

                # === LOG LEADERBOARD METRICS ===
                metrics_to_log = {}
                if "score_val" in model_info and model_info["score_val"] is not None:
                    metrics_to_log["score_val"] = float(model_info["score_val"])
                if "score_test" in model_info and model_info["score_test"] is not None:
                    metrics_to_log["score_test"] = float(model_info["score_test"])
                if "fit_time" in model_info and model_info["fit_time"] is not None:
                    metrics_to_log["fit_time_seconds"] = float(model_info["fit_time"])
                if "fit_time_marginal" in model_info and model_info["fit_time_marginal"] is not None:
                    metrics_to_log["fit_time_marginal_seconds"] = float(model_info["fit_time_marginal"])
                if "pred_time_val" in model_info and model_info["pred_time_val"] is not None:
                    metrics_to_log["pred_time_val_seconds"] = float(model_info["pred_time_val"])
                if "pred_time_test" in model_info and model_info["pred_time_test"] is not None:
                    metrics_to_log["pred_time_test_seconds"] = float(model_info["pred_time_test"])

                metrics_to_log["leaderboard_rank"] = rank

                # === CALCULATE DETAILED PER-MODEL METRICS (like notebooks) ===
                if predictor is not None:
                    target_column = job_config.get("target_column", "")
                    problem_type = str(job_config.get("problem_type", "")).lower()
                    model_type = str(job_config.get("model_type", "")).lower()

                    # Fallback: if problem_type is "auto" or empty, try to detect from predictor
                    if problem_type in ["auto", ""] and hasattr(predictor, "problem_type"):
                        problem_type = str(predictor.problem_type).lower()
                        logger.debug(f"Detected problem_type from predictor: {problem_type}")

                    if model_type == "tabular" and target_column and test_data is not None:
                        if problem_type in ["binary", "multiclass", "classification"]:
                            # Calculate classification metrics (precision, recall, F1 per class)
                            detailed_metrics = self._calculate_per_model_classification_metrics(
                                predictor, model_name, test_data, target_column
                            )
                            metrics_to_log.update(detailed_metrics)
                        elif problem_type in ["regression", "quantile"]:
                            # Calculate regression metrics (RMSE, MAE, R², MAPE)
                            detailed_metrics = self._calculate_per_model_regression_metrics(
                                predictor, model_name, test_data, target_column
                            )
                            metrics_to_log.update(detailed_metrics)
                    elif model_type == "timeseries":
                        # For timeseries, calculate forecast metrics if test data available
                        if test_data is not None:
                            detailed_metrics = self._calculate_per_model_timeseries_metrics(
                                predictor, model_name, test_data, None  # train_data not available here
                            )
                            metrics_to_log.update(detailed_metrics)

                mlflow.log_metrics(metrics_to_log)

                # Log how many detailed metrics were calculated
                logger.debug(f"Logged {len(metrics_to_log)} metrics for {model_name}")

                # === ADD TAGS FOR FILTERING IN DOMINO UI ===
                mlflow.set_tags({
                    "experiment": job_config.get("name", "automl"),
                    "model_type": job_config.get("model_type", "tabular"),
                    "problem_type": str(job_config.get("problem_type", "classification")),
                    "algorithm": algorithm,
                    "model_family": model_family,
                    "automl_framework": "autogluon",
                    "is_best_model": str(rank == 1),
                    "stack_level": str(stack_level),
                    "job_id": str(job_config.get("job_id", "")),
                })

                logger.info(f"Logged model run: {model_name} (rank {rank}, score_val={model_info.get('score_val', 'N/A')})")

        except Exception as e:
            logger.warning(f"Failed to log individual model {model_name}: {e}")

    def _extract_algorithm(self, model_name: str) -> str:
        """Extract the algorithm name from the AutoGluon model name."""
        algorithms = {
            "LightGBM": "LightGBM",
            "XGBoost": "XGBoost",
            "CatBoost": "CatBoost",
            "RandomForest": "RandomForest",
            "ExtraTrees": "ExtraTrees",
            "NeuralNetTorch": "NeuralNetTorch",
            "NeuralNetFastAI": "NeuralNetFastAI",
            "WeightedEnsemble": "WeightedEnsemble",
            "KNeighbors": "KNeighbors",
            "LinearModel": "LinearModel",
            "TabularNeuralNet": "TabularNeuralNet",
        }

        for key, algo in algorithms.items():
            if key in model_name:
                return algo
        return model_name.split("_")[0] if "_" in model_name else model_name

    def _extract_stack_level(self, model_name: str) -> int:
        """Extract the stack level from AutoGluon model name."""
        for level in range(1, 5):
            if f"_L{level}" in model_name:
                return level
        return 1

    def _get_model_family(self, model_name: str) -> str:
        """Determine the model family from the model name."""
        name_lower = model_name.lower()

        if "lightgbm" in name_lower or "gbm" in name_lower:
            return "gradient_boosting"
        elif "catboost" in name_lower or "cat" in name_lower:
            return "gradient_boosting"
        elif "xgboost" in name_lower or "xgb" in name_lower:
            return "gradient_boosting"
        elif "randomforest" in name_lower or "rf" in name_lower:
            return "random_forest"
        elif "extratrees" in name_lower or "xt" in name_lower:
            return "extra_trees"
        elif "knn" in name_lower or "kneighbors" in name_lower:
            return "knn"
        elif "linear" in name_lower or "lr" in name_lower:
            return "linear_model"
        elif "nn" in name_lower or "neural" in name_lower or "mlp" in name_lower:
            return "neural_network"
        elif "tabular" in name_lower or "transformer" in name_lower:
            return "transformer"
        elif "ensemble" in name_lower or "weighted" in name_lower:
            return "ensemble"
        else:
            return "other"

    def _log_model_hyperparameters(self, predictor: Any, model_name: str, max_params: int = 30):
        """Extract and log ACTUAL hyperparameters from a trained model.

        For bagged models (most AutoGluon models), the actual hyperparameters are in:
        - model.get_info()['bagged_info']['child_hyperparameters'] - configured params
        - model.get_info()['bagged_info']['child_hyperparameters_fit'] - actual fitted values (e.g., early-stopped)
        """
        import mlflow

        try:
            # Try to get the model from predictor
            model = predictor._trainer.load_model(model_name)
            param_count = 0
            params_logged = {}

            # First, try to get hyperparameters from bagged_info (most AutoGluon models are bagged)
            if hasattr(model, 'get_info'):
                info = model.get_info()

                if 'bagged_info' in info and info['bagged_info']:
                    bagged_info = info['bagged_info']

                    # Get the ACTUAL child hyperparameters (what was configured)
                    if 'child_hyperparameters' in bagged_info and bagged_info['child_hyperparameters']:
                        for key, value in bagged_info['child_hyperparameters'].items():
                            if param_count >= max_params:
                                break
                            if isinstance(value, (int, float, str, bool)):
                                try:
                                    mlflow.log_param(f"hp_{key}", str(value)[:250])
                                    params_logged[key] = value
                                    param_count += 1
                                except Exception:
                                    pass

                    # Get the FITTED values (e.g., early-stopped num_boost_round)
                    if 'child_hyperparameters_fit' in bagged_info and bagged_info['child_hyperparameters_fit']:
                        for key, value in bagged_info['child_hyperparameters_fit'].items():
                            if param_count >= max_params:
                                break
                            # Only log if different from configured or not already logged
                            if key not in params_logged or params_logged.get(key) != value:
                                if isinstance(value, (int, float, str, bool)):
                                    try:
                                        mlflow.log_param(f"hp_{key}_actual", str(value)[:250])
                                        param_count += 1
                                    except Exception:
                                        pass

                    # Log number of bagged models (folds)
                    if 'num_child_models' in bagged_info:
                        try:
                            mlflow.log_param("hp_num_bag_folds", str(bagged_info['num_child_models']))
                            param_count += 1
                        except Exception:
                            pass

                # For ensemble models, log the model weights
                if 'Ensemble' in model_name or 'WeightedEnsemble' in model_name:
                    if 'model_weights' in info:
                        weights = info['model_weights']
                        if isinstance(weights, dict):
                            for child_model, weight in list(weights.items())[:10]:  # Limit to top 10
                                if param_count >= max_params:
                                    break
                                try:
                                    clean_name = child_model.replace("/", "_").replace(" ", "_")[:30]
                                    mlflow.log_param(f"weight_{clean_name}", f"{weight:.4f}")
                                    param_count += 1
                                except Exception:
                                    pass

            # Fallback to model.params if no bagged_info (for non-bagged models)
            if param_count == 0 and hasattr(model, 'params') and model.params:
                params = model.params if isinstance(model.params, dict) else {}
                for key, value in params.items():
                    if param_count >= max_params:
                        break
                    if isinstance(value, (int, float, str, bool)):
                        try:
                            mlflow.log_param(f"hp_{key}", str(value)[:250])
                            param_count += 1
                        except Exception:
                            pass

            if param_count > 0:
                logger.debug(f"Logged {param_count} hyperparameters for {model_name}")

        except Exception as e:
            logger.debug(f"Could not extract hyperparameters for {model_name}: {e}")

    def _calculate_per_model_classification_metrics(
        self,
        predictor: Any,
        model_name: str,
        test_data: Any,
        target_column: str,
    ) -> dict[str, float]:
        """Calculate detailed classification metrics for a specific model.

        Returns per-class precision, recall, F1 and aggregate metrics.
        """
        import numpy as np
        from sklearn.metrics import precision_recall_fscore_support, accuracy_score, balanced_accuracy_score

        metrics = {}
        try:
            y_pred = predictor.predict(test_data, model=model_name)
            y_true = test_data[target_column]

            # Get class labels
            class_labels = sorted(y_true.unique())

            # Calculate per-class metrics
            precision, recall, f1, support = precision_recall_fscore_support(
                y_true, y_pred, labels=class_labels, zero_division=0
            )

            for i, label in enumerate(class_labels):
                clean_label = str(label).replace(" ", "_").replace("/", "_")[:20]
                metrics[f"precision_{clean_label}"] = float(precision[i])
                metrics[f"recall_{clean_label}"] = float(recall[i])
                metrics[f"f1_{clean_label}"] = float(f1[i])
                metrics[f"support_{clean_label}"] = int(support[i])

            # Calculate aggregate metrics (matching notebook pattern)
            metrics["accuracy"] = float(accuracy_score(y_true, y_pred))
            metrics["balanced_accuracy"] = float(balanced_accuracy_score(y_true, y_pred))
            metrics["macro_precision"] = float(np.mean(precision))
            metrics["macro_recall"] = float(np.mean(recall))
            metrics["macro_f1"] = float(np.mean(f1))
            metrics["weighted_f1"] = float(np.average(f1, weights=support))
            # Add weighted precision and recall (matching notebook: precision_weighted, recall_weighted)
            metrics["weighted_precision"] = float(np.average(precision, weights=support))
            metrics["weighted_recall"] = float(np.average(recall, weights=support))
            # Also add notebook-style naming for consistency with both naming conventions
            metrics["f1_weighted"] = metrics["weighted_f1"]
            metrics["f1_macro"] = metrics["macro_f1"]
            metrics["precision_weighted"] = metrics["weighted_precision"]
            metrics["precision_macro"] = metrics["macro_precision"]
            metrics["recall_weighted"] = metrics["weighted_recall"]
            metrics["recall_macro"] = metrics["macro_recall"]

        except Exception as e:
            logger.debug(f"Could not calculate classification metrics for {model_name}: {e}")

        return metrics

    def _calculate_per_model_regression_metrics(
        self,
        predictor: Any,
        model_name: str,
        test_data: Any,
        target_column: str,
    ) -> dict[str, float]:
        """Calculate detailed regression metrics for a specific model.

        Returns RMSE, MAE, R², MAPE, and max error.
        """
        import numpy as np
        from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

        metrics = {}
        try:
            y_pred = predictor.predict(test_data, model=model_name)
            y_true = test_data[target_column]

            metrics["rmse"] = float(np.sqrt(mean_squared_error(y_true, y_pred)))
            metrics["mae"] = float(mean_absolute_error(y_true, y_pred))
            metrics["r2"] = float(r2_score(y_true, y_pred))

            # MAPE - handle division by zero
            non_zero_mask = y_true != 0
            if non_zero_mask.sum() > 0:
                mape = np.mean(np.abs((y_true[non_zero_mask] - y_pred[non_zero_mask]) / y_true[non_zero_mask])) * 100
                metrics["mape"] = float(mape)

            metrics["max_error"] = float(np.max(np.abs(y_true - y_pred)))

            # Additional statistics
            residuals = y_true - y_pred
            metrics["mean_residual"] = float(np.mean(residuals))
            metrics["std_residual"] = float(np.std(residuals))

        except Exception as e:
            logger.debug(f"Could not calculate regression metrics for {model_name}: {e}")

        return metrics

    def _calculate_per_model_timeseries_metrics(
        self,
        predictor: Any,
        model_name: str,
        test_data: Any,
        train_data: Any = None,
    ) -> dict[str, float]:
        """Calculate detailed time series forecast metrics for a specific model.

        Returns MAE, RMSE, MAPE, and sMAPE.
        For timeseries, we use the leaderboard scores since per-model prediction
        requires train_data which may not be available.
        """
        import numpy as np

        metrics = {}
        try:
            # If we have train_data, we can make predictions
            if train_data is not None:
                predictions = predictor.predict(train_data, model=model_name)
                target = predictor.target

                # Align predictions with test data for metric calculation
                pred_values = predictions['mean'].values
                actual_values = test_data[target].values[-len(pred_values):]

                if len(pred_values) == len(actual_values):
                    # MAE
                    metrics["mae"] = float(np.mean(np.abs(actual_values - pred_values)))

                    # RMSE
                    metrics["rmse"] = float(np.sqrt(np.mean((actual_values - pred_values) ** 2)))

                    # MAPE - handle division by zero
                    non_zero_mask = actual_values != 0
                    if non_zero_mask.sum() > 0:
                        mape = np.mean(np.abs((actual_values[non_zero_mask] - pred_values[non_zero_mask]) / actual_values[non_zero_mask])) * 100
                        metrics["mape"] = float(mape)

                    # sMAPE (symmetric MAPE)
                    denominator = np.abs(actual_values) + np.abs(pred_values)
                    non_zero_denom = denominator != 0
                    if non_zero_denom.sum() > 0:
                        smape = np.mean(2 * np.abs(actual_values[non_zero_denom] - pred_values[non_zero_denom]) / denominator[non_zero_denom]) * 100
                        metrics["smape"] = float(smape)

        except Exception as e:
            logger.debug(f"Could not calculate time series metrics for {model_name}: {e}")

        return metrics

    def log_training_results(
        self,
        job_config: dict[str, Any],
        metrics: dict[str, Any],
        leaderboard: dict[str, Any],
        model_path: str,
        predictor: Any = None,
        test_data: Any = None,
    ) -> str:
        """Log complete training results with individual model runs.

        This follows the notebook pattern:
        1. Log each model in the leaderboard as a SEPARATE MLflow run
           - With ACTUAL hyperparameters from bagged_info['child_hyperparameters']
           - With detailed per-model metrics (precision/recall/F1 for classification, RMSE/MAE/R² for regression)
        2. Log a final evaluation summary run with artifacts
        """
        import mlflow

        run_id = None
        # Handle both list format and dict with "models" key format
        if isinstance(leaderboard, list):
            models = leaderboard
        elif isinstance(leaderboard, dict):
            models = leaderboard.get("models", [])
        else:
            models = []

        try:
            # End any active run first (we'll create separate runs for each model)
            if mlflow.active_run():
                logger.info("Ending active MLflow run before logging individual model runs")
                mlflow.end_run()

            logger.info(f"Logging {len(models)} individual model runs to Domino Experiments")
            logger.info(f"Job config: model_type={job_config.get('model_type')}, problem_type={job_config.get('problem_type')}")
            logger.info(f"Predictor available: {predictor is not None}, Test data available: {test_data is not None}")
            # Log detected problem type from predictor for debugging
            if predictor is not None and hasattr(predictor, 'problem_type'):
                logger.info(f"Predictor detected problem_type: {predictor.problem_type}")
            if test_data is not None:
                logger.info(f"Test data shape: {test_data.shape}")

            if len(models) == 0:
                logger.warning("No models in leaderboard to log!")

            # Log individual models as SEPARATE runs (like notebooks do)
            for rank, model_info in enumerate(models, start=1):
                model_name = model_info.get("model", f"model_{rank}")
                logger.info(f"Logging individual run for model {rank}/{len(models)}: {model_name}")
                self.log_individual_model_run(
                    model_name=model_name,
                    model_info=model_info,
                    rank=rank,
                    job_config=job_config,
                    predictor=predictor,
                    test_data=test_data,
                )

            # Create final evaluation summary run (like notebooks do)
            with mlflow.start_run(run_name="final_evaluation_summary") as summary_run:
                run_id = summary_run.info.run_id

                # Log overall parameters
                mlflow.log_params({
                    "experiment_type": job_config.get("name", "automl_training"),
                    "model_type": job_config.get("model_type", "tabular"),
                    "problem_type": str(job_config.get("problem_type", "auto")),
                    "target_column": str(job_config.get("target_column", "")),
                    "preset": str(job_config.get("preset", "medium_quality")),
                    "eval_metric": str(job_config.get("eval_metric", "auto")),
                    "time_limit": str(job_config.get("time_limit", "")),
                    "best_model": metrics.get("best_model", ""),
                    "total_models_trained": str(len(models)),
                })

                # Log aggregate metrics
                metrics_to_log = {}
                if metrics.get("best_score") is not None:
                    metrics_to_log["best_score"] = float(metrics["best_score"])
                if metrics.get("accuracy") is not None:
                    metrics_to_log["accuracy"] = float(metrics["accuracy"])
                if metrics.get("f1_score") is not None:
                    metrics_to_log["f1_score"] = float(metrics["f1_score"])
                if metrics.get("num_models") is not None:
                    metrics_to_log["num_models_trained"] = float(metrics["num_models"])

                if metrics_to_log:
                    mlflow.log_metrics(metrics_to_log)

                # Set summary tags
                mlflow.set_tags({
                    "experiment": job_config.get("name", "automl"),
                    "run_type": "evaluation_summary",
                    "automl_framework": "autogluon",
                    "job_id": str(job_config.get("job_id", "")),
                })

                # Log leaderboard as artifact (ensure it's in dict format)
                leaderboard_data = {"models": models} if isinstance(leaderboard, list) else leaderboard
                self.log_artifact_dict(leaderboard_data, "leaderboard.json")

                # Log feature importance if available
                if metrics.get("feature_importance"):
                    self.log_artifact_dict(
                        {"features": metrics["feature_importance"]},
                        "feature_importance.json"
                    )

                # Log model artifacts
                if model_path and os.path.exists(model_path):
                    mlflow.log_artifacts(model_path, artifact_path="autogluon_model")
                    logger.info(f"Logged model artifacts from: {model_path}")

            logger.info(f"Training results logged: {len(models)} model runs + final summary run {run_id}")

        except Exception as e:
            logger.error(f"Failed to log training results: {e}")

        return run_id

    def get_run_metrics(self, run_id: str) -> dict[str, float]:
        """Get metrics from a specific MLflow run."""
        import mlflow

        client = mlflow.tracking.MlflowClient()
        try:
            run = client.get_run(run_id)
            return run.data.metrics
        except Exception as e:
            logger.warning(f"Failed to get metrics for run {run_id}: {e}")
            return {}

    def end_run(self, status: str = "FINISHED"):
        """End the current MLflow run."""
        import mlflow

        mlflow.end_run(status=status)
        logger.debug("Ended MLflow run")


@lru_cache()
def get_experiment_tracker() -> ExperimentTracker:
    """Get the experiment tracker singleton (cached)."""
    return ExperimentTracker()
