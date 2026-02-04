"""Job management endpoints."""

import logging
import os
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Request

logger = logging.getLogger(__name__)
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.db import crud
from app.db.models import Job, JobStatus, ModelType, ProblemType
from app.api.schemas.job import (
    JobCreateRequest,
    JobResponse,
    JobStatusResponse,
    JobMetricsResponse,
    JobLogResponse,
    JobListResponse,
    JobListRequest,
    JobProgressResponse,
    RegisterModelRequest,
    RegisterModelResponse,
)
from app.workers.training_worker import run_training_job, register_trained_model
from app.config import get_settings

router = APIRouter()


def get_user_from_request(request: Request) -> str:
    """Extract username from Domino headers."""
    return request.headers.get("domino-username", "anonymous")


def get_project_info() -> tuple[Optional[str], Optional[str]]:
    """Get project ID and name from Domino environment variables."""
    settings = get_settings()
    return (
        settings.domino_project_id or os.environ.get("DOMINO_PROJECT_ID"),
        settings.domino_project_name or os.environ.get("DOMINO_PROJECT_NAME"),
    )


@router.post("", response_model=JobResponse)
async def create_job(
    job_request: JobCreateRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    request: Request = None,
):
    """Create a new training job.

    The job is automatically associated with the current user (from domino-username header)
    and project (from DOMINO_PROJECT_ID environment variable).
    """
    # Get user and project context
    owner = get_user_from_request(request) if request else "anonymous"
    project_id, project_name = get_project_info()

    logger.info(f"[JOB CREATE] User: {owner}, Project: {project_id} ({project_name})")

    # Validate request
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

    # Build autogluon_config from advanced configs
    autogluon_config = {}
    if job_request.advanced_config:
        autogluon_config["advanced"] = job_request.advanced_config.model_dump(exclude_none=True)
    if job_request.timeseries_config:
        autogluon_config["timeseries"] = job_request.timeseries_config.model_dump(exclude_none=True)
    if job_request.multimodal_config:
        autogluon_config["multimodal"] = job_request.multimodal_config.model_dump(exclude_none=True)
    if job_request.feature_columns:
        autogluon_config["feature_columns"] = job_request.feature_columns

    # DEBUG: Log the incoming request
    logger.info(f"[JOB CREATE DEBUG] Received job create request")
    logger.info(f"[JOB CREATE DEBUG] data_source: {job_request.data_source}")
    logger.info(f"[JOB CREATE DEBUG] file_path from request: {job_request.file_path}")
    logger.info(f"[JOB CREATE DEBUG] dataset_id: {job_request.dataset_id}")

    # Create job record with owner and project info
    job = Job(
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
        autogluon_config=autogluon_config if autogluon_config else None,
    )

    job = await crud.create_job(db, job)

    # Start training in background
    background_tasks.add_task(run_training_job, job.id)

    return job


@router.get("", response_model=JobListResponse)
async def list_jobs(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
):
    """List all training jobs."""
    status_filter = JobStatus(status) if status else None
    jobs = await crud.get_jobs(db, skip=skip, limit=limit, status=status_filter)

    return JobListResponse(
        jobs=[JobResponse.model_validate(j) for j in jobs],
        total=len(jobs),
        skip=skip,
        limit=limit,
    )


@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: str, db: AsyncSession = Depends(get_db)):
    """Get a specific job by ID."""
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Fix leaderboard format if it's the old {"models": [...]} format
    if job.leaderboard and isinstance(job.leaderboard, dict) and "models" in job.leaderboard:
        job.leaderboard = job.leaderboard["models"]

    return job


@router.get("/{job_id}/status", response_model=JobStatusResponse)
async def get_job_status(job_id: str, db: AsyncSession = Depends(get_db)):
    """Get job status."""
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return JobStatusResponse(
        id=job.id,
        status=job.status.value,
        error_message=job.error_message,
        started_at=job.started_at,
        completed_at=job.completed_at,
    )


@router.get("/{job_id}/metrics", response_model=JobMetricsResponse)
async def get_job_metrics(job_id: str, db: AsyncSession = Depends(get_db)):
    """Get job metrics."""
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    leaderboard_list = None
    if job.leaderboard:
        # Convert leaderboard dict to list format
        leaderboard_list = job.leaderboard.get("models", [])

    return JobMetricsResponse(
        id=job.id,
        metrics=job.metrics,
        leaderboard=leaderboard_list,
    )


@router.get("/{job_id}/logs", response_model=list[JobLogResponse])
async def get_job_logs(
    job_id: str,
    limit: int = 1000,
    db: AsyncSession = Depends(get_db),
):
    """Get job logs."""
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    logs = await crud.get_job_logs(db, job_id, limit=limit)
    return [JobLogResponse.model_validate(log) for log in logs]


@router.post("/{job_id}/cancel")
async def cancel_job(job_id: str, db: AsyncSession = Depends(get_db)):
    """Cancel a running job."""
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if job.status not in [JobStatus.PENDING, JobStatus.RUNNING]:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot cancel job with status: {job.status.value}",
        )

    await crud.update_job_status(
        db,
        job_id,
        JobStatus.CANCELLED,
        completed_at=datetime.utcnow(),
    )

    return {"message": "Job cancelled", "job_id": job_id}


@router.delete("/{job_id}")
async def delete_job(job_id: str, db: AsyncSession = Depends(get_db)):
    """Delete a job."""
    success = await crud.delete_job(db, job_id)
    if not success:
        raise HTTPException(status_code=404, detail="Job not found")

    return {"message": "Job deleted", "job_id": job_id}


@router.post("/list", response_model=JobListResponse)
async def list_jobs_post(
    list_request: JobListRequest,
    db: AsyncSession = Depends(get_db),
    request: Request = None,
):
    """List jobs (POST for Domino compatibility).

    Supports filtering by:
    - status: Filter by job status (pending, running, completed, failed, cancelled)
    - model_type: Filter by model type (tabular, timeseries, multimodal)
    - owner: Filter by owner username. If not provided, uses current user from domino-username header.
             Pass owner="" (empty string) to see all users' jobs.
    - project_name: Filter by project name. Pass project_name="" to see jobs from all projects.
    - project_id: Filter by project ID (legacy, prefer project_name).
    """
    status_filter = JobStatus(list_request.status) if list_request.status else None
    model_type_filter = ModelType(list_request.model_type) if list_request.model_type else None

    # Determine owner filter
    # - If explicitly provided in request, use it (even if empty string for "all users")
    # - Otherwise, default to current user from headers
    if list_request.owner is not None:
        owner_filter = list_request.owner if list_request.owner else None  # "" means no filter
    else:
        owner_filter = get_user_from_request(request) if request else None

    # Determine project_name filter
    # - If explicitly provided in request, use it (even if empty string for "all projects")
    # - Otherwise, no default (show all projects)
    if list_request.project_name is not None:
        project_name_filter = list_request.project_name if list_request.project_name else None  # "" means no filter
    else:
        project_name_filter = None  # No default - show all projects unless specified

    # Legacy project_id filter (if project_name not provided but project_id is)
    if list_request.project_id is not None:
        project_id_filter = list_request.project_id if list_request.project_id else None
    else:
        project_id_filter = None

    logger.debug(f"[JOB LIST] Filters - owner: {owner_filter}, project_name: {project_name_filter}, status: {status_filter}")

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

    return JobListResponse(
        jobs=[JobResponse.model_validate(j) for j in jobs],
        total=len(jobs),
        skip=list_request.skip,
        limit=list_request.limit,
    )


@router.get("/{job_id}/progress", response_model=JobProgressResponse)
async def get_job_progress(job_id: str, db: AsyncSession = Depends(get_db)):
    """Get detailed job progress."""
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return JobProgressResponse(
        id=job.id,
        status=job.status.value,
        progress=job.progress if hasattr(job, 'progress') and job.progress else 0,
        current_step=job.current_step if hasattr(job, 'current_step') else None,
        models_trained=job.models_trained if hasattr(job, 'models_trained') else 0,
        current_model=job.current_model if hasattr(job, 'current_model') else None,
        eta_seconds=job.eta_seconds if hasattr(job, 'eta_seconds') else None,
        started_at=job.started_at,
    )


@router.post("/{job_id}/register", response_model=RegisterModelResponse)
async def register_job_model(
    job_id: str,
    request: RegisterModelRequest,
    db: AsyncSession = Depends(get_db),
):
    """Register a trained model from a completed job to Domino registry."""
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    if job.status != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot register model from job with status: {job.status.value}"
        )

    try:
        # Add automlapp- prefix to model name for filtering in registry
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
    except Exception as e:
        return RegisterModelResponse(
            success=False,
            model_name=request.model_name,
            error=str(e),
        )
