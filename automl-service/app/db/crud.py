"""Database CRUD operations."""

from datetime import datetime
from typing import Optional, Sequence

from sqlalchemy import select, update, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Job, JobLog, JobStatus, ModelType, RegisteredModel


# Job CRUD operations

async def create_job(db: AsyncSession, job: Job) -> Job:
    """Create a new job."""
    db.add(job)
    await db.commit()
    await db.refresh(job)
    return job


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
) -> Optional[Job]:
    """Update job with training results."""
    update_data = {
        "metrics": metrics,
        "leaderboard": leaderboard,
        "model_path": model_path,
        "status": JobStatus.COMPLETED,
        "completed_at": datetime.utcnow(),
        "progress": 100,
        "current_step": "Complete",
    }

    if experiment_run_id:
        update_data["experiment_run_id"] = experiment_run_id

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
) -> Sequence[RegisteredModel]:
    """Get all registered models."""
    result = await db.execute(
        select(RegisteredModel).order_by(desc(RegisteredModel.created_at))
    )
    return result.scalars().all()
