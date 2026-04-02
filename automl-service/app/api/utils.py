"""Shared utilities for API route handlers."""

import asyncio
from typing import Optional, Tuple

from fastapi import HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.job_file_cache import download_mlflow_artifact
from app.db import crud


def resolve_request_project_id(request: Optional[Request]) -> Optional[str]:
    """Resolve project context from ``projectId`` / ``project_id`` query param.

    Returns ``None`` when no project context is available.
    """
    if request is not None:
        for query_key in ("projectId", "project_id"):
            query_project_id = request.query_params.get(query_key)
            if query_project_id:
                return query_project_id

    return None


async def get_job_paths(
    db: AsyncSession, job_id: str
) -> Tuple[str, str, Optional[str], Optional[str]]:
    """
    Look up a job and return (model_path, model_type, file_path, problem_type).

    Raises HTTPException(404) if job not found.
    Raises HTTPException(400) if model_path not available.
    Raises HTTPException(500) if model_path is not an MLflow URI or download fails.
    """
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job not found: {job_id}")

    if not job.model_path:
        raise HTTPException(
            status_code=400,
            detail=f"Job {job_id} has no trained model. Status: {job.status.value}",
        )

    loop = asyncio.get_event_loop()
    try:
        local_model_path = await loop.run_in_executor(
            None, download_mlflow_artifact, job.model_path, job_id
        )
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

    # TODO: file_path refers to a dataset path in the training job's project, which is
    # inaccessible to this app (different project, no cross-project dataset mounting).
    # Future: the file cache should use the Domino Datasets API to download the file and cache.
    # this func would read that (populating the cache if missing).
    return (
        local_model_path,
        job.model_type.value,
        job.file_path,
        job.problem_type.value if job.problem_type else None,
    )
