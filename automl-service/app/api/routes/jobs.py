"""Job management endpoints."""

from typing import Optional

from fastapi import APIRouter, Depends, Request

from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.api.schemas.job import (
    BulkDeleteJobsRequest,
    BulkDeleteJobsResponse,
    JobCreateRequest,
    JobListItemResponse,
    JobResponse,
    JobStatusResponse,
    JobMetricsResponse,
    JobLogResponse,
    JobListResponse,
    JobListRequest,
    JobProgressResponse,
    CleanupRequest,
    RegisterModelRequest,
    RegisterModelResponse,
)
from app.services.job_service import (
    bulk_cleanup as bulk_cleanup_service,
    bulk_delete_jobs as bulk_delete_jobs_service,
    cancel_job as cancel_job_service,
    create_job_with_context,
    delete_job as delete_job_service,
    delete_orphans as delete_orphans_service,
    get_job_metrics_response,
    get_job_logs as get_job_logs_service,
    get_job_progress_response,
    get_job_response,
    get_job_status_response,
    get_queue_status as get_queue_status_service,
    build_job_list_item_response,
    list_jobs_basic,
    list_jobs_filtered,
    preview_cleanup as preview_cleanup_service,
    register_model_for_job,
)

router = APIRouter()


@router.post("", response_model=JobResponse)
async def create_job(
    job_request: JobCreateRequest,
    db: AsyncSession = Depends(get_db),
    request: Request = None,
):
    """Create a new training job.

    The job is automatically associated with the current user (from domino-username header)
    and project (from DOMINO_PROJECT_ID environment variable).
    """
    return await create_job_with_context(db=db, job_request=job_request, request=request)


@router.get("", response_model=JobListResponse)
async def list_jobs(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    request: Request = None,
):
    """List all training jobs."""
    jobs = await list_jobs_basic(db=db, skip=skip, limit=limit, status=status, request=request)

    return JobListResponse(
        jobs=[JobListItemResponse.model_validate(build_job_list_item_response(j)) for j in jobs],
        total=len(jobs),
        skip=skip,
        limit=limit,
    )


@router.get("/queue/status")
async def get_queue_status():
    """Get current job queue status."""
    return get_queue_status_service()


@router.get("/cleanup/preview")
async def preview_cleanup(
    statuses: str = "failed,cancelled",
    older_than_days: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
    request: Request = None,
):
    """Preview what would be deleted by a bulk cleanup."""
    from app.services.job_service import get_request_owner
    return await preview_cleanup_service(
        db=db,
        statuses=statuses,
        older_than_days=older_than_days,
        owner=get_request_owner(request) if request else None,
        project_id=request.headers.get("X-Project-Id") if request else None,
    )


@router.post("/cleanup")
async def bulk_cleanup(
    cleanup_request: CleanupRequest,
    db: AsyncSession = Depends(get_db),
    http_request: Request = None,
):
    """Delete artifacts and DB rows for jobs matching the given criteria."""
    from app.services.job_service import get_request_owner
    return await bulk_cleanup_service(
        db=db,
        statuses=cleanup_request.statuses,
        older_than_days=cleanup_request.older_than_days,
        include_orphans=cleanup_request.include_orphans,
        owner=get_request_owner(http_request) if http_request else None,
        project_id=http_request.headers.get("X-Project-Id") if http_request else None,
    )


@router.post("/cleanup/orphans")
async def delete_orphans(db: AsyncSession = Depends(get_db), request: Request = None):
    """Delete orphaned model dirs and upload files with no matching job."""
    return await delete_orphans_service(
        db,
        project_id=request.headers.get("X-Project-Id") if request else None,
    )


@router.post("/bulk-delete", response_model=BulkDeleteJobsResponse)
async def bulk_delete_jobs(
    request: BulkDeleteJobsRequest,
    db: AsyncSession = Depends(get_db),
):
    """Delete multiple jobs at once. Active jobs are cancelled first."""
    result = await bulk_delete_jobs_service(db, request.job_ids)
    return BulkDeleteJobsResponse(**result)


@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: str, db: AsyncSession = Depends(get_db), request: Request = None):
    """Get a specific job by ID."""
    return await get_job_response(db, job_id, request=request)


@router.get("/{job_id}/status", response_model=JobStatusResponse)
async def get_job_status(job_id: str, db: AsyncSession = Depends(get_db), request: Request = None):
    """Get job status."""
    return await get_job_status_response(db, job_id, request=request)


@router.get("/{job_id}/metrics", response_model=JobMetricsResponse)
async def get_job_metrics(job_id: str, db: AsyncSession = Depends(get_db), request: Request = None):
    """Get job metrics."""
    return await get_job_metrics_response(db, job_id, request=request)


@router.get("/{job_id}/logs", response_model=list[JobLogResponse])
async def get_job_logs(
    job_id: str,
    limit: int = 1000,
    db: AsyncSession = Depends(get_db),
    request: Request = None,
):
    """Get job logs."""
    logs = await get_job_logs_service(db=db, job_id=job_id, limit=limit, request=request)
    return [JobLogResponse.model_validate(log) for log in logs]


@router.post("/{job_id}/cancel")
async def cancel_job(job_id: str, db: AsyncSession = Depends(get_db), request: Request = None):
    """Cancel a running or queued job."""
    return await cancel_job_service(db, job_id, request=request)


@router.delete("/{job_id}")
async def delete_job(job_id: str, db: AsyncSession = Depends(get_db), request: Request = None):
    """Delete a job and all its artifacts."""
    return await delete_job_service(db, job_id, request=request)


@router.post("/list", response_model=JobListResponse)
async def list_jobs_post(
    list_request: JobListRequest,
    db: AsyncSession = Depends(get_db),
    request: Request = None,
):
    """List jobs (POST for Domino compatibility).

    Supports filtering by:
    - status: Filter by job status (pending, running, completed, failed, cancelled)
    - model_type: Filter by model type (tabular, timeseries)
    - project_name: Filter by project name.
    - project_id: Filter by project ID (legacy, prefer project_name).

    Owner is always resolved from the domino-username header (cannot be overridden).
    """
    jobs = await list_jobs_filtered(db=db, list_request=list_request, request=request)

    return JobListResponse(
        jobs=[JobListItemResponse.model_validate(build_job_list_item_response(j)) for j in jobs],
        total=len(jobs),
        skip=list_request.skip,
        limit=list_request.limit,
    )


@router.get("/{job_id}/progress", response_model=JobProgressResponse)
async def get_job_progress(job_id: str, db: AsyncSession = Depends(get_db), request: Request = None):
    """Get detailed job progress."""
    return await get_job_progress_response(db, job_id, request=request)


@router.post("/{job_id}/register", response_model=RegisterModelResponse)
async def register_job_model(
    job_id: str,
    request: RegisterModelRequest,
    db: AsyncSession = Depends(get_db),
):
    """Register a trained model from a completed job to Domino registry."""
    return await register_model_for_job(db, job_id, request)
