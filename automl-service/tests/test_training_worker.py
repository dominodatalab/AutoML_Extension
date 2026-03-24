"""Tests for training worker helpers in app.workers.training_worker."""

from app.workers.training_worker import (
    _ensure_feature_importance_diagnostics,
)


class TestEnsureFeatureImportanceDiagnostics:
    """Verify fallback behavior for feature-importance persistence."""

    def test_uses_trainer_feature_importance_when_diagnostics_missing(self):
        diagnostics_data, feature_importance = _ensure_feature_importance_diagnostics(
            diagnostics_data={
                "get_feature_importance": {
                    "model_type": "tabular",
                    "method": "auto",
                    "features": [],
                    "error": "stored failure",
                }
            },
            training_result={
                "feature_importance": [{"feature": "age", "importance": 0.31}],
            },
            model_path="/tmp/model",
            model_type="tabular",
        )

        assert feature_importance == [{"feature": "age", "importance": 0.31}]
        assert diagnostics_data["get_feature_importance"]["features"] == feature_importance
        assert diagnostics_data["get_feature_importance"]["method"] == "auto"
        assert diagnostics_data["get_feature_importance"]["error"] is None
