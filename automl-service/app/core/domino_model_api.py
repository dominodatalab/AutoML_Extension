"""Domino Model API client for managing model deployments."""

import os
import logging
from functools import lru_cache
from typing import Any, Dict, Optional
import httpx

from app.config import get_settings
from app.core.domino_http import domino_request

logger = logging.getLogger(__name__)


class DominoModelAPIClient:
    """Base client for Domino Model Serving API with HTTP request handling."""

    def __init__(self):
        self.settings = get_settings()

    @staticmethod
    def _extract_error(response: httpx.Response) -> str:
        content_type = response.headers.get("content-type", "")
        if "text/html" in content_type:
            return (
                f"Received HTML from Domino API (status {response.status_code}). "
                "This usually indicates an authentication failure."
            )
        try:
            payload = response.json()
            if isinstance(payload, dict):
                detail = payload.get("detail") or payload.get("error") or payload.get("message")
                if detail:
                    return str(detail)
        except ValueError:
            pass
        text = response.text.strip()
        if text:
            return text
        return f"Domino API request failed with status {response.status_code}"

    async def _make_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        try:
            payload = json_data if method.upper() != "GET" else None
            response = await domino_request(method.upper(), path, json=payload, params=params)
            if not response.text:
                return {"success": True, "data": {}}
            try:
                result = response.json()
            except ValueError:
                logger.error(f"Domino API returned non-JSON response for {path}")
                return {"success": False, "data": [], "error": "Domino API returned non-JSON response"}
            return {"success": True, "data": result}
        except httpx.HTTPStatusError as e:
            error_message = self._extract_error(e.response)
            logger.error(f"Domino API HTTP error for {path}: {error_message}")
            return {"success": False, "data": [], "error": error_message, "status_code": e.response.status_code}
        except Exception as e:
            logger.error(f"Error making request to {path}: {e}")
            return {"success": False, "data": [], "error": str(e)}


class ModelAPIManager:
    """Manages Model API resources."""

    def __init__(self, client: DominoModelAPIClient):
        self.client = client

    def _resolve_project_id(self, project_id: Optional[str]) -> Optional[str]:
        return project_id or self.client.settings.domino_project_id or os.environ.get("DOMINO_PROJECT_ID")

    async def create_model_api_from_registry(
        self,
        name: str,
        registered_model_name: str,
        registered_model_version: int,
        description: str = "",
        project_id: Optional[str] = None,
        environment_id: Optional[str] = None,
        replicas: int = 1,
    ) -> Dict[str, Any]:
        """Create a Model API sourced from a registered model version.

        POST /api/modelServing/v1/modelApis

        NOTE: The API accepts environmentId but not environmentRevisionId. Domino
        resolves the revision server-side using the environment's active revision at
        the time of creation. If the active revision has changed since training, the
        Model API may run on a different revision than the training job did.
        """
        resolved_project_id = self._resolve_project_id(project_id)
        if not resolved_project_id:
            return {
                "success": False,
                "error": (
                    "Missing project id for Model API creation. "
                    "Set DOMINO_PROJECT_ID or provide project_id."
                ),
            }

        if not environment_id:
            return {
                "success": False,
                "error": (
                    "Missing environment id for Model API creation. "
                    "DOMINO_ENVIRONMENT_ID must be set."
                ),
            }

        payload = {
            "name": name,
            "description": description,
            "environmentId": environment_id,
            "replicas": replicas,
            "strictNodeAntiAffinity": False,
            "isAsync": False,
            "environmentVariables": [],
            "version": {
                "projectId": resolved_project_id,
                "source": {
                    "type": "Registry",
                    "registeredModelName": registered_model_name,
                    "registeredModelVersion": registered_model_version,
                },
                "logHttpRequestResponse": False,
                "monitoringEnabled": False,
                "shouldDeploy": True,
            },
        }

        return await self.client._make_request("POST", "/api/modelServing/v1/modelApis", json_data=payload)


class ModelDeploymentManager:
    """Manages Model Deployment resources."""

    def __init__(self, client: DominoModelAPIClient):
        self.client = client

    async def list_deployments(self, model_api_id: str) -> Dict[str, Any]:
        """List deployments for a Model API.

        GET /api/modelServing/v1/modelDeployments
        """
        result = await self.client._make_request(
            "GET", "/api/modelServing/v1/modelDeployments", params={"modelApiId": model_api_id}
        )

        if result.get("success") and "data" in result:
            data = result["data"]
            if isinstance(data, dict) and "items" in data:
                result["data"] = data.get("items", [])

        return result


class DominoModelAPI:
    """Domino Model API client."""

    def __init__(self):
        self._client = DominoModelAPIClient()
        self.model_apis = ModelAPIManager(self._client)
        self.deployments = ModelDeploymentManager(self._client)

    async def create_model_api_from_registry(
        self,
        name: str,
        registered_model_name: str,
        registered_model_version: int,
        description: str = "",
        project_id: Optional[str] = None,
        environment_id: Optional[str] = None,
        replicas: int = 1,
    ) -> Dict[str, Any]:
        return await self.model_apis.create_model_api_from_registry(
            name, registered_model_name, registered_model_version,
            description, project_id, environment_id, replicas,
        )

    async def list_deployments(self, model_api_id: str) -> Dict[str, Any]:
        return await self.deployments.list_deployments(model_api_id)


@lru_cache()
def get_domino_model_api() -> DominoModelAPI:
    return DominoModelAPI()
