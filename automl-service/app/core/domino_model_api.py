"""Domino Model API client for deploying, starting, and stopping model endpoints.

This module integrates with Domino's Model Serving API to manage model deployments.
API Reference: https://docs.dominodatalab.com/en/latest/api_guide/8c929e/rest-api-reference/
"""

import asyncio
import os
import logging
from functools import lru_cache
from typing import Any, Dict, List, Optional
import httpx

from app.config import get_settings
from app.core.context.auth import get_request_auth_header

logger = logging.getLogger(__name__)


class DominoModelAPIClient:
    """Base client for Domino Model Serving API with HTTP request handling."""

    def __init__(self):
        self.settings = get_settings()
        self._client: Optional[httpx.AsyncClient] = None

    def _resolve_api_host(self) -> str:
        """Resolve Domino API host/proxy URL without hardcoded tenant fallbacks."""
        api_host = (
            os.environ.get("DOMINO_API_PROXY")
            or self.settings.domino_api_host
            or os.environ.get("DOMINO_API_HOST")
        )
        if not api_host:
            raise ValueError(
                "Domino API host is not configured. Set DOMINO_API_PROXY or DOMINO_API_HOST."
            )
        return api_host.rstrip("/")

    async def _get_ephemeral_token(self) -> Optional[str]:
        """Get a short-lived Domino access token for this request."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as token_client:
                # TODO this url must be dynamically resolved
                response = await token_client.get("http://localhost:8899/access-token")
            if response.status_code == 200 and response.text:
                return response.text.strip()
        except Exception as exc:
            logger.debug(f"Local token endpoint not available: {exc}")
        return None

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

    async def _get_client(self) -> httpx.AsyncClient:
        """Get HTTP client configured with Domino API base URL."""
        if self._client is None or self._client.is_closed:
            api_host = self._resolve_api_host()
            logger.info(f"Connecting to Domino API at {api_host}")
            self._client = httpx.AsyncClient(
                base_url=api_host,
                timeout=30.0
            )
        return self._client

    async def close(self):
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None

    async def _make_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make an HTTP request to the Domino API via domino_http.domino_request."""
        try:
            payload = json_data if method.upper() != "GET" else None
            response = await domino_request(method.upper(), path, json=payload)
            if method.upper() == "DELETE":
                return {"success": True, "message": f"Resource deleted successfully"}
            if not response.text:
                return {"success": True, "data": {}}
            try:
                result = response.json()
            except ValueError:
                error_message = "Domino API returned non-JSON response"
                logger.error(f"{error_message} for {path}")
                return {
                    "success": False,
                    "data": [],
                    "error": error_message,
                    "status_code": getattr(response, 'status_code', 500),
                }
            return {"success": True, "data": result}
        except httpx.HTTPStatusError as e:
            error_message = self._extract_error(e.response)
            logger.error(f"Domino API HTTP error for {path}: {error_message}")
            return {
                "success": False,
                "data": [],
                "error": error_message,
                "status_code": e.response.status_code,
            }
        except Exception as e:
            logger.error(f"Error making request to {path}: {e}")
            return {"success": False, "data": [], "error": str(e)}

    async def _make_text_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make an authenticated request when endpoint response is plain text."""
        try:
            response = await domino_request(method.upper(), path)
            return {"success": True, "text": response.text}
        except httpx.HTTPStatusError as e:
            error_message = self._extract_error(e.response)
            logger.error(f"Domino API HTTP error for {path}: {error_message}")
            return {
                "success": False,
                "error": error_message,
                "status_code": e.response.status_code,
            }
        except Exception as e:
            logger.error(f"Error making text request to {path}: {e}")
            return {"success": False, "error": str(e)}

    async def resolve_project_default_environment_id(self, project_id: str) -> Optional[str]:
        """Resolve project default environment id from Domino v4 project settings."""
        if not project_id:
            return None

        settings_paths = [
            f"/v4/projects/{project_id}/settings",
            f"/projects/{project_id}/settings",
        ]

        seen_paths = set()
        for path in settings_paths:
            if path in seen_paths:
                continue
            seen_paths.add(path)

            result = await self._make_request("GET", path)
            if not result.get("success"):
                continue

            data = result.get("data")
            if not isinstance(data, dict):
                continue

            environment_id = data.get("defaultEnvironmentId")
            if environment_id:
                logger.info(
                    "Resolved default environment id from Domino project settings "
                    f"for project {project_id}"
                )
                return str(environment_id)

        return None


class ModelAPIManager:
    """Manages Model API resources (endpoint definitions)."""

    def __init__(self, client: DominoModelAPIClient):
        self.client = client

    def _resolve_project_id(self, project_id: Optional[str]) -> Optional[str]:
        """Resolve project id from request args or Domino environment."""
        return project_id or self.client.settings.domino_project_id or os.environ.get("DOMINO_PROJECT_ID")

    async def _resolve_environment_id(
        self,
        environment_id: Optional[str],
        project_id: Optional[str],
    ) -> Optional[str]:
        """Resolve environment id for model API creation."""
        resolved = (
            environment_id
            or os.environ.get("DOMINO_MODEL_API_ENVIRONMENT_ID")
            or self.client.settings.domino_training_environment_id
            or os.environ.get("DOMINO_TRAINING_ENVIRONMENT_ID")
            or os.environ.get("DOMINO_ENVIRONMENT_ID")
            or self.client.settings.domino_eda_environment_id
            or os.environ.get("DOMINO_EDA_ENVIRONMENT_ID")
        )
        if resolved:
            return resolved

        if project_id:
            return await self.client.resolve_project_default_environment_id(project_id)
        return None

    @staticmethod
    def _is_validation_shape_error(error: str) -> bool:
        """Return true when Domino rejects request JSON shape/fields."""
        normalized = (error or "").lower()
        shape_markers = (
            "json validation error",
            "error.path.missing",
            "error.expected",
            "error.invalid",
        )
        return any(marker in normalized for marker in shape_markers)

    @staticmethod
    def _build_model_api_payload_variants(
        *,
        name: str,
        description: str,
        project_id: str,
        environment_id: str,
        owner_id: Optional[str],
        source_file: Optional[str],
        source_function: Optional[str],
        include_version: bool,
        should_deploy: bool,
        environment_variables: Optional[List[Dict[str, str]]],
    ) -> List[Dict[str, Any]]:
        """Build payload variants for Domino version compatibility."""
        normalized_environment_variables: List[Dict[str, str]] = []
        if environment_variables:
            for item in environment_variables:
                if not isinstance(item, dict):
                    continue
                key = item.get("key")
                value = item.get("value")
                if key is None or value is None:
                    continue
                normalized_environment_variables.append(
                    {
                        "key": str(key),
                        "value": str(value),
                    }
                )

        base_payload: Dict[str, Any] = {
            "name": name,
            "description": description,
            "environmentId": environment_id,
            "strictNodeAntiAffinity": False,
            "isAsync": False,
            "environmentVariables": normalized_environment_variables,
        }
        if owner_id:
            base_payload["ownerId"] = owner_id

        if not include_version:
            return [base_payload]

        source_file_candidates: List[str] = []
        if source_file:
            source_file_candidates.append(source_file)
            source_basename = os.path.basename(source_file)
            source_has_directory = bool(os.path.dirname(source_file))
            if (
                source_basename
                and source_basename not in source_file_candidates
                and not source_has_directory
            ):
                source_file_candidates.append(source_basename)
        else:
            source_file_candidates.append("model.py")

        resolved_function = source_function or "predict"

        variants: List[Dict[str, Any]] = []
        for file_candidate in source_file_candidates:
            for include_version_environment in (True, False):
                version_payload: Dict[str, Any] = {
                    "projectId": project_id,
                    "source": {
                        "type": "File",
                        "file": file_candidate,
                        "function": resolved_function,
                        "excludeFiles": [],
                    },
                    "logHttpRequestResponse": False,
                    "monitoringEnabled": False,
                    "description": description,
                    "recordInvocation": False,
                    "shouldDeploy": should_deploy,
                }
                if include_version_environment:
                    version_payload["environmentId"] = environment_id

                payload = dict(base_payload)
                payload["version"] = version_payload
                variants.append(payload)
        return variants

    # ========== Model APIs (Endpoint Definitions) ==========

    async def list_model_apis(self, project_id: Optional[str] = None) -> Dict[str, Any]:
        """List all Model APIs.

        GET /api/modelServing/v1/modelApis
        """
        params = {}
        if project_id:
            params["projectId"] = project_id
        elif self.client.settings.domino_project_id:
            params["projectId"] = self.client.settings.domino_project_id

        result = await self.client._make_request("GET", "/api/modelServing/v1/modelApis", params=params)

        # Extract items from Domino API response format
        if result.get("success") and "data" in result:
            data = result["data"]
            if isinstance(data, dict) and "items" in data:
                result["data"] = data.get("items", [])

        return result

    async def create_model_api(
        self,
        name: str,
        description: str = "",
        project_id: Optional[str] = None,
        owner_id: Optional[str] = None,
        environment_id: Optional[str] = None,
        source_file: Optional[str] = None,
        source_function: Optional[str] = None,
        include_version: bool = True,
        should_deploy: bool = False,
        environment_variables: Optional[List[Dict[str, str]]] = None,
    ) -> Dict[str, Any]:
        """Create a new Model API.

        POST /api/modelServing/v1/modelApis
        """
        resolved_project_id = self._resolve_project_id(project_id)
        if not resolved_project_id:
            return {
                "success": False,
                "data": [],
                "error": (
                    "Missing project id for Model API creation. "
                    "Set DOMINO_PROJECT_ID or provide project_id."
                ),
            }

        resolved_environment_id = await self._resolve_environment_id(
            environment_id=environment_id,
            project_id=resolved_project_id,
        )
        if not resolved_environment_id:
            return {
                "success": False,
                "data": [],
                "error": (
                    "Missing environment id for Model API creation. "
                    "Could not resolve project default environment from Domino settings. "
                    "Set DOMINO_MODEL_API_ENVIRONMENT_ID, DOMINO_TRAINING_ENVIRONMENT_ID, "
                    "or DOMINO_ENVIRONMENT_ID."
                ),
            }

        payload_variants = self._build_model_api_payload_variants(
            name=name,
            description=description,
            project_id=resolved_project_id,
            environment_id=resolved_environment_id,
            owner_id=owner_id,
            source_file=source_file,
            source_function=source_function,
            include_version=include_version,
            should_deploy=should_deploy,
            environment_variables=environment_variables,
        )

        last_error: Optional[str] = None
        for index, payload in enumerate(payload_variants):
            result = await self.client._make_request(
                "POST",
                "/api/modelServing/v1/modelApis",
                json_data=payload,
            )
            if result.get("success"):
                return result

            last_error = str(result.get("error") or "")
            if not self._is_validation_shape_error(last_error):
                return result

            logger.warning(
                "Model API create payload variant %s/%s rejected by Domino validation: %s",
                index + 1,
                len(payload_variants),
                last_error,
            )

        return {
            "success": False,
            "data": [],
            "error": (
                "Failed to create Model API after trying compatibility payload variants. "
                f"Last error: {last_error or 'Unknown error'}"
            ),
        }

    async def get_model_api(self, model_api_id: str) -> Dict[str, Any]:
        """Get a specific Model API.

        GET /api/modelServing/v1/modelApis/{modelApiId}
        """
        return await self.client._make_request("GET", f"/api/modelServing/v1/modelApis/{model_api_id}")

    async def update_model_api(
        self,
        model_api_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Update a Model API.

        PUT /api/modelServing/v1/modelApis/{modelApiId}
        """
        payload = {}
        if name:
            payload["name"] = name
        if description is not None:
            payload["description"] = description

        return await self.client._make_request("PUT", f"/api/modelServing/v1/modelApis/{model_api_id}", json_data=payload)

    async def delete_model_api(self, model_api_id: str) -> Dict[str, Any]:
        """Delete a Model API.

        DELETE /api/modelServing/v1/modelApis/{modelApiId}
        """
        result = await self.client._make_request("DELETE", f"/api/modelServing/v1/modelApis/{model_api_id}")
        if result.get("success"):
            result["message"] = f"Model API {model_api_id} deleted"
        return result


class ModelVersionManager:
    """Manages Model API Version resources."""

    def __init__(self, client: DominoModelAPIClient):
        self.client = client

    def _resolve_project_id(self) -> Optional[str]:
        """Resolve project id from settings/environment."""
        return self.client.settings.domino_project_id or os.environ.get("DOMINO_PROJECT_ID")

    @staticmethod
    def _is_validation_shape_error(error: str) -> bool:
        normalized = (error or "").lower()
        return any(
            marker in normalized
            for marker in (
                "json validation error",
                "error.path.missing",
                "error.expected",
                "error.invalid",
            )
        )

    # ========== Model API Versions ==========

    async def list_model_api_versions(self, model_api_id: str) -> Dict[str, Any]:
        """List all versions of a Model API.

        GET /api/modelServing/v1/modelApis/{modelApiId}/versions
        """
        return await self.client._make_request("GET", f"/api/modelServing/v1/modelApis/{model_api_id}/versions")

    async def create_model_api_version(
        self,
        model_api_id: str,
        model_file: str,
        function_name: str,
        environment_id: Optional[str] = None,
        description: str = "",
        should_deploy: bool = False,
    ) -> Dict[str, Any]:
        """Create a new version of a Model API.

        POST /api/modelServing/v1/modelApis/{modelApiId}/versions
        """
        project_id = self._resolve_project_id()
        if not project_id:
            return {
                "success": False,
                "data": [],
                "error": (
                    "Missing project id for Model API version creation. "
                    "Set DOMINO_PROJECT_ID."
                ),
            }

        resolved_function = function_name or "predict"
        file_candidates = [model_file]
        model_file_basename = os.path.basename(model_file)
        model_file_has_directory = bool(os.path.dirname(model_file))
        if (
            model_file_basename
            and model_file_basename not in file_candidates
            and not model_file_has_directory
        ):
            file_candidates.append(model_file_basename)

        payload_variants: List[Dict[str, Any]] = []
        for file_candidate in file_candidates:
            for include_environment in (True, False):
                payload: Dict[str, Any] = {
                    "projectId": project_id,
                    "source": {
                        "type": "File",
                        "file": file_candidate,
                        "function": resolved_function,
                        "excludeFiles": [],
                    },
                    "logHttpRequestResponse": False,
                    "monitoringEnabled": False,
                    "description": description,
                    "recordInvocation": False,
                    "shouldDeploy": should_deploy,
                }
                if include_environment and environment_id:
                    payload["environmentId"] = environment_id
                payload_variants.append(payload)

        last_error: Optional[str] = None
        for index, payload in enumerate(payload_variants):
            result = await self.client._make_request(
                "POST",
                f"/api/modelServing/v1/modelApis/{model_api_id}/versions",
                json_data=payload,
            )
            if result.get("success"):
                return result

            last_error = str(result.get("error") or "")
            if not self._is_validation_shape_error(last_error):
                return result

            logger.warning(
                "Model API version payload variant %s/%s rejected by Domino validation: %s",
                index + 1,
                len(payload_variants),
                last_error,
            )

        return {
            "success": False,
            "data": [],
            "error": (
                "Failed to create Model API version after trying compatibility payload variants. "
                f"Last error: {last_error or 'Unknown error'}"
            ),
        }

    async def get_model_api_version(
        self,
        model_api_id: str,
        version_id: str
    ) -> Dict[str, Any]:
        """Get a specific version of a Model API.

        GET /api/modelServing/v1/modelApis/{modelApiId}/versions/{modelApiVersionId}
        """
        return await self.client._make_request("GET", f"/api/modelServing/v1/modelApis/{model_api_id}/versions/{version_id}")

    async def get_version_build_logs(
        self,
        model_api_id: str,
        version_id: str
    ) -> Dict[str, Any]:
        """Get build logs for a Model API version.

        GET /api/modelServing/v1/modelApis/{modelApiId}/versions/{versionId}/buildLogs
        """
        result = await self.client._make_text_request(
            "GET",
            f"/api/modelServing/v1/modelApis/{model_api_id}/versions/{version_id}/buildLogs",
        )
        if not result.get("success"):
            return result
        return {"success": True, "logs": result.get("text", "")}


class ModelDeploymentManager:
    """Manages Model Deployment resources."""

    def __init__(self, client: DominoModelAPIClient):
        self.client = client

    # ========== Model Deployments ==========

    async def list_deployments(
        self,
        project_id: Optional[str] = None,
        model_api_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """List all Model Deployments.

        GET /api/modelServing/v1/modelDeployments
        """
        params = {}
        if project_id:
            params["projectId"] = project_id
        elif self.client.settings.domino_project_id:
            params["projectId"] = self.client.settings.domino_project_id
        if model_api_id:
            params["modelApiId"] = model_api_id

        result = await self.client._make_request("GET", "/api/modelServing/v1/modelDeployments", params=params)

        # Extract items from Domino API response format
        if result.get("success") and "data" in result:
            data = result["data"]
            if isinstance(data, dict) and "items" in data:
                result["data"] = data.get("items", [])

        return result

    async def create_deployment(
        self,
        model_api_id: str,
        model_api_version_id: str,
        name: Optional[str] = None,
        description: str = "",
        environment_id: Optional[str] = None,
        hardware_tier_id: Optional[str] = None,
        min_replicas: int = 1,
        max_replicas: int = 1,
    ) -> Dict[str, Any]:
        """Create a new Model Deployment.

        POST /api/modelServing/v1/modelDeployments
        """
        payload = {
            "modelApiId": model_api_id,
            "modelApiVersionId": model_api_version_id,
            "minReplicas": min_replicas,
            "maxReplicas": max_replicas,
        }
        if name:
            payload["name"] = name
        if description:
            payload["description"] = description
        if environment_id:
            payload["environmentId"] = environment_id
        if hardware_tier_id:
            payload["hardwareTierId"] = hardware_tier_id

        return await self.client._make_request("POST", "/api/modelServing/v1/modelDeployments", json_data=payload)

    async def get_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Get a specific Model Deployment.

        GET /api/modelServing/v1/modelDeployments/{modelDeploymentId}
        """
        return await self.client._make_request("GET", f"/api/modelServing/v1/modelDeployments/{deployment_id}")

    async def update_deployment(
        self,
        deployment_id: str,
        min_replicas: Optional[int] = None,
        max_replicas: Optional[int] = None,
        model_api_version_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Update a Model Deployment.

        PATCH /api/modelServing/v1/modelDeployments/{modelDeploymentId}
        """
        payload = {}
        if min_replicas is not None:
            payload["minReplicas"] = min_replicas
        if max_replicas is not None:
            payload["maxReplicas"] = max_replicas
        if model_api_version_id:
            payload["modelApiVersionId"] = model_api_version_id

        return await self.client._make_request("PATCH", f"/api/modelServing/v1/modelDeployments/{deployment_id}", json_data=payload)

    async def delete_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Delete a Model Deployment.

        DELETE /api/modelServing/v1/modelDeployments/{modelDeploymentId}
        """
        result = await self.client._make_request("DELETE", f"/api/modelServing/v1/modelDeployments/{deployment_id}")
        if result.get("success"):
            result["message"] = f"Deployment {deployment_id} deleted"
        return result

    async def start_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Start a stopped Model Deployment.

        POST /api/modelServing/v1/modelDeployments/{modelDeploymentId}/start
        """
        result = await self.client._make_request("POST", f"/api/modelServing/v1/modelDeployments/{deployment_id}/start")
        if result.get("success"):
            result.update({
                "deployment_id": deployment_id,
                "status": "starting",
                "message": "Deployment start initiated"
            })
        return result

    async def stop_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Stop a running Model Deployment.

        POST /api/modelServing/v1/modelDeployments/{modelDeploymentId}/stop
        """
        result = await self.client._make_request("POST", f"/api/modelServing/v1/modelDeployments/{deployment_id}/stop")
        if result.get("success"):
            result.update({
                "deployment_id": deployment_id,
                "status": "stopping",
                "message": "Deployment stop initiated"
            })
        return result

    async def get_deployment_logs(
        self,
        deployment_id: str,
        log_suffix: str = "stdout"
    ) -> Dict[str, Any]:
        """Get logs for a Model Deployment.

        GET /api/modelServing/v1/modelDeployments/{modelDeploymentId}/logs/{logSuffix}

        logSuffix can be 'stdout', 'stderr', etc.
        """
        result = await self.client._make_text_request(
            "GET",
            f"/api/modelServing/v1/modelDeployments/{deployment_id}/logs/{log_suffix}",
        )
        if not result.get("success"):
            return result
        return {"success": True, "logs": result.get("text", "")}

    async def get_deployment_versions(self, deployment_id: str) -> Dict[str, Any]:
        """Get all versions of a Model Deployment.

        GET /api/modelServing/v1/modelDeployments/{modelDeploymentId}/versions
        """
        return await self.client._make_request("GET", f"/api/modelServing/v1/modelDeployments/{deployment_id}/versions")

    async def get_deployment_credentials(
        self,
        deployment_id: str,
        operation_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get temporary credentials for a Model Deployment.

        GET /api/modelServing/v1/modelDeployments/{modelDeploymentId}/credentials
        GET /api/modelServing/v1/modelDeployments/{modelDeploymentId}/credentials/{operationType}
        """
        if operation_type:
            url = f"/api/modelServing/v1/modelDeployments/{deployment_id}/credentials/{operation_type}"
        else:
            url = f"/api/modelServing/v1/modelDeployments/{deployment_id}/credentials"

        return await self.client._make_request("GET", url)

    async def get_deployment_status(self, deployment_id: str) -> Dict[str, Any]:
        """Get the current status of a deployment."""
        result = await self.get_deployment(deployment_id)
        if result["success"]:
            data = result["data"]
            return {
                "success": True,
                "deployment_id": deployment_id,
                "status": data.get("status"),
                "replicas": {
                    "min": data.get("minReplicas"),
                    "max": data.get("maxReplicas"),
                    "current": data.get("currentReplicas"),
                },
                "url": data.get("url"),
                "created_at": data.get("createdAt"),
                "updated_at": data.get("updatedAt"),
            }
        return result


class DominoModelAPI:
    """Main Domino Model API client that delegates to specialized managers.

    Provides methods to:
    - List, create, and manage Model APIs (endpoint definitions)
    - List, create, and manage Model API Versions
    - Manage Model Deployments (start, stop, scale)
    - Access deployment logs and credentials
    """

    def __init__(self):
        self._client = DominoModelAPIClient()
        self.model_apis = ModelAPIManager(self._client)
        self.versions = ModelVersionManager(self._client)
        self.deployments = ModelDeploymentManager(self._client)

    async def close(self):
        """Close the HTTP client."""
        await self._client.close()

    # Convenience methods that delegate to managers
    async def list_model_apis(self, project_id: Optional[str] = None) -> Dict[str, Any]:
        """List all Model APIs."""
        return await self.model_apis.list_model_apis(project_id)

    async def create_model_api(
        self,
        name: str,
        description: str = "",
        project_id: Optional[str] = None,
        owner_id: Optional[str] = None,
        environment_id: Optional[str] = None,
        source_file: Optional[str] = None,
        source_function: Optional[str] = None,
        include_version: bool = True,
        should_deploy: bool = False,
        environment_variables: Optional[List[Dict[str, str]]] = None,
    ) -> Dict[str, Any]:
        """Create a new Model API."""
        return await self.model_apis.create_model_api(
            name,
            description,
            project_id,
            owner_id,
            environment_id,
            source_file,
            source_function,
            include_version,
            should_deploy,
            environment_variables,
        )

    async def get_model_api(self, model_api_id: str) -> Dict[str, Any]:
        """Get a specific Model API."""
        return await self.model_apis.get_model_api(model_api_id)

    async def update_model_api(self, model_api_id: str, name: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
        """Update a Model API."""
        return await self.model_apis.update_model_api(model_api_id, name, description)

    async def delete_model_api(self, model_api_id: str) -> Dict[str, Any]:
        """Delete a Model API."""
        return await self.model_apis.delete_model_api(model_api_id)

    async def list_model_api_versions(self, model_api_id: str) -> Dict[str, Any]:
        """List all versions of a Model API."""
        return await self.versions.list_model_api_versions(model_api_id)

    async def create_model_api_version(
        self,
        model_api_id: str,
        model_file: str,
        function_name: str,
        environment_id: Optional[str] = None,
        description: str = "",
        should_deploy: bool = False,
    ) -> Dict[str, Any]:
        """Create a new version of a Model API."""
        return await self.versions.create_model_api_version(
            model_api_id,
            model_file,
            function_name,
            environment_id,
            description,
            should_deploy,
        )

    async def get_model_api_version(self, model_api_id: str, version_id: str) -> Dict[str, Any]:
        """Get a specific version of a Model API."""
        return await self.versions.get_model_api_version(model_api_id, version_id)

    async def get_version_build_logs(self, model_api_id: str, version_id: str) -> Dict[str, Any]:
        """Get build logs for a Model API version."""
        return await self.versions.get_version_build_logs(model_api_id, version_id)

    async def list_deployments(self, project_id: Optional[str] = None, model_api_id: Optional[str] = None) -> Dict[str, Any]:
        """List all Model Deployments."""
        return await self.deployments.list_deployments(project_id, model_api_id)

    async def create_deployment(self, model_api_id: str, model_api_version_id: str, name: Optional[str] = None, description: str = "", environment_id: Optional[str] = None, hardware_tier_id: Optional[str] = None, min_replicas: int = 1, max_replicas: int = 1) -> Dict[str, Any]:
        """Create a new Model Deployment."""
        return await self.deployments.create_deployment(model_api_id, model_api_version_id, name, description, environment_id, hardware_tier_id, min_replicas, max_replicas)

    async def get_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Get a specific Model Deployment."""
        return await self.deployments.get_deployment(deployment_id)

    async def update_deployment(self, deployment_id: str, min_replicas: Optional[int] = None, max_replicas: Optional[int] = None, model_api_version_id: Optional[str] = None) -> Dict[str, Any]:
        """Update a Model Deployment."""
        return await self.deployments.update_deployment(deployment_id, min_replicas, max_replicas, model_api_version_id)

    async def delete_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Delete a Model Deployment."""
        return await self.deployments.delete_deployment(deployment_id)

    async def start_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Start a stopped Model Deployment."""
        return await self.deployments.start_deployment(deployment_id)

    async def stop_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Stop a running Model Deployment."""
        return await self.deployments.stop_deployment(deployment_id)

    async def get_deployment_logs(self, deployment_id: str, log_suffix: str = "stdout") -> Dict[str, Any]:
        """Get logs for a Model Deployment."""
        return await self.deployments.get_deployment_logs(deployment_id, log_suffix)

    async def get_deployment_versions(self, deployment_id: str) -> Dict[str, Any]:
        """Get all versions of a Model Deployment."""
        return await self.deployments.get_deployment_versions(deployment_id)

    async def get_deployment_credentials(self, deployment_id: str, operation_type: Optional[str] = None) -> Dict[str, Any]:
        """Get temporary credentials for a Model Deployment."""
        return await self.deployments.get_deployment_credentials(deployment_id, operation_type)

    async def get_deployment_status(self, deployment_id: str) -> Dict[str, Any]:
        """Get the current status of a deployment."""
        return await self.deployments.get_deployment_status(deployment_id)

    # ========== Helper Methods ==========

    @staticmethod
    def _extract_version_id_from_create_payload(payload: Any) -> Optional[str]:
        """Extract a model API version id from create-model-api response payloads."""
        if not isinstance(payload, dict):
            return None

        direct_keys = (
            "modelApiVersionId",
            "versionId",
            "latestVersionId",
            "latestModelApiVersionId",
        )
        for key in direct_keys:
            value = payload.get(key)
            if value:
                return str(value)

        nested_keys = ("version", "latestVersion", "modelApiVersion")
        for key in nested_keys:
            nested = payload.get(key)
            if isinstance(nested, dict):
                nested_id = nested.get("id")
                if nested_id:
                    return str(nested_id)

        versions = payload.get("versions")
        if isinstance(versions, list):
            for version in versions:
                if isinstance(version, dict):
                    version_id = version.get("id")
                    if version_id:
                        return str(version_id)

        return None

    @staticmethod
    def _extract_version_id_from_versions_payload(payload: Any) -> Optional[str]:
        """Extract latest version id from list-model-api-versions payloads."""
        versions: List[Dict[str, Any]] = []

        if isinstance(payload, list):
            versions = [item for item in payload if isinstance(item, dict)]
        elif isinstance(payload, dict):
            if isinstance(payload.get("items"), list):
                versions = [item for item in payload["items"] if isinstance(item, dict)]
            elif isinstance(payload.get("versions"), list):
                versions = [item for item in payload["versions"] if isinstance(item, dict)]

        if not versions:
            return None

        versions.sort(
            key=lambda item: str(
                item.get("createdAt")
                or item.get("updatedAt")
                or item.get("created")
                or item.get("updated")
                or ""
            ),
            reverse=True,
        )

        for version in versions:
            version_id = version.get("id") or version.get("modelApiVersionId") or version.get("versionId")
            if version_id:
                return str(version_id)

        return None

    @staticmethod
    def _extract_endpoint_url(payload: Any) -> Optional[str]:
        """Extract endpoint URL from Domino deployment/model API payloads."""
        if not isinstance(payload, dict):
            return None

        for key in ("url", "endpointUrl", "endpointURL"):
            value = payload.get(key)
            if value:
                return str(value)

        for key in ("deployment", "modelDeployment"):
            nested = payload.get(key)
            if isinstance(nested, dict):
                nested_url = DominoModelAPI._extract_endpoint_url(nested)
                if nested_url:
                    return nested_url

        return None

    async def _wait_for_created_version_id(
        self,
        model_api_id: str,
        initial_payload: Optional[Dict[str, Any]] = None,
        attempts: int = 6,
        delay_seconds: float = 1.0,
    ) -> Optional[str]:
        """Resolve version id created as part of model API creation."""
        if initial_payload:
            version_id = self._extract_version_id_from_create_payload(initial_payload)
            if version_id:
                return version_id

        for attempt in range(attempts):
            list_result = await self.list_model_api_versions(model_api_id)
            if list_result.get("success"):
                version_id = self._extract_version_id_from_versions_payload(list_result.get("data"))
                if version_id:
                    return version_id

            if attempt < attempts - 1:
                await asyncio.sleep(delay_seconds)

        return None

    async def deploy_model(
        self,
        model_name: str,
        model_file: str,
        function_name: str,
        model_artifact_dir: Optional[str] = None,
        description: str = "",
        environment_id: Optional[str] = None,
        hardware_tier_id: Optional[str] = None,
        min_replicas: int = 1,
        max_replicas: int = 1,
        auto_start: bool = True,
        project_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """High-level method to deploy a model end-to-end.

        This creates a Model API and exactly one version, then optionally deploys it.
        """
        result = {
            "success": False,
            "model_api_id": None,
            "version_id": None,
            "deployment_id": None,
            "steps_completed": [],
        }

        try:
            environment_variables: List[Dict[str, str]] = []
            if model_artifact_dir:
                environment_variables.append(
                    {
                        "key": "AUTOML_MODEL_DIR",
                        "value": str(model_artifact_dir),
                    }
                )

            # Step 1: Create Model API
            api_result = await self.create_model_api(
                name=model_name,
                description=description,
                project_id=project_id,
                environment_id=environment_id,
                source_file=model_file,
                source_function=function_name,
                include_version=True,
                should_deploy=auto_start,
                environment_variables=environment_variables,
            )
            if not api_result["success"]:
                result["error"] = f"Failed to create Model API: {api_result.get('error')}"
                return result

            api_data = api_result.get("data")
            if not isinstance(api_data, dict):
                result["error"] = "Failed to create Model API: invalid response payload"
                return result

            model_api_id = api_data.get("id")
            if not model_api_id:
                result["error"] = "Failed to create Model API: missing model API id in response"
                return result

            result["model_api_id"] = model_api_id
            result["steps_completed"].append("create_model_api")

            # Step 2: Resolve version created along with the model API.
            version_id = await self._wait_for_created_version_id(
                model_api_id=str(model_api_id),
                initial_payload=api_data,
            )
            if not version_id:
                result["error"] = (
                    "Model API was created but version id could not be resolved. "
                    "No extra version was created to avoid duplicate publishes."
                )
                return result

            result["version_id"] = version_id
            result["steps_completed"].append("create_version")

            # Step 3: Deployment is requested as part of version creation.
            if auto_start:
                result["steps_completed"].append("deploy_version")

            active_version = api_data.get("activeVersion")
            if isinstance(active_version, dict):
                deployment_info = active_version.get("deployment")
                if isinstance(deployment_info, dict):
                    deployment_status = deployment_info.get("status")
                    if deployment_status:
                        result["deployment_status"] = deployment_status

            result["success"] = True
            result["message"] = (
                f"Model '{model_name}' deployment requested successfully"
                if auto_start
                else f"Model '{model_name}' version created successfully"
            )
            result["endpoint_url"] = (
                self._extract_endpoint_url(api_data)
            )

        except Exception as e:
            logger.error(f"Error in deploy_model: {e}")
            result["error"] = str(e)

        return result


@lru_cache()
def get_domino_model_api() -> DominoModelAPI:
    """Get the Domino Model API singleton (cached)."""
    return DominoModelAPI()
