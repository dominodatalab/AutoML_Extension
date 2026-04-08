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


async def get_model_api_status_safe(model_api_id: str) -> dict:
    """Get active status for a Model API."""
    try:
        api = get_domino_model_api()
        result = await api.get_model_api_status(model_api_id=model_api_id)
        if not result.get("success"):
            return {"success": False, "error": result.get("error", "Unknown error")}
        data = result.get("data") or {}
        return {
            "success": True,
            "status": data.get("status", "unknown"),
            "isPending": data.get("isPending", False),
        }
    except Exception as exc:
        logger.error(f"Error fetching model API status: {exc}")
        return {"success": False, "error": str(exc)}



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
        raise HTTPException(status_code=500, detail=result.get("error"))

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
        "message": f"Model API '{deploy_name}' created from registered model {job.registered_model_name} version {job.registered_model_version}",
    }
