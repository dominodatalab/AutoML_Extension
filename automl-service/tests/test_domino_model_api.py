"""Tests for ModelAPIManager.create_model_api_from_registry."""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.domino_model_api import ModelAPIManager


def _make_manager(*, project_id: str = "proj-123", make_request_return=None):
    """Build a ModelAPIManager with a mocked client."""
    client = MagicMock()
    client.settings.domino_project_id = project_id
    client._make_request = AsyncMock(
        return_value=make_request_return or {"success": True, "data": {"id": "api-abc"}}
    )
    return ModelAPIManager(client)


class TestCreateModelApiFromRegistry:

    @pytest.mark.asyncio
    async def test_missing_project_id_returns_error(self):
        manager = _make_manager(project_id=None)
        with patch.dict("os.environ", {}, clear=True):
            result = await manager.create_model_api_from_registry(
                name="my-api",
                registered_model_name="automlapp-model",
                registered_model_version=1,
                environment_id="env-123",
            )
        assert result["success"] is False
        assert "project id" in result["error"].lower()
        manager.client._make_request.assert_not_called()

    @pytest.mark.asyncio
    async def test_missing_environment_id_returns_error(self):
        manager = _make_manager()
        result = await manager.create_model_api_from_registry(
            name="my-api",
            registered_model_name="automlapp-model",
            registered_model_version=1,
            environment_id=None,
        )
        assert result["success"] is False
        assert "environment id" in result["error"].lower()
        manager.client._make_request.assert_not_called()

    @pytest.mark.asyncio
    async def test_happy_path_calls_correct_endpoint(self):
        manager = _make_manager()
        result = await manager.create_model_api_from_registry(
            name="my-api",
            registered_model_name="automlapp-model",
            registered_model_version=2,
            description="A test model",
            environment_id="env-123",
            replicas=3,
        )
        assert result["success"] is True
        manager.client._make_request.assert_awaited_once()
        method, path = manager.client._make_request.call_args.args
        assert method == "POST"
        assert path == "/api/modelServing/v1/modelApis"

    @pytest.mark.asyncio
    async def test_happy_path_payload_shape(self):
        manager = _make_manager()
        await manager.create_model_api_from_registry(
            name="my-api",
            registered_model_name="automlapp-model",
            registered_model_version=2,
            description="A test model",
            environment_id="env-123",
            replicas=3,
        )
        payload = manager.client._make_request.call_args.kwargs["json_data"]

        assert payload["name"] == "my-api"
        assert payload["description"] == "A test model"
        assert payload["environmentId"] == "env-123"
        assert payload["replicas"] == 3
        assert payload["isAsync"] is False
        assert payload["strictNodeAntiAffinity"] is False
        assert payload["environmentVariables"] == []

        version = payload["version"]
        assert version["projectId"] == "proj-123"
        assert version["source"] == {
            "type": "Registry",
            "registeredModelName": "automlapp-model",
            "registeredModelVersion": 2,
        }
        assert version["logHttpRequestResponse"] is False
        assert version["monitoringEnabled"] is False
        assert version["shouldDeploy"] is True

    @pytest.mark.asyncio
    async def test_registered_model_version_is_integer(self):
        manager = _make_manager()
        await manager.create_model_api_from_registry(
            name="my-api",
            registered_model_name="automlapp-model",
            registered_model_version=5,
            environment_id="env-123",
        )
        payload = manager.client._make_request.call_args.kwargs["json_data"]
        version_num = payload["version"]["source"]["registeredModelVersion"]
        assert isinstance(version_num, int)
        assert version_num == 5
