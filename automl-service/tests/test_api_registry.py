"""Tests for POST /svc/v1/registry/register."""

from unittest.mock import MagicMock, patch

import pytest
from app.core.context.auth import set_request_auth_header
from app.api.generated.domino_public_api_client.models.register_model_response_v2 import RegisterModelResponseV2

pytestmark = pytest.mark.domino

REGISTER_URL = "/svc/v1/registry/register"


def _make_job(*, experiment_run_id="run-abc"):
    job = MagicMock()
    job.experiment_run_id = experiment_run_id
    job.is_registered = False
    job.registered_model_name = None
    job.registered_model_version = None
    return job


def _make_success_response(model_version: int = 3):
    model_version_details = MagicMock()
    model_version_details.model_version = model_version
    parsed = MagicMock(spec=RegisterModelResponseV2)
    parsed.model_version = model_version_details
    response = MagicMock()
    response.parsed = parsed
    response.status_code = 200
    return response


@pytest.mark.asyncio
async def test_register_model_happy_path(app_client):
    set_request_auth_header("Bearer test-token")
    try:
        job = _make_job()
        with patch("app.api.routes.registry.crud.get_job", return_value=job), \
             patch("app.api.routes.registry.register_model_v2.sync_detailed", return_value=_make_success_response(3)), \
             patch("app.api.routes.registry.get_domino_public_api_client_sync"):
            response = await app_client.post(REGISTER_URL, json={
                "job_id": "job-123",
                "model_name": "my-model",
                "description": "test model",
            })
    finally:
        set_request_auth_header(None)

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["model_name"] == "my-model"
    assert body["model_version"] == "3"
    assert job.is_registered is True
    assert job.registered_model_name == "my-model"
    assert job.registered_model_version == "3"


@pytest.mark.asyncio
async def test_register_model_job_not_found(app_client):
    set_request_auth_header("Bearer test-token")
    try:
        with patch("app.api.routes.registry.crud.get_job", return_value=None):
            response = await app_client.post(REGISTER_URL, json={
                "job_id": "nonexistent",
                "model_name": "my-model",
            })
    finally:
        set_request_auth_header(None)

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_register_model_no_experiment_run(app_client):
    set_request_auth_header("Bearer test-token")
    try:
        job = _make_job(experiment_run_id=None)
        with patch("app.api.routes.registry.crud.get_job", return_value=job):
            response = await app_client.post(REGISTER_URL, json={
                "job_id": "job-123",
                "model_name": "my-model",
            })
    finally:
        set_request_auth_header(None)

    assert response.status_code == 400
    assert "MLflow" in response.json()["detail"]


@pytest.mark.asyncio
async def test_register_model_domino_error(app_client):
    set_request_auth_header("Bearer test-token")
    try:
        job = _make_job()
        error_response = MagicMock()
        error_response.parsed = None
        error_response.status_code = 500
        with patch("app.api.routes.registry.crud.get_job", return_value=job), \
             patch("app.api.routes.registry.register_model_v2.sync_detailed", return_value=error_response), \
             patch("app.api.routes.registry.get_domino_public_api_client_sync"):
            response = await app_client.post(REGISTER_URL, json={
                "job_id": "job-123",
                "model_name": "my-model",
            })
    finally:
        set_request_auth_header(None)

    assert response.status_code == 500
