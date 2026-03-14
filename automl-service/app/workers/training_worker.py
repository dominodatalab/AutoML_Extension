"""Background training worker with Domino experiment tracking."""

import asyncio
import json
import logging
import os
from typing import Any, Dict, Optional

from app.config import get_settings
from app.db.database import async_session_maker
from app.db import crud
from app.db.models import JobStatus
from app.core.autogluon_runner import AutoGluonRunner
from app.api.schemas.job import AdvancedAutoGluonConfig as AdvancedConfig
from app.core.experiment_tracker import ExperimentTracker
from app.core.dataset_manager import DominoDatasetManager
from app.core.domino_registry import get_domino_registry
from app.core.model_diagnostics import get_model_diagnostics
from app.core.model_loader import load_predictor, load_dataframe
from app.core.utils import ensure_local_file, remap_shared_path, utc_now

logger = logging.getLogger(__name__)


async def _check_cancelled(job_id: str, db_session: Optional[Any] = None) -> None:
    """Raise CancelledError if the job has been cancelled via queue or DB status."""
    from app.core.job_queue import get_job_queue
    if get_job_queue().is_job_cancelled(job_id):
        raise asyncio.CancelledError(f"Job {job_id} cancelled via queue")

    # Domino jobs run outside the in-process queue, so cancellation is reflected in DB.
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

        await crud.add_job_log(
            self.db, self.job_id,
            f"Training model {model_index + 1}/{total_models}: {model_name}",
            "INFO"
        )

        # Update job progress with models_trained and current_model
        await crud.update_job_progress(
            self.db, self.job_id,
            progress=self.progress_percent,
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

        await crud.add_job_log(
            self.db, self.job_id,
            f"Model {model_name} completed - metrics: {json.dumps(metrics)}",
            "INFO"
        )

        # Update job progress with new models_trained count
        await crud.update_job_progress(
            self.db, self.job_id,
            progress=self.progress_percent,
            current_step=f"Completed {model_name}",
            models_trained=self.models_trained,
            current_model=model_name
        )

    async def on_progress_update(self, progress: int, message: str):
        """Called for general progress updates."""
        self.progress_percent = progress
        await crud.update_job_progress(
            self.db, self.job_id,
            progress=progress,
            current_step=message,
            models_trained=self.models_trained,
            current_model=self.current_model
        )


async def run_training_job(job_id: str, advanced_config: Optional[Dict[str, Any]] = None):
    """
    Run a training job in the background with Domino experiment tracking.

    This function is called as a background task by FastAPI.
    """
    settings = get_settings()
    tracker = None

    async with async_session_maker() as db:
        try:
            # Get job from database
            job = await crud.get_job(db, job_id)
            if not job:
                logger.error(f"Job not found: {job_id}")
                return

            await _check_cancelled(job_id, db)

            # Update status to running
            await crud.update_job_status(
                db, job_id, JobStatus.RUNNING, started_at=utc_now()
            )
            await crud.add_job_log(db, job_id, "Training job started", "INFO")

            # Initialize components
            runner = AutoGluonRunner()
            if job.enable_mlflow and not settings.standalone_mode:
                tracker = ExperimentTracker()
            else:
                reason = "not requested" if not job.enable_mlflow else "standalone mode"
                await crud.add_job_log(db, job_id, f"Experiment tracking disabled ({reason})", "INFO")
            dataset_manager = DominoDatasetManager()

            # Get data file path
            logger.info(f"[TRAINING DEBUG] Job data_source: {job.data_source}")
            logger.info(f"[TRAINING DEBUG] Job file_path: {job.file_path}")
            logger.info(f"[TRAINING DEBUG] Job dataset_id: {job.dataset_id}")

            if job.data_source == "domino_dataset":
                data_path = await dataset_manager.get_dataset_file_path(job.dataset_id)
                await crud.add_job_log(db, job_id, f"Using Domino dataset: {job.dataset_id}")
            else:
                data_path = remap_shared_path(job.file_path)
                await crud.add_job_log(db, job_id, f"Using uploaded file: {data_path}")

            data_path = await ensure_local_file(data_path, getattr(job, 'project_id', None))

            logger.info(f"[TRAINING DEBUG] Resolved data_path: {data_path}")
            await crud.add_job_log(db, job_id, f"[DEBUG] Data path resolved to: {data_path}", "INFO")

            await _check_cancelled(job_id, db)

            # Check if file exists
            import os
            if not os.path.exists(data_path):
                logger.error(f"[TRAINING DEBUG] FILE NOT FOUND: {data_path}")
                await crud.add_job_log(db, job_id, f"[DEBUG] FILE DOES NOT EXIST: {data_path}", "ERROR")

            # Set up experiment tracking (Domino uses MLflow)
            experiment_name = job.experiment_name or f"{job.name}__{utc_now().strftime('%Y%m%d_%H%M%S')}"
            run_id = None
            if tracker:
                tracker.create_experiment(experiment_name)
                await crud.add_job_log(db, job_id, f"MLflow experiment: {experiment_name}")

                # Start MLflow run with comprehensive tags
                run_id = tracker.start_run(
                    run_name=job.name,
                    tags={
                        "job_id": job_id,
                        "model_type": job.model_type.value,
                        "target_column": job.target_column or "",
                        "preset": job.preset or "medium_quality",
                        "framework": "autogluon",
                        "created_by": "automl-service",
                        "domino_run": os.environ.get("DOMINO_RUN_ID", ""),
                        "domino_project": job.project_name or os.environ.get("DOMINO_PROJECT_NAME", ""),
                    },
                    project_id=job.project_id,
                    project_name=job.project_name,
                )

            # Create progress reporter
            progress_reporter = TrainingProgressReporter(job_id, db, tracker)

            await crud.add_job_log(db, job_id, "Starting AutoGluon training...")
            await progress_reporter.on_progress_update(5, "Initializing AutoGluon")

            # Parse advanced config from job.autogluon_config
            adv_config = None
            if advanced_config:
                adv_config = parse_advanced_config(advanced_config)
            elif job.autogluon_config:
                # Config is stored as {"advanced": {...}, "timeseries": {...}}
                if "advanced" in job.autogluon_config:
                    adv_config = parse_advanced_config(job.autogluon_config["advanced"])
                    logger.info(f"[TRAINING] Parsed advanced config: {adv_config}")
                else:
                    # Legacy format - try direct parsing
                    adv_config = parse_advanced_config(job.autogluon_config)
                    logger.info(f"[TRAINING] Parsed legacy config: {adv_config}")

            # Log all training parameters to MLflow
            training_params = {
                "model_type": job.model_type.value,
                "target_column": job.target_column,
                "preset": job.preset,
                "time_limit": job.time_limit,
                "eval_metric": job.eval_metric,
                "problem_type": job.problem_type.value if job.problem_type else "auto",
            }

            if job.model_type.value == "timeseries":
                training_params.update({
                    "time_column": job.time_column,
                    "id_column": job.id_column,
                    "prediction_length": job.prediction_length,
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
            if job.autogluon_config:
                if "timeseries" in job.autogluon_config:
                    timeseries_config = job.autogluon_config["timeseries"]
                    logger.info(f"[TRAINING] Parsed timeseries config: {timeseries_config}")

            # Resolve project-scoped storage for model output
            models_path = None
            temp_path = None
            if job.project_id and not settings.standalone_mode:
                try:
                    from app.services.storage_resolver import get_storage_resolver

                    project_paths = await get_storage_resolver().resolve_project_paths(
                        job.project_id
                    )
                    models_path = project_paths.models_path
                    os.makedirs(models_path, exist_ok=True)
                    temp_path = project_paths.temp_path
                    os.makedirs(temp_path, exist_ok=True)
                except Exception as e:
                    logger.warning(
                        "Could not resolve project storage, using default: %s", e
                    )

            # Run training with advanced config
            result = await runner.run_training(
                job_id=job_id,
                model_type=job.model_type,
                data_path=data_path,
                target_column=job.target_column,
                time_column=job.time_column,
                id_column=job.id_column,
                prediction_length=job.prediction_length,
                problem_type=job.problem_type,
                preset=job.preset,
                time_limit=job.time_limit,
                eval_metric=job.eval_metric,
                advanced_config=adv_config,
                timeseries_config=timeseries_config,
                models_path=models_path,
                temp_path=temp_path,
            )

            await crud.add_job_log(db, job_id, "Training completed successfully")
            await _check_cancelled(job_id, db)

            # Update progress with actual models trained from results
            num_models = result.get("metrics", {}).get("num_models", 0)
            best_model = result.get("metrics", {}).get("best_model", None)
            await crud.update_job_progress(
                db, job_id,
                progress=90,
                current_step="Processing results",
                models_trained=num_models,
                current_model=best_model,
                eta_seconds=0  # Training complete, no ETA
            )
            await crud.add_job_log(db, job_id, f"Trained {num_models} models, best: {best_model}")

            # End the initial training run before logging individual models
            if tracker:
                tracker.end_run(status="FINISHED")

            # Generate feature importance
            feature_importance = None
            try:
                diagnostics = get_model_diagnostics()
                fi_result = diagnostics.get_feature_importance(
                    model_path=result.get("model_path"),
                    model_type=job.model_type.value,
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
                    predictor = load_predictor(model_path, job.model_type.value)
                except Exception as e:
                    logger.warning(f"Could not load predictor for hyperparameter logging: {e}")

            # Log individual model runs to Domino Experiments (like notebooks do)
            # This creates separate runs for each model in the leaderboard
            # IMPORTANT: Use the DETECTED problem_type from AutoGluon (result["metrics"]["problem_type"]),
            # NOT the user-provided job.problem_type which may be "auto".
            # This ensures per-model metrics are calculated correctly for classification/regression.
            detected_problem_type = result.get("metrics", {}).get("problem_type", "auto")
            job_config = {
                "job_id": job_id,
                "name": job.name,
                "model_type": job.model_type.value,
                "target_column": job.target_column,
                "preset": job.preset,
                "time_limit": job.time_limit,
                "eval_metric": job.eval_metric,
                "problem_type": detected_problem_type,  # Use detected type, not user-provided "auto"
            }

            metrics_with_fi = result.get("metrics", {}).copy()
            if feature_importance:
                metrics_with_fi["feature_importance"] = feature_importance

            # Load test data for per-model metric calculation (like notebooks do)
            test_data = None
            try:
                test_data = load_dataframe(data_path)

                # Add data shape info to job_config for logging
                if test_data is not None:
                    job_config["n_train_samples"] = len(test_data)
                    job_config["n_features"] = len(test_data.columns) - 1  # Exclude target

                logger.info(f"Loaded test data with {len(test_data)} rows for per-model metrics")
            except Exception as e:
                logger.warning(f"Could not load test data for per-model metrics: {e}")

            if tracker:
                await crud.add_job_log(db, job_id, f"Logging {num_models} individual model runs to Domino Experiments")

                run_id = tracker.log_training_results(
                    job_config=job_config,
                    metrics=metrics_with_fi,
                    leaderboard=result.get("leaderboard", {}),
                    model_path=model_path,
                    predictor=predictor,
                    test_data=test_data,
                    temp_path=temp_path,
                )

                await crud.add_job_log(db, job_id, f"Model runs logged to MLflow experiment")
            await _check_cancelled(job_id, db)

            # Update progress: finalizing
            await crud.update_job_progress(
                db, job_id,
                progress=95,
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
            await crud.update_job_progress(
                db, job_id,
                progress=100,
                current_step="Complete",
                models_trained=num_models,
                current_model=best_model,
                eta_seconds=0
            )

            # Update job status to COMPLETED
            await crud.update_job_status(
                db, job_id, JobStatus.COMPLETED, completed_at=utc_now()
            )

            # Auto-register to Domino Model Registry if configured
            if job.auto_register and model_path and not settings.standalone_mode:
                reg_model_name = job.register_name or f"{job.name}-{job_id[:8]}"
                await crud.add_job_log(
                    db, job_id,
                    f"Auto-registering model as '{reg_model_name}' in project {job.project_name or job.project_id}",
                    "INFO",
                )
                try:
                    registry = get_domino_registry()
                    reg_result = registry.register_model(
                        model_path=model_path,
                        model_name=reg_model_name,
                        model_type=job.model_type.value,
                        description=f"AutoML model from job {job.name}",
                        metrics=result.get("metrics", {}),
                        params=training_params,
                        experiment_name=experiment_name,  # Use same experiment as training
                        project_id=job.project_id,
                        project_name=job.project_name,
                        temp_path=temp_path,
                    )
                    if reg_result.get("success"):
                        await crud.add_job_log(
                            db, job_id,
                            f"Model registered: {reg_result.get('model_name')} v{reg_result.get('model_version')}",
                            "INFO",
                        )
                    else:
                        await crud.add_job_log(
                            db, job_id,
                            f"Model registration returned failure: {reg_result.get('error', 'unknown')}",
                            "WARNING",
                        )
                except Exception as e:
                    logger.warning(f"Auto-registration failed: {e}")
                    await crud.add_job_log(
                        db, job_id,
                        f"Auto-registration failed: {e}",
                        "ERROR",
                    )

            await crud.add_job_log(
                db, job_id,
                f"Job completed. Best model: {result['metrics'].get('best_model')}"
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
            await crud.update_job_status(
                db, job_id, JobStatus.CANCELLED,
                completed_at=utc_now(),
            )
            await crud.add_job_log(db, job_id, "Training cancelled", "WARNING")
            if tracker:
                try:
                    tracker.end_run(status="KILLED")
                except Exception:
                    pass
            raise  # Re-raise so the Task is properly marked cancelled

        except Exception as e:
            logger.error(f"Training job failed: {job_id} - {str(e)}")

            # Update job status to failed
            await crud.update_job_status(
                db,
                job_id,
                JobStatus.FAILED,
                error_message=str(e),
                completed_at=utc_now(),
            )
            await crud.add_job_log(db, job_id, f"Training failed: {str(e)}", "ERROR")

            # End MLflow run with failure status
            if tracker:
                try:
                    tracker.end_run(status="FAILED")
                except Exception:
                    pass


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
        job = await crud.get_job(db, job_id)
        if not job:
            raise ValueError(f"Job not found: {job_id}")

        if job.status != JobStatus.COMPLETED:
            raise ValueError(f"Job not completed: {job_id}")

        if not job.model_path:
            raise ValueError(f"Job has no model path: {job_id}")

        # Resolve temp_path from project storage or fall back to settings
        temp_path = None
        if job.project_id and not get_settings().standalone_mode:
            try:
                from app.services.storage_resolver import get_storage_resolver

                project_paths = await get_storage_resolver().resolve_project_paths(
                    job.project_id
                )
                temp_path = project_paths.temp_path
            except Exception:
                pass

        # Use Domino registry
        registry = get_domino_registry()

        # Prepare job info for model card
        job_info = {
            "job_id": job_id,
            "model_type": job.model_type.value if job.model_type else "tabular",
            "problem_type": job.problem_type.value if job.problem_type else "unknown",
            "target_column": job.target_column,
            "preset": job.preset,
            "time_limit": job.time_limit,
            "dataset_id": job.dataset_id,
        }

        # Get experiment name from job (set during training)
        exp_name = job.experiment_name if hasattr(job, 'experiment_name') and job.experiment_name else None

        result = registry.register_model(
            model_path=job.model_path,
            model_name=model_name,
            model_type=job.model_type.value if job.model_type else "tabular",
            description=description or f"AutoML model from job {job.name}",
            tags={
                "job_id": job_id,
                "job_name": job.name,
                "domino_project": job.project_name or os.environ.get("DOMINO_PROJECT_NAME", ""),
            },
            metrics=job.metrics if hasattr(job, 'metrics') and job.metrics else {},
            params=job_info,
            experiment_name=exp_name,  # Use same experiment as training
            temp_path=temp_path,
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
                metrics=job.metrics if hasattr(job, 'metrics') and job.metrics else {},
            )
            # Log model card as artifact
            tracker = ExperimentTracker()
            if job.experiment_run_id:
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
