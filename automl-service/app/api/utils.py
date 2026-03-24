"""Shared utilities for API route handlers."""

from typing import Optional, Tuple

from fastapi import HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.utils import remap_shared_path
from app.db import crud


def resolve_request_project_id(request: Optional[Request]) -> Optional[str]:
    """Resolve project context from request metadata.

    Checks ``X-Project-Id`` header, then ``projectId`` / ``project_id``
    query params.  Returns ``None`` when no project context is available.

    **No env-var fallback** — ``DOMINO_PROJECT_ID`` is the App's own
    project, not the target project the user is working in.  Falling back
    to it silently operates on the wrong project.
    """
    if request is not None:
        header_project_id = request.headers.get("X-Project-Id")
        if header_project_id:
            return header_project_id

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

    Paths are remapped via ``remap_shared_path`` so they resolve correctly
    when the App and child jobs run in different Domino projects.

    Raises HTTPException(404) if job not found.
    Raises HTTPException(400) if model_path not available.
    """
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job not found: {job_id}")

    if not job.model_path:
        raise HTTPException(
            status_code=400,
            detail=f"Job {job_id} has no trained model. Status: {job.status.value}",
        )

    return (
        remap_shared_path(job.model_path),
        job.model_type.value,
        remap_shared_path(job.file_path) if job.file_path else None,
        job.problem_type.value if job.problem_type else None,
    )
