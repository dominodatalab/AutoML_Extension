"""Database CRUD operations."""

import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import Optional, Sequence

from sqlalchemy import select, update, desc, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import load_only

from app.core.utils import utc_now
from app.core.websocket_manager import get_websocket_manager

from app.db.models import (
    EDAResult,
    Job,
    JobLog,
    JobStatus,
    ModelType,
    RegisteredModel,
)

logger = logging.getLogger(__name__)


def _job_update_payload(job: Job, event_type: str = "job_update") -> dict:
    """Serialize the current job state for websocket subscribers."""
    status = job.status.value if hasattr(job.status, "value") else str(job.status)
    payload = {
        "type": event_type,
        "job_id": job.id,
        "status": status,
        "progress": int(getattr(job, "progress", 0) or 0),
        "current_step": getattr(job, "current_step", None),
        "models_trained": int(getattr(job, "models_trained", 0) or 0),
        "current_model": getattr(job, "current_model", None),
        "eta_seconds": getattr(job, "eta_seconds", None),
        "domino_job_status": getattr(job, "domino_job_status", None),
        "started_at": job.started_at.isoformat() if getattr(job, "started_at", None) else None,
        "completed_at": job.completed_at.isoformat() if getattr(job, "completed_at", None) else None,
    }
    return payload


def _schedule_job_broadcast(job: Optional[Job], event_type: str = "job_update") -> None:
    """Fire-and-forget websocket broadcast for a job update."""
    if job is None:
        return

    async def _broadcast() -> None:
        await get_websocket_manager().send_progress(job.id, _job_update_payload(job, event_type=event_type))

    task = asyncio.create_task(_broadcast())
    task.add_done_callback(_log_broadcast_error)


def _schedule_job_log_broadcast(log: JobLog) -> None:
    """Broadcast a newly written log line to job subscribers."""
    async def _broadcast() -> None:
        await get_websocket_manager().send_progress(
            log.job_id,
            {
                "type": "job_log",
                "job_id": log.job_id,
                "log": {
                    "id": log.id,
                    "job_id": log.job_id,
                    "level": log.level,
                    "message": log.message,
                    "timestamp": log.timestamp.isoformat() if log.timestamp else None,
                },
            },
        )

    task = asyncio.create_task(_broadcast())
    task.add_done_callback(_log_broadcast_error)


def _log_broadcast_error(task: asyncio.Task) -> None:
    """Log background websocket errors without surfacing them to callers."""
    try:
        task.result()
    except Exception:
        logger.exception("Background websocket broadcast failed")


# Job CRUD operations

async def create_job(db: AsyncSession, job: Job) -> Job:
    """Create a new job."""
    db.add(job)
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
    await db.refresh(job)
    return job


async def get_job_by_scoped_name(
    db: AsyncSession,
    name: str,
    owner: Optional[str] = None,
    project_id: Optional[str] = None,
    project_name: Optional[str] = None,
) -> Optional[Job]:
    """Get a job by normalized name within owner+project scope."""
    normalized_name = name.strip().lower()
    owner_scope = owner.strip() if owner else ""
    project_scope = (project_id or project_name or "").strip()

    query = (
        select(Job)
        .where(
            func.lower(func.trim(Job.name)) == normalized_name,
            func.coalesce(Job.owner, "") == owner_scope,
            func.coalesce(Job.project_id, Job.project_name, "") == project_scope,
        )
        .order_by(desc(Job.created_at))
        .limit(1)
    )
    result = await db.execute(query)
    return result.scalars().first()


async def get_job(db: AsyncSession, job_id: str) -> Optional[Job]:
    """Get a job by ID."""
    result = await db.execute(select(Job).where(Job.id == job_id))
    return result.scalar_one_or_none()


async def get_jobs(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 100,
    status: Optional[JobStatus] = None,
    model_type: Optional[ModelType] = None,
    owner: Optional[str] = None,
    project_id: Optional[str] = None,
    project_name: Optional[str] = None,
    summary_only: bool = False,
) -> Sequence[Job]:
    """Get all jobs with optional filtering.

    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum records to return
        status: Filter by job status
        model_type: Filter by model type
        owner: Filter by owner username (from Domino header)
        project_id: Filter by project ID (from Domino environment)
        project_name: Filter by project name (from Domino environment)
    """
    query = select(Job).order_by(desc(Job.created_at))
    if summary_only:
        query = query.options(
            load_only(
                Job.id,
                Job.name,
                Job.description,
                Job.owner,
                Job.project_id,
                Job.project_name,
                Job.model_type,
                Job.problem_type,
                Job.status,
                Job.execution_target,
                Job.domino_job_id,
                Job.domino_job_status,
                Job.progress,
                Job.current_step,
                Job.data_source,
                Job.dataset_id,
                Job.file_path,
                Job.metrics,
                Job.experiment_name,
                Job.error_message,
                Job.is_registered,
                Job.registered_model_name,
                Job.registered_model_version,
                Job.created_at,
                Job.started_at,
                Job.completed_at,
            )
        )

    if status:
        query = query.where(Job.status == status)

    if model_type:
        query = query.where(Job.model_type == model_type)

    # Filter by owner (user) if provided
    if owner:
        query = query.where(Job.owner == owner)

    # Filter by project_id if provided
    if project_id:
        query = query.where(Job.project_id == project_id)

    # Filter by project_name if provided
    if project_name:
        query = query.where(Job.project_name == project_name)

    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


async def get_jobs_by_statuses(
    db: AsyncSession,
    statuses: list[JobStatus],
    execution_target: Optional[str] = None,
) -> Sequence[Job]:
    """Get jobs matching any of the given statuses, ordered by created_at (FIFO)."""
    query = select(Job).where(Job.status.in_(statuses))
    if execution_target is not None:
        query = query.where(Job.execution_target == execution_target)
    query = query.order_by(Job.created_at)
    result = await db.execute(query)
    return result.scalars().all()


async def update_job_domino_fields(
    db: AsyncSession,
    job_id: str,
    domino_job_id: Optional[str] = None,
    domino_job_status: Optional[str] = None,
) -> Optional[Job]:
    """Update Domino execution metadata for a job."""
    update_data: dict[str, Optional[str]] = {}
    if domino_job_id is not None:
        update_data["domino_job_id"] = domino_job_id
    if domino_job_status is not None:
        update_data["domino_job_status"] = domino_job_status

    if not update_data:
        return await get_job(db, job_id)

    await db.execute(update(Job).where(Job.id == job_id).values(**update_data))
    await db.commit()
    job = await get_job(db, job_id)
    _schedule_job_broadcast(job, event_type="job_update")
    return job


async def update_job_status(
    db: AsyncSession,
    job_id: str,
    status: JobStatus,
    error_message: Optional[str] = None,
    started_at: Optional[datetime] = None,
    completed_at: Optional[datetime] = None,
) -> Optional[Job]:
    """Update job status."""
    update_data = {"status": status}

    if error_message is not None:
        update_data["error_message"] = error_message
    if started_at is not None:
        update_data["started_at"] = started_at
    if completed_at is not None:
        update_data["completed_at"] = completed_at

    await db.execute(
        update(Job).where(Job.id == job_id).values(**update_data)
    )
    await db.commit()
    job = await get_job(db, job_id)
    _schedule_job_broadcast(job, event_type="job_update")
    return job


async def update_job_progress(
    db: AsyncSession,
    job_id: str,
    progress: int,
    current_step: Optional[str] = None,
    models_trained: Optional[int] = None,
    current_model: Optional[str] = None,
    eta_seconds: Optional[int] = None,
) -> Optional[Job]:
    """Update job progress during training."""
    update_data = {"progress": progress}

    if current_step is not None:
        update_data["current_step"] = current_step
    if models_trained is not None:
        update_data["models_trained"] = models_trained
    if current_model is not None:
        update_data["current_model"] = current_model
    if eta_seconds is not None:
        update_data["eta_seconds"] = eta_seconds

    await db.execute(
        update(Job).where(Job.id == job_id).values(**update_data)
    )
    await db.commit()
    job = await get_job(db, job_id)
    _schedule_job_broadcast(job, event_type="job_update")
    return job


async def update_job_results(
    db: AsyncSession,
    job_id: str,
    metrics: dict,
    leaderboard: dict,
    model_path: str,
    experiment_run_id: Optional[str] = None,
    experiment_name: Optional[str] = None,
    diagnostics_data: Optional[dict] = None,
) -> Optional[Job]:
    """Update job with training results."""
    update_data = {
        "metrics": metrics,
        "leaderboard": leaderboard,
        "model_path": model_path,
        "status": JobStatus.COMPLETED,
        "completed_at": utc_now(),
        "progress": 100,
        "current_step": "Complete",
    }

    if experiment_run_id:
        update_data["experiment_run_id"] = experiment_run_id

    if experiment_name:
        update_data["experiment_name"] = experiment_name

    if diagnostics_data is not None:
        update_data["diagnostics_data"] = diagnostics_data

    await db.execute(
        update(Job).where(Job.id == job_id).values(**update_data)
    )
    await db.commit()
    job = await get_job(db, job_id)
    _schedule_job_broadcast(job, event_type="job_update")
    return job


async def delete_job(db: AsyncSession, job_id: str) -> bool:
    """Delete a job."""
    job = await get_job(db, job_id)
    if job:
        await db.delete(job)
        await db.commit()
        return True
    return False


# Job Log operations

async def add_job_log(
    db: AsyncSession,
    job_id: str,
    message: str,
    level: str = "INFO",
) -> JobLog:
    """Add a log entry for a job."""
    log = JobLog(job_id=job_id, message=message, level=level)
    db.add(log)
    await db.commit()
    await db.refresh(log)
    _schedule_job_log_broadcast(log)
    return log


async def get_job_logs(
    db: AsyncSession,
    job_id: str,
    limit: int = 1000,
) -> Sequence[JobLog]:
    """Get logs for a job."""
    result = await db.execute(
        select(JobLog)
        .where(JobLog.job_id == job_id)
        .order_by(JobLog.timestamp)
        .limit(limit)
    )
    return result.scalars().all()


# Registered Model operations

async def create_registered_model(
    db: AsyncSession,
    model: RegisteredModel,
) -> RegisteredModel:
    """Register a new model."""
    db.add(model)
    await db.commit()
    await db.refresh(model)
    return model


async def get_registered_model(
    db: AsyncSession,
    name: str,
) -> Optional[RegisteredModel]:
    """Get a registered model by name."""
    result = await db.execute(
        select(RegisteredModel).where(RegisteredModel.name == name)
    )
    return result.scalar_one_or_none()


async def get_registered_models(
    db: AsyncSession,
    project_id: Optional[str] = None,
) -> Sequence[RegisteredModel]:
    """Get all registered models, optionally filtered by project via job FK."""
    query = select(RegisteredModel)
    if project_id:
        query = query.join(Job, RegisteredModel.job_id == Job.id).where(
            Job.project_id == project_id
        )
    query = query.order_by(desc(RegisteredModel.created_at))
    result = await db.execute(query)
    return result.scalars().all()


# Cleanup helpers

async def delete_job_logs(db: AsyncSession, job_id: str) -> int:
    """Delete all log entries for a job. Returns number of rows deleted."""
    result = await db.execute(delete(JobLog).where(JobLog.job_id == job_id))
    await db.commit()
    return result.rowcount


async def delete_registered_models_for_job(db: AsyncSession, job_id: str) -> int:
    """Delete registered model records for a job. Returns number of rows deleted."""
    result = await db.execute(delete(RegisteredModel).where(RegisteredModel.job_id == job_id))
    await db.commit()
    return result.rowcount


async def count_jobs_with_file_path(db: AsyncSession, file_path: str) -> int:
    """Count how many jobs reference a given file_path."""
    result = await db.execute(
        select(func.count()).select_from(Job).where(Job.file_path == file_path)
    )
    return result.scalar()


async def get_jobs_for_cleanup(
    db: AsyncSession,
    statuses: list[JobStatus],
    older_than_days: Optional[int] = None,
    project_id: Optional[str] = None,
) -> Sequence[Job]:
    """Get jobs matching statuses and optional age filter, ordered by created_at."""
    query = select(Job).where(Job.status.in_(statuses))
    if older_than_days is not None:
        cutoff = utc_now() - timedelta(days=older_than_days)
        query = query.where(Job.created_at < cutoff)
    if project_id:
        query = query.where(Job.project_id == project_id)
    return (await db.execute(query.order_by(Job.created_at))).scalars().all()


async def count_job_logs(db: AsyncSession, job_id: str) -> int:
    """Count log entries for a job."""
    result = await db.execute(
        select(func.count()).select_from(JobLog).where(JobLog.job_id == job_id)
    )
    return result.scalar()


# EDA Result operations


async def create_eda_request(
    db: AsyncSession, request_id: str, mode: str, request_payload: dict
) -> EDAResult:
    """Create a new EDA request record."""
    eda = EDAResult(
        id=request_id,
        status="pending",
        mode=mode,
        request_payload=json.dumps(request_payload),
    )
    db.add(eda)
    await db.commit()
    await db.refresh(eda)
    return eda


async def get_eda_request(
    db: AsyncSession, request_id: str
) -> Optional[EDAResult]:
    """Get an EDA request by ID."""
    result = await db.execute(select(EDAResult).where(EDAResult.id == request_id))
    return result.scalar_one_or_none()


async def update_eda_request(
    db: AsyncSession, request_id: str, **updates
) -> Optional[EDAResult]:
    """Update an EDA request with arbitrary fields."""
    eda = await get_eda_request(db, request_id)
    if eda is None:
        return None
    for key, value in updates.items():
        if hasattr(eda, key) and value is not None:
            setattr(eda, key, value)
    eda.updated_at = utc_now()
    await db.commit()
    await db.refresh(eda)
    return eda


async def write_eda_result(
    db: AsyncSession, request_id: str, mode: str, result: dict
) -> Optional[EDAResult]:
    """Write EDA profiling result payload."""
    return await update_eda_request(
        db, request_id, status="completed", mode=mode,
        result_payload=json.dumps(result), error=None,
    )


async def write_eda_error(
    db: AsyncSession, request_id: str, error_message: str
) -> Optional[EDAResult]:
    """Mark an EDA request as failed with an error message."""
    return await update_eda_request(
        db, request_id, status="failed", error=error_message,
    )


async def get_eda_result(
    db: AsyncSession, request_id: str
) -> Optional[dict]:
    """Get the parsed result payload for an EDA request."""
    eda = await get_eda_request(db, request_id)
    if eda is None or eda.result_payload is None:
        return None
    return json.loads(eda.result_payload)


async def delete_stale_eda_results(
    db: AsyncSession, max_age_hours: float = 72.0
) -> int:
    """Delete EDA results older than *max_age_hours*. Returns rows deleted."""
    cutoff = utc_now() - timedelta(hours=max_age_hours)
    result = await db.execute(
        delete(EDAResult).where(EDAResult.created_at < cutoff)
    )
    await db.commit()
    return result.rowcount
