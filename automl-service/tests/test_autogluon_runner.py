import logging
from pathlib import Path

import mlflow
import pytest

from app.core.autogluon_runner import AutoGluonRunner
from app.db.models import ModelType, ProblemType
from app.workers.training_worker import parse_advanced_config

pytestmark = pytest.mark.slow

DEFAULT_ADVANCED_CONFIG = {
    "advanced": {
        "num_gpus": 0,
        "auto_stack": False,
        "dynamic_stacking": False,
        "excluded_model_types": [],
        "included_model_types": [],
        "feature_prune": False,
        "calibrate": False,
        "refit_full": False,
        "set_best_to_refit_full": False,
        "use_bag_holdout": False,
        "pseudo_labeling": False,
        "drop_unique": False,
        "cache_data": True,
        "verbosity": 2,
        "distill": False,
        "use_tabular_foundation_models": False,
    }
}


def _get_advanced_config():
    return parse_advanced_config(DEFAULT_ADVANCED_CONFIG)


@pytest.fixture
def local_mlflow_tracking(tmp_path, monkeypatch):
    previous_tracking_uri = mlflow.get_tracking_uri()
    matplotlib_logger = logging.getLogger("matplotlib")
    previous_matplotlib_level = matplotlib_logger.level
    home_dir = tmp_path / "home"
    xdg_cache_dir = home_dir / ".cache"
    mpl_config_dir = tmp_path / "mplconfig"
    fontconfig_cache_dir = xdg_cache_dir / "fontconfig"

    home_dir.mkdir()
    xdg_cache_dir.mkdir(parents=True)
    mpl_config_dir.mkdir()
    fontconfig_cache_dir.mkdir(parents=True)

    monkeypatch.setenv("HOME", str(home_dir))
    monkeypatch.setenv("XDG_CACHE_HOME", str(xdg_cache_dir))
    monkeypatch.setenv("MPLCONFIGDIR", str(mpl_config_dir))
    matplotlib_logger.setLevel(logging.ERROR)

    while mlflow.active_run() is not None:
        mlflow.end_run()
    mlflow.set_tracking_uri(str(tmp_path / "mlruns"))

    yield

    while mlflow.active_run() is not None:
        mlflow.end_run()
    mlflow.set_tracking_uri(previous_tracking_uri)
    matplotlib_logger.setLevel(previous_matplotlib_level)


def _assert_no_warning_or_error_output(caplog, capsys):
    problem_records = [record for record in caplog.records if record.levelno >= logging.WARNING]

    captured = capsys.readouterr()
    problem_output_lines = []
    for source, text in (("stdout", captured.out), ("stderr", captured.err)):
        for line in text.splitlines():
            lowered = line.lower()
            if "warning" in lowered or "error" in lowered:
                problem_output_lines.append(f"[{source}] {line}")

    if not problem_records and not problem_output_lines:
        return

    record_lines = "\n".join(
        f"{record.levelname} {record.name}: {record.getMessage()}"
        for record in problem_records
    )
    output_lines = "\n".join(problem_output_lines)
    pytest.fail(
        "Warnings or errors were emitted during model build.\n\n"
        f"Captured warning/error log records:\n{record_lines or '(none)'}\n\n"
        f"Captured warning/error stdout/stderr lines:\n{output_lines or '(none)'}\n\n"
        f"Full captured log output:\n{caplog.text}\n\n"
        f"Full captured stdout:\n{captured.out}\n\n"
        f"Full captured stderr:\n{captured.err}"
    )


@pytest.mark.asyncio
async def test_run_tabular_multi_class_job(multiclass_csv, local_mlflow_tracking, caplog, capsys):
    """Verify that all medium-quality tabular multiclass models train cleanly."""
    runner = AutoGluonRunner()
    caplog.set_level(logging.INFO)
    caplog.clear()

    results = await runner.run_training(
        job_id="multiclassjob",
        model_type=ModelType.TABULAR,
        data_path=multiclass_csv,
        target_column="label",
        time_column=None,
        id_column=None,
        prediction_length=10,
        problem_type=ProblemType.MULTICLASS,
        preset="medium_quality_faster_train",
        time_limit=3600,
        eval_metric=None,
        advanced_config=_get_advanced_config(),
        timeseries_config=None,
    )

    assert results["metrics"]["num_models"] == 12
    assert len(results["leaderboard"]) == 12
    _assert_no_warning_or_error_output(caplog, capsys)


@pytest.mark.asyncio
async def test_run_tabular_binary_job(tabular_csv, local_mlflow_tracking, caplog, capsys):
    """Verify that all medium-quality tabular binary models train cleanly."""
    runner = AutoGluonRunner()
    caplog.set_level(logging.INFO)
    caplog.clear()

    results = await runner.run_training(
        job_id="binaryjob",
        model_type=ModelType.TABULAR,
        data_path=tabular_csv,
        target_column="target",
        time_column=None,
        id_column=None,
        prediction_length=10,
        problem_type=ProblemType.BINARY,
        preset="medium_quality_faster_train",
        time_limit=3600,
        eval_metric=None,
        advanced_config=_get_advanced_config(),
        timeseries_config=None,
    )

    assert results["metrics"]["num_models"] == 12
    assert len(results["leaderboard"]) == 12
    _assert_no_warning_or_error_output(caplog, capsys)


@pytest.mark.asyncio
async def test_run_tabular_regression_job(regression_csv, local_mlflow_tracking, caplog, capsys):
    """Verify that all medium-quality tabular regression models train cleanly."""
    runner = AutoGluonRunner()
    caplog.set_level(logging.INFO)
    caplog.clear()

    results = await runner.run_training(
        job_id="regressionjob",
        model_type=ModelType.TABULAR,
        data_path=regression_csv,
        target_column="target",
        time_column=None,
        id_column=None,
        prediction_length=10,
        problem_type=ProblemType.REGRESSION,
        preset="medium_quality_faster_train",
        time_limit=3600,
        eval_metric=None,
        advanced_config=_get_advanced_config(),
        timeseries_config=None,
    )

    assert results["metrics"]["num_models"] == 10
    assert len(results["leaderboard"]) == 10
    _assert_no_warning_or_error_output(caplog, capsys)


@pytest.mark.asyncio
async def test_run_timeseries_job(timeseries_csv, local_mlflow_tracking, caplog, capsys):
    """Verify that the fast-training time series preset trains cleanly."""
    runner = AutoGluonRunner()
    caplog.set_level(logging.INFO)
    caplog.clear()

    results = await runner.run_training(
        job_id="timeseriesjob",
        model_type=ModelType.TIMESERIES,
        data_path=timeseries_csv,
        target_column="value",
        time_column="timestamp",
        id_column="item_id",
        prediction_length=10,
        problem_type=None,
        preset="optimize_for_deployment",
        time_limit=3600,
        eval_metric=None,
        advanced_config=_get_advanced_config(),
        timeseries_config=None,
    )

    assert results["metrics"]["num_models"] == 7
    assert len(results["leaderboard"]) == 7
    _assert_no_warning_or_error_output(caplog, capsys)
