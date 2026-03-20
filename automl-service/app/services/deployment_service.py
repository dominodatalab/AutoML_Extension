"""Service helpers for deployment route orchestration."""

import logging
import keyword
import os
import re
from typing import Optional

from fastapi import HTTPException

from app.core.domino_model_api import get_domino_model_api
from app.core.utils import remap_shared_path
from app.db import crud
from app.db.models import JobStatus
from app.dependencies import get_db_session
from app.services.storage_resolver import DATASET_NAME, get_storage_resolver

logger = logging.getLogger(__name__)

STATIC_MODEL_API_SOURCE_FILE = "automl-service/app/serving/model_api_entrypoint.py"

# Known mount prefixes for Domino datasets — used to extract the relative
# path within the dataset from an absolute filesystem path.
_MOUNT_PREFIXES = [
    "/mnt/data/",
    "/mnt/imported/data/",
    "/domino/datasets/",
    "/domino/datasets/local/",
]


async def _model_exists_in_dataset(
    project_id: Optional[str],
    model_path: str,
) -> bool:
    """Check whether *model_path* exists inside the project's dataset.

    Extracts the relative path (e.g. ``models/job_xxx``) from the absolute
    mount path and lists files in the dataset snapshot via the Domino API.
    Returns ``True`` if the directory is present, ``False`` otherwise.
    """
    if not project_id:
        return False

    # Derive the relative path within the dataset.
    relative: Optional[str] = None
    dataset_with_slash = DATASET_NAME + "/"
    for prefix in _MOUNT_PREFIXES:
        full_prefix = prefix + dataset_with_slash
        if model_path.startswith(full_prefix):
            relative = model_path[len(full_prefix):]
            break

    if relative is None:
        return False

    try:
        resolver = get_storage_resolver()
        # Use get_dataset_info first (cached), fall back to full resolve
        info = await resolver.get_dataset_info(project_id)
        if not info:
            # Cache is empty after restart — do a full API lookup
            try:
                info = await resolver.ensure_dataset_exists(project_id)
            except Exception:
                pass
        if not info:
            logger.debug("No dataset info found for project %s", project_id)
            return False
        rw_id = await resolver.get_rw_snapshot_id(info.dataset_id)
        if not rw_id:
            logger.debug("No RW snapshot for dataset %s", info.dataset_id)
            return False
        files = await resolver.list_snapshot_files(rw_id, path=relative)
        logger.debug(
            "Dataset file listing for '%s' in project %s: %d entries",
            relative, project_id, len(files),
        )
        return len(files) > 0
    except Exception:
        logger.warning(
            "Could not verify model path in dataset for project %s",
            project_id,
            exc_info=True,
        )
        return False


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
    model_path = remap_shared_path(job.model_path)
    if not model_path:
        raise HTTPException(status_code=400, detail="Model path not found for this job")
    if not os.path.isdir(model_path):
        # The App may not have the target project's dataset mounted.
        # Verify the model exists in the dataset via the API — use the
        # original stored path (not the remapped one) for prefix matching.
        if not await _model_exists_in_dataset(job.project_id, job.model_path):
            raise HTTPException(
                status_code=400,
                detail=f"Model directory not found: {model_path}",
            )
        # The model lives in the dataset — the Model API container will have
        # the mount, so use the original (un-remapped) path it was trained with.
        model_path = job.model_path
        logger.info(
            "Model not locally mounted but verified in dataset for project %s; "
            "proceeding with stored path %s",
            job.project_id, model_path,
        )

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
