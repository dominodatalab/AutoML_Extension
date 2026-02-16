"""Service helpers for deployment route orchestration."""

import logging
from typing import Optional

from fastapi import HTTPException

from app.core.domino_model_api import get_domino_model_api
from app.db import crud
from app.db.models import JobStatus
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


async def list_deployments_safe(
    project_id: Optional[str] = None,
    model_api_id: Optional[str] = None,
) -> dict:
    """List deployments and gracefully handle errors."""
    try:
        api = get_domino_model_api()
        result = await api.list_deployments(
            project_id=project_id,
            model_api_id=model_api_id,
        )
        return _safe_deployment_result(result, "Invalid response")
    except Exception as exc:
        logger.error(f"Error listing deployments: {exc}")
        return {"success": False, "data": [], "error": str(exc)}


async def list_model_apis_safe(project_id: Optional[str] = None) -> dict:
    """List model APIs and gracefully handle errors."""
    try:
        api = get_domino_model_api()
        result = await api.list_model_apis(project_id=project_id)
        return _safe_deployment_result(result, "Invalid response")
    except Exception as exc:
        logger.error(f"Error listing model APIs: {exc}")
        return {"success": False, "data": [], "error": str(exc)}


async def deploy_from_job(
    job_id: str,
    model_name: Optional[str] = None,
    function_name: str = "predict",
    min_replicas: int = 1,
    max_replicas: int = 1,
) -> dict:
    """Deploy a trained model from a completed AutoML job."""
    async with get_db_session() as db:
        job = await crud.get_job(db, job_id)
        if not job:
            raise HTTPException(status_code=404, detail=f"Job not found: {job_id}")

    if job.status != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400,
            detail=f"Job must be completed to deploy. Current status: {job.status.value}",
        )

    deploy_name = model_name or job.name or f"automl-model-{job_id[:8]}"
    model_path = job.model_path
    if not model_path:
        raise HTTPException(status_code=400, detail="Model path not found for this job")

    model_file = f"{model_path}/model.py"
    api = get_domino_model_api()
    result = await api.deploy_model(
        model_name=deploy_name,
        model_file=model_file,
        function_name=function_name,
        description=f"AutoML model from job {job_id}. Type: {job.model_type}",
        min_replicas=min_replicas,
        max_replicas=max_replicas,
        auto_start=True,
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    return {
        "success": True,
        "job_id": job_id,
        "deployment_id": result.get("deployment_id"),
        "model_api_id": result.get("model_api_id"),
        "endpoint_url": result.get("endpoint_url"),
        "message": f"Model '{deploy_name}' deployed from job {job_id}",
    }
