"""Helpers for building Domino and Experiment Manager links for jobs."""

import os
import asyncio
from fastapi import HTTPException
from typing import Optional
from urllib.parse import quote, urlparse, urlunparse

from app.core.domino_http import get_domino_public_api_client_sync
from app.api.generated.domino_public_api_client.api.projects import get_project_by_id
from app.api.generated.domino_public_api_client.models.project_v1 import ProjectV1

from app.config import get_settings
from app.db.models import Job


def _normalize_domino_ui_host(raw: Optional[str]) -> Optional[str]:
    """Normalize a configured Domino host into a UI-safe base URL."""
    if not raw:
        return None
    candidate = raw.strip()
    if not candidate:
        return None
    if "://" not in candidate:
        candidate = f"https://{candidate}"

    parsed = urlparse(candidate)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None

    hostname = (parsed.hostname or "").strip()
    if not hostname:
        return None

    # Domino UI links should resolve to tenant root, not apps subdomain.
    if hostname.startswith("apps."):
        hostname = hostname[len("apps.") :]

    if not hostname:
        return None

    netloc = f"{hostname}:{parsed.port}" if parsed.port else hostname
    return urlunparse((parsed.scheme, netloc, "", "", "", ""))


def _resolve_domino_ui_host() -> Optional[str]:
    """Resolve preferred Domino tenant host for user-facing links."""
    settings = get_settings()
    for raw in (
        os.environ.get("DOMINO_USER_HOST"),
        os.environ.get("DOMINO_EXTERNAL_HOST"),
        os.environ.get("DOMINO_LINK_HOST"),
        settings.domino_api_host,
        os.environ.get("DOMINO_API_HOST"),
    ):
        normalized = _normalize_domino_ui_host(raw)
        if normalized:
            return normalized.rstrip("/")
    return None

def _resolve_project_details(project_id: str) -> ProjectV1:
    client = get_domino_public_api_client_sync()
    response = get_project_by_id.sync(project_id, client=client)
    if not response:
        raise HTTPException(500, "No response from Domino when fetching project details")

    return response.project

def _resolve_project_owner(job: Optional[Job] = None) -> Optional[str]:
    """Resolve Domino project owner for project-scoped UI links.

    Prefers the job record's project_owner (set via sidebar resolution),
    then falls back to environment/settings.
    """
    job_owner = getattr(job, "project_owner", None) if job else None
    if isinstance(job_owner, str) and job_owner.strip():
        return job_owner.strip()

    settings = get_settings()
    owner = settings.domino_project_owner or os.environ.get("DOMINO_PROJECT_OWNER")
    if not owner:
        return None
    owner = owner.strip()
    return owner or None


def _resolve_project_name(job: Job) -> Optional[str]:
    """Resolve Domino project name preferring job metadata, then environment."""
    if job.project_name and job.project_name.strip():
        return job.project_name.strip()

    settings = get_settings()
    project_name = settings.domino_project_name or os.environ.get("DOMINO_PROJECT_NAME")
    if not project_name:
        return None
    project_name = project_name.strip()
    return project_name or None


def _build_domino_job_url(job: Job) -> Optional[str]:
    """Build canonical Domino run URL for a job id when context is available."""
    if not job.domino_job_id:
        return None

    project_info = _resolve_project_details(job.project_id)

    owner = project_info.owner_username
    project_name = project_info.name

    encoded_owner = quote(owner, safe="")
    encoded_project = quote(project_name, safe="")
    encoded_run_id = quote(job.domino_job_id, safe="")
    path = f"/jobs/{encoded_owner}/{encoded_project}/{encoded_run_id}/logs?status=all"
    host = _resolve_domino_ui_host()
    return f"{host}{path}" if host else path


def _resolve_experiment_id(job: Job, logger) -> Optional[str]:
    """Best-effort experiment-id lookup for the job's MLflow run."""
    run_id = (job.experiment_run_id or "").strip()
    experiment_name = (job.experiment_name or "").strip()
    if not run_id and not experiment_name:
        return None

    try:
        import mlflow
    except Exception:
        logger.debug("MLflow unavailable while resolving experiment id for job %s", job.id)
        return None

    tracking_uri = get_settings().mlflow_tracking_uri or os.environ.get("MLFLOW_TRACKING_URI")
    try:
        client = (
            mlflow.tracking.MlflowClient(tracking_uri=tracking_uri)
            if tracking_uri
            else mlflow.tracking.MlflowClient()
        )
    except Exception:
        logger.debug("Failed creating MLflow client while resolving experiment id for job %s", job.id)
        return None

    if run_id:
        try:
            run = client.get_run(run_id)
            run_experiment_id = getattr(run.info, "experiment_id", None)
            if run_experiment_id:
                return str(run_experiment_id)
        except Exception:
            logger.debug("Failed to resolve experiment id from run id for job %s", job.id)

    if experiment_name:
        try:
            experiment = client.get_experiment_by_name(experiment_name)
            if experiment and getattr(experiment, "experiment_id", None):
                return str(experiment.experiment_id)
        except Exception:
            logger.debug("Failed to resolve experiment id from name for job %s", job.id)

    return None


def _build_experiment_run_url(job: Job, experiment_id: Optional[str]) -> Optional[str]:
    """Build deep link to Domino Experiment Manager."""
    if not experiment_id:
        return None

    if not job.project_id:
        return None

    project = _resolve_project_details(job.project_id)

    owner = project.owner_username
    project_name = project.name

    encoded_owner = quote(owner, safe="")
    encoded_project = quote(project_name, safe="")
    encoded_experiment_id = quote(str(experiment_id), safe="")
    path = f"/experiments/{encoded_owner}/{encoded_project}/{encoded_experiment_id}"
    host = _resolve_domino_ui_host()
    return f"{host}{path}" if host else path


def _build_model_registry_url(job: Job) -> Optional[str]:
    """Build deep link to Domino Model Registry model card."""
    if not job.registered_model_name:
        return None

    if not job.project_id:
        return None

    project = _resolve_project_details(job.project_id)

    owner = project.owner_username
    project_name = project.name

    encoded_owner = quote(owner, safe="")
    encoded_project = quote(project_name, safe="")
    encoded_model = quote(job.registered_model_name, safe="")
    path = f"/u/{encoded_owner}/{encoded_project}/model-registry/{encoded_model}/model-card"
    if job.registered_model_version:
        path += f"?version={quote(job.registered_model_version, safe='')}"
    host = _resolve_domino_ui_host()
    return f"{host}{path}" if host else path


def attach_external_links(job: Job, logger) -> Job:
    """Attach computed external URLs used by the Job Overview UI."""
    experiment_id = _resolve_experiment_id(job, logger)
    setattr(job, "domino_job_url", _build_domino_job_url(job))
    setattr(job, "experiment_id", experiment_id)
    setattr(job, "experiment_run_url", _build_experiment_run_url(job, experiment_id))
    setattr(job, "model_registry_url", _build_model_registry_url(job))
    return job
