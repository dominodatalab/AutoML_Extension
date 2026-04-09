"""Domino Model API client for managing model deployments."""

import json
import os
import logging
from functools import lru_cache
from typing import Any, Dict, Optional
import httpx

from app.api.generated.domino_public_api_client.api.model_api import create_model_api
from app.api.generated.domino_public_api_client.models.model_api_creation_request import ModelApiCreationRequest
from app.api.generated.domino_public_api_client.models.model_api_source import ModelApiSource
from app.api.generated.domino_public_api_client.models.model_api_source_type import ModelApiSourceType
from app.api.generated.domino_public_api_client.models.model_api_version_creation_request import ModelApiVersionCreationRequest
from app.config import get_settings
from app.core.domino_http import domino_request, get_domino_public_api_client_sync

logger = logging.getLogger(__name__)


class ModelAPIManager:
    """Manages Model API resources."""

    def __init__(self):
        self.settings = get_settings()

    def _resolve_project_id(self, project_id: Optional[str]) -> Optional[str]:
        return project_id or self.settings.domino_project_id or os.environ.get("DOMINO_PROJECT_ID")

    def create_model_api_from_registry(
        self,
        name: str,
        registered_model_name: str,
        registered_model_version: int,
        description: str = "",
        project_id: Optional[str] = None,
        environment_id: Optional[str] = None,
        replicas: int = 1,
    ) -> Dict[str, Any]:
        """Create a Model API sourced from a registered model version."""
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

        body = ModelApiCreationRequest(
            name=name,
            description=description,
            environment_id=environment_id,
            replicas=replicas,
            strict_node_anti_affinity=False,
            is_async=False,
            environment_variables=[],
            version=ModelApiVersionCreationRequest(
                project_id=resolved_project_id,
                source=ModelApiSource(
                    type_=ModelApiSourceType.REGISTRY,
                    registered_model_name=registered_model_name,
                    registered_model_version=registered_model_version,
                ),
                log_http_request_response=False,
                monitoring_enabled=False,
                should_deploy=True,
            ),
        )

        try:
            response = create_model_api.sync_detailed(client=get_domino_public_api_client_sync(), body=body)
        except Exception as e:
            logger.error(f"Error creating Model API: {e}")
            return {"success": False, "error": str(e)}

        if response.parsed is None:
            # The generated client only parses 201; handle 200 as well since Domino
            # returns either status code for a successful creation.
            if response.status_code in (200, 201):
                return {"success": True, "data": {"id": json.loads(response.content).get("id")}}
            return {"success": False, "error": f"Model API creation failed with status {response.status_code}"}

        return {"success": True, "data": {"id": response.parsed.id}}

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

    async def get_status(self, model_api_id: str) -> Dict[str, Any]:
        # The generated public API client does not cover GET /models/{id}/activeStatus —
        # that endpoint lives under /models/ (not /api/modelServing/v1/) and returns
        # ModelApiVersionDeployment fields (status, isPending) that have no corresponding
        # generated endpoint. Raw request is intentional here.
        try:
            response = await domino_request("GET", f"/models/{model_api_id}/activeStatus")
            if not response.text:
                return {"success": True, "data": {}}
            try:
                result = response.json()
            except ValueError:
                logger.error(f"Domino API returned non-JSON response for activeStatus")
                return {"success": False, "error": "Domino API returned non-JSON response"}
            return {"success": True, "data": result}
        except httpx.HTTPStatusError as e:
            error_message = self._extract_error(e.response)
            logger.error(f"Domino API HTTP error fetching model API status: {error_message}")
            return {"success": False, "error": error_message, "status_code": e.response.status_code}
        except Exception as e:
            logger.error(f"Error fetching model API status: {e}")
            return {"success": False, "error": str(e)}


class DominoModelAPI:
    """Domino Model API client."""

    def __init__(self):
        self.model_apis = ModelAPIManager()

    def create_model_api_from_registry(
        self,
        name: str,
        registered_model_name: str,
        registered_model_version: int,
        description: str = "",
        project_id: Optional[str] = None,
        environment_id: Optional[str] = None,
        replicas: int = 1,
    ) -> Dict[str, Any]:
        return self.model_apis.create_model_api_from_registry(
            name, registered_model_name, registered_model_version,
            description, project_id, environment_id, replicas,
        )

    async def get_model_api_status(self, model_api_id: str) -> Dict[str, Any]:
        return await self.model_apis.get_status(model_api_id)


@lru_cache()
def get_domino_model_api() -> DominoModelAPI:
    return DominoModelAPI()
