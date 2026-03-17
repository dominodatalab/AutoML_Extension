"""Static Domino Model API entrypoint for AutoML job artifacts.

This file is committed in project code so Domino Model API builds can always
resolve it. The trained model directory is provided at runtime through the
AUTOML_MODEL_DIR environment variable.
"""

import os
from pathlib import Path
from typing import Any, Dict, Tuple

import pandas as pd

_PREDICTOR = None
_MODEL_TYPE = None


def _resolve_model_dir() -> Path:
    configured = os.environ.get("AUTOML_MODEL_DIR", "").strip()
    if configured:
        return Path(configured).expanduser().resolve()
    return Path(__file__).resolve().parent


def _load_predictor() -> Tuple[Any, str]:
    global _PREDICTOR, _MODEL_TYPE

    if _PREDICTOR is not None and _MODEL_TYPE is not None:
        return _PREDICTOR, _MODEL_TYPE

    model_dir = _resolve_model_dir()
    if not model_dir.exists():
        raise RuntimeError(
            f"AUTOML_MODEL_DIR does not exist: {model_dir}. "
            "Set AUTOML_MODEL_DIR to a valid trained model directory."
        )

    errors = []

    try:
        from autogluon.tabular import TabularPredictor

        _PREDICTOR = TabularPredictor.load(str(model_dir))
        _MODEL_TYPE = "tabular"
        return _PREDICTOR, _MODEL_TYPE
    except Exception as exc:
        errors.append(f"tabular={exc}")

    try:
        from autogluon.timeseries import TimeSeriesPredictor

        _PREDICTOR = TimeSeriesPredictor.load(str(model_dir))
        _MODEL_TYPE = "timeseries"
        return _PREDICTOR, _MODEL_TYPE
    except Exception as exc:
        errors.append(f"timeseries={exc}")

    raise RuntimeError(
        f"Unable to load AutoGluon predictor from {model_dir}. "
        f"Errors: {'; '.join(errors)}"
    )


def _to_dataframe(payload: Any) -> pd.DataFrame:
    if isinstance(payload, pd.DataFrame):
        return payload
    if isinstance(payload, list):
        return pd.DataFrame(payload)
    if isinstance(payload, dict):
        if "data" in payload:
            inner = payload["data"]
            if isinstance(inner, pd.DataFrame):
                return inner
            if isinstance(inner, list):
                return pd.DataFrame(inner)
            if isinstance(inner, dict):
                return pd.DataFrame([inner])
        return pd.DataFrame([payload])
    return pd.DataFrame(payload)


def _to_serializable(value: Any):
    if hasattr(value, "to_dict"):
        try:
            return value.to_dict(orient="records")
        except TypeError:
            return value.to_dict()
    if hasattr(value, "tolist"):
        return value.tolist()
    return value


def predict(data: Any) -> Dict[str, Any]:
    predictor, model_type = _load_predictor()

    if model_type == "tabular":
        input_df = _to_dataframe(data)
        predictions = predictor.predict(input_df)
        response = {"predictions": _to_serializable(predictions)}

        try:
            probabilities = predictor.predict_proba(input_df)
            response["probabilities"] = _to_serializable(probabilities)
        except Exception:
            pass

        return response

    payload = data["data"] if isinstance(data, dict) and "data" in data else data
    if isinstance(payload, list):
        payload = pd.DataFrame(payload)
    elif isinstance(payload, dict):
        payload = pd.DataFrame(payload)

    predictions = predictor.predict(payload)
    return {"predictions": _to_serializable(predictions)}


def __getattr__(name: str):
    """Return predict for arbitrary public function names configured in Domino."""
    if name.startswith("_"):
        raise AttributeError(name)
    return predict

