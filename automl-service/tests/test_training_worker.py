"""Tests for app.workers.training_worker dispatch behaviour."""

from contextlib import ExitStack, contextmanager
import logging
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, call, patch

import pandas as pd
import pytest

from app.services.models import JobConfig
from app.db.models import JobStatus
from app.workers.training_worker import add_job_log, run_training_job, run_training_job_with_db


@pytest.fixture
def training_worker_db_harness(make_job, tmp_path):
    """Build common patched dependencies for run_training_job_with_db tests."""
    training_csv = tmp_path / "train.csv"
    training_csv.write_text("feature,target\n1,0\n2,1\n", encoding="utf-8")

    model_dir = tmp_path / "model_artifacts"
    model_dir.mkdir()

    result = {
        "metrics": {
            "best_model": "LightGBM",
            "num_models": 3,
            "problem_type": "binary",
        },
        "leaderboard": [{"model": "LightGBM", "score_val": 0.91}],
        "model_path": str(model_dir),
    }
    diagnostics = SimpleNamespace(
        get_feature_importance=lambda **_: {
            "features": [{"feature": "feature", "importance": 1.0}]
        }
    )
    predictor = object()
    test_df = pd.DataFrame({"feature": [1, 2], "target": [0, 1]})

    def make_job_config(**overrides):
        defaults = {
            "file_path": str(training_csv),
            "execution_target": "local",
            "experiment_name": "exp-1",
        }
        defaults.update(overrides)
        return JobConfig.from_job(make_job(**defaults))

    @contextmanager
    def _build(*, standalone_mode: bool, tracker: MagicMock | None = None):
        mock_db = AsyncMock()
        mock_runner = SimpleNamespace(run_training=AsyncMock(return_value=result))

        with ExitStack() as stack:
            stack.enter_context(
                patch(
                    "app.workers.training_worker.get_settings",
                    return_value=SimpleNamespace(standalone_mode=standalone_mode),
                )
            )
            mock_check_cancelled = stack.enter_context(
                patch("app.workers.training_worker._check_cancelled", new_callable=AsyncMock)
            )
            stack.enter_context(
                patch("app.workers.training_worker.AutoGluonRunner", return_value=mock_runner)
            )
            stack.enter_context(patch("app.workers.training_worker.DominoDatasetManager"))
            stack.enter_context(
                patch(
                    "app.workers.training_worker.remap_shared_path",
                    return_value=str(training_csv),
                )
            )
            stack.enter_context(
                patch(
                    "app.workers.training_worker.get_model_diagnostics",
                    return_value=diagnostics,
                )
            )
            mock_load_predictor = stack.enter_context(
                patch(
                    "app.workers.training_worker.load_predictor",
                    return_value=predictor,
                )
            )
            mock_load_dataframe = stack.enter_context(
                patch(
                    "app.workers.training_worker.load_dataframe",
                    return_value=test_df,
                )
            )
            mock_add_job_log = stack.enter_context(
                patch("app.workers.training_worker.add_job_log", new_callable=AsyncMock)
            )
            mock_update_job_status = stack.enter_context(
                patch("app.workers.training_worker.crud.update_job_status", new_callable=AsyncMock)
            )
            mock_update_job_progress = stack.enter_context(
                patch("app.workers.training_worker.crud.update_job_progress", new_callable=AsyncMock)
            )
            mock_update_job_results = stack.enter_context(
                patch("app.workers.training_worker.crud.update_job_results", new_callable=AsyncMock)
            )
            mock_tracker_cls = None
            if tracker is not None:
                mock_tracker_cls = stack.enter_context(
                    patch(
                        "app.workers.training_worker.ExperimentTracker",
                        return_value=tracker,
                    )
                )

            yield SimpleNamespace(
                make_job_config=make_job_config,
                training_csv=training_csv,
                model_dir=model_dir,
                result=result,
                predictor=predictor,
                test_df=test_df,
                mock_db=mock_db,
                mock_runner=mock_runner,
                mock_check_cancelled=mock_check_cancelled,
                mock_load_predictor=mock_load_predictor,
                mock_load_dataframe=mock_load_dataframe,
                mock_add_job_log=mock_add_job_log,
                mock_update_job_status=mock_update_job_status,
                mock_update_job_progress=mock_update_job_progress,
                mock_update_job_results=mock_update_job_results,
                mock_tracker=tracker,
                mock_tracker_cls=mock_tracker_cls,
            )

    return _build


class TestRunTrainingJob:
    """Tests for the top-level training worker entrypoint."""

    @pytest.mark.asyncio
    async def test_local_job_config_opens_db_session_and_delegates(self, make_job):
        job_config = JobConfig.from_job(make_job(execution_target="local"))
        advanced_config = {"num_gpus": 1}

        mock_db = AsyncMock()
        mock_ctx = AsyncMock()
        mock_ctx.__aenter__ = AsyncMock(return_value=mock_db)
        mock_ctx.__aexit__ = AsyncMock(return_value=False)

        with (
            patch("app.workers.training_worker.async_session_maker", return_value=mock_ctx) as mock_session_maker,
            patch("app.workers.training_worker.run_training_job_with_db", new_callable=AsyncMock) as mock_run_with_db,
        ):
            await run_training_job(job_config.id, job_config, advanced_config)

        mock_session_maker.assert_called_once_with()
        mock_run_with_db.assert_awaited_once_with(
            job_config.id,
            job_config,
            advanced_config,
            mock_db,
        )

    @pytest.mark.asyncio
    async def test_domino_job_config_skips_db_session_and_delegates(self, make_job):
        job_config = JobConfig.from_job(make_job(execution_target="domino_job"))
        advanced_config = {"num_gpus": 1}

        with (
            patch("app.workers.training_worker.async_session_maker") as mock_session_maker,
            patch("app.workers.training_worker.run_training_job_with_db", new_callable=AsyncMock) as mock_run_with_db,
        ):
            await run_training_job(job_config.id, job_config, advanced_config)

        mock_session_maker.assert_not_called()
        mock_run_with_db.assert_awaited_once_with(
            job_config.id,
            job_config,
            advanced_config,
        )


class TestRunTrainingJobWithDb:
    """Tests for the full training worker happy path."""

    @pytest.mark.asyncio
    async def test_happy_path_runs_to_completion(self, training_worker_db_harness):
        with training_worker_db_harness(standalone_mode=True) as harness:
            job_config = harness.make_job_config()
            await run_training_job_with_db(job_config.id, job_config=job_config, db=harness.mock_db)

        harness.mock_runner.run_training.assert_awaited_once_with(
            job_id=job_config.id,
            model_type=job_config.model_type,
            data_path=str(harness.training_csv),
            target_column=job_config.target_column,
            time_column=job_config.time_column,
            id_column=job_config.id_column,
            prediction_length=job_config.prediction_length,
            problem_type=job_config.problem_type,
            preset=job_config.preset,
            time_limit=job_config.time_limit,
            eval_metric=job_config.eval_metric,
            advanced_config=None,
            timeseries_config=None,
        )
        assert harness.mock_check_cancelled.await_count == 4
        harness.mock_load_predictor.assert_called_once_with(str(harness.model_dir), job_config.model_type.value)
        harness.mock_load_dataframe.assert_called_once_with(str(harness.training_csv))
        harness.mock_update_job_results.assert_awaited_once_with(
            harness.mock_db,
            job_config.id,
            metrics=harness.result["metrics"],
            leaderboard=harness.result["leaderboard"],
            model_path=harness.result["model_path"],
            experiment_run_id=None,
            experiment_name="exp-1",
        )
        assert harness.mock_update_job_status.await_args_list[0].args[:3] == (
            harness.mock_db,
            job_config.id,
            JobStatus.RUNNING,
        )
        assert harness.mock_update_job_status.await_args_list[-1].args[:3] == (
            harness.mock_db,
            job_config.id,
            JobStatus.COMPLETED,
        )
        assert harness.mock_update_job_progress.await_args_list[-1] == call(
            harness.mock_db,
            job_config.id,
            100,
            current_step="Complete",
            models_trained=3,
            current_model="LightGBM",
            eta_seconds=0,
        )
        assert any(
            awaited.args[0] == job_config.id and "Job completed. Best model: LightGBM" in awaited.args[1]
            for awaited in harness.mock_add_job_log.await_args_list
        )

    @pytest.mark.asyncio
    async def test_happy_path_runs_to_completion_with_mlflow_enabled(self, training_worker_db_harness):
        mock_tracker = MagicMock()
        mock_tracker.start_run.return_value = "initial-run-id"
        mock_tracker.log_training_results.return_value = "final-run-id"

        with training_worker_db_harness(standalone_mode=False, tracker=mock_tracker) as harness:
            job_config = harness.make_job_config(enable_mlflow=True)
            await run_training_job_with_db(job_config.id, job_config=job_config, db=harness.mock_db)

        harness.mock_tracker_cls.assert_called_once_with()
        mock_tracker.create_experiment.assert_called_once_with("exp-1")
        mock_tracker.start_run.assert_called_once()
        mock_tracker.log_params.assert_called_once()
        mock_tracker.log_training_results.assert_called_once()
        assert mock_tracker.end_run.call_args_list == [
            call(status="FINISHED"),
            call(status="FINISHED"),
        ]

        logged_job_config = mock_tracker.log_training_results.call_args.kwargs["job_config"]
        assert logged_job_config["problem_type"] == "binary"
        assert logged_job_config["n_train_samples"] == 2
        assert logged_job_config["n_features"] == 1

        harness.mock_update_job_results.assert_awaited_once_with(
            harness.mock_db,
            job_config.id,
            metrics=harness.result["metrics"],
            leaderboard=harness.result["leaderboard"],
            model_path=harness.result["model_path"],
            experiment_run_id="final-run-id",
            experiment_name="exp-1",
        )
        assert harness.mock_update_job_status.await_args_list[0].args[:3] == (
            harness.mock_db,
            job_config.id,
            JobStatus.RUNNING,
        )
        assert harness.mock_update_job_status.await_args_list[-1].args[:3] == (
            harness.mock_db,
            job_config.id,
            JobStatus.COMPLETED,
        )
        assert harness.mock_check_cancelled.await_count == 4
        assert any(
            awaited.args[0] == job_config.id and "MLflow experiment: exp-1" in awaited.args[1]
            for awaited in harness.mock_add_job_log.await_args_list
        )
        assert any(
            awaited.args[0] == job_config.id and "Model runs logged to MLflow experiment" in awaited.args[1]
            for awaited in harness.mock_add_job_log.await_args_list
        )


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
