"""Authorization helpers for storage-management features."""

from __future__ import annotations

import logging
from typing import Optional

from fastapi import HTTPException

from app.core.authorized_actions import AuthorizedActionRequestItem, authorized_action_allowed
from app.core.domino_http import get_domino_public_api_client_sync, resolve_domino_project_id

logger = logging.getLogger(__name__)

def _current_user_can_change_project_settings(client, project_id: str) -> bool:
    """Return True when the current user is authorized to change project settings."""
    action = AuthorizedActionRequestItem(
        id=f"project.change_project_settings-{project_id}",
        code="project.change_project_settings",
        context={"projectId": project_id},
    )
    return authorized_action_allowed(client, action)


def current_user_can_modify_storage(project_id: Optional[str] = None) -> bool:
    """Return True when the current user may change project settings."""
    try:
        client = get_domino_public_api_client_sync()
        effective_project_id = project_id or resolve_domino_project_id()
        return _current_user_can_change_project_settings(client, effective_project_id)
    except Exception:
        logger.exception("Failed to resolve project settings permission for storage modification check")
        return False


def require_storage_modify(project_id: Optional[str] = None) -> None:
    """Raise 403 unless the current user may edit the extension."""
    if not current_user_can_modify_storage(project_id=project_id):
        raise HTTPException(
            status_code=403,
            detail="This operation requires permission to edit the extension.",
        )


def _current_user_can_list_jobs(client, project_id: str) -> bool:
    action = AuthorizedActionRequestItem(
        id=f"job.project.list_jobs-{project_id}",
        code="job.project.list_jobs",
        context={"projectId": project_id},
    )
    return authorized_action_allowed(client, action)


def _current_user_can_start_job(client, project_id: str) -> bool:
    action = AuthorizedActionRequestItem(
        id=f"job.project.start_job-{project_id}",
        code="job.project.start_job",
        context={"projectId": project_id},
    )
    return authorized_action_allowed(client, action)


def _current_user_can_stop_job(client, job_id: str) -> bool:
    action = AuthorizedActionRequestItem(
        id=f"job.project.stop_job-{job_id}",
        code="job.project.stop_job",
        context={"jobId": job_id},
    )
    return authorized_action_allowed(client, action)


def current_user_can_list_jobs(project_id: Optional[str] = None) -> bool:
    try:
        client = get_domino_public_api_client_sync()
        effective_project_id = project_id or resolve_domino_project_id()
        return _current_user_can_list_jobs(client, effective_project_id)
    except Exception:
        logger.exception("Failed to resolve project job listing permissions")
        return False


def current_user_can_start_job(project_id: Optional[str] = None) -> bool:
    try:
        client = get_domino_public_api_client_sync()
        effective_project_id = project_id or resolve_domino_project_id()
        return _current_user_can_start_job(client, effective_project_id)
    except Exception:
        logger.exception("Failed to resolve project job start permissions")
        return False


def current_user_can_stop_job(job_id: str) -> bool:
    try:
        client = get_domino_public_api_client_sync()
        return _current_user_can_stop_job(client, job_id)
    except Exception:
        logger.exception("Failed to resolve job stop permissions")
        return False


def require_domino_job_list(project_id: Optional[str] = None) -> None:
    if not current_user_can_list_jobs(project_id=project_id):
        raise HTTPException(
            status_code=403,
            detail="This operation requires permission to list jobs in the target project",
        )


def require_domino_job_start(project_id: Optional[str] = None) -> None:
    if not current_user_can_start_job(project_id=project_id):
        raise HTTPException(
            status_code=403,
            detail="This operation requires permission to start jobs in the target project",
        )


def require_domino_job_stop(job_id: str) -> None:
    if not current_user_can_stop_job(job_id=job_id):
        raise HTTPException(
            status_code=403,
            detail="This operation requires permission to stop the target job",
        )
