"""Tests for ExperimentTracker.log_training_results."""

from contextlib import contextmanager
from unittest.mock import MagicMock, patch

from app.core.experiment_tracker import ExperimentTracker


def _make_tracker() -> ExperimentTracker:
    tracker = ExperimentTracker.__new__(ExperimentTracker)
    tracker.settings = MagicMock(mlflow_tracking_uri=None)
    return tracker


def _mock_mlflow_run(run_id: str = "run-abc"):
    run = MagicMock()
    run.info.run_id = run_id
    run.__enter__ = MagicMock(return_value=run)
    run.__exit__ = MagicMock(return_value=False)
    return run


@contextmanager
def _patch_mlflow():
    with (
        patch("mlflow.start_run", return_value=_mock_mlflow_run()),
        patch("mlflow.end_run"),
        patch("mlflow.active_run", return_value=None),
        patch("mlflow.log_params"),
        patch("mlflow.log_metrics"),
        patch("mlflow.set_tags"),
        patch("mlflow.log_artifact"),
        patch("mlflow.log_artifacts") as mock_log_artifacts,
        patch("mlflow.pyfunc.log_model") as mock_pyfunc_log_model,
    ):
        yield mock_pyfunc_log_model, mock_log_artifacts


class TestLogTrainingResults:

    def test_pyfunc_log_model_call_contract(self, tmp_path):
        """pyfunc.log_model must be used (not log_artifacts) with the correct artifact_path
        and artifacts dict so Domino can find MLmodel for model category inference and
        the registration route can parse the artifact URI correctly."""
        model_dir = str(tmp_path / "model")
        tracker = _make_tracker()

        with _patch_mlflow() as (mock_pyfunc, mock_log_artifacts):
            tracker.log_training_results(
                job_config={"model_type": "tabular", "name": "test"},
                metrics={},
                leaderboard=[],
                model_path=model_dir,
            )

        mock_pyfunc.assert_called_once()
        assert mock_pyfunc.call_args.kwargs["artifact_path"] == "autogluon_model"
        assert mock_pyfunc.call_args.kwargs["artifacts"] == {"model": model_dir}
        mock_log_artifacts.assert_not_called()

    def test_skips_pyfunc_when_no_model_path(self):
        tracker = _make_tracker()

        with _patch_mlflow() as (mock_pyfunc, _):
            tracker.log_training_results(
                job_config={"model_type": "tabular", "name": "test"},
                metrics={},
                leaderboard=[],
                model_path=None,
            )

        mock_pyfunc.assert_not_called()
