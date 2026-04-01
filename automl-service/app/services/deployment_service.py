"""Service helpers for deployment route orchestration."""

import asyncio
import logging
import keyword
import os
import re
from typing import Optional

from fastapi import HTTPException

from app.core.domino_model_api import get_domino_model_api
from app.core.job_file_cache import download_mlflow_artifact
from app.db import crud
from app.db.models import JobStatus
from app.dependencies import get_db_session

logger = logging.getLogger(__name__)

STATIC_MODEL_API_SOURCE_FILE = "automl-service/app/serving/model_api_entrypoint.py"


def _is_valid_python_identifier(name: str) -> bool:
    """Check that the requested prediction function name is a valid identifier."""
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name)) and not keyword.iskeyword(name)


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
    project_id: Optional[str] = None,
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
    if not job.model_path:
        raise HTTPException(status_code=400, detail="Model path not found for this job")
    loop = asyncio.get_event_loop()
    try:
        model_path = await loop.run_in_executor(None, download_mlflow_artifact, job.model_path, job_id)
    except (ValueError, FileNotFoundError) as e:
        raise HTTPException(status_code=500, detail=str(e))

    resolved_function_name = (function_name or "predict").strip() or "predict"
    if not _is_valid_python_identifier(resolved_function_name):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid prediction function '{resolved_function_name}'. Use a valid Python identifier.",
        )

    # Use a committed source entrypoint so Domino can resolve it from project code.
    model_file = STATIC_MODEL_API_SOURCE_FILE
    api = get_domino_model_api()
    result = await api.deploy_model(
        model_name=deploy_name,
        model_file=model_file,
        function_name=resolved_function_name,
        model_artifact_dir=model_path,
        description=f"AutoML model from job {job_id}. Type: {job.model_type}",
        min_replicas=min_replicas,
        max_replicas=max_replicas,
        auto_start=True,
        project_id=project_id,
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result.get("error"))

    model_api_id = result.get("model_api_id")

    return {
        "success": True,
        "job_id": job_id,
        "deployment_id": result.get("deployment_id"),
        "model_api_id": model_api_id,
        "endpoint_url": result.get("endpoint_url"),
        "message": f"Model '{deploy_name}' deployed from job {job_id}",
    }
