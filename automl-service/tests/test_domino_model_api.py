"""Tests for ModelAPIManager.create_model_api_from_registry and get_status."""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.domino_model_api import ModelAPIManager
from app.api.generated.domino_public_api_client.models.model_api_source_type import ModelApiSourceType


def _make_manager(*, project_id: str = "proj-123"):
    manager = ModelAPIManager()
    manager.settings = MagicMock()
    manager.settings.domino_project_id = project_id
    return manager


def _mock_sync_response(model_api_id: str = "api-abc"):
    parsed = MagicMock()
    parsed.id = model_api_id
    response = MagicMock()
    response.parsed = parsed
    return response


class TestCreateModelApiFromRegistry:

    def test_missing_project_id_returns_error(self):
        manager = _make_manager(project_id=None)
        with patch.dict("os.environ", {}, clear=True):
            result = manager.create_model_api_from_registry(
                name="my-api",
                registered_model_name="automlapp-model",
                registered_model_version=1,
                environment_id="env-123",
            )
        assert result["success"] is False
        assert "project id" in result["error"].lower()

    def test_missing_environment_id_returns_error(self):
        manager = _make_manager()
        result = manager.create_model_api_from_registry(
            name="my-api",
            registered_model_name="automlapp-model",
            registered_model_version=1,
            environment_id=None,
        )
        assert result["success"] is False
        assert "environment id" in result["error"].lower()

    def test_happy_path_returns_model_api_id(self):
        manager = _make_manager()
        with patch("app.core.domino_model_api.create_model_api.sync_detailed", return_value=_mock_sync_response("api-abc")), \
             patch("app.core.domino_model_api.get_domino_public_api_client_sync"):
            result = manager.create_model_api_from_registry(
                name="my-api",
                registered_model_name="automlapp-model",
                registered_model_version=2,
                description="A test model",
                environment_id="env-123",
                replicas=3,
            )
        assert result["success"] is True
        assert result["data"]["id"] == "api-abc"

    def test_happy_path_request_body(self):
        manager = _make_manager()
        with patch("app.core.domino_model_api.create_model_api.sync_detailed", return_value=_mock_sync_response()) as mock_call, \
             patch("app.core.domino_model_api.get_domino_public_api_client_sync"):
            manager.create_model_api_from_registry(
                name="my-api",
                registered_model_name="automlapp-model",
                registered_model_version=2,
                description="A test model",
                environment_id="env-123",
                replicas=3,
            )
        body = mock_call.call_args.kwargs["body"]
        assert body.name == "my-api"
        assert body.description == "A test model"
        assert body.environment_id == "env-123"
        assert body.replicas == 3
        assert body.is_async is False
        assert body.strict_node_anti_affinity is False
        assert body.environment_variables == []
        assert body.version.project_id == "proj-123"
        assert body.version.source.type_ == ModelApiSourceType.REGISTRY
        assert body.version.source.registered_model_name == "automlapp-model"
        assert body.version.source.registered_model_version == 2
        assert body.version.log_http_request_response is False
        assert body.version.monitoring_enabled is False
        assert body.version.should_deploy is True

    def test_registered_model_version_is_integer(self):
        manager = _make_manager()
        with patch("app.core.domino_model_api.create_model_api.sync_detailed", return_value=_mock_sync_response()) as mock_call, \
             patch("app.core.domino_model_api.get_domino_public_api_client_sync"):
            manager.create_model_api_from_registry(
                name="my-api",
                registered_model_name="automlapp-model",
                registered_model_version=5,
                environment_id="env-123",
            )
        body = mock_call.call_args.kwargs["body"]
        assert isinstance(body.version.source.registered_model_version, int)
        assert body.version.source.registered_model_version == 5

    def test_status_200_with_no_parsed_falls_back_to_content(self):
        manager = _make_manager()
        mock_response = MagicMock()
        mock_response.parsed = None
        mock_response.status_code = 200
        mock_response.content = b'{"id": "api-from-200"}'
        with patch("app.core.domino_model_api.create_model_api.sync_detailed", return_value=mock_response), \
             patch("app.core.domino_model_api.get_domino_public_api_client_sync"):
            result = manager.create_model_api_from_registry(
                name="my-api",
                registered_model_name="automlapp-model",
                registered_model_version=1,
                environment_id="env-123",
            )
        assert result["success"] is True
        assert result["data"]["id"] == "api-from-200"

    def test_failed_response_returns_error(self):
        manager = _make_manager()
        mock_response = MagicMock()
        mock_response.parsed = None
        mock_response.status_code = 400
        with patch("app.core.domino_model_api.create_model_api.sync_detailed", return_value=mock_response), \
             patch("app.core.domino_model_api.get_domino_public_api_client_sync"):
            result = manager.create_model_api_from_registry(
                name="my-api",
                registered_model_name="automlapp-model",
                registered_model_version=1,
                environment_id="env-123",
            )
        assert result["success"] is False
        assert "400" in result["error"]

    def test_exception_returns_error(self):
        manager = _make_manager()
        with patch("app.core.domino_model_api.create_model_api.sync_detailed", side_effect=RuntimeError("connection refused")), \
             patch("app.core.domino_model_api.get_domino_public_api_client_sync"):
            result = manager.create_model_api_from_registry(
                name="my-api",
                registered_model_name="automlapp-model",
                registered_model_version=1,
                environment_id="env-123",
            )
        assert result["success"] is False
        assert "connection refused" in result["error"]


class TestGetStatus:

    @pytest.mark.asyncio
    async def test_calls_active_status_endpoint(self):
        manager = _make_manager()
        mock_response = MagicMock()
        mock_response.text = '{"status": "Running", "isPending": false}'
        mock_response.json = MagicMock(return_value={"status": "Running", "isPending": False})
        with patch("app.core.domino_model_api.domino_request", AsyncMock(return_value=mock_response)) as mock_req:
            result = await manager.get_status("api-xyz")
        assert result["success"] is True
        assert result["data"]["status"] == "Running"
        mock_req.assert_awaited_once_with("GET", "/models/api-xyz/activeStatus")

    @pytest.mark.asyncio
    async def test_returns_error_on_exception(self):
        manager = _make_manager()
        with patch("app.core.domino_model_api.domino_request", AsyncMock(side_effect=RuntimeError("timeout"))):
            result = await manager.get_status("api-missing")
        assert result["success"] is False
        assert "timeout" in result["error"]
