"""Service helpers for deployment route orchestration."""

import logging
import os
from typing import Optional

from fastapi import HTTPException

from sqlalchemy import update as sa_update

from app.core.domino_model_api import get_domino_model_api
from app.db import crud
from app.db.models import Job as JobModel, JobStatus
from app.dependencies import get_db_session

logger = logging.getLogger(__name__)


def _safe_deployment_result(result, invalid_message: str) -> dict:
    """Normalize deployment API responses for compatibility handlers."""
    if isinstance(result, dict):
        normalized = dict(result)
        normalized.setdefault("success", False)
        normalized.setdefault("data", [])
        return normalized
    return {"success": False, "data": [], "error": invalid_message}


async def list_deployments_safe(model_api_id: str) -> dict:
    """List deployments for a Model API."""
    try:
        api = get_domino_model_api()
        result = await api.list_deployments(model_api_id=model_api_id)
        return _safe_deployment_result(result, "Invalid response")
    except Exception as exc:
        logger.error(f"Error listing deployments: {exc}")
        return {"success": False, "data": [], "error": str(exc)}



async def deploy_from_job(
    job_id: str,
    model_name: Optional[str] = None,
    replicas: int = 1,
) -> dict:
    """Create a Domino Model API from a job's registered model."""
    async with get_db_session() as db:
        job = await crud.get_job(db, job_id)
        if not job:
            raise HTTPException(status_code=404, detail=f"Job not found: {job_id}")

    if job.status != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Job must be completed to deploy. Current status: {job.status.value}",
        )

    if not job.is_registered or not job.registered_model_name or not job.registered_model_version:
        raise HTTPException(
            status_code=400,
            detail="Model must be registered in the Domino Model Registry before deploying as a Model API.",
        )

    deploy_name = model_name or job.name or f"automl-model-{job_id[:8]}"
    environment_id = os.environ.get("DOMINO_ENVIRONMENT_ID")

    api = get_domino_model_api()
    result = await api.create_model_api_from_registry(
        name=deploy_name,
        registered_model_name=job.registered_model_name,
        registered_model_version=int(job.registered_model_version),
        description=f"AutoML model from job {job_id}",
        environment_id=environment_id,
        replicas=replicas,
        project_id=job.project_id,
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    api_data = result.get("data") or {}
    model_api_id = api_data.get("id")

    if model_api_id:
        async with get_db_session() as db:
            await db.execute(sa_update(JobModel).where(JobModel.id == job_id).values(model_api_id=model_api_id))
            await db.commit()

    return {
        "success": True,
        "job_id": job_id,
        "model_api_id": model_api_id,
        "message": f"Model API '{deploy_name}' created from registered model {job.registered_model_name} v{job.registered_model_version}",
    }
