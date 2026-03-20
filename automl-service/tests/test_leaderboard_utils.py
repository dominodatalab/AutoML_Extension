"""Tests for leaderboard payload normalization helpers."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.leaderboard_utils import (  # noqa: E402
    normalize_leaderboard_payload,
    normalize_leaderboard_rows,
)


def test_normalize_leaderboard_rows_copies_fit_time_from_marginal():
    rows = [
        {
            "model": "WeightedEnsemble",
            "fit_time": None,
            "fit_time_marginal": 0.42,
            "pred_time_val": 1.5,
        }
    ]

    normalized = normalize_leaderboard_rows(rows)

    assert normalized == [
        {
            "model": "WeightedEnsemble",
            "fit_time": 0.42,
            "fit_time_marginal": 0.42,
            "pred_time_val": 1.5,
        }
    ]


def test_normalize_leaderboard_rows_preserves_existing_fit_time():
    rows = [
        {
            "model": "DirectTabular",
            "fit_time": 12.3,
            "fit_time_marginal": 4.5,
        }
    ]

    normalized = normalize_leaderboard_rows(rows)

    assert normalized[0]["fit_time"] == 12.3
    assert normalized[0]["fit_time_marginal"] == 4.5


def test_normalize_leaderboard_payload_updates_models_wrapper():
    payload = {
        "models": [
            {
                "model": "Theta",
                "fit_time_marginal": 0.07,
            }
        ],
        "best_model": "Theta",
    }

    normalized = normalize_leaderboard_payload(payload)

    assert normalized["models"][0]["fit_time"] == 0.07
    assert normalized["best_model"] == "Theta"
