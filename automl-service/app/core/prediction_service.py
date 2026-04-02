"""Prediction service for trained AutoGluon models."""

import logging
from functools import lru_cache
from typing import Any, Dict, List, Optional, Union
from pathlib import Path

import pandas as pd

from app.config import get_settings
from app.core.model_loader import load_predictor

logger = logging.getLogger(__name__)


class PredictionService:
    """Service for loading and running predictions with trained models."""

    def __init__(self):
        self.settings = get_settings()
        self._loaded_models: Dict[str, Any] = {}

    def _get_model_path(self, model_id: str) -> Path:
        """Get the path to a trained model."""
        return Path(self.settings.models_path) / model_id

    def _load_model(self, model_id: str, model_type: str) -> Any:
        """Load a model from disk with caching."""
        if model_id in self._loaded_models:
            return self._loaded_models[model_id]

        model_path = self._get_model_path(model_id)
        predictor = load_predictor(str(model_path), model_type)
        self._loaded_models[model_id] = predictor
        return predictor

    def predict(
        self,
        model_id: str,
        model_type: str,
        data: Union[List[Dict], pd.DataFrame],
        return_probabilities: bool = False,
    ) -> Dict[str, Any]:
        """Run predictions on input data."""
        predictor = self._load_model(model_id, model_type)

        # Convert data to DataFrame if needed
        if isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            df = data

        logger.info(f"Running prediction on {len(df)} rows")

        result = {
            "model_id": model_id,
            "model_type": model_type,
            "num_rows": len(df),
        }

        if model_type == "tabular":
            predictions = predictor.predict(df)
            result["predictions"] = predictions.tolist()

            if return_probabilities:
                try:
                    probas = predictor.predict_proba(df)
                    if isinstance(probas, pd.DataFrame):
                        result["probabilities"] = probas.to_dict(orient="records")
                    else:
                        result["probabilities"] = probas.tolist()
                except Exception as e:
                    logger.warning(f"Could not get probabilities: {e}")

            # Get prediction metadata
            result["problem_type"] = predictor.problem_type
            result["label"] = predictor.label

        elif model_type == "timeseries":
            predictions = predictor.predict(df)
            result["predictions"] = predictions.to_dict(orient="records")
            result["prediction_length"] = predictor.prediction_length
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

        return result

    def predict_from_file(
        self,
        model_id: str,
        model_type: str,
        file_path: str,
        return_probabilities: bool = False,
    ) -> Dict[str, Any]:
        """Run predictions on data from a file."""
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith((".parquet", ".pq")):
            df = pd.read_parquet(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")

        return self.predict(model_id, model_type, df, return_probabilities)

    def batch_predict(
        self,
        model_id: str,
        model_type: str,
        input_file: str,
        output_file: str,
        return_probabilities: bool = False,
    ) -> Dict[str, Any]:
        """Run batch predictions and save to file."""
        result = self.predict_from_file(model_id, model_type, input_file, return_probabilities)

        # Create output DataFrame
        output_df = pd.DataFrame({
            "prediction": result["predictions"]
        })

        if "probabilities" in result:
            prob_df = pd.DataFrame(result["probabilities"])
            output_df = pd.concat([output_df, prob_df], axis=1)

        # Save to file
        if output_file.endswith(".csv"):
            output_df.to_csv(output_file, index=False)
        elif output_file.endswith((".parquet", ".pq")):
            output_df.to_parquet(output_file, index=False)
        else:
            output_df.to_csv(output_file, index=False)

        result["output_file"] = output_file
        result["output_rows"] = len(output_df)

        return result

    def forecast(
        self,
        model_id: str,
        prediction_length: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Generate time series forecast without input data (future predictions)."""
        predictor = self._load_model(model_id, "timeseries")

        result = {
            "model_id": model_id,
            "model_type": "timeseries",
            "num_rows": 0,
        }

        try:
            # Use model's prediction_length if not specified
            if prediction_length is None:
                prediction_length = predictor.prediction_length

            # For time series, predict returns future forecasts
            # We need to get the known data from training to generate forecasts
            predictions = predictor.predict(prediction_length=prediction_length)

            if hasattr(predictions, 'to_dict'):
                result["predictions"] = predictions.to_dict(orient="records")
            else:
                result["predictions"] = predictions.tolist() if hasattr(predictions, 'tolist') else list(predictions)

            result["num_rows"] = len(predictions) if hasattr(predictions, '__len__') else 0
            result["prediction_length"] = prediction_length

        except Exception as e:
            logger.error(f"Forecast error: {e}")
            # Return empty predictions on error
            result["predictions"] = []
            result["error"] = str(e)

        return result

    def get_model_info(self, model_id: str, model_type: str) -> Dict[str, Any]:
        """Get information about a trained model."""
        predictor = self._load_model(model_id, model_type)

        info = {
            "model_id": model_id,
            "model_type": model_type,
        }

        if model_type == "tabular":
            info.update({
                "problem_type": predictor.problem_type,
                "label": predictor.label,
                "features": predictor.feature_metadata.get_features() if predictor.feature_metadata else [],
                "model_names": predictor.model_names(),
                "best_model": predictor.model_best,
                "leaderboard": predictor.leaderboard().to_dict(orient="records"),
            })
        elif model_type == "timeseries":
            info.update({
                "prediction_length": predictor.prediction_length,
                "target": predictor.target,
                "leaderboard": predictor.leaderboard().to_dict(orient="records"),
            })
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

        return info

    def unload_model(self, model_id: str) -> bool:
        """Unload a model from memory."""
        if model_id in self._loaded_models:
            del self._loaded_models[model_id]
            return True
        return False

    def get_loaded_models(self) -> List[str]:
        """Get list of currently loaded models."""
        return list(self._loaded_models.keys())


@lru_cache()
def get_prediction_service() -> PredictionService:
    """Get the prediction service singleton (cached)."""
    return PredictionService()
