"""Tests for POST /svc/v1/deployments"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from types import SimpleNamespace
from fastapi import HTTPException
from app.core.context.auth import set_request_auth_header
from app.api.generated.domino_public_api_client.models.model_api import ModelApi

def _make_job(*, experiment_run_id="run-abc", job_id=""):
    job = MagicMock()
    job.id = job_id
    job.status = 'completed'

    job.is_registered = True
    job.registered_model_name = 'registeredmodelname'
    job.registered_model_version = '1'

    job.experiment_run_id = experiment_run_id
    return job


def _make_success_response(model_id: str, model_version: int = 3):
    # had to use simplenamespace here, because magic mock types can't be inserted into sqlite
    # without causing type errors
    model_api = SimpleNamespace()
    parsed = SimpleNamespace(id=model_id, spec=ModelApi)
    response = SimpleNamespace()
    response.parsed = parsed
    response.status_code = 200
    return response


@pytest.mark.asyncio
async def test_deploy_from_job_happy_path(app_client, monkeypatch):
    """
    Verifies that the helper that reaches out to domino to get jobs is called and that the domino api
    for creating model apis is called
    """
    monkeypatch.setenv("DOMINO_ENVIRONMENT_ID", "fakeenvid")
    set_request_auth_header("Bearer test-token")
    job_id = "8771df7b-5550-4b6e-bea9-838f9fad040b"
    project_id = "69c66e4d729d187bd89d71f4"
    try:
        job = _make_job(job_id=job_id)
        with patch("app.services.deployment_service.get_job_or_404", new_callable=AsyncMock, return_value=job), \
             patch("app.core.domino_model_api.create_model_api.sync_detailed", return_value=_make_success_response(model_id='testid')), \
             patch("app.core.domino_model_api.get_domino_public_api_client_sync"):
            response = await app_client.post(f"/svc/v1/deployments/deploy-from-job/{job_id}?projectId={project_id}", json={
                "model_name": "my-model",
                "replicas": 1,
            })
    finally:
        set_request_auth_header(None)
    body = response.json()

    assert body['success'], f"Body was not successful, {body}"
    assert response.status_code == 200
