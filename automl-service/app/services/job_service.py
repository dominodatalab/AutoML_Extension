"""Service helpers for job route orchestration."""

import os
import logging
from datetime import datetime
from typing import Optional

from fastapi import HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.job import (
    JobCreateRequest,
    JobListRequest,
    JobMetricsResponse,
    JobProgressResponse,
    JobStatusResponse,
    RegisterModelRequest,
    RegisterModelResponse,
)
from app.config import get_settings
from app.db.models import Job, JobStatus, ModelType, ProblemType
from app.db import crud
from app.workers.training_worker import register_trained_model

logger = logging.getLogger(__name__)


def get_request_owner(request: Optional[Request]) -> str:
    """Extract the requesting username from Domino headers."""
    if request is None:
        return "anonymous"
    return request.headers.get("domino-username", "anonymous")


def get_project_context() -> tuple[Optional[str], Optional[str]]:
    """Resolve Domino project id/name from settings or environment."""
    settings = get_settings()
    return (
        settings.domino_project_id or os.environ.get("DOMINO_PROJECT_ID"),
        settings.domino_project_name or os.environ.get("DOMINO_PROJECT_NAME"),
    )


def validate_job_create_request(job_request: JobCreateRequest) -> None:
    """Validate job creation requirements by data/model type."""
    if job_request.data_source == "domino_dataset" and not job_request.dataset_id:
        raise HTTPException(
            status_code=400,
            detail="dataset_id is required when data_source is 'domino_dataset'",
        )

    if job_request.data_source == "upload" and not job_request.file_path:
        raise HTTPException(
            status_code=400,
            detail="file_path is required when data_source is 'upload'",
        )

    if job_request.model_type == "timeseries":
        if not job_request.time_column:
            raise HTTPException(
                status_code=400,
                detail="time_column is required for timeseries models",
            )
        if not job_request.prediction_length:
            raise HTTPException(
                status_code=400,
                detail="prediction_length is required for timeseries models",
            )


def build_autogluon_config(job_request: JobCreateRequest) -> Optional[dict]:
    """Build persisted AutoGluon config blob from request sections."""
    autogluon_config: dict = {}
    if job_request.advanced_config:
        autogluon_config["advanced"] = job_request.advanced_config.model_dump(exclude_none=True)
    if job_request.timeseries_config:
        autogluon_config["timeseries"] = job_request.timeseries_config.model_dump(exclude_none=True)
    if job_request.multimodal_config:
        autogluon_config["multimodal"] = job_request.multimodal_config.model_dump(exclude_none=True)
    if job_request.feature_columns:
        autogluon_config["feature_columns"] = job_request.feature_columns
    return autogluon_config or None


def build_job_model(
    job_request: JobCreateRequest,
    owner: str,
    project_id: Optional[str],
    project_name: Optional[str],
) -> Job:
    """Build a Job ORM model from request and resolved context."""
    execution_target = resolve_execution_target(job_request)

    return Job(
        name=job_request.name,
        description=job_request.description,
        owner=owner,
        project_id=project_id,
        project_name=project_name,
        model_type=ModelType(job_request.model_type),
        problem_type=ProblemType(job_request.problem_type) if job_request.problem_type else None,
        data_source=job_request.data_source,
        dataset_id=job_request.dataset_id,
        file_path=job_request.file_path,
        target_column=job_request.target_column,
        time_column=job_request.time_column,
        id_column=job_request.id_column,
        prediction_length=job_request.prediction_length,
        preset=job_request.preset,
        time_limit=job_request.time_limit,
        eval_metric=job_request.eval_metric,
        experiment_name=job_request.experiment_name,
        status=JobStatus.PENDING,
        execution_target=execution_target,
        autogluon_config=build_autogluon_config(job_request),
    )


def resolve_execution_target(job_request: JobCreateRequest) -> str:
    """Resolve training execution target, supporting legacy and explicit flags."""
    if job_request.execution_target == "domino_job" or job_request.run_as_domino_job:
        return "domino_job"
    return "local"


async def create_job_with_context(
    db: AsyncSession,
    job_request: JobCreateRequest,
    request: Optional[Request] = None,
) -> Job:
    """Validate, create, and enqueue a job using request-derived context."""
    owner = get_request_owner(request)
    project_id, project_name = get_project_context()

    logger.info(f"[JOB CREATE] User: {owner}, Project: {project_id} ({project_name})")
    logger.info("[JOB CREATE DEBUG] Received job create request")
    logger.info(f"[JOB CREATE DEBUG] data_source: {job_request.data_source}")
    logger.info(f"[JOB CREATE DEBUG] file_path from request: {job_request.file_path}")
    logger.info(f"[JOB CREATE DEBUG] dataset_id: {job_request.dataset_id}")

    validate_job_create_request(job_request)
    job = build_job_model(job_request, owner, project_id, project_name)
    job = await crud.create_job(db, job)

    if job.execution_target == "domino_job":
        from app.core.domino_job_launcher import get_domino_job_launcher

        settings = get_settings()
        launcher = get_domino_job_launcher()
        launch_result = launcher.start_training_job(
            job_id=job.id,
            title=job.name,
            hardware_tier_name=job_request.domino_hardware_tier_name or settings.domino_training_hardware_tier_name,
            environment_id=job_request.domino_environment_id or settings.domino_training_environment_id,
        )
        if not launch_result.get("success"):
            error_message = launch_result.get("error", "Failed to launch Domino Job")
            await crud.update_job_status(
                db=db,
                job_id=job.id,
                status=JobStatus.FAILED,
                error_message=error_message,
                completed_at=datetime.utcnow(),
            )
            raise HTTPException(status_code=502, detail=error_message)

        await crud.update_job_domino_fields(
            db=db,
            job_id=job.id,
            domino_job_id=launch_result.get("domino_job_id"),
            domino_job_status=launch_result.get("domino_job_status", "Submitted"),
        )
        refreshed = await crud.get_job(db, job.id)
        return refreshed or job

    from app.core.job_queue import get_job_queue

    await get_job_queue().enqueue(job.id)
    return job


async def list_jobs_basic(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
) -> list[Job]:
    """List jobs with optional basic status filtering."""
    status_filter = JobStatus(status) if status else None
    jobs = await crud.get_jobs(db, skip=skip, limit=limit, status=status_filter)
    return list(jobs)


async def list_jobs_filtered(
    db: AsyncSession,
    list_request: JobListRequest,
    request: Optional[Request] = None,
) -> list[Job]:
    """List jobs using advanced POST filters."""
    (
        status_filter,
        model_type_filter,
        owner_filter,
        project_id_filter,
        project_name_filter,
    ) = resolve_job_list_filters(list_request, request)

    logger.debug(
        f"[JOB LIST] Filters - owner: {owner_filter}, "
        f"project_name: {project_name_filter}, status: {status_filter}"
    )

    jobs = await crud.get_jobs(
        db,
        skip=list_request.skip,
        limit=list_request.limit,
        status=status_filter,
        model_type=model_type_filter,
        owner=owner_filter,
        project_id=project_id_filter,
        project_name=project_name_filter,
    )
    return list(jobs)


async def get_job_logs(
    db: AsyncSession,
    job_id: str,
    limit: int = 1000,
) -> list:
    """Return logs for a job after validating job existence."""
    await get_job_or_404(db, job_id)
    logs = await crud.get_job_logs(db, job_id, limit=limit)
    return list(logs)


def get_queue_status() -> dict:
    """Return current queue status."""
    from app.core.job_queue import get_job_queue

    return get_job_queue().get_queue_status()


def resolve_job_list_filters(
    list_request: JobListRequest,
    request: Optional[Request],
) -> tuple[
    Optional[JobStatus],
    Optional[ModelType],
    Optional[str],
    Optional[str],
    Optional[str],
]:
    """Resolve list filter values for status/model/user/project semantics."""
    status_filter = JobStatus(list_request.status) if list_request.status else None
    model_type_filter = ModelType(list_request.model_type) if list_request.model_type else None

    if list_request.owner is not None:
        owner_filter = list_request.owner if list_request.owner else None
    else:
        owner_filter = get_request_owner(request) if request else None

    if list_request.project_name is not None:
        project_name_filter = list_request.project_name if list_request.project_name else None
    else:
        project_name_filter = None

    if list_request.project_id is not None:
        project_id_filter = list_request.project_id if list_request.project_id else None
    else:
        project_id_filter = None

    return (
        status_filter,
        model_type_filter,
        owner_filter,
        project_id_filter,
        project_name_filter,
    )


def _parse_statuses_csv(statuses: str) -> list[JobStatus]:
    """Parse comma-separated status values."""
    return [JobStatus(s.strip()) for s in statuses.split(",")]


async def preview_cleanup(
    db: AsyncSession,
    statuses: str = "failed,cancelled",
    older_than_days: Optional[int] = None,
) -> dict:
    """Preview what would be removed by bulk cleanup."""
    from app.core.cleanup_service import get_cleanup_service

    cleanup = get_cleanup_service()
    status_list = _parse_statuses_csv(statuses)
    preview = await cleanup.preview_cleanup(db, status_list, older_than_days)
    orphans = await cleanup.find_orphans_checked(db)
    return {**preview, "orphans": orphans}


async def bulk_cleanup(
    db: AsyncSession,
    statuses: list[str],
    older_than_days: Optional[int] = None,
    include_orphans: bool = False,
) -> dict:
    """Delete artifacts and DB rows for jobs matching given criteria."""
    from app.core.cleanup_service import get_cleanup_service

    cleanup = get_cleanup_service()
    status_list = [JobStatus(s) for s in statuses]
    result = await cleanup.bulk_cleanup(db, status_list, older_than_days)

    if include_orphans:
        orphan_result = await cleanup.delete_orphans(db)
        result["orphans_cleaned"] = orphan_result

    return result


async def delete_orphans(db: AsyncSession) -> dict:
    """Delete orphaned artifacts with no matching job rows."""
    from app.core.cleanup_service import get_cleanup_service

    return await get_cleanup_service().delete_orphans(db)


async def find_orphans_checked(db: AsyncSession) -> dict:
    """Preview orphaned artifacts without deleting them."""
    from app.core.cleanup_service import get_cleanup_service

    return await get_cleanup_service().find_orphans_checked(db)


async def get_job_or_404(db: AsyncSession, job_id: str) -> Job:
    """Get job by id or raise a 404."""
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


def normalize_job_leaderboard(job: Job) -> Job:
    """Normalize legacy leaderboard payloads for API compatibility."""
    if job.leaderboard and isinstance(job.leaderboard, dict) and "models" in job.leaderboard:
        job.leaderboard = job.leaderboard["models"]
    return job


async def get_job_response(db: AsyncSession, job_id: str) -> Job:
    """Get job payload normalized for API response compatibility."""
    return normalize_job_leaderboard(await get_job_or_404(db, job_id))


def extract_metrics_leaderboard(job: Job) -> Optional[list[dict]]:
    """Extract leaderboard in list format for metrics responses."""
    if not job.leaderboard:
        return None
    if isinstance(job.leaderboard, dict):
        return job.leaderboard.get("models", [])
    if isinstance(job.leaderboard, list):
        return job.leaderboard
    return None


async def get_job_status_response(db: AsyncSession, job_id: str) -> JobStatusResponse:
    """Build status response payload for a job."""
    job = await get_job_or_404(db, job_id)
    return JobStatusResponse(
        id=job.id,
        status=job.status.value,
        error_message=job.error_message,
        started_at=job.started_at,
        completed_at=job.completed_at,
    )


async def get_job_metrics_response(db: AsyncSession, job_id: str) -> JobMetricsResponse:
    """Build metrics response payload for a job."""
    job = await get_job_or_404(db, job_id)
    return JobMetricsResponse(
        id=job.id,
        metrics=job.metrics,
        leaderboard=extract_metrics_leaderboard(job),
    )


async def get_job_progress_response(db: AsyncSession, job_id: str) -> JobProgressResponse:
    """Build progress response payload for a job."""
    job = await get_job_or_404(db, job_id)
    return JobProgressResponse(
        id=job.id,
        status=job.status.value,
        progress=job.progress if hasattr(job, "progress") and job.progress else 0,
        current_step=job.current_step if hasattr(job, "current_step") else None,
        models_trained=job.models_trained if hasattr(job, "models_trained") else 0,
        current_model=job.current_model if hasattr(job, "current_model") else None,
        eta_seconds=job.eta_seconds if hasattr(job, "eta_seconds") else None,
        started_at=job.started_at,
    )


async def cancel_job(db: AsyncSession, job_id: str) -> dict:
    """Cancel a pending/running job and queue task."""
    job = await get_job_or_404(db, job_id)

    if job.status not in [JobStatus.PENDING, JobStatus.RUNNING]:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot cancel job with status: {job.status.value}",
        )

    if getattr(job, "execution_target", "local") == "domino_job":
        stop_success = False
        stop_error = None
        if job.domino_job_id:
            from app.core.domino_job_launcher import get_domino_job_launcher

            stop_result = get_domino_job_launcher().stop_job(job.domino_job_id)
            stop_success = bool(stop_result.get("success"))
            stop_error = stop_result.get("error")
            await crud.update_job_domino_fields(
                db=db,
                job_id=job_id,
                domino_job_status="Cancelled" if stop_success else "CancelFailed",
            )
        await crud.update_job_status(
            db,
            job_id,
            JobStatus.CANCELLED,
            completed_at=datetime.utcnow(),
            error_message=stop_error if stop_error and not stop_success else None,
        )
        return {
            "message": "Job cancelled",
            "job_id": job_id,
            "external_cancelled": stop_success,
            "external_error": stop_error,
        }

    from app.core.job_queue import get_job_queue

    task_cancelled = await get_job_queue().cancel(job_id)
    await crud.update_job_status(
        db,
        job_id,
        JobStatus.CANCELLED,
        completed_at=datetime.utcnow(),
    )
    return {"message": "Job cancelled", "job_id": job_id, "task_cancelled": task_cancelled}


async def delete_job(db: AsyncSession, job_id: str) -> dict:
    """Delete job artifacts and DB row."""
    from app.core.cleanup_service import get_cleanup_service

    job = await get_job_or_404(db, job_id)
    cleanup_result = await get_cleanup_service().delete_job_artifacts(job, db)
    await crud.delete_job(db, job_id)
    return {"message": "Job deleted", "job_id": job_id, "cleanup": cleanup_result}


async def register_model_for_job(
    db: AsyncSession,
    job_id: str,
    request: RegisterModelRequest,
) -> RegisterModelResponse:
    """Register a completed job's trained model in Domino registry."""
    job = await get_job_or_404(db, job_id)
    if job.status != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot register model from job with status: {job.status.value}",
        )

    try:
        prefixed_model_name = request.model_name
        if not prefixed_model_name.startswith("automlapp-"):
            prefixed_model_name = f"automlapp-{prefixed_model_name}"

        result = await register_trained_model(
            job_id=job_id,
            model_name=prefixed_model_name,
            description=request.description,
            stage=request.stage,
        )
        return RegisterModelResponse(
            success=True,
            model_name=result.get("model_name"),
            version=result.get("version"),
            run_id=result.get("run_id"),
            artifact_uri=result.get("artifact_uri"),
            stage=result.get("stage"),
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to register model: {exc}") from exc
