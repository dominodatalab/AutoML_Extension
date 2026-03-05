"""Compat adapters for job-related /svc* routes.

Only contains adapters with actual logic beyond arg-reordering.
Simple pass-throughs (get_job, cancel_job, delete_job, get_job_status,
get_job_metrics, get_job_progress) are routed directly to service functions
via db_first=True in patterns.py.
"""

from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.job import CleanupRequest, JobLogResponse
from app.services.job_service import (
    bulk_cleanup as bulk_cleanup_service,
    get_job_logs as get_job_logs_service,
    get_queue_status as get_queue_status_service,
)


async def get_queue_status():
    """Return current queue status."""
    return get_queue_status_service()


async def bulk_cleanup(request: CleanupRequest, db: AsyncSession, *, project_id: Optional[str] = None):
    """Bulk cleanup adapter for compat pattern routes."""
    return await bulk_cleanup_service(
        db=db,
        statuses=request.statuses,
        older_than_days=request.older_than_days,
        include_orphans=request.include_orphans,
        project_id=project_id,
    )


async def get_job_logs(job_id: str, limit: int = 100, db: AsyncSession = None):
    """Get job logs adapter."""
    logs = await get_job_logs_service(db=db, job_id=job_id, limit=limit)
    return [JobLogResponse.model_validate(log) for log in logs]
