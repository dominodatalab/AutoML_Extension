from pathlib import Path
import pytest

from app.core.autogluon_runner import AutoGluonRunner
from app.workers.training_worker import parse_advanced_config
from app.db.models import ModelType, ProblemType

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
        "use_tabular_foundation_models": False
    }
}


def _get_advanced_config():
    return parse_advanced_config(DEFAULT_ADVANCED_CONFIG)


@pytest.mark.asyncio
async def test_run_tabular_multi_class_job():
    """
    This verifies that 12 models are trained when training a multiclass model with tabular data
    """
    runner = AutoGluonRunner()
    job_id = "fakejobid"

    data_path = str(Path(__file__).resolve().parent / "data" / "sample_tabular.csv")
    results = await runner.run_training(
        job_id=job_id,
        model_type=ModelType.TABULAR,
        data_path=data_path,
        target_column="target",
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

    assert results['metrics']['num_models'] == 12
    assert len(results["leaderboard"]) == 12


@pytest.mark.asyncio
async def test_run_tabular_binary_job(tabular_csv):
    """Verify that all medium-quality tabular binary models are trained."""
    runner = AutoGluonRunner()
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


@pytest.mark.asyncio
async def test_run_tabular_regression_job(regression_csv):
    """Verify that all medium-quality tabular regression models are trained."""
    runner = AutoGluonRunner()
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


@pytest.mark.asyncio
async def test_run_timeseries_job(timeseries_csv):
    """Verify that the fast-training time series preset builds all expected models."""
    runner = AutoGluonRunner()
    results = await runner.run_training(
        job_id="timeseriesjob",
        model_type=ModelType.TIMESERIES,
        data_path=timeseries_csv,
        target_column="value",
        time_column="timestamp",
        id_column="item_id",
        prediction_length=10,
        problem_type=None,
        # This maps to AutoGluon TimeSeries `fast_training`, which avoids
        # foundation-model downloads while still exercising real model building.
        preset="optimize_for_deployment",
        time_limit=3600,
        eval_metric=None,
        advanced_config=_get_advanced_config(),
        timeseries_config=None,
    )

    assert results["metrics"]["num_models"] == 7
    assert len(results["leaderboard"]) == 7
