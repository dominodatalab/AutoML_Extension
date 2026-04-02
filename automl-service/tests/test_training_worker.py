"""Tests for app.workers.training_worker dispatch behaviour."""

import logging
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.db.models import ModelType
from app.services.models import JobConfig
from app.workers.training_worker import add_job_log, run_training_job


class TestAddJobLog:
    """Tests for stdout/logger emission when no DB session is available."""

    @pytest.mark.asyncio
    async def test_logs_to_worker_logger_when_db_is_none(self, caplog):
        with (
            caplog.at_level(logging.INFO, logger="app.workers.training_worker"),
            patch("app.workers.training_worker.crud.add_job_log", new_callable=AsyncMock) as mock_add_job_log,
        ):
            await add_job_log("job-123", "Training job started", level="INFO", db=None)
            await add_job_log("job-123", "Training failed", level="ERROR", db=None)

        records = [
            (record.levelname, record.message)
            for record in caplog.records
            if record.name == "app.workers.training_worker"
        ]
        assert ("INFO", "Training job started") in records
        assert ("ERROR", "Training failed") in records
        mock_add_job_log.assert_not_awaited()


def _make_job_config(job_id: str = "job-abc", data_path: str = "/tmp/data.csv") -> JobConfig:
    return JobConfig(
        id=job_id,
        name="test-job",
        model_type=ModelType.TABULAR,
        target_column="target",
        file_path=data_path,
        data_source="domino_dataset",
        dataset_id="ds-test-123",
        preset="medium_quality_faster_train",
        time_limit=60,
        created_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
    )


def _make_training_result(tmp_path) -> dict:
    return {
        "metrics": {
            "best_model": "LightGBM",
            "best_score": 0.92,
            "num_models": 3,
            "eval_metric": "roc_auc",
            "problem_type": "binary",
        },
        "leaderboard": {"models": [{"model": "LightGBM", "score": 0.92}]},
        "model_path": str(tmp_path / "model"),
    }


class TestRunTrainingJob:
    """Tests that run_training_job correctly logs results to MLflow."""

    @pytest.mark.asyncio
    async def test_logs_training_results_to_mlflow(self, tmp_path):
        job_id = "job-abc"
        data_path = str(tmp_path / "data.csv")
        open(data_path, "w").close()

        job_config = _make_job_config(job_id=job_id, data_path=data_path)
        training_result = _make_training_result(tmp_path)
        fi_features = [{"feature": "age", "importance": 0.5}]

        mock_tracker = MagicMock()
        mock_tracker.log_training_results.return_value = "run-xyz"
        mock_runner = MagicMock()
        mock_runner.run_training = AsyncMock(return_value=training_result)
        mock_diagnostics = MagicMock()
        mock_diagnostics.get_feature_importance.return_value = {"features": fi_features}
        settings = MagicMock(standalone_mode=False)

        with (
            patch("app.workers.training_worker._get_job_config", new_callable=AsyncMock, return_value=job_config),
            patch("app.workers.training_worker._check_cancelled", new_callable=AsyncMock),
            patch("app.workers.training_worker.update_job_status", new_callable=AsyncMock),
            patch("app.workers.training_worker.update_job_progress", new_callable=AsyncMock),
            patch("app.workers.training_worker.add_job_log", new_callable=AsyncMock),
            patch("app.workers.training_worker.get_settings", return_value=settings),
            patch("app.workers.training_worker.AutoGluonRunner", return_value=mock_runner),
            patch("app.workers.training_worker.ExperimentTracker", return_value=mock_tracker),
            patch("app.workers.training_worker.get_model_diagnostics", return_value=mock_diagnostics),
            patch("app.workers.training_worker.load_predictor", return_value=MagicMock()),
            patch("app.workers.training_worker.load_dataframe", return_value=MagicMock()),
            patch("os.path.exists", return_value=True),
        ):
            await run_training_job(job_id=job_id, job_config=job_config)

        mock_tracker.log_training_results.assert_called_once()
        kwargs = mock_tracker.log_training_results.call_args.kwargs
        assert kwargs["metrics"]["feature_importance"] == fi_features
        assert kwargs["leaderboard"] == training_result["leaderboard"]
        assert kwargs["model_path"] == training_result["model_path"]