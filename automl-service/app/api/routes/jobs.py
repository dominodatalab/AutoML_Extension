"""Job management endpoints."""

from typing import Optional

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_project_context, get_request_project_id
from app.api.schemas.job import (
    BulkDeleteJobsRequest,
    BulkDeleteJobsResponse,
    JobCreateRequest,
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
    find_orphans_checked,
    get_job_metrics_response,
    get_job_logs as get_job_logs_service,
    get_job_progress_response,
    get_job_response,
    get_job_status_response,
    list_jobs_filtered,
    preview_cleanup as preview_cleanup_service,
    register_model_for_job,
)

router = APIRouter()


@router.post("", response_model=JobResponse)
async def create_job(
    job_request: JobCreateRequest,
    db: AsyncSession = Depends(get_db),
    project_context: tuple = Depends(get_project_context),
):
    """Create a new training job."""
    project_id, project_name, project_owner = project_context
    return await create_job_with_context(
        db=db,
        job_request=job_request,
        project_id=project_id,
        project_name=project_name,
        project_owner=project_owner,
    )


@router.get("/orphans/preview")
async def preview_orphans(
    db: AsyncSession = Depends(get_db),
    project_id: str = Depends(get_request_project_id),
):
    """Preview orphaned model dirs and upload files with no matching job."""
    return await find_orphans_checked(db, project_id=project_id)


@router.get("/cleanup/preview")
async def preview_cleanup(
    statuses: str = "failed,cancelled",
    older_than_days: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
    project_id: str = Depends(get_request_project_id),
):
    """Preview what would be deleted by a bulk cleanup."""
    return await preview_cleanup_service(
        db=db,
        statuses=statuses,
        older_than_days=older_than_days,
        project_id=project_id,
    )


@router.post("/cleanup")
async def bulk_cleanup(
    request: CleanupRequest,
    db: AsyncSession = Depends(get_db),
    project_id: str = Depends(get_request_project_id),
):
    """Delete artifacts and DB rows for jobs matching the given criteria."""
    return await bulk_cleanup_service(
        db=db,
        statuses=request.statuses,
        older_than_days=request.older_than_days,
        include_orphans=request.include_orphans,
        project_id=project_id,
    )


@router.post("/cleanup/orphans")
async def delete_orphans(
    db: AsyncSession = Depends(get_db),
    project_id: str = Depends(get_request_project_id),
):
    """Delete orphaned model dirs and upload files with no matching job."""
    return await delete_orphans_service(
        db,
        project_id=project_id,
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
async def get_job(job_id: str, db: AsyncSession = Depends(get_db)):
    """Get a specific job by ID."""
    return await get_job_response(db, job_id)


@router.get("/{job_id}/status", response_model=JobStatusResponse)
async def get_job_status(job_id: str, db: AsyncSession = Depends(get_db)):
    """Get job status."""
    return await get_job_status_response(db, job_id)


@router.get("/{job_id}/metrics", response_model=JobMetricsResponse)
async def get_job_metrics(job_id: str, db: AsyncSession = Depends(get_db)):
    """Get job metrics."""
    return await get_job_metrics_response(db, job_id)


@router.get("/{job_id}/logs", response_model=list[JobLogResponse])
async def get_job_logs(
    job_id: str,
    limit: int = 1000,
    db: AsyncSession = Depends(get_db),
):
    """Get job logs."""
    logs = await get_job_logs_service(db=db, job_id=job_id, limit=limit)
    return [JobLogResponse.model_validate(log) for log in logs]


@router.post("/{job_id}/cancel")
async def cancel_job(job_id: str, db: AsyncSession = Depends(get_db)):
    """Cancel a running or queued job."""
    return await cancel_job_service(db, job_id)


@router.delete("/{job_id}")
async def delete_job(job_id: str, db: AsyncSession = Depends(get_db)):
    """Delete a job and all its artifacts."""
    return await delete_job_service(db, job_id)


@router.get("", response_model=JobListResponse)
async def list_jobs(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    modelType: Optional[str] = None,
    owner: Optional[str] = None,
    projectId: str = Depends(get_request_project_id),
    projectName: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
):
    """List jobs with optional filters."""
    list_request = JobListRequest(
        skip=skip,
        limit=limit,
        status=status,
        model_type=modelType,
        owner=owner,
        project_id=projectId,
        project_name=projectName,
    )
    jobs = await list_jobs_filtered(db=db, list_request=list_request)
    return JobListResponse(
        jobs=[JobResponse.model_validate(j) for j in jobs],
        total=len(jobs),
        skip=skip,
        limit=limit,
    )


@router.get("/{job_id}/progress", response_model=JobProgressResponse)
async def get_job_progress(job_id: str, db: AsyncSession = Depends(get_db)):
    """Get detailed job progress."""
    return await get_job_progress_response(db, job_id)


@router.post("/{job_id}/register", response_model=RegisterModelResponse)
async def register_job_model(
    job_id: str,
    request: RegisterModelRequest,
    db: AsyncSession = Depends(get_db),
):
    """Register a trained model from a completed job to Domino registry."""
    return await register_model_for_job(db, job_id, request)
