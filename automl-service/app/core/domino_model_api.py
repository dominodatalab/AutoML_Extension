"""Domino Model API client for deploying, starting, and stopping model endpoints.

This module integrates with Domino's Model Serving API to manage model deployments.
API Reference: https://docs.dominodatalab.com/en/latest/api_guide/8c929e/rest-api-reference/
"""

import os
import logging
from functools import lru_cache
from typing import Any, Dict, List, Optional
from datetime import datetime
import httpx

from app.config import get_settings

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
                response = await token_client.get("http://localhost:8899/access-token")
            if response.status_code == 200 and response.text:
                return response.text.strip()
        except Exception as exc:
            logger.debug(f"Local token endpoint not available: {exc}")
        return None

    @staticmethod
    def _to_bearer_header(token: str) -> str:
        token = token.strip()
        if token.lower().startswith("bearer "):
            return token
        return f"Bearer {token}"

    async def _get_auth_headers(self) -> Dict[str, str]:
        """Build auth headers for each request.

        Domino app tokens are short-lived, so we re-acquire from localhost on every call.
        """
        api_key_override = os.environ.get("API_KEY_OVERRIDE")
        if api_key_override:
            return {"X-Domino-Api-Key": api_key_override}

        token = await self._get_ephemeral_token()
        if token:
            return {"Authorization": self._to_bearer_header(token)}

        api_key = (
            os.environ.get("DOMINO_API_KEY")
            or os.environ.get("DOMINO_USER_API_KEY")
            or self.settings.effective_api_key
        )
        if api_key:
            return {"X-Domino-Api-Key": api_key}

        raise ValueError(
            "No Domino credentials available. Configure API_KEY_OVERRIDE, "
            "local access token, or DOMINO_API_KEY/DOMINO_USER_API_KEY."
        )

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
        """Make an HTTP request to the Domino API."""
        try:
            client = await self._get_client()
            auth_headers = await self._get_auth_headers()
        except ValueError as e:
            logger.warning(f"Domino API not configured: {e}")
            return {"success": False, "data": [], "error": str(e)}

        try:
            request_headers: Dict[str, str] = {
                **auth_headers,
                "Accept": "application/json",
            }
            if json_data is not None:
                request_headers["Content-Type"] = "application/json"

            response = await client.request(
                method=method,
                url=path,
                params=params,
                json=json_data,
                headers=request_headers,
            )

            # Check if response is HTML (authentication error)
            content_type = response.headers.get("content-type", "")
            if "text/html" in content_type:
                error_message = self._extract_error(response)
                logger.error(f"Received HTML response from Domino API for {path}: {error_message}")
                return {
                    "success": False,
                    "data": [],
                    "error": error_message,
                    "status_code": response.status_code,
                }

            response.raise_for_status()

            # Parse response
            if method == "DELETE":
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
                    "status_code": response.status_code,
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


class ModelAPIManager:
    """Manages Model API resources (endpoint definitions)."""

    def __init__(self, client: DominoModelAPIClient):
        self.client = client

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
    ) -> Dict[str, Any]:
        """Create a new Model API.

        POST /api/modelServing/v1/modelApis
        """
        payload = {
            "name": name,
            "description": description,
            "projectId": project_id or self.client.settings.domino_project_id,
        }
        if owner_id:
            payload["ownerId"] = owner_id

        return await self.client._make_request("POST", "/api/modelServing/v1/modelApis", json_data=payload)

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
    ) -> Dict[str, Any]:
        """Create a new version of a Model API.

        POST /api/modelServing/v1/modelApis/{modelApiId}/versions
        """
        payload = {
            "modelFile": model_file,
            "function": function_name,
            "description": description,
        }
        if environment_id:
            payload["environmentId"] = environment_id

        return await self.client._make_request("POST", f"/api/modelServing/v1/modelApis/{model_api_id}/versions", json_data=payload)

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
        try:
            client = await self.client._get_client()
            response = await client.get(
                f"/api/modelServing/v1/modelApis/{model_api_id}/versions/{version_id}/buildLogs"
            )
            response.raise_for_status()
            return {"success": True, "logs": response.text}
        except Exception as e:
            logger.error(f"Error getting build logs: {e}")
            return {"success": False, "error": str(e)}


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
        try:
            client = await self.client._get_client()
            response = await client.get(
                f"/api/modelServing/v1/modelDeployments/{deployment_id}/logs/{log_suffix}"
            )
            response.raise_for_status()
            return {"success": True, "logs": response.text}
        except Exception as e:
            logger.error(f"Error getting deployment logs: {e}")
            return {"success": False, "error": str(e)}

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

    async def create_model_api(self, name: str, description: str = "", project_id: Optional[str] = None, owner_id: Optional[str] = None) -> Dict[str, Any]:
        """Create a new Model API."""
        return await self.model_apis.create_model_api(name, description, project_id, owner_id)

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

    async def create_model_api_version(self, model_api_id: str, model_file: str, function_name: str, environment_id: Optional[str] = None, description: str = "") -> Dict[str, Any]:
        """Create a new version of a Model API."""
        return await self.versions.create_model_api_version(model_api_id, model_file, function_name, environment_id, description)

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

    async def deploy_model(
        self,
        model_name: str,
        model_file: str,
        function_name: str,
        description: str = "",
        environment_id: Optional[str] = None,
        hardware_tier_id: Optional[str] = None,
        min_replicas: int = 1,
        max_replicas: int = 1,
        auto_start: bool = True,
    ) -> Dict[str, Any]:
        """High-level method to deploy a model end-to-end.

        This creates a Model API, version, and deployment in one call.
        """
        result = {
            "success": False,
            "model_api_id": None,
            "version_id": None,
            "deployment_id": None,
            "steps_completed": [],
        }

        try:
            # Step 1: Create Model API
            api_result = await self.create_model_api(
                name=model_name,
                description=description,
            )
            if not api_result["success"]:
                result["error"] = f"Failed to create Model API: {api_result.get('error')}"
                return result

            model_api_id = api_result["data"].get("id")
            result["model_api_id"] = model_api_id
            result["steps_completed"].append("create_model_api")

            # Step 2: Create Version
            version_result = await self.create_model_api_version(
                model_api_id=model_api_id,
                model_file=model_file,
                function_name=function_name,
                environment_id=environment_id,
                description=description,
            )
            if not version_result["success"]:
                result["error"] = f"Failed to create version: {version_result.get('error')}"
                return result

            version_id = version_result["data"].get("id")
            result["version_id"] = version_id
            result["steps_completed"].append("create_version")

            # Step 3: Create Deployment
            deploy_result = await self.create_deployment(
                model_api_id=model_api_id,
                model_api_version_id=version_id,
                name=f"{model_name}-deployment",
                description=description,
                environment_id=environment_id,
                hardware_tier_id=hardware_tier_id,
                min_replicas=min_replicas,
                max_replicas=max_replicas,
            )
            if not deploy_result["success"]:
                result["error"] = f"Failed to create deployment: {deploy_result.get('error')}"
                return result

            deployment_id = deploy_result["data"].get("id")
            result["deployment_id"] = deployment_id
            result["steps_completed"].append("create_deployment")

            # Step 4: Start deployment if requested
            if auto_start:
                start_result = await self.start_deployment(deployment_id)
                if start_result["success"]:
                    result["steps_completed"].append("start_deployment")

            result["success"] = True
            result["message"] = f"Model '{model_name}' deployed successfully"
            result["endpoint_url"] = deploy_result["data"].get("url")

        except Exception as e:
            logger.error(f"Error in deploy_model: {e}")
            result["error"] = str(e)

        return result


@lru_cache()
def get_domino_model_api() -> DominoModelAPI:
    """Get the Domino Model API singleton (cached)."""
    return DominoModelAPI()
