"""Database CRUD operations."""

from datetime import datetime, timedelta
from typing import Optional, Sequence

from sqlalchemy import select, update, desc, delete, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.utils import utc_now

from app.db.models import (
    Job,
    JobLog,
    JobStatus,
    ModelType,
    RegisteredModel,
)


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
    execution_target: Optional[str] = None,
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
        summary_only: Load only list-view columns (skip large blobs)
        execution_target: Filter by job execution target. If none, fetches all
    """
    query = select(Job).order_by(desc(Job.created_at))
    if summary_only:
        from sqlalchemy.orm import load_only
        query = query.options(
            load_only(
                Job.id, Job.name, Job.description, Job.owner,
                Job.project_id, Job.project_name, Job.model_type,
                Job.problem_type, Job.status, Job.execution_target,
                Job.domino_job_id, Job.domino_job_status, Job.progress,
                Job.current_step, Job.data_source, Job.dataset_id,
                Job.file_path, Job.metrics, Job.experiment_name,
                Job.error_message, Job.is_registered,
                Job.registered_model_name, Job.registered_model_version,
                Job.created_at, Job.started_at, Job.completed_at,
            )
        )

    if execution_target:
        query = query.where(Job.execution_target == execution_target)

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
    return await get_job(db, job_id)


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
    return await get_job(db, job_id)


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
    return await get_job(db, job_id)


async def update_job_results(
    db: AsyncSession,
    job_id: str,
    metrics: dict,
    leaderboard: dict,
    model_path: str,
    experiment_run_id: Optional[str] = None,
    experiment_name: Optional[str] = None,
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

    await db.execute(
        update(Job).where(Job.id == job_id).values(**update_data)
    )
    await db.commit()
    return await get_job(db, job_id)


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
    owner: Optional[str] = None,
) -> Sequence[RegisteredModel]:
    """Get all registered models, optionally filtered by project/owner via job FK."""
    query = select(RegisteredModel)
    if project_id or owner:
        query = query.join(Job, RegisteredModel.job_id == Job.id)
        if project_id:
            query = query.where(Job.project_id == project_id)
        if owner:
            query = query.where(Job.owner == owner)
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
    owner: Optional[str] = None,
) -> Sequence[Job]:
    """Get jobs matching statuses and optional age filter, ordered by created_at."""
    query = select(Job).where(Job.status.in_(statuses))
    if older_than_days is not None:
        cutoff = utc_now() - timedelta(days=older_than_days)
        query = query.where(Job.created_at < cutoff)
    if project_id:
        query = query.where(Job.project_id == project_id)
    if owner:
        query = query.where(Job.owner == owner)
    return (await db.execute(query.order_by(Job.created_at))).scalars().all()


async def count_job_logs(db: AsyncSession, job_id: str) -> int:
    """Count log entries for a job."""
    result = await db.execute(
        select(func.count()).select_from(JobLog).where(JobLog.job_id == job_id)
    )
    return result.scalar()
