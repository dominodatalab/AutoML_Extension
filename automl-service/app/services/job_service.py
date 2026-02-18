"""Service helpers for job route orchestration."""

import asyncio
import os
import logging
from datetime import datetime
from typing import Optional

from fastapi import HTTPException, Request
from sqlalchemy.exc import IntegrityError
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
from app.core.dataset_mounts import resolve_dataset_mount_paths
from app.db.models import Job, JobStatus, ModelType, ProblemType
from app.db import crud
from app.workers.training_worker import register_trained_model

logger = logging.getLogger(__name__)

_TERMINAL_JOB_STATUSES = {JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED}
_DOMINO_PENDING_STATUSES = {"submitted", "queued", "pending", "initializing", "provisioning"}
_DOMINO_RUNNING_STATUSES = {"running", "executing"}
_DOMINO_COMPLETED_STATUSES = {"succeeded", "success", "successful", "completed", "complete", "done", "finished"}
_DOMINO_FAILED_STATUSES = {"failed", "error"}
_DOMINO_CANCELLED_STATUSES = {"stopped", "cancelled", "canceled", "archived"}
_DOMINO_TERMINAL_METADATA_SCAN_LIMIT = 100
_DOMINO_TERMINAL_METADATA_SYNC_LIMIT = 20
_DOMINO_MISSING_JOB_MESSAGE = "External Domino job is no longer accessible (archived or deleted)."
_MISSING_DATA_MESSAGE = "Training data is no longer available for this job (dataset/file was deleted)."
_DOMINO_MISSING_ERROR_MARKERS = (
    "404",
    "not found",
    "does not exist",
    "unknown run",
    "no run",
    "archiv",
)


def _normalize_job_name(name: str) -> str:
    """Return canonical job name used for validation and persistence."""
    return name.strip()


def _job_name_conflict_detail(name: str) -> str:
    """Build a consistent duplicate-name error message."""
    return (
        f"A job named '{name}' already exists in this project for this user. "
        "Please choose a different name."
    )


def _is_job_name_unique_violation(exc: IntegrityError) -> bool:
    """Return True when the DB rejects duplicate scoped job names."""
    error_text = str(getattr(exc, "orig", exc)).lower()
    return (
        "uq_jobs_owner_project_name_ci" in error_text
        or ("unique constraint" in error_text and "jobs" in error_text and "name" in error_text)
    )


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


async def validate_job_name_availability(
    db: AsyncSession,
    name: str,
    owner: Optional[str],
    project_id: Optional[str],
    project_name: Optional[str],
) -> str:
    """Ensure job name is non-empty and unique within owner+project scope."""
    normalized_name = _normalize_job_name(name)
    if not normalized_name:
        raise HTTPException(status_code=400, detail="name must not be blank")

    existing_job = await crud.get_job_by_scoped_name(
        db=db,
        name=normalized_name,
        owner=owner,
        project_id=project_id,
        project_name=project_name,
    )
    if existing_job:
        raise HTTPException(status_code=409, detail=_job_name_conflict_detail(normalized_name))

    return normalized_name


def build_autogluon_config(job_request: JobCreateRequest) -> Optional[dict]:
    """Build persisted AutoGluon config blob from request sections."""
    autogluon_config: dict = {}
    if job_request.advanced_config:
        autogluon_config["advanced"] = job_request.advanced_config.model_dump(exclude_none=True)
    if job_request.timeseries_config:
        autogluon_config["timeseries"] = job_request.timeseries_config.model_dump(exclude_none=True)
    if job_request.feature_columns:
        autogluon_config["feature_columns"] = job_request.feature_columns
    return autogluon_config or None


def build_job_model(
    job_request: JobCreateRequest,
    job_name: str,
    owner: str,
    project_id: Optional[str],
    project_name: Optional[str],
) -> Job:
    """Build a Job ORM model from request and resolved context."""
    execution_target = resolve_execution_target(job_request)

    return Job(
        name=job_name,
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
    normalized_job_name = await validate_job_name_availability(
        db=db,
        name=job_request.name,
        owner=owner,
        project_id=project_id,
        project_name=project_name,
    )
    job = build_job_model(
        job_request=job_request,
        job_name=normalized_job_name,
        owner=owner,
        project_id=project_id,
        project_name=project_name,
    )
    try:
        job = await crud.create_job(db, job)
    except IntegrityError as exc:
        if _is_job_name_unique_violation(exc):
            raise HTTPException(
                status_code=409,
                detail=_job_name_conflict_detail(normalized_job_name),
            ) from exc
        raise

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
    await _sync_active_domino_jobs_for_overview(db)
    status_filter = JobStatus(status) if status else None
    jobs = await crud.get_jobs(db, skip=skip, limit=limit, status=status_filter)
    return list(jobs)


async def list_jobs_filtered(
    db: AsyncSession,
    list_request: JobListRequest,
    request: Optional[Request] = None,
) -> list[Job]:
    """List jobs using advanced POST filters."""
    await _sync_active_domino_jobs_for_overview(db)
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


async def _sync_active_domino_jobs_for_overview(db: AsyncSession) -> None:
    """Refresh active Domino-backed jobs so list views show current status."""
    active_jobs = await crud.get_jobs_by_statuses(
        db,
        [JobStatus.PENDING, JobStatus.RUNNING],
        execution_target="domino_job",
    )
    if active_jobs:
        for job in active_jobs:
            if not job.domino_job_id:
                continue
            await _sync_domino_job_state(db, job)

    await _sync_recent_terminal_domino_metadata_for_overview(db)


async def _sync_recent_terminal_domino_metadata_for_overview(db: AsyncSession) -> None:
    """Refresh stale Domino terminal metadata for recently listed jobs."""
    recent_jobs = await crud.get_jobs(db, skip=0, limit=_DOMINO_TERMINAL_METADATA_SCAN_LIMIT)
    if not recent_jobs:
        return

    candidates: list[Job] = []
    for job in recent_jobs:
        if getattr(job, "execution_target", "local") != "domino_job":
            continue
        if job.status not in _TERMINAL_JOB_STATUSES:
            continue
        if not job.domino_job_id:
            continue
        if _is_domino_terminal_status(job.domino_job_status):
            continue
        candidates.append(job)
        if len(candidates) >= _DOMINO_TERMINAL_METADATA_SYNC_LIMIT:
            break

    for job in candidates:
        await _sync_domino_job_state(db, job, sync_terminal_metadata=True)


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

    await reconcile_jobs_for_storage_cleanup(db)
    return await get_cleanup_service().delete_orphans(db)


async def find_orphans_checked(db: AsyncSession) -> dict:
    """Preview orphaned artifacts without deleting them."""
    from app.core.cleanup_service import get_cleanup_service

    await reconcile_jobs_for_storage_cleanup(db)
    return await get_cleanup_service().find_orphans_checked(db)


async def get_job_or_404(db: AsyncSession, job_id: str) -> Job:
    """Get job by id or raise a 404."""
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


def _normalize_domino_status(status: Optional[str]) -> str:
    """Normalize external Domino status for matching."""
    return (status or "").strip().lower()


def _terminal_status_from_domino(status: Optional[str]) -> Optional[JobStatus]:
    """Map Domino terminal statuses to local JobStatus values."""
    normalized = _normalize_domino_status(status)
    if normalized in _DOMINO_COMPLETED_STATUSES:
        return JobStatus.COMPLETED
    if normalized in _DOMINO_FAILED_STATUSES:
        return JobStatus.FAILED
    if normalized in _DOMINO_CANCELLED_STATUSES:
        return JobStatus.CANCELLED
    return None


def _is_domino_terminal_status(status: Optional[str]) -> bool:
    """Return True if Domino status is already terminal."""
    normalized = _normalize_domino_status(status)
    return (
        normalized in _DOMINO_COMPLETED_STATUSES
        or normalized in _DOMINO_FAILED_STATUSES
        or normalized in _DOMINO_CANCELLED_STATUSES
    )


def _is_domino_missing_error(error: Optional[str]) -> bool:
    """Return True when Domino reports a run as missing/archived."""
    normalized = (error or "").strip().lower()
    if not normalized:
        return False
    return any(marker in normalized for marker in _DOMINO_MISSING_ERROR_MARKERS)


def _first_dataset_file(path: str) -> Optional[str]:
    """Return first supported dataset file under a directory."""
    for root, _, files in os.walk(path):
        for file_name in files:
            if file_name.endswith((".csv", ".parquet", ".pq")):
                return os.path.join(root, file_name)
    return None


async def _resolve_job_data_path(job: Job) -> Optional[str]:
    """Resolve a job's current data path for stale-reference checks."""
    if job.data_source == "upload":
        return job.file_path

    if job.data_source != "domino_dataset" or not job.dataset_id:
        return None

    # Storage cleanup reconciliation only validates mounted dataset refs
    # (domino:<name>) to avoid false failures from transient API issues.
    if not job.dataset_id.startswith("domino:"):
        return None

    dataset_name = job.dataset_id.replace("domino:", "", 1)
    mount_paths = resolve_dataset_mount_paths(fallback_path=get_settings().datasets_path)
    for mount_path in mount_paths:
        dataset_path = os.path.join(mount_path, dataset_name)
        if os.path.isfile(dataset_path):
            return dataset_path
        if os.path.isdir(dataset_path):
            first_file = _first_dataset_file(dataset_path)
            if first_file:
                return first_file
    return None


async def _mark_pending_job_failed_for_missing_data(
    db: AsyncSession,
    job: Job,
) -> Optional[Job]:
    """Fail pending jobs when their referenced source data was deleted."""
    if job.status != JobStatus.PENDING:
        return None
    if job.data_source not in {"upload", "domino_dataset"}:
        return None
    if (
        job.data_source == "domino_dataset"
        and job.dataset_id
        and not job.dataset_id.startswith("domino:")
    ):
        return None

    data_path = await _resolve_job_data_path(job)
    if data_path and os.path.exists(data_path):
        return None

    error_message = job.error_message or _MISSING_DATA_MESSAGE
    updated = await crud.update_job_status(
        db=db,
        job_id=job.id,
        status=JobStatus.FAILED,
        error_message=error_message,
        completed_at=datetime.utcnow(),
    )
    try:
        await crud.add_job_log(db, job.id, error_message, "ERROR")
    except Exception:
        logger.exception("Failed to write missing-data sync log for job %s", job.id)
    return updated or job


async def _sync_domino_job_state(
    db: AsyncSession,
    job: Job,
    finalize_missing: bool = False,
    sync_terminal_metadata: bool = False,
) -> Job:
    """Sync local status for externally executed Domino jobs.

    This keeps UI state accurate when external runs fail before they can
    update our local database (for example, import/runtime bootstrap errors).
    """
    if getattr(job, "execution_target", "local") != "domino_job":
        return job
    if not job.domino_job_id:
        return job

    is_terminal_local = job.status in _TERMINAL_JOB_STATUSES
    if is_terminal_local and not sync_terminal_metadata:
        return job
    if is_terminal_local and sync_terminal_metadata and _is_domino_terminal_status(job.domino_job_status):
        return job

    try:
        from app.core.domino_job_launcher import get_domino_job_launcher

        status_result = await asyncio.wait_for(
            asyncio.to_thread(get_domino_job_launcher().get_job_status, job.domino_job_id),
            timeout=8.0,
        )
    except asyncio.TimeoutError:
        logger.warning(
            "Timed out polling Domino status for job %s (domino id %s)",
            job.id,
            job.domino_job_id,
        )
        return job
    except Exception:
        logger.exception("Failed to poll Domino status for job %s", job.id)
        return job

    if not status_result.get("success"):
        error = status_result.get("error")
        if error:
            logger.warning(
                "Domino status poll failed for job %s (domino id %s): %s",
                job.id,
                job.domino_job_id,
                error,
            )
        if (finalize_missing or sync_terminal_metadata) and _is_domino_missing_error(error):
            await crud.update_job_domino_fields(
                db=db,
                job_id=job.id,
                domino_job_status="ArchivedOrMissing",
            )
            job.domino_job_status = "ArchivedOrMissing"
        if finalize_missing and _is_domino_missing_error(error):
            error_message = job.error_message or _DOMINO_MISSING_JOB_MESSAGE
            updated = await crud.update_job_status(
                db=db,
                job_id=job.id,
                status=JobStatus.CANCELLED,
                error_message=error_message,
                completed_at=datetime.utcnow(),
            )
            try:
                await crud.add_job_log(
                    db,
                    job.id,
                    f"{_DOMINO_MISSING_JOB_MESSAGE} Domino API error: {error}",
                    "WARNING",
                )
            except Exception:
                logger.exception("Failed to write missing-job sync log for job %s", job.id)
            return updated or job
        return job

    latest_domino_status = status_result.get("domino_job_status")
    normalized = _normalize_domino_status(latest_domino_status)

    if latest_domino_status and latest_domino_status != job.domino_job_status:
        await crud.update_job_domino_fields(
            db=db,
            job_id=job.id,
            domino_job_status=latest_domino_status,
        )
        job.domino_job_status = latest_domino_status

    # If local status is already terminal, this pass is metadata-only.
    if is_terminal_local and sync_terminal_metadata:
        return job

    # Promote pending -> running based on external execution signal.
    if normalized in _DOMINO_RUNNING_STATUSES and job.status == JobStatus.PENDING:
        updated = await crud.update_job_status(
            db=db,
            job_id=job.id,
            status=JobStatus.RUNNING,
            started_at=job.started_at or datetime.utcnow(),
        )
        return updated or job

    # Keep pending state for queued/submitted external jobs.
    if normalized in _DOMINO_PENDING_STATUSES:
        return job

    terminal_status = _terminal_status_from_domino(latest_domino_status)
    if not terminal_status:
        if normalized:
            logger.warning(
                "Unrecognized Domino terminal status '%s' for job %s (domino id %s)",
                latest_domino_status,
                job.id,
                job.domino_job_id,
            )
        return job

    if terminal_status == JobStatus.COMPLETED:
        updated = await crud.update_job_status(
            db=db,
            job_id=job.id,
            status=JobStatus.COMPLETED,
            completed_at=job.completed_at or datetime.utcnow(),
        )
        return updated or job

    if terminal_status == JobStatus.FAILED:
        error_message = job.error_message or (
            f"External Domino job ended with status: {latest_domino_status}. "
            "Check Domino run logs for details."
        )
        updated = await crud.update_job_status(
            db=db,
            job_id=job.id,
            status=JobStatus.FAILED,
            error_message=error_message,
            completed_at=datetime.utcnow(),
        )
        try:
            await crud.add_job_log(
                db,
                job.id,
                f"External Domino job ended with status: {latest_domino_status}",
                "ERROR",
            )
        except Exception:
            logger.exception("Failed to write terminal sync log for job %s", job.id)
        return updated or job

    updated = await crud.update_job_status(
        db=db,
        job_id=job.id,
        status=JobStatus.CANCELLED,
        completed_at=datetime.utcnow(),
    )
    try:
        await crud.add_job_log(
            db,
            job.id,
            f"External Domino job ended with status: {latest_domino_status}",
            "WARNING",
        )
    except Exception:
        logger.exception("Failed to write terminal sync log for job %s", job.id)
    return updated or job


async def reconcile_jobs_for_storage_cleanup(db: AsyncSession) -> dict:
    """Reconcile stale job rows before orphan preview/cleanup actions."""
    active_jobs = await crud.get_jobs_by_statuses(
        db,
        [JobStatus.PENDING, JobStatus.RUNNING],
    )
    if not active_jobs:
        return {
            "active_jobs_checked": 0,
            "domino_jobs_checked": 0,
            "missing_domino_jobs_finalized": 0,
            "missing_data_jobs_finalized": 0,
        }

    active_jobs_checked = 0
    domino_jobs_checked = 0
    missing_domino_jobs_finalized = 0
    missing_data_jobs_finalized = 0

    for job in active_jobs:
        active_jobs_checked += 1
        if getattr(job, "execution_target", "local") == "domino_job":
            domino_jobs_checked += 1
            previous_status = job.status
            previous_error = job.error_message
            job = await _sync_domino_job_state(db, job, finalize_missing=True)
            if (
                previous_status != JobStatus.CANCELLED
                and job.status == JobStatus.CANCELLED
                and (job.error_message or previous_error or "") == _DOMINO_MISSING_JOB_MESSAGE
            ):
                missing_domino_jobs_finalized += 1

        if job.status == JobStatus.PENDING and job.data_source in {"upload", "domino_dataset"}:
            updated_job = await _mark_pending_job_failed_for_missing_data(
                db,
                job,
            )
            if updated_job is not None:
                missing_data_jobs_finalized += 1

    logger.info(
        "Storage cleanup reconciliation complete: checked=%s domino_checked=%s "
        "missing_domino_finalized=%s missing_data_finalized=%s",
        active_jobs_checked,
        domino_jobs_checked,
        missing_domino_jobs_finalized,
        missing_data_jobs_finalized,
    )
    return {
        "active_jobs_checked": active_jobs_checked,
        "domino_jobs_checked": domino_jobs_checked,
        "missing_domino_jobs_finalized": missing_domino_jobs_finalized,
        "missing_data_jobs_finalized": missing_data_jobs_finalized,
    }


def normalize_job_leaderboard(job: Job) -> Job:
    """Normalize legacy leaderboard payloads for API compatibility."""
    if job.leaderboard and isinstance(job.leaderboard, dict) and "models" in job.leaderboard:
        job.leaderboard = job.leaderboard["models"]
    return job


async def get_job_response(db: AsyncSession, job_id: str) -> Job:
    """Get job payload normalized for API response compatibility."""
    job = await get_job_or_404(db, job_id)
    job = await _sync_domino_job_state(db, job, sync_terminal_metadata=True)
    return normalize_job_leaderboard(job)


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
    job = await _sync_domino_job_state(db, job, sync_terminal_metadata=True)
    return JobStatusResponse(
        id=job.id,
        status=job.status.value,
        domino_job_status=job.domino_job_status,
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
    job = await _sync_domino_job_state(db, job, sync_terminal_metadata=True)
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
