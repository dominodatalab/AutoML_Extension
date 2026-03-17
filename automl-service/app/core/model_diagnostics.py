"""Model diagnostics and explainability service.

NOTE: This service returns RAW DATA only. Charts are rendered in the UI using recharts.
Do NOT generate matplotlib/PNG images here.
"""

import os
import logging
from functools import lru_cache
from typing import Any, Dict, List, Optional

import pandas as pd
import numpy as np

from app.core.leaderboard_utils import normalize_leaderboard_rows
from app.core.model_loader import load_predictor, load_dataframe

logger = logging.getLogger(__name__)


def _importance_frame_to_features(importance: pd.DataFrame) -> list[dict[str, Any]]:
    """Convert an AutoGluon feature-importance frame into UI-ready rows."""
    if importance is None or len(importance) == 0:
        return []

    features: list[dict[str, Any]] = []
    for idx, row in importance.iterrows():
        feature = {
            "feature": str(idx),
            "importance": float(row.get("importance", row.iloc[0])) if isinstance(row, pd.Series) else float(row),
        }

        if isinstance(row, pd.Series):
            if "stddev" in row and pd.notna(row.get("stddev")):
                feature["stddev"] = float(row["stddev"])
            elif "stdev" in row and pd.notna(row.get("stdev")):
                feature["stddev"] = float(row["stdev"])

            if "p_value" in row and pd.notna(row.get("p_value")):
                feature["p_value"] = float(row["p_value"])

        features.append(feature)

    features.sort(key=lambda x: abs(x["importance"]), reverse=True)
    return features


class ModelDiagnostics:
    """Service for model diagnostics, feature importance, and data extraction.

    IMPORTANT: This service returns raw data for the UI to render charts.
    Do NOT generate images or base64 encoded charts here.
    """

    def __init__(self):
        pass

    def get_feature_importance(
        self,
        model_path: str,
        model_type: str,
        data_path: Optional[str] = None,
        method: str = "auto"
    ) -> Dict[str, Any]:
        """Get feature importance for a trained model.

        Returns raw data for UI to render chart with recharts.
        """
        result = {
            "model_path": model_path,
            "model_type": model_type,
            "method": method,
            "features": []
        }

        try:
            if model_type == "tabular":
                predictor = load_predictor(model_path, model_type)

                # Get feature importance
                if data_path and os.path.exists(data_path):
                    data = load_dataframe(data_path)
                    importance = predictor.feature_importance(data, silent=True)
                else:
                    importance = predictor.feature_importance(silent=True)

                if importance is not None and len(importance) > 0:
                    result["features"] = _importance_frame_to_features(importance)

            elif model_type == "timeseries":
                predictor = load_predictor(model_path, model_type)

                try:
                    importance = predictor.feature_importance()
                    if isinstance(importance, pd.DataFrame):
                        result["features"] = _importance_frame_to_features(importance)
                except Exception as e:
                    logger.warning(f"Could not get timeseries feature importance: {e}")

        except Exception as e:
            logger.error(f"Error getting feature importance: {e}")
            result["error"] = str(e)

        return result

    def get_leaderboard(self, model_path: str, model_type: str) -> Dict[str, Any]:
        """Get model leaderboard with detailed metrics.

        Returns raw data for UI to render chart with recharts.
        """
        result = {
            "model_path": model_path,
            "models": [],
            "best_model": None,
            "eval_metric": None
        }

        try:
            if model_type == "tabular":
                predictor = load_predictor(model_path, model_type)

                leaderboard = predictor.leaderboard(silent=True)
                if leaderboard is not None and len(leaderboard) > 0:
                    models = []
                    for _, row in leaderboard.iterrows():
                        model_data = {}
                        for col in leaderboard.columns:
                            val = row[col]
                            if pd.isna(val):
                                model_data[col] = None
                            elif isinstance(val, (np.integer, np.floating)):
                                model_data[col] = float(val)
                            else:
                                model_data[col] = val
                        models.append(model_data)
                    result["models"] = normalize_leaderboard_rows(models) or []
                    result["best_model"] = predictor.model_best
                    result["eval_metric"] = predictor.eval_metric.name if hasattr(predictor.eval_metric, 'name') else str(predictor.eval_metric)

            elif model_type == "timeseries":
                predictor = load_predictor(model_path, model_type)

                leaderboard = predictor.leaderboard()
                if leaderboard is not None and len(leaderboard) > 0:
                    models = []
                    for _, row in leaderboard.iterrows():
                        model_data = {}
                        for col in leaderboard.columns:
                            val = row[col]
                            if pd.isna(val):
                                model_data[col] = None
                            elif isinstance(val, (np.integer, np.floating)):
                                model_data[col] = float(val)
                            else:
                                model_data[col] = val
                        models.append(model_data)
                    result["models"] = normalize_leaderboard_rows(models) or []

        except Exception as e:
            logger.error(f"Error getting leaderboard: {e}")
            result["error"] = str(e)

        return result

    def get_confusion_matrix(
        self,
        model_path: str,
        model_type: str,
        data_path: str
    ) -> Dict[str, Any]:
        """Generate confusion matrix for classification models.

        Returns raw data for UI to render chart with recharts.
        """
        result = {
            "matrix": None,
            "labels": [],
            "metrics": {}
        }

        try:
            if model_type != "tabular":
                result["error"] = "Confusion matrix only available for tabular models"
                return result

            predictor = load_predictor(model_path, "tabular")

            if predictor.problem_type not in ['binary', 'multiclass']:
                result["error"] = "Confusion matrix only available for classification problems"
                return result

            data = load_dataframe(data_path)

            # Get predictions
            y_true = data[predictor.label]
            y_pred = predictor.predict(data)

            # Compute confusion matrix
            from sklearn.metrics import confusion_matrix, classification_report

            labels = sorted(y_true.unique())
            cm = confusion_matrix(y_true, y_pred, labels=labels)

            result["matrix"] = cm.tolist()
            result["labels"] = [str(l) for l in labels]

            # Compute additional metrics with proper float conversion
            report = classification_report(y_true, y_pred, labels=labels, output_dict=True)

            def convert_metrics(obj):
                """Recursively convert numpy types to Python types."""
                if isinstance(obj, dict):
                    return {str(k): convert_metrics(v) for k, v in obj.items()}
                elif isinstance(obj, (np.integer, np.floating)):
                    return float(obj)
                elif isinstance(obj, np.ndarray):
                    return obj.tolist()
                return obj

            result["metrics"] = {
                "accuracy": float(report.get("accuracy", 0)),
                "macro_avg": convert_metrics(report.get("macro avg", {})),
                "weighted_avg": convert_metrics(report.get("weighted avg", {})),
                "per_class": convert_metrics({str(k): v for k, v in report.items() if k not in ['accuracy', 'macro avg', 'weighted avg']})
            }

        except Exception as e:
            logger.error(f"Error generating confusion matrix: {e}")
            result["error"] = str(e)

        return result

    def get_roc_curve(
        self,
        model_path: str,
        model_type: str,
        data_path: str
    ) -> Dict[str, Any]:
        """Generate ROC curve for binary classification.

        Returns raw data for UI to render chart with recharts.
        """
        result = {
            "auc": None,
            "fpr": [],
            "tpr": [],
            "thresholds": [],
            "curve_data": []  # Pre-formatted for recharts
        }

        try:
            if model_type != "tabular":
                result["error"] = "ROC curve only available for tabular models"
                return result

            predictor = load_predictor(model_path, "tabular")

            if predictor.problem_type != 'binary':
                result["error"] = "ROC curve only available for binary classification"
                return result

            data = load_dataframe(data_path)

            # Get probabilities
            y_true = data[predictor.label]
            y_proba = predictor.predict_proba(data)

            # Get positive class probability
            if isinstance(y_proba, pd.DataFrame):
                pos_class = y_proba.columns[-1]
                y_score = y_proba[pos_class]
            else:
                y_score = y_proba[:, 1] if y_proba.ndim > 1 else y_proba

            # Compute ROC curve
            from sklearn.metrics import roc_curve, auc

            fpr, tpr, thresholds = roc_curve(y_true, y_score, pos_label=y_true.unique().max())
            roc_auc = auc(fpr, tpr)

            result["auc"] = float(roc_auc)
            result["fpr"] = [float(x) for x in fpr]
            result["tpr"] = [float(x) for x in tpr]
            result["thresholds"] = [float(x) if np.isfinite(x) else None for x in thresholds]

            # Pre-format data for recharts LineChart
            result["curve_data"] = [
                {"fpr": float(f), "tpr": float(t)}
                for f, t in zip(fpr, tpr)
            ]

        except Exception as e:
            logger.error(f"Error generating ROC curve: {e}")
            result["error"] = str(e)

        return result

    def get_precision_recall_curve(
        self,
        model_path: str,
        model_type: str,
        data_path: str
    ) -> Dict[str, Any]:
        """Generate Precision-Recall curve for binary classification.

        Returns raw data for UI to render chart with recharts.
        """
        result = {
            "average_precision": None,
            "precision": [],
            "recall": [],
            "thresholds": [],
            "curve_data": []  # Pre-formatted for recharts
        }

        try:
            if model_type != "tabular":
                result["error"] = "PR curve only available for tabular models"
                return result

            predictor = load_predictor(model_path, "tabular")

            if predictor.problem_type != 'binary':
                result["error"] = "PR curve only available for binary classification"
                return result

            data = load_dataframe(data_path)

            # Get probabilities
            y_true = data[predictor.label]
            y_proba = predictor.predict_proba(data)

            if isinstance(y_proba, pd.DataFrame):
                pos_class = y_proba.columns[-1]
                y_score = y_proba[pos_class]
            else:
                y_score = y_proba[:, 1] if y_proba.ndim > 1 else y_proba

            # Compute PR curve
            from sklearn.metrics import precision_recall_curve, average_precision_score

            precision, recall, thresholds = precision_recall_curve(y_true, y_score)
            avg_precision = average_precision_score(y_true, y_score)

            result["average_precision"] = float(avg_precision)
            result["precision"] = [float(x) for x in precision]
            result["recall"] = [float(x) for x in recall]
            result["thresholds"] = [float(x) for x in thresholds]

            # Pre-format data for recharts LineChart
            result["curve_data"] = [
                {"recall": float(r), "precision": float(p)}
                for r, p in zip(recall, precision)
            ]

        except Exception as e:
            logger.error(f"Error generating PR curve: {e}")
            result["error"] = str(e)

        return result

    def get_regression_diagnostics(
        self,
        model_path: str,
        model_type: str,
        data_path: str
    ) -> Dict[str, Any]:
        """Generate diagnostic data for regression models.

        Returns raw data for UI to render charts with recharts.
        """
        result = {
            "metrics": {},
            "scatter_data": [],  # For predicted vs actual scatter plot
            "residuals_data": [],  # For residuals scatter plot
            "histogram_data": []  # For residuals histogram
        }

        try:
            if model_type != "tabular":
                result["error"] = "Regression diagnostics only available for tabular models"
                return result

            predictor = load_predictor(model_path, "tabular")

            if predictor.problem_type != 'regression':
                result["error"] = "These diagnostics are only for regression problems"
                return result

            data = load_dataframe(data_path)

            # Get predictions
            y_true = data[predictor.label].values
            y_pred = predictor.predict(data).values

            # Compute metrics
            from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

            residuals = y_true - y_pred

            result["metrics"] = {
                "mse": float(mean_squared_error(y_true, y_pred)),
                "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
                "mae": float(mean_absolute_error(y_true, y_pred)),
                "r2": float(r2_score(y_true, y_pred)),
                "mean_residual": float(np.mean(residuals)),
                "std_residual": float(np.std(residuals)),
                "min_actual": float(np.min(y_true)),
                "max_actual": float(np.max(y_true)),
                "min_predicted": float(np.min(y_pred)),
                "max_predicted": float(np.max(y_pred))
            }

            # Sample data for scatter plots (limit to 500 points for performance)
            sample_size = min(500, len(y_true))
            if len(y_true) > sample_size:
                indices = np.random.choice(len(y_true), sample_size, replace=False)
                y_true_sample = y_true[indices]
                y_pred_sample = y_pred[indices]
                residuals_sample = residuals[indices]
            else:
                y_true_sample = y_true
                y_pred_sample = y_pred
                residuals_sample = residuals

            # Predicted vs Actual scatter data
            result["scatter_data"] = [
                {"actual": float(a), "predicted": float(p)}
                for a, p in zip(y_true_sample, y_pred_sample)
            ]

            # Residuals scatter data
            result["residuals_data"] = [
                {"predicted": float(p), "residual": float(r)}
                for p, r in zip(y_pred_sample, residuals_sample)
            ]

            # Histogram data (bin the residuals)
            hist, bin_edges = np.histogram(residuals, bins=30)
            result["histogram_data"] = [
                {"bin": float((bin_edges[i] + bin_edges[i+1]) / 2), "count": int(hist[i])}
                for i in range(len(hist))
            ]

        except Exception as e:
            logger.error(f"Error generating regression diagnostics: {e}")
            result["error"] = str(e)

        return result

    def get_learning_curves(
        self,
        model_path: str,
        model_type: str
    ) -> Dict[str, Any]:
        """Get learning curves from training history.

        Returns raw data for UI to render charts with recharts.
        """
        result = {
            "fit_summary": None,
            "models": [],  # List of model training data for charts
            "fit_summary_raw": None  # Raw fit summary as dict/string
        }

        def convert_to_serializable(obj):
            """Convert pandas/numpy objects to JSON-serializable types."""
            if obj is None:
                return None
            if isinstance(obj, pd.DataFrame):
                return obj.to_dict(orient='records')
            if isinstance(obj, pd.Series):
                return obj.to_dict()
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            if isinstance(obj, (np.integer, np.floating)):
                return float(obj)
            if isinstance(obj, dict):
                return {k: convert_to_serializable(v) for k, v in obj.items()}
            if isinstance(obj, (list, tuple)):
                return [convert_to_serializable(item) for item in obj]
            return obj

        try:
            if model_type == "tabular":
                predictor = load_predictor(model_path, model_type)

                # Try to get fit summary - convert to string to avoid serialization issues
                try:
                    fit_summary = predictor.fit_summary()
                    if fit_summary:
                        # Convert to serializable format
                        result["fit_summary_raw"] = convert_to_serializable(fit_summary)
                except Exception as e:
                    logger.debug(f"Could not get fit summary: {e}")

                # Get model info from leaderboard for chart data
                leaderboard = predictor.leaderboard(silent=True)
                if leaderboard is not None:
                    models = []
                    for _, row in leaderboard.iterrows():
                        model_data = {
                            "model": str(row.get('model', 'Unknown')),
                            "fit_time": float(row.get('fit_time', 0)) if pd.notna(row.get('fit_time')) else 0,
                            "score_val": float(row.get('score_val', 0)) if pd.notna(row.get('score_val')) else 0,
                            "pred_time_val": float(row.get('pred_time_val', 0)) if pd.notna(row.get('pred_time_val')) else 0
                        }
                        models.append(model_data)
                    result["models"] = normalize_leaderboard_rows(models) or []

            elif model_type == "timeseries":
                predictor = load_predictor(model_path, model_type)

                leaderboard = predictor.leaderboard()
                if leaderboard is not None:
                    models = []
                    for _, row in leaderboard.iterrows():
                        model_data = {}
                        for col in leaderboard.columns:
                            val = row[col]
                            if pd.isna(val):
                                model_data[col] = None
                            elif isinstance(val, (np.integer, np.floating)):
                                model_data[col] = float(val)
                            else:
                                model_data[col] = str(val)
                        models.append(model_data)
                    result["models"] = normalize_leaderboard_rows(models) or []

        except Exception as e:
            logger.error(f"Error getting learning curves: {e}")
            result["error"] = str(e)

        return result

    def get_shap_values(
        self,
        model_path: str,
        model_type: str,
        data_path: str,
        num_samples: int = 100
    ) -> Dict[str, Any]:
        """Get SHAP values for model interpretability.

        First checks for pre-computed values (saved during training).
        Falls back to computing on-demand if not available.

        Returns raw data for UI to render chart with recharts.
        """
        result = {
            "feature_names": [],
            "feature_importance": []  # Pre-computed mean |SHAP| values for bar chart
        }

        try:
            if model_type != "tabular":
                result["error"] = "SHAP analysis only available for tabular models"
                return result

            # Check for pre-computed SHAP values first
            import json
            shap_file = os.path.join(model_path, "shap_importance.json")
            if os.path.exists(shap_file):
                logger.info(f"Loading pre-computed SHAP values from {shap_file}")
                with open(shap_file, 'r') as f:
                    shap_data = json.load(f)
                result["feature_names"] = shap_data.get("feature_names", [])
                result["feature_importance"] = shap_data.get("feature_importance", [])[:20]
                result["precomputed"] = True
                return result

            # No pre-computed values, compute on-demand
            logger.info("No pre-computed SHAP values found, computing on-demand")

            predictor = load_predictor(model_path, "tabular")

            data = load_dataframe(data_path)

            # Sample data if too large
            if len(data) > num_samples:
                data = data.sample(n=num_samples, random_state=42)

            # Remove target column
            X = data.drop(columns=[predictor.label], errors='ignore')

            try:
                import shap

                # Get the best model
                best_model_name = predictor.model_best

                # Store feature names for conversion
                feature_names = X.columns.tolist()

                # Create SHAP explainer - wrapper to convert numpy arrays back to DataFrame
                def model_predict(X_input):
                    # SHAP passes numpy arrays, but AutoGluon requires DataFrames
                    if isinstance(X_input, np.ndarray):
                        X_df = pd.DataFrame(X_input, columns=feature_names)
                    else:
                        X_df = X_input
                    return predictor.predict(X_df, model=best_model_name).values

                explainer = shap.KernelExplainer(model_predict, shap.sample(X, 50))
                shap_values = explainer.shap_values(X.iloc[:min(50, len(X))])

                result["feature_names"] = X.columns.tolist()

                # Calculate mean absolute SHAP values for bar chart
                if isinstance(shap_values, np.ndarray):
                    mean_abs_shap = np.abs(shap_values).mean(axis=0)
                else:
                    mean_abs_shap = np.abs(np.array(shap_values)).mean(axis=0)

                # Create feature importance data for recharts
                feature_importance = []
                for i, (name, val) in enumerate(zip(X.columns.tolist(), mean_abs_shap)):
                    feature_importance.append({
                        "feature": str(name),
                        "importance": float(val)
                    })

                # Sort by importance
                feature_importance.sort(key=lambda x: x["importance"], reverse=True)
                result["feature_importance"] = feature_importance[:20]  # Top 20

                # Save for next time
                try:
                    shap_data = {
                        "feature_names": feature_names,
                        "feature_importance": feature_importance,
                        "num_samples_used": len(data),
                        "computed_at": pd.Timestamp.now().isoformat()
                    }
                    with open(shap_file, 'w') as f:
                        json.dump(shap_data, f, indent=2)
                    logger.info(f"Saved SHAP values to {shap_file}")
                except Exception as save_err:
                    logger.warning(f"Could not save SHAP values: {save_err}")

            except ImportError:
                result["error"] = "SHAP package not installed. Install with: pip install shap"
            except Exception as e:
                result["error"] = f"SHAP analysis failed: {str(e)}"

        except Exception as e:
            logger.error(f"Error computing SHAP values: {e}")
            result["error"] = str(e)

        return result


    def compute_all_diagnostics(
        self,
        model_path: str,
        model_type: str,
        data_path: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Compute all diagnostics at once and return a dict keyed by method name.

        Called during training (in the Domino Job) while the model and data are
        on the local filesystem.  The returned dict is stored in the DB so the
        App can serve diagnostics without needing the model files.
        """
        stored: Dict[str, Any] = {}

        # --- leaderboard ---
        stored["get_leaderboard"] = self.get_leaderboard(model_path, model_type)

        # --- feature importance ---
        stored["get_feature_importance"] = self.get_feature_importance(
            model_path, model_type, data_path=data_path
        )

        # --- learning curves ---
        stored["get_learning_curves"] = self.get_learning_curves(model_path, model_type)

        if not data_path or not os.path.exists(data_path):
            return stored

        # Diagnostics that require the data file:

        # --- confusion matrix (classification only) ---
        cm = self.get_confusion_matrix(model_path, model_type, data_path)
        if not cm.get("error"):
            stored["get_confusion_matrix"] = cm

        # --- ROC curve (binary classification only) ---
        roc = self.get_roc_curve(model_path, model_type, data_path)
        if not roc.get("error"):
            stored["get_roc_curve"] = roc

        # --- precision-recall curve (binary classification only) ---
        pr = self.get_precision_recall_curve(model_path, model_type, data_path)
        if not pr.get("error"):
            stored["get_precision_recall_curve"] = pr

        # --- regression diagnostics ---
        reg = self.get_regression_diagnostics(model_path, model_type, data_path)
        if not reg.get("error"):
            stored["get_regression_diagnostics"] = reg

        return stored


@lru_cache()
def get_model_diagnostics() -> ModelDiagnostics:
    """Get the model diagnostics singleton (cached)."""
    return ModelDiagnostics()
