"""Service helpers for deployment route orchestration."""

import logging
import keyword
import os
import re
import shutil
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Optional

from fastapi import HTTPException

from app.core.model_api_source_bundle_gc import get_model_api_source_bundle_gc
from app.core.domino_model_api import get_domino_model_api
from app.db import crud
from app.db.models import JobStatus
from app.dependencies import get_db_session

logger = logging.getLogger(__name__)

STATIC_MODEL_API_SOURCE_FILE = "model_api.py"


def _is_valid_python_identifier(name: str) -> bool:
    """Check that the requested prediction function name is a valid identifier."""
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name)) and not keyword.iskeyword(name)


def _render_model_entrypoint(function_name: str) -> str:
    """Render a Domino Model API entrypoint script for AutoGluon artifacts."""
    extra_function = ""
    if function_name != "predict":
        extra_function = f"""

def {function_name}(data):
    return predict(data)
"""

    return (
        textwrap.dedent(
            """
            \"\"\"Auto-generated Domino Model API entrypoint for AutoML models.\"\"\"

            from pathlib import Path
            from typing import Any, Dict, Tuple

            import pandas as pd

            _MODEL_DIR = Path(__file__).resolve().parent
            _PREDICTOR = None
            _MODEL_TYPE = None


            def _load_predictor() -> Tuple[Any, str]:
                global _PREDICTOR, _MODEL_TYPE

                if _PREDICTOR is not None and _MODEL_TYPE is not None:
                    return _PREDICTOR, _MODEL_TYPE

                errors = []

                try:
                    from autogluon.tabular import TabularPredictor

                    _PREDICTOR = TabularPredictor.load(str(_MODEL_DIR))
                    _MODEL_TYPE = "tabular"
                    return _PREDICTOR, _MODEL_TYPE
                except Exception as exc:
                    errors.append(f"tabular={exc}")

                try:
                    from autogluon.timeseries import TimeSeriesPredictor

                    _PREDICTOR = TimeSeriesPredictor.load(str(_MODEL_DIR))
                    _MODEL_TYPE = "timeseries"
                    return _PREDICTOR, _MODEL_TYPE
                except Exception as exc:
                    errors.append(f"timeseries={exc}")

                raise RuntimeError(
                    "Unable to load AutoGluon predictor from "
                    f"{_MODEL_DIR}. Errors: {'; '.join(errors)}"
                )


            def _to_dataframe(payload: Any) -> pd.DataFrame:
                if isinstance(payload, pd.DataFrame):
                    return payload
                if isinstance(payload, list):
                    return pd.DataFrame(payload)
                if isinstance(payload, dict):
                    if "data" in payload:
                        inner = payload["data"]
                        if isinstance(inner, pd.DataFrame):
                            return inner
                        if isinstance(inner, list):
                            return pd.DataFrame(inner)
                        if isinstance(inner, dict):
                            return pd.DataFrame([inner])
                    return pd.DataFrame([payload])
                return pd.DataFrame(payload)


            def _to_serializable(value: Any):
                if hasattr(value, "to_dict"):
                    try:
                        return value.to_dict(orient="records")
                    except TypeError:
                        return value.to_dict()
                if hasattr(value, "tolist"):
                    return value.tolist()
                return value


            def predict(data: Any) -> Dict[str, Any]:
                predictor, model_type = _load_predictor()

                if model_type == "tabular":
                    input_df = _to_dataframe(data)
                    predictions = predictor.predict(input_df)
                    response = {"predictions": _to_serializable(predictions)}

                    try:
                        probabilities = predictor.predict_proba(input_df)
                        response["probabilities"] = _to_serializable(probabilities)
                    except Exception:
                        pass

                    return response

                payload = data["data"] if isinstance(data, dict) and "data" in data else data
                if isinstance(payload, list):
                    payload = pd.DataFrame(payload)
                elif isinstance(payload, dict):
                    payload = pd.DataFrame(payload)

                predictions = predictor.predict(payload)
                return {"predictions": _to_serializable(predictions)}
            """
        ).strip()
        + "\n"
        + extra_function
    )


def _ensure_model_entrypoint(model_path: str, function_name: str, overwrite: bool = False) -> str:
    """Ensure model.py exists inside the trained model directory."""
    if not os.path.isdir(model_path):
        raise HTTPException(status_code=400, detail=f"Model directory not found: {model_path}")

    if not _is_valid_python_identifier(function_name):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid prediction function '{function_name}'. Use a valid Python identifier.",
        )

    model_file = os.path.join(model_path, "model.py")
    if os.path.isfile(model_file) and not overwrite:
        return model_file

    try:
        with open(model_file, "w", encoding="utf-8") as handle:
            handle.write(_render_model_entrypoint(function_name))
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate model entrypoint at {model_file}: {exc}",
        ) from exc

    logger.info(f"Prepared model entrypoint at {model_file}")
    return model_file


def _prepare_model_api_source_bundle(job_id: str, model_path: str, function_name: str) -> tuple[str, str]:
    """Copy model artifacts into project code tree and return source_file and bundle_dir."""
    if not os.path.isdir(model_path):
        raise HTTPException(status_code=400, detail=f"Model directory not found: {model_path}")

    bundle_gc = get_model_api_source_bundle_gc()
    bundle_root = bundle_gc.bundle_root()
    bundle_root.mkdir(parents=True, exist_ok=True)
    bundle_suffix = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")
    bundle_dir = (bundle_root / f"job_{job_id}_{bundle_suffix}").resolve()

    try:
        shutil.copytree(model_path, bundle_dir)
        _ensure_model_entrypoint(str(bundle_dir), function_name, overwrite=True)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to prepare model API source bundle for job {job_id}: {exc}",
        ) from exc

    source_file = Path("automl_model_api_sources") / bundle_dir.name / "model.py"

    source_file_str = source_file.as_posix()
    bundle_dir_str = str(bundle_dir)
    logger.info(
        "Prepared Model API source bundle for job %s: source_file=%s, bundle_dir=%s",
        job_id,
        source_file_str,
        bundle_dir_str,
    )
    return source_file_str, bundle_dir_str


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
    if not os.path.isdir(model_path):
        raise HTTPException(status_code=400, detail=f"Model directory not found: {model_path}")

    resolved_function_name = (function_name or "predict").strip() or "predict"
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
