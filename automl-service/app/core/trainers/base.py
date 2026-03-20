"""Base trainer class with shared configuration and utilities."""

import logging
import pandas as pd

# Canonical type definitions live in the Pydantic schemas.
# Re-export them here under short aliases so trainers and the runner
# can keep using the concise names they already use.
from app.api.schemas.job import (
    AdvancedAutoGluonConfig as AdvancedConfig,
    HyperparameterTuningConfig as HpoConfig,
    DecisionThresholdConfig as ThresholdConfig,
)

logger = logging.getLogger(__name__)


class BaseTrainer:
    """Base class for all AutoGluon trainers."""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def load_data(self, data_path: str) -> pd.DataFrame:
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
