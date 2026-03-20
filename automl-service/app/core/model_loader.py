"""Shared model loading utility for AutoGluon models."""

import logging
from typing import Any
from pathlib import Path

logger = logging.getLogger(__name__)


def load_predictor(model_path: str, model_type: str) -> Any:
    """Load an AutoGluon predictor from disk.

    Args:
        model_path: Path to the saved model directory.
        model_type: One of "tabular", "timeseries".

    Returns:
        The loaded AutoGluon predictor.

    Raises:
        FileNotFoundError: If model_path doesn't exist.
        ValueError: If model_type is unknown.
    """
    path = Path(model_path)
    if not path.exists():
        raise FileNotFoundError(f"Model not found at: {model_path}")

    logger.info(f"Loading {model_type} model from {model_path}")

    if model_type == "tabular":
        from autogluon.tabular import TabularPredictor
        return TabularPredictor.load(str(path))
    elif model_type == "timeseries":
        from autogluon.timeseries import TimeSeriesPredictor
        return TimeSeriesPredictor.load(str(path))
    else:
        raise ValueError(f"Unknown model type: {model_type}")


def load_dataframe(data_path: str) -> "pd.DataFrame":
    """Load a DataFrame from a file path.

    Args:
        data_path: Path to CSV, Parquet, JSON, or Excel file.

    Returns:
        pandas DataFrame.
    """
    import pandas as pd

    if data_path.endswith(".csv"):
        return pd.read_csv(data_path)
    elif data_path.endswith((".parquet", ".pq")):
        return pd.read_parquet(data_path)
    elif data_path.endswith(".json"):
        return pd.read_json(data_path)
    elif data_path.endswith((".xlsx", ".xls")):
        return pd.read_excel(data_path)
    else:
        return pd.read_csv(data_path)
