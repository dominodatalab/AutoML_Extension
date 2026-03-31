"""Background training worker with Domino experiment tracking."""

import asyncio
import json
import logging
import os
from typing import Any, Dict, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_settings
from app.db.database import async_session_maker
from app.db import crud
from app.db.models import JobStatus
from app.core.autogluon_runner import AutoGluonRunner
from app.api.schemas.job import AdvancedAutoGluonConfig as AdvancedConfig
from app.core.experiment_tracker import ExperimentTracker
from app.core.domino_registry import get_domino_registry
from app.core.model_diagnostics import get_model_diagnostics
from app.core.model_loader import load_predictor, load_dataframe
from app.core.utils import utc_now
from app.services.models import JobConfig

logger = logging.getLogger(__name__)


async def add_job_log(
    job_id: str,
    message: str,
    db: Optional[AsyncSession],
    level: str = "info",
):
    """This logs the job log

    This logs to stdout/stderr if we are running a domino job
    and still writes to the db if run locally"""

    if db is None:
        level = level.lower()
        if level == "info":
            logger.info(message)
        elif level == "debug":
            logger.debug(message)
        elif level in {"warn", "warning"}:
            logger.warning(message)
        elif level == "error":
            logger.error(message)
    else:
        await crud.add_job_log(
            db,
            job_id,
            message,
            level,
        )

async def update_job_status(
    job_id: str,
    status: JobStatus,
    db: Optional[AsyncSession] = None,
    **kwargs: Any,
):
    """Update job status when a database session is available."""
    if db is not None:
        return await crud.update_job_status(db, job_id, status, **kwargs)
    return None


async def update_job_progress(
    job_id: str,
    progress: int,
    db: Optional[AsyncSession] = None,
    **kwargs: Any,
):
    """Update job progress when a database session is available."""
    if db is not None:
        return await crud.update_job_progress(db, job_id, progress, **kwargs)
    return None


async def _get_job_config(
    job_config: Optional[JobConfig],
    job_id: str,
    db: Optional[AsyncSession] = None,
):
    """Resolve a JobConfig from the provided config or the database."""
    if job_config is not None and job_config.id == job_id:
        return job_config

    if job_config is None and db is not None:
        job = await crud.get_job(db, job_id)
        if job is None:
            return None
        return JobConfig.from_job(job)

    return None


async def _check_cancelled(
    job_id: str,
    db_session: Optional[Any] = None,
) -> None:
    """Raise CancelledError if the job has been cancelled in the database."""
    if db_session is not None:
        job = await crud.get_job(db_session, job_id)
        if job and job.status == JobStatus.CANCELLED:
            raise asyncio.CancelledError(f"Job {job_id} cancelled via database status")


def parse_advanced_config(config_dict: Dict[str, Any]) -> AdvancedConfig:
    """Parse advanced config dict into AdvancedConfig (Pydantic) object.

    Pydantic's model_validate handles nested object deserialization (e.g.
    hpo_config, threshold_config, per_model_hyperparameters) automatically,
    and silently ignores unknown keys via model_config, so no manual
    filtering or construction is needed.
    """
    if not config_dict:
        return AdvancedConfig()

    return AdvancedConfig.model_validate(config_dict)


class TrainingProgressReporter:
    """Reports training progress to database and MLflow."""

    def __init__(self, job_id: str, db_session, tracker: ExperimentTracker):
        self.job_id = job_id
        self.db = db_session
        self.tracker = tracker
        self.models_trained = 0
        self.current_model = None
        self.progress_percent = 0
        self.metrics_history = []

    async def on_model_start(self, model_name: str, model_index: int, total_models: int):
        """Called when a model starts training."""
        self.current_model = model_name
        self.progress_percent = int((model_index / max(total_models, 1)) * 100)

        await add_job_log(
            self.job_id,
            f"Training model {model_index + 1}/{total_models}: {model_name}",
            self.db,
        )

        # Update job progress with models_trained and current_model
        await update_job_progress(
            self.job_id,
            progress=self.progress_percent,
            db=self.db,
            current_step=f"Training {model_name}",
            models_trained=self.models_trained,
            current_model=model_name
        )

    async def on_model_complete(self, model_name: str, metrics: Dict[str, float]):
        """Called when a model completes training."""
        self.models_trained += 1
        self.metrics_history.append({
            "model": model_name,
            "metrics": metrics,
            "timestamp": utc_now().isoformat()
        })

        # Note: Individual model metrics are logged by log_training_results
        # after training completes, with each model getting its own MLflow run
        # (matching the notebook pattern)

        await add_job_log(
            self.job_id,
            f"Model {model_name} completed - metrics: {json.dumps(metrics)}",
            self.db,
        )

        # Update job progress with new models_trained count
        await update_job_progress(
            self.job_id,
            progress=self.progress_percent,
            db=self.db,
            current_step=f"Completed {model_name}",
            models_trained=self.models_trained,
            current_model=model_name
        )

    async def on_progress_update(self, progress: int, message: str):
        """Called for general progress updates."""
        self.progress_percent = progress
        await update_job_progress(
            self.job_id,
            progress=progress,
            db=self.db,
            current_step=message,
            models_trained=self.models_trained,
            current_model=self.current_model
        )

async def run_training_job(
    job_id: str,
    job_config: Optional[JobConfig] = None,
    advanced_config: Optional[Dict[str, Any]] = None,
):
    """
    Run a training job in the background with Domino experiment tracking.

    This function is called as a background task by FastAPI.
    """
    await run_training_job_with_db(job_id, job_config, advanced_config)

async def run_training_job_with_db(
    job_id: str,
    job_config: Optional[JobConfig] = None,
    advanced_config: Optional[Dict[str, Any]] = None,
    db: Optional[AsyncSession] = None,
):
        settings = get_settings()
        tracker = None

        try:
            job_config = await _get_job_config(job_config, job_id, db)
            if not job_config:
                logger.error(f"Job config unresolved for job: {job_id}")
                return

            await _check_cancelled(job_id, db)

            # Update status to running
            await update_job_status(
                job_id, JobStatus.RUNNING, db, started_at=utc_now()
            )
            await add_job_log(job_id, "Training job started", db)

            # Initialize components
            runner = AutoGluonRunner()
            if job_config.enable_mlflow and not settings.standalone_mode:
                tracker = ExperimentTracker()
            else:
                reason = "not requested" if not job_config.enable_mlflow else "standalone mode"
                await add_job_log(job_id, f"Experiment tracking disabled ({reason})", db)
            data_path = job_config.file_path
            logger.info(f"[TRAINING] data_path: {data_path}")
            await add_job_log(job_id, f"Using data file: {data_path}", db)

            await _check_cancelled(job_id, db)

            # Check if file exists
            if not os.path.exists(data_path):
                logger.error(f"[TRAINING DEBUG] FILE NOT FOUND: {data_path}")
                await add_job_log(job_id, f"[DEBUG] FILE DOES NOT EXIST: {data_path}", db, "ERROR")

            # Set up experiment tracking (Domino uses MLflow)
            experiment_name = job_config.experiment_name or f"{job_config.name}__{utc_now().strftime('%Y%m%d_%H%M%S')}"
            run_id = None
            if tracker:
                tracker.create_experiment(experiment_name)
                await add_job_log(job_id, f"MLflow experiment: {experiment_name}", db)

                # Start MLflow run with comprehensive tags
                run_id = tracker.start_run(
                    run_name=job_config.name,
                    tags={
                        "job_id": job_id,
                        "model_type": job_config.model_type.value,
                        "target_column": job_config.target_column or "",
                        "preset": job_config.preset or "medium_quality",
                        "framework": "autogluon",
                        "created_by": "automl-service",
                        "domino_run": os.environ.get("DOMINO_RUN_ID", ""),
                        "domino_project": job_config.project_name or os.environ.get("DOMINO_PROJECT_NAME", ""),
                    },
                    project_id=job_config.project_id,
                    project_name=job_config.project_name,
                )

            # Create progress reporter
            progress_reporter = TrainingProgressReporter(job_id, db, tracker)

            await add_job_log(job_id, "Starting AutoGluon training...", db)
            await progress_reporter.on_progress_update(5, "Initializing AutoGluon")

            # Parse advanced config from job_config.autogluon_config
            adv_config = None
            if advanced_config:
                adv_config = parse_advanced_config(advanced_config)
            elif job_config.autogluon_config:
                # Config is stored as {"advanced": {...}, "timeseries": {...}}
                if "advanced" in job_config.autogluon_config:
                    adv_config = parse_advanced_config(job_config.autogluon_config["advanced"])
                    logger.info(f"[TRAINING] Parsed advanced config: {adv_config}")
                else:
                    # Legacy format - try direct parsing
                    adv_config = parse_advanced_config(job_config.autogluon_config)
                    logger.info(f"[TRAINING] Parsed legacy config: {adv_config}")

            # Log all training parameters to MLflow
            training_params = {
                "model_type": job_config.model_type.value,
                "target_column": job_config.target_column,
                "preset": job_config.preset,
                "time_limit": job_config.time_limit,
                "eval_metric": job_config.eval_metric,
                "problem_type": job_config.problem_type.value if job_config.problem_type else "auto",
            }

            if job_config.model_type.value == "timeseries":
                training_params.update({
                    "time_column": job_config.time_column,
                    "id_column": job_config.id_column,
                    "prediction_length": job_config.prediction_length,
                })

            if adv_config:
                training_params.update({
                    "num_gpus": adv_config.num_gpus,
                    "num_cpus": adv_config.num_cpus,
                    "num_bag_folds": adv_config.num_bag_folds,
                    "num_stack_levels": adv_config.num_stack_levels,
                    "auto_stack": adv_config.auto_stack,
                    "calibrate": adv_config.calibrate,
                    "refit_full": adv_config.refit_full,
                })

            if tracker:
                tracker.log_params(training_params)

            await progress_reporter.on_progress_update(10, "Loading data")

            # Parse timeseries config
            timeseries_config = None
            if job_config.autogluon_config:
                if "timeseries" in job_config.autogluon_config:
                    timeseries_config = job_config.autogluon_config["timeseries"]
                    logger.info(f"[TRAINING] Parsed timeseries config: {timeseries_config}")

            # Run training with advanced config
            result = await runner.run_training(
                job_id=job_id,
                model_type=job_config.model_type,
                data_path=data_path,
                target_column=job_config.target_column,
                time_column=job_config.time_column,
                id_column=job_config.id_column,
                prediction_length=job_config.prediction_length,
                problem_type=job_config.problem_type,
                preset=job_config.preset,
                time_limit=job_config.time_limit,
                eval_metric=job_config.eval_metric,
                advanced_config=adv_config,
                timeseries_config=timeseries_config,
            )

            await add_job_log(job_id, "Training completed successfully", db)
            await _check_cancelled(job_id, db)

            # Update progress with actual models trained from results
            num_models = result.get("metrics", {}).get("num_models", 0)
            best_model = result.get("metrics", {}).get("best_model", None)
            await update_job_progress(
                job_id,
                progress=90,
                db=db,
                current_step="Processing results",
                models_trained=num_models,
                current_model=best_model,
                eta_seconds=0  # Training complete, no ETA
            )
            await add_job_log(job_id, f"Trained {num_models} models, best: {best_model}", db)

            # End the initial training run before logging individual models
            if tracker:
                tracker.end_run(status="FINISHED")

            # Generate feature importance
            feature_importance = None
            try:
                diagnostics = get_model_diagnostics()
                fi_result = diagnostics.get_feature_importance(
                    model_path=result.get("model_path"),
                    model_type=job_config.model_type.value,
                    data_path=data_path
                )
                if fi_result.get("features"):
                    feature_importance = fi_result["features"]
            except Exception as e:
                logger.warning(f"Could not generate feature importance: {e}")

            # Get the predictor for hyperparameter extraction
            predictor = None
            model_path = result.get("model_path")
            if model_path and os.path.exists(model_path):
                try:
                    predictor = load_predictor(model_path, job_config.model_type.value)
                except Exception as e:
                    logger.warning(f"Could not load predictor for hyperparameter logging: {e}")

            # Log individual model runs to Domino Experiments (like notebooks do)
            # This creates separate runs for each model in the leaderboard
            # IMPORTANT: Use the DETECTED problem_type from AutoGluon (result["metrics"]["problem_type"]),
            # NOT the user-provided job_config.problem_type which may be "auto".
            # This ensures per-model metrics are calculated correctly for classification/regression.
            detected_problem_type = result.get("metrics", {}).get("problem_type", "auto")
            experiment_job_config = {
                "job_id": job_id,
                "name": job_config.name,
                "model_type": job_config.model_type.value,
                "target_column": job_config.target_column,
                "preset": job_config.preset,
                "time_limit": job_config.time_limit,
                "eval_metric": job_config.eval_metric,
                "problem_type": detected_problem_type,  # Use detected type, not user-provided "auto"
            }

            metrics_with_fi = result.get("metrics", {}).copy()
            if feature_importance:
                metrics_with_fi["feature_importance"] = feature_importance

            # Load test data for per-model metric calculation (like notebooks do)
            test_data = None
            try:
                test_data = load_dataframe(data_path)

                # Add data shape info to experiment_job_config for logging
                if test_data is not None:
                    experiment_job_config["n_train_samples"] = len(test_data)
                    experiment_job_config["n_features"] = len(test_data.columns) - 1  # Exclude target

                logger.info(f"Loaded test data with {len(test_data)} rows for per-model metrics")
            except Exception as e:
                logger.warning(f"Could not load test data for per-model metrics: {e}")

            if tracker:
                await add_job_log(job_id, f"Logging {num_models} individual model runs to Domino Experiments", db)

                run_id = tracker.log_training_results(
                    job_config=experiment_job_config,
                    metrics=metrics_with_fi,
                    leaderboard=result.get("leaderboard", {}),
                    model_path=model_path,
                    predictor=predictor,
                    test_data=test_data,
                )

                await add_job_log(job_id, f"Model runs logged to MLflow experiment", db)
            await _check_cancelled(job_id, db)

            # Update progress: finalizing
            await update_job_progress(
                job_id,
                progress=95,
                db=db,
                current_step="Finalizing",
                models_trained=num_models,
                current_model=best_model,
                eta_seconds=0
            )

            # Update job with results
            await crud.update_job_results(
                db,
                job_id,
                metrics=result["metrics"],
                leaderboard=result["leaderboard"],
                model_path=result["model_path"],
                experiment_run_id=run_id,
                experiment_name=experiment_name,
            )

            # Final progress update: complete
            await update_job_progress(
                job_id,
                progress=100,
                db=db,
                current_step="Complete",
                models_trained=num_models,
                current_model=best_model,
                eta_seconds=0
            )

            # Update job status to COMPLETED
            await update_job_status(
                job_id, JobStatus.COMPLETED, db, completed_at=utc_now()
            )

            # Auto-register to Domino Model Registry if configured
            if job_config.auto_register and model_path and not settings.standalone_mode:
                reg_model_name = job_config.register_name or f"{job_config.name}-{job_id[:8]}"
                await add_job_log(
                    job_id,
                    f"Auto-registering model as '{reg_model_name}' in project {job_config.project_name or job_config.project_id}",
                    db,
                )
                try:
                    registry = get_domino_registry()
                    reg_result = registry.register_model(
                        model_path=model_path,
                        model_name=reg_model_name,
                        model_type=job_config.model_type.value,
                        description=f"AutoML model from job {job_config.name}",
                        metrics=result.get("metrics", {}),
                        params=training_params,
                        experiment_name=experiment_name,  # Use same experiment as training
                        project_id=job_config.project_id,
                        project_name=job_config.project_name,
                    )
                    if reg_result.get("success"):
                        await add_job_log(
                            job_id,
                            f"Model registered: {reg_result.get('model_name')} v{reg_result.get('model_version')}",
                            db,
                        )
                    else:
                        await add_job_log(
                            job_id,
                            f"Model registration returned failure: {reg_result.get('error', 'unknown')}",
                            db,
                            "WARNING",
                        )
                except Exception as e:
                    logger.warning(f"Auto-registration failed: {e}")
                    await add_job_log(
                        job_id,
                        f"Auto-registration failed: {e}",
                        db,
                        "ERROR",
                    )

            await add_job_log(
                job_id,
                f"Job completed. Best model: {result['metrics'].get('best_model')}",
                db=db,
            )

            # End MLflow run with success status
            if tracker:
                try:
                    tracker.end_run(status="FINISHED")
                except Exception as mlflow_err:
                    logger.warning(f"Could not end MLflow run: {mlflow_err}")

            logger.info(f"Training job completed: {job_id}")

        except asyncio.CancelledError:
            logger.info(f"Training job cancelled: {job_id}")
            await update_job_status(
                job_id,
                JobStatus.CANCELLED,
                db,
                completed_at=utc_now(),
            )
            await add_job_log(job_id, "Training cancelled", db, "WARNING")
            if tracker:
                try:
                    tracker.end_run(status="KILLED")
                except Exception:
                    pass
            raise  # Re-raise so the Task is properly marked cancelled

        except Exception as e:
            logger.error(f"Training job failed: {job_id} - {str(e)}")

            # Update job status to failed
            await update_job_status(
                job_id,
                JobStatus.FAILED,
                db,
                error_message=str(e),
                completed_at=utc_now(),
            )
            await add_job_log(job_id, f"Training failed: {str(e)}", db, "ERROR")

            # End MLflow run with failure status
            if tracker:
                try:
                    tracker.end_run(status="FAILED")
                except Exception:
                    pass


# TODO this is not called from in here. Is it ever used in domino job?
# I think this was used for the "register model within the app" funcitonality
async def register_trained_model(
    job_id: str,
    model_name: str,
    description: Optional[str] = None,
    stage: Optional[str] = None,
):
    """
    Register a trained model from a completed job to Domino Model Registry.

    This creates an entry in the Domino/MLflow model registry.
    """
    async with async_session_maker() as db:
        job_config = await _get_job_config(None, job_id, db)
        if not job_config:
            raise ValueError(f"Job config unresolved for job: {job_id}")

        if job_config.status != JobStatus.COMPLETED:
            raise ValueError(f"Job not completed: {job_id}")

        if not job_config.model_path:
            raise ValueError(f"Job has no model path: {job_id}")

        # Use Domino registry
        registry = get_domino_registry()

        # Prepare job info for model card
        job_info = {
            "job_id": job_id,
            "model_type": job_config.model_type.value if job_config.model_type else "tabular",
            "problem_type": job_config.problem_type.value if job_config.problem_type else "unknown",
            "target_column": job_config.target_column,
            "preset": job_config.preset,
            "time_limit": job_config.time_limit,
            "dataset_id": job_config.dataset_id,
        }

        # Get experiment name from job (set during training)
        exp_name = job_config.experiment_name if hasattr(job_config, 'experiment_name') and job_config.experiment_name else None

        result = registry.register_model(
            model_path=job_config.model_path,
            model_name=model_name,
            model_type=job_config.model_type.value if job_config.model_type else "tabular",
            description=description or f"AutoML model from job {job_config.name}",
            tags={
                "job_id": job_id,
                "job_name": job_config.name,
                "domino_project": job_config.project_name or os.environ.get("DOMINO_PROJECT_NAME", ""),
            },
            metrics=job_config.metrics if hasattr(job_config, 'metrics') and job_config.metrics else {},
            params=job_info,
            experiment_name=exp_name,  # Use same experiment as training
        )

        if not result.get("success"):
            raise ValueError(f"Registration failed: {result.get('error')}")

        version = result.get("model_version")
        logger.info(f"Registered model {model_name} version {version}")

        # Transition to requested stage if specified
        if stage and stage in ["Staging", "Production"]:
            registry.transition_model_stage(
                model_name=model_name,
                version=version,
                stage=stage
            )
            logger.info(f"Transitioned {model_name} v{version} to {stage}")

        # Generate and store model card
        try:
            model_card = registry.create_model_card(
                model_name=model_name,
                version=version,
                job_info=job_info,
                metrics=job_config.metrics if hasattr(job_config, 'metrics') and job_config.metrics else {},
            )
            # Log model card as artifact
            tracker = ExperimentTracker()
            if job_config.experiment_run_id:
                tracker.log_text(model_card, "model_card.md")
        except Exception as e:
            logger.warning(f"Could not generate model card: {e}")
        finally:
            # Ensure no MLflow run is left active — log_text / log_artifact
            # may auto-start a run that isn't closed by a context manager.
            import mlflow as _mlflow
            _mlflow.end_run()

        return {
            "model_name": model_name,
            "version": version,
            "run_id": result.get("run_id"),
            "artifact_uri": result.get("artifact_uri"),
            "stage": stage,
        }


async def deploy_model_to_production(
    model_name: str,
    version: str,
    archive_existing: bool = True,
):
    """
    Deploy a model version to production stage.

    This transitions the model to Production and optionally archives
    other production versions.
    """
    registry = get_domino_registry()

    result = registry.transition_model_stage(
        model_name=model_name,
        version=version,
        stage="Production",
        archive_existing=archive_existing
    )

    if result.get("success"):
        logger.info(f"Deployed {model_name} v{version} to Production")
    else:
        logger.error(f"Failed to deploy: {result.get('error')}")

    return result


async def compare_model_versions(model_name: str) -> Dict[str, Any]:
    """
    Compare all versions of a registered model.

    Returns metrics and metadata for each version to facilitate comparison.
    """
    registry = get_domino_registry()
    versions = registry.get_model_versions(model_name)

    comparison = {
        "model_name": model_name,
        "versions": [],
        "best_version": None,
        "best_metric": None,
    }

    for v in versions:
        version_info = {
            "version": v.get("version"),
            "stage": v.get("stage"),
            "creation_timestamp": v.get("creation_timestamp"),
            "run_id": v.get("run_id"),
            "tags": v.get("tags", {}),
        }

        # Try to get metrics from the run
        if v.get("run_id"):
            try:
                tracker = ExperimentTracker()
                run_metrics = tracker.get_run_metrics(v["run_id"])
                version_info["metrics"] = run_metrics
            except Exception:
                version_info["metrics"] = {}

        comparison["versions"].append(version_info)

    return comparison
