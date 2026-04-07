"""Tests for ExperimentTracker.log_training_results."""

from contextlib import contextmanager
from unittest.mock import MagicMock, patch

import pandas as pd

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
        patch("mlflow.pyfunc.save_model") as mock_pyfunc_save_model,
    ):
        yield mock_pyfunc_save_model, mock_log_artifacts


class TestLogTrainingResults:

    def test_model_logging_contract(self, tmp_path):
        """save_model must be called to produce an MLmodel file (so Domino can infer
        model category), and log_artifacts must upload files to the run-based artifact
        path so the endpoint build's `mlflow artifacts download` can find them.
        Using log_model in MLflow 3.x stores files at the logged-model path instead,
        breaking the download."""
        model_dir = str(tmp_path / "model")
        tracker = _make_tracker()

        with _patch_mlflow() as (mock_save_model, mock_log_artifacts):
            tracker.log_training_results(
                job_config={"model_type": "tabular", "name": "test"},
                metrics={},
                leaderboard=[],
                model_path=model_dir,
            )

        mock_save_model.assert_called_once()
        assert mock_save_model.call_args.kwargs["artifacts"] == {"model": model_dir}
        mock_log_artifacts.assert_called_once()
        assert mock_log_artifacts.call_args.kwargs["artifact_path"] == "autogluon_model"

    def test_predict_parses_dataframe_split_format(self, tmp_path):
        """predict must parse MLflow's dataframe_split format into a DataFrame.
        Domino's MlflowWrapper passes the raw request body dict to LOADED_MODEL.predict(),
        which MLflow forwards unchanged (no signature = no schema enforcement)."""
        model_dir = str(tmp_path / "model")
        tracker = _make_tracker()

        with _patch_mlflow() as (mock_save_model, _):
            tracker.log_training_results(
                job_config={"model_type": "tabular", "name": "test"},
                metrics={},
                leaderboard=[],
                model_path=model_dir,
            )

        wrapper = mock_save_model.call_args.kwargs["python_model"]
        wrapper._predictor = MagicMock()

        wrapper.predict(None, {
            "dataframe_split": {
                "columns": ["age", "income"],
                "data": [[25, 45000]],
            }
        }, params=None)
        call_arg = wrapper._predictor.predict.call_args[0][0]
        assert isinstance(call_arg, pd.DataFrame)
        assert list(call_arg.columns) == ["age", "income"]
        assert call_arg.iloc[0]["age"] == 25

    def test_predict_coerces_plain_dict_to_dataframe(self, tmp_path):
        """predict must convert a plain dict to DataFrame as a fallback."""
        model_dir = str(tmp_path / "model")
        tracker = _make_tracker()

        with _patch_mlflow() as (mock_save_model, _):
            tracker.log_training_results(
                job_config={"model_type": "tabular", "name": "test"},
                metrics={},
                leaderboard=[],
                model_path=model_dir,
            )

        wrapper = mock_save_model.call_args.kwargs["python_model"]
        wrapper._predictor = MagicMock()

        wrapper.predict(None, {"age": [25], "income": [45000]}, params=None)
        call_arg = wrapper._predictor.predict.call_args[0][0]
        assert isinstance(call_arg, pd.DataFrame)

    def test_predict_passes_dataframe_through_unchanged(self, tmp_path):
        """predict must not re-wrap input that is already a DataFrame."""
        model_dir = str(tmp_path / "model")
        tracker = _make_tracker()

        with _patch_mlflow() as (mock_save_model, _):
            tracker.log_training_results(
                job_config={"model_type": "tabular", "name": "test"},
                metrics={},
                leaderboard=[],
                model_path=model_dir,
            )

        wrapper = mock_save_model.call_args.kwargs["python_model"]
        wrapper._predictor = MagicMock()

        df = pd.DataFrame({"age": [25], "income": [45000]})
        wrapper.predict(None, df, params=None)
        call_arg = wrapper._predictor.predict.call_args[0][0]
        assert call_arg is df

    def test_skips_model_logging_when_no_model_path(self):
        tracker = _make_tracker()

        with _patch_mlflow() as (mock_save_model, _):
            tracker.log_training_results(
                job_config={"model_type": "tabular", "name": "test"},
                metrics={},
                leaderboard=[],
                model_path=None,
            )

        mock_save_model.assert_not_called()
