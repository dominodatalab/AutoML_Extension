"""Tests for training data-path resolution in app.workers.training_worker."""

import types
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.workers.training_worker import (
    _ensure_feature_importance_diagnostics,
    _resolve_training_data_path,
)


class TestResolveTrainingDataPath:
    """Verify the worker uses the exact user-selected dataset file."""

    @pytest.mark.asyncio
    async def test_prefers_selected_domino_dataset_file_path(self):
        job = types.SimpleNamespace(
            id="job-1",
            data_source="domino_dataset",
            dataset_id="ds-123",
            file_path="/mnt/data/sales-data/selected.csv",
            project_id="proj-1",
        )
        dataset_manager = MagicMock()
        dataset_manager.get_dataset_file_path = AsyncMock()

        with patch(
            "app.workers.training_worker.ensure_local_file",
            AsyncMock(return_value="/tmp/cache/selected.csv"),
        ), patch(
            "app.workers.training_worker.os.path.exists",
            side_effect=lambda path: path == "/tmp/cache/selected.csv",
        ):
            data_path, log_message = await _resolve_training_data_path(job, dataset_manager)

        assert data_path == "/tmp/cache/selected.csv"
        assert "selected.csv" in log_message
        dataset_manager.get_dataset_file_path.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_falls_back_to_dataset_lookup_with_selected_relative_path(self):
        job = types.SimpleNamespace(
            id="job-2",
            data_source="domino_dataset",
            dataset_id="ds-123",
            file_path="/mnt/data/sales-data/nested/selected.csv",
            project_id="proj-1",
        )
        dataset_manager = MagicMock()
        dataset_manager.get_dataset_file_path = AsyncMock(
            return_value="/mnt/imported/data/sales-data/nested/selected.csv"
        )

        with patch(
            "app.workers.training_worker.ensure_local_file",
            AsyncMock(
                side_effect=[
                    "/mnt/data/sales-data/nested/selected.csv",
                    "/tmp/cache/nested/selected.csv",
                ]
            ),
        ), patch(
            "app.workers.training_worker.os.path.exists",
            side_effect=lambda path: path == "/tmp/cache/nested/selected.csv",
        ):
            data_path, log_message = await _resolve_training_data_path(job, dataset_manager)

        assert data_path == "/tmp/cache/nested/selected.csv"
        assert log_message == "Using Domino dataset file: nested/selected.csv"
        dataset_manager.get_dataset_file_path.assert_awaited_once_with(
            "ds-123",
            file_name="nested/selected.csv",
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
