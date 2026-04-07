from pathlib import Path
import pytest

from app.core.autogluon_runner import AutoGluonRunner
from app.workers.training_worker import parse_advanced_config
from app.db.models import ModelType, ProblemType

@pytest.mark.asyncio
async def test_run_tabular_multi_class_job():
    """
    This verifies that 12 models are trained when training a multiclass model with tabular data
    """
    runner = AutoGluonRunner()
    job_id = "fakejobid"

    advanced_config = {
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

    parsed_advanced_config = parse_advanced_config(advanced_config)
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
        advanced_config=parsed_advanced_config,
        timeseries_config=None,
    )

    assert results['metrics']['num_models'] == 12
