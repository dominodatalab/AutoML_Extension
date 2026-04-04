"""Tests for app.services.deployment_service helper functions."""

from contextlib import asynccontextmanager
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
import sys

import pytest
from fastapi import HTTPException

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.db.models import Job, JobStatus, ModelType
from app.services.deployment_service import (
    _safe_deployment_result,
    deploy_from_job,
)


# ---------------------------------------------------------------------------
# _safe_deployment_result
# ---------------------------------------------------------------------------


class TestSafeDeploymentResult:
    """Tests for the _safe_deployment_result normalizer."""

    def test_dict_with_all_keys_preserved(self) -> None:
        result = _safe_deployment_result(
            {"success": True, "data": [{"id": "d1"}], "extra": "val"},
            "fallback msg",
        )
        assert result["success"] is True
        assert result["data"] == [{"id": "d1"}]
        assert result["extra"] == "val"

    def test_dict_missing_success_gets_default_false(self) -> None:
        result = _safe_deployment_result({"data": [1, 2]}, "fallback msg")
        assert result["success"] is False
        assert result["data"] == [1, 2]

    def test_dict_missing_data_gets_default_empty_list(self) -> None:
        result = _safe_deployment_result({"success": True}, "fallback msg")
        assert result["success"] is True
        assert result["data"] == []

    def test_empty_dict_gets_both_defaults(self) -> None:
        result = _safe_deployment_result({}, "fallback msg")
        assert result == {"success": False, "data": []}

    def test_dict_with_error_key_preserved(self) -> None:
        result = _safe_deployment_result(
            {"error": "something went wrong"},
            "fallback msg",
        )
        assert result["error"] == "something went wrong"
        assert result["success"] is False
        assert result["data"] == []

    def test_dict_does_not_mutate_original(self) -> None:
        original = {"success": True}
        result = _safe_deployment_result(original, "msg")
        assert "data" in result
        assert "data" not in original

    def test_none_returns_error_dict(self) -> None:
        result = _safe_deployment_result(None, "Invalid response")
        assert result == {"success": False, "data": [], "error": "Invalid response"}

    def test_string_returns_error_dict(self) -> None:
        result = _safe_deployment_result("some string", "bad response")
        assert result == {"success": False, "data": [], "error": "bad response"}

    def test_list_returns_error_dict(self) -> None:
        result = _safe_deployment_result([1, 2, 3], "not a dict")
        assert result == {"success": False, "data": [], "error": "not a dict"}

    def test_int_returns_error_dict(self) -> None:
        result = _safe_deployment_result(42, "invalid")
        assert result == {"success": False, "data": [], "error": "invalid"}

    def test_bool_returns_error_dict(self) -> None:
        result = _safe_deployment_result(True, "nope")
        assert result == {"success": False, "data": [], "error": "nope"}


# ---------------------------------------------------------------------------
# deploy_from_job
# ---------------------------------------------------------------------------


def _make_job(**overrides) -> Job:
    job = MagicMock(spec=Job)
    job.status = JobStatus.COMPLETED
    job.is_registered = True
    job.registered_model_name = "automlapp-my-model"
    job.registered_model_version = "1"
    job.name = "my-job"
    job.model_type = ModelType.TABULAR
    for k, v in overrides.items():
        setattr(job, k, v)
    return job


def _make_db_session(job):
    """Return an async context manager that yields a db mock returning the given job."""
    db = AsyncMock()
    db.__aenter__ = AsyncMock(return_value=db)
    db.__aexit__ = AsyncMock(return_value=False)

    @asynccontextmanager
    async def _session():
        yield db

    return _session, db


class TestDeployFromJob:

    @pytest.mark.asyncio
    async def test_job_not_found_raises_404(self):
        session_cm, db = _make_db_session(None)
        db.execute = AsyncMock()

        with patch("app.services.deployment_service.get_db_session", session_cm), \
             patch("app.services.deployment_service.crud.get_job", AsyncMock(return_value=None)):
            with pytest.raises(HTTPException) as exc_info:
                await deploy_from_job("nonexistent-job-id")
            assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_job_not_completed_raises_400(self):
        job = _make_job(status=JobStatus.RUNNING)
        session_cm, _ = _make_db_session(job)

        with patch("app.services.deployment_service.get_db_session", session_cm), \
             patch("app.services.deployment_service.crud.get_job", AsyncMock(return_value=job)):
            with pytest.raises(HTTPException) as exc_info:
                await deploy_from_job("job-id")
            assert exc_info.value.status_code == 400
            assert "completed" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_job_not_registered_raises_400(self):
        job = _make_job(is_registered=False)
        session_cm, _ = _make_db_session(job)

        with patch("app.services.deployment_service.get_db_session", session_cm), \
             patch("app.services.deployment_service.crud.get_job", AsyncMock(return_value=job)):
            with pytest.raises(HTTPException) as exc_info:
                await deploy_from_job("job-id")
            assert exc_info.value.status_code == 400
            assert "registered" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_missing_registered_model_name_raises_400(self):
        job = _make_job(registered_model_name=None)
        session_cm, _ = _make_db_session(job)

        with patch("app.services.deployment_service.get_db_session", session_cm), \
             patch("app.services.deployment_service.crud.get_job", AsyncMock(return_value=job)):
            with pytest.raises(HTTPException) as exc_info:
                await deploy_from_job("job-id")
            assert exc_info.value.status_code == 400

    @pytest.mark.asyncio
    async def test_api_error_raises_400(self):
        job = _make_job()
        session_cm, _ = _make_db_session(job)
        mock_api = AsyncMock()
        mock_api.create_model_api_from_registry = AsyncMock(
            return_value={"success": False, "error": "environment not found"}
        )

        with patch("app.services.deployment_service.get_db_session", session_cm), \
             patch("app.services.deployment_service.crud.get_job", AsyncMock(return_value=job)), \
             patch("app.services.deployment_service.get_domino_model_api", return_value=mock_api), \
             patch.dict("os.environ", {"DOMINO_ENVIRONMENT_ID": "env-123"}):
            with pytest.raises(HTTPException) as exc_info:
                await deploy_from_job("job-id")
            assert exc_info.value.status_code == 400
            assert "environment not found" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_happy_path_returns_model_api_id(self):
        job = _make_job()
        session_cm, _ = _make_db_session(job)
        mock_api = AsyncMock()
        mock_api.create_model_api_from_registry = AsyncMock(
            return_value={"success": True, "data": {"id": "api-abc123"}}
        )

        with patch("app.services.deployment_service.get_db_session", session_cm), \
             patch("app.services.deployment_service.crud.get_job", AsyncMock(return_value=job)), \
             patch("app.services.deployment_service.get_domino_model_api", return_value=mock_api), \
             patch.dict("os.environ", {"DOMINO_ENVIRONMENT_ID": "env-123"}):
            result = await deploy_from_job("job-id", model_name="my-api", replicas=2)

        assert result["success"] is True
        assert result["model_api_id"] == "api-abc123"
        mock_api.create_model_api_from_registry.assert_awaited_once_with(
            name="my-api",
            registered_model_name="automlapp-my-model",
            registered_model_version=1,
            description="AutoML model from job job-id",
            environment_id="env-123",
            replicas=2,
        )

    @pytest.mark.asyncio
    async def test_model_name_defaults_to_job_name(self):
        job = _make_job()
        session_cm, _ = _make_db_session(job)
        mock_api = AsyncMock()
        mock_api.create_model_api_from_registry = AsyncMock(
            return_value={"success": True, "data": {"id": "api-xyz"}}
        )

        with patch("app.services.deployment_service.get_db_session", session_cm), \
             patch("app.services.deployment_service.crud.get_job", AsyncMock(return_value=job)), \
             patch("app.services.deployment_service.get_domino_model_api", return_value=mock_api), \
             patch.dict("os.environ", {"DOMINO_ENVIRONMENT_ID": "env-123"}):
            await deploy_from_job("job-id")

        call_kwargs = mock_api.create_model_api_from_registry.call_args
        assert call_kwargs.kwargs["name"] == "my-job"

    @pytest.mark.asyncio
    async def test_uses_domino_environment_id(self):
        job = _make_job()
        session_cm, _ = _make_db_session(job)
        mock_api = AsyncMock()
        mock_api.create_model_api_from_registry = AsyncMock(
            return_value={"success": True, "data": {"id": "api-xyz"}}
        )

        with patch("app.services.deployment_service.get_db_session", session_cm), \
             patch("app.services.deployment_service.crud.get_job", AsyncMock(return_value=job)), \
             patch("app.services.deployment_service.get_domino_model_api", return_value=mock_api), \
             patch.dict("os.environ", {"DOMINO_ENVIRONMENT_ID": "my-env-id"}):
            await deploy_from_job("job-id")

        call_kwargs = mock_api.create_model_api_from_registry.call_args
        assert call_kwargs.kwargs["environment_id"] == "my-env-id"
