"""Tests for app.core.prediction_service."""

from pathlib import Path
from types import SimpleNamespace
import sys

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.prediction_service import PredictionService


class TestPredictionServiceModelPaths:
    """Model path resolution for prediction and forecasting."""

    def test_absolute_model_path_remaps_across_domino_mounts(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ) -> None:
        """Absolute paths from child jobs should resolve in the app runtime."""
        remapped_model_dir = tmp_path / "domino" / "datasets" / "local" / "automl-extension" / "models" / "job_123"
        remapped_model_dir.mkdir(parents=True)
        original_model_path = "/mnt/data/automl-extension/models/job_123"

        monkeypatch.setattr(
            "app.core.prediction_service.get_settings",
            lambda: SimpleNamespace(models_path=str(tmp_path / "unused-models")),
        )
        monkeypatch.setattr(
            "app.core.prediction_service.remap_shared_path",
            lambda path: str(remapped_model_dir) if path == original_model_path else path,
        )

        service = PredictionService()

        assert service._get_model_path(original_model_path) == remapped_model_dir

    def test_relative_model_id_resolves_under_configured_models_path(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ) -> None:
        """Relative model ids should still resolve against the configured models root."""
        models_root = tmp_path / "models"
        model_dir = models_root / "job_456"
        model_dir.mkdir(parents=True)

        monkeypatch.setattr(
            "app.core.prediction_service.get_settings",
            lambda: SimpleNamespace(models_path=str(models_root)),
        )
        monkeypatch.setattr(
            "app.core.prediction_service.remap_shared_path",
            lambda path: path,
        )

        service = PredictionService()

        assert service._get_model_path("job_456") == model_dir

    def test_format_forecast_predictions_for_single_series(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ) -> None:
        """Single-series forecasts expose point forecasts, timestamps, and quantiles."""
        monkeypatch.setattr(
            "app.core.prediction_service.get_settings",
            lambda: SimpleNamespace(models_path=str(tmp_path / "models")),
        )
        monkeypatch.setattr(
            "app.core.prediction_service.remap_shared_path",
            lambda path: path,
        )

        service = PredictionService()
        forecast_df = pd.DataFrame(
            {
                "item_id": ["default", "default"],
                "timestamp": pd.to_datetime(["2026-03-18", "2026-03-19"]),
                "mean": [10.5, 11.25],
                "0.1": [9.8, 10.4],
                "0.9": [11.2, 12.1],
            }
        )

        result = service._format_forecast_predictions(forecast_df)

        assert result["predictions"] == {"Forecast": [10.5, 11.25]}
        assert result["timestamps"] == ["2026-03-18 00:00:00", "2026-03-19 00:00:00"]
        assert result["quantiles"] == {"0.1": [9.8, 10.4], "0.9": [11.2, 12.1]}
        assert result["num_rows"] == 2

    def test_format_forecast_predictions_for_multiple_series(
        self,
        monkeypatch: pytest.MonkeyPatch,
        tmp_path: Path,
    ) -> None:
        """Multi-series forecasts are grouped by series name for table display."""
        monkeypatch.setattr(
            "app.core.prediction_service.get_settings",
            lambda: SimpleNamespace(models_path=str(tmp_path / "models")),
        )
        monkeypatch.setattr(
            "app.core.prediction_service.remap_shared_path",
            lambda path: path,
        )

        service = PredictionService()
        forecast_df = pd.DataFrame(
            {
                "item_id": ["series_a", "series_a", "series_b", "series_b"],
                "timestamp": pd.to_datetime(
                    ["2026-03-18", "2026-03-19", "2026-03-18", "2026-03-19"]
                ),
                "mean": [1.0, 2.0, 3.0, 4.0],
                "0.1": [0.5, 1.5, 2.5, 3.5],
            }
        )

        result = service._format_forecast_predictions(forecast_df)

        assert result["predictions"] == {
            "series_a": [1.0, 2.0],
            "series_b": [3.0, 4.0],
        }
        assert result["timestamps"] == ["2026-03-18 00:00:00", "2026-03-19 00:00:00"]
        assert result["quantiles"] is None
        assert result["num_rows"] == 4
