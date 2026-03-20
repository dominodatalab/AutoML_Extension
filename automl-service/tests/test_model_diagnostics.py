"""Tests for model diagnostics helpers."""

from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.model_diagnostics import ModelDiagnostics  # noqa: E402


class _FakeTimeSeriesPredictor:
    def __init__(self, importance: pd.DataFrame):
        self._importance = importance

    def feature_importance(self):
        return self._importance


def test_timeseries_feature_importance_parses_dataframe(monkeypatch):
    importance = pd.DataFrame(
        {
            "importance": [0.73, -0.11],
            "stdev": [0.04, 0.02],
        },
        index=["promo", "price"],
    )

    monkeypatch.setattr(
        "app.core.model_diagnostics.load_predictor",
        lambda *_: _FakeTimeSeriesPredictor(importance),
    )

    result = ModelDiagnostics().get_feature_importance(
        model_path="/tmp/model",
        model_type="timeseries",
    )

    assert result["features"] == [
        {"feature": "promo", "importance": 0.73, "stddev": 0.04},
        {"feature": "price", "importance": -0.11, "stddev": 0.02},
    ]


def test_timeseries_feature_importance_returns_empty_for_target_only_model(monkeypatch):
    monkeypatch.setattr(
        "app.core.model_diagnostics.load_predictor",
        lambda *_: _FakeTimeSeriesPredictor(pd.DataFrame(columns=["importance", "stdev"])),
    )

    result = ModelDiagnostics().get_feature_importance(
        model_path="/tmp/model",
        model_type="timeseries",
    )

    assert result["features"] == []
    assert result.get("error") is None
