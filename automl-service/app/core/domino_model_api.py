"""Domino Model API client for deploying, starting, and stopping model endpoints.

This module integrates with Domino's Model Serving API to manage model deployments.
API Reference: https://docs.dominodatalab.com/en/latest/api_guide/8c929e/rest-api-reference/
"""

import os
import logging
from typing import Any, Dict, List, Optional
from datetime import datetime
import httpx

from app.config import get_settings

logger = logging.getLogger(__name__)


class DominoModelAPI:
    """Client for Domino Model Serving API.

    Provides methods to:
    - List, create, and manage Model APIs (endpoint definitions)
    - List, create, and manage Model API Versions
    - Manage Model Deployments (start, stop, scale)
    - Access deployment logs and credentials
    """

    def __init__(self):
        self.settings = get_settings()
        self._client: Optional[httpx.AsyncClient] = None
        self._token: Optional[str] = None

    def _get_token_sync(self) -> str:
        """Get authentication token for Domino API (synchronous)."""
        if self._token:
            return self._token

        # Try local token endpoint first (works in Domino Apps) - this is the preferred method
        try:
            import requests
            response = requests.get("http://localhost:8899/access-token", timeout=5)
            if response.status_code == 200 and response.text:
                self._token = response.text.strip()
                logger.info("Got token from local endpoint")
                return self._token
        except Exception as e:
            logger.debug(f"Local token endpoint not available: {e}")

        # Get API key from environment variables (DOMINO_API_KEY is primary)
        token = (
            os.environ.get("DOMINO_API_KEY") or
            os.environ.get("DOMINO_USER_API_KEY") or
            self.settings.effective_api_key
        )

        # Try reading from token file
        if not token:
            token_file = os.environ.get("DOMINO_TOKEN_FILE")
            if token_file and os.path.exists(token_file):
                with open(token_file, 'r') as f:
                    token = f.read().strip()

        if token:
            self._token = token
            logger.info("Using token from environment variable")
            return self._token

        raise ValueError("No Domino API token available")

    async def _get_token(self) -> str:
        """Get authentication token for Domino API (async wrapper)."""
        return self._get_token_sync()

    async def _get_client(self) -> httpx.AsyncClient:
        """Get HTTP client with authentication headers."""
        if self._client is None:
            # Get API key from environment
            api_key = os.environ.get("DOMINO_API_KEY", "")
            if not api_key:
                raise ValueError("DOMINO_API_KEY environment variable not set")

            # Use the external Domino API host
            # The internal host (nucleus-frontend) doesn't work for Model Serving API
            api_host = os.environ.get("DOMINO_API_PROXY", "https://se-demo.domino.tech")

            logger.info(f"Connecting to Domino API at {api_host}")

            # Use X-Domino-Api-Key header (not Bearer token)
            self._client = httpx.AsyncClient(
                base_url=api_host,
                headers={
                    "X-Domino-Api-Key": api_key,
                    "Content-Type": "application/json",
                },
                timeout=30.0
            )
        return self._client

    async def close(self):
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None

    # ========== Model APIs (Endpoint Definitions) ==========

    async def list_model_apis(self, project_id: Optional[str] = None) -> Dict[str, Any]:
        """List all Model APIs.

        GET /api/modelServing/v1/modelApis
        """
        try:
            client = await self._get_client()
        except ValueError as e:
            # Domino API not configured - return empty list gracefully
            logger.warning(f"Domino API not configured: {e}")
            return {"success": True, "data": [], "warning": str(e)}

        params = {}
        if project_id:
            params["projectId"] = project_id
        elif self.settings.domino_project_id:
            params["projectId"] = self.settings.domino_project_id

        try:
            response = await client.get("/api/modelServing/v1/modelApis", params=params)
            response.raise_for_status()

            # Check if response is HTML (authentication error)
            content_type = response.headers.get("content-type", "")
            if "text/html" in content_type:
                logger.error("Received HTML response - likely authentication issue")
                return {"success": True, "data": [], "warning": "Authentication required for Domino API"}

            # Domino API returns {"items": [...], "metadata": {...}}
            result = response.json()
            items = result.get("items", []) if isinstance(result, dict) else result
            return {"success": True, "data": items}
        except Exception as e:
            logger.error(f"Error listing model APIs: {e}")
            return {"success": True, "data": [], "error": str(e)}

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
        client = await self._get_client()

        payload = {
            "name": name,
            "description": description,
            "projectId": project_id or self.settings.domino_project_id,
        }
        if owner_id:
            payload["ownerId"] = owner_id

        try:
            response = await client.post("/api/modelServing/v1/modelApis", json=payload)
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error creating model API: {e}")
            return {"success": False, "error": str(e)}

    async def get_model_api(self, model_api_id: str) -> Dict[str, Any]:
        """Get a specific Model API.

        GET /api/modelServing/v1/modelApis/{modelApiId}
        """
        client = await self._get_client()

        try:
            response = await client.get(f"/api/modelServing/v1/modelApis/{model_api_id}")
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error getting model API: {e}")
            return {"success": False, "error": str(e)}

    async def update_model_api(
        self,
        model_api_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Update a Model API.

        PUT /api/modelServing/v1/modelApis/{modelApiId}
        """
        client = await self._get_client()

        payload = {}
        if name:
            payload["name"] = name
        if description is not None:
            payload["description"] = description

        try:
            response = await client.put(
                f"/api/modelServing/v1/modelApis/{model_api_id}",
                json=payload
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error updating model API: {e}")
            return {"success": False, "error": str(e)}

    async def delete_model_api(self, model_api_id: str) -> Dict[str, Any]:
        """Delete a Model API.

        DELETE /api/modelServing/v1/modelApis/{modelApiId}
        """
        client = await self._get_client()

        try:
            response = await client.delete(f"/api/modelServing/v1/modelApis/{model_api_id}")
            response.raise_for_status()
            return {"success": True, "message": f"Model API {model_api_id} deleted"}
        except Exception as e:
            logger.error(f"Error deleting model API: {e}")
            return {"success": False, "error": str(e)}

    # ========== Model API Versions ==========

    async def list_model_api_versions(self, model_api_id: str) -> Dict[str, Any]:
        """List all versions of a Model API.

        GET /api/modelServing/v1/modelApis/{modelApiId}/versions
        """
        client = await self._get_client()

        try:
            response = await client.get(
                f"/api/modelServing/v1/modelApis/{model_api_id}/versions"
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error listing model API versions: {e}")
            return {"success": False, "error": str(e)}

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
        client = await self._get_client()

        payload = {
            "modelFile": model_file,
            "function": function_name,
            "description": description,
        }
        if environment_id:
            payload["environmentId"] = environment_id

        try:
            response = await client.post(
                f"/api/modelServing/v1/modelApis/{model_api_id}/versions",
                json=payload
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error creating model API version: {e}")
            return {"success": False, "error": str(e)}

    async def get_model_api_version(
        self,
        model_api_id: str,
        version_id: str
    ) -> Dict[str, Any]:
        """Get a specific version of a Model API.

        GET /api/modelServing/v1/modelApis/{modelApiId}/versions/{modelApiVersionId}
        """
        client = await self._get_client()

        try:
            response = await client.get(
                f"/api/modelServing/v1/modelApis/{model_api_id}/versions/{version_id}"
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error getting model API version: {e}")
            return {"success": False, "error": str(e)}

    async def get_version_build_logs(
        self,
        model_api_id: str,
        version_id: str
    ) -> Dict[str, Any]:
        """Get build logs for a Model API version.

        GET /api/modelServing/v1/modelApis/{modelApiId}/versions/{versionId}/buildLogs
        """
        client = await self._get_client()

        try:
            response = await client.get(
                f"/api/modelServing/v1/modelApis/{model_api_id}/versions/{version_id}/buildLogs"
            )
            response.raise_for_status()
            return {"success": True, "logs": response.text}
        except Exception as e:
            logger.error(f"Error getting build logs: {e}")
            return {"success": False, "error": str(e)}

    # ========== Model Deployments ==========

    async def list_deployments(
        self,
        project_id: Optional[str] = None,
        model_api_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """List all Model Deployments.

        GET /api/modelServing/v1/modelDeployments
        """
        try:
            client = await self._get_client()
        except ValueError as e:
            # Domino API not configured - return empty list gracefully
            logger.warning(f"Domino API not configured: {e}")
            return {"success": True, "data": [], "warning": str(e)}

        params = {}
        if project_id:
            params["projectId"] = project_id
        elif self.settings.domino_project_id:
            params["projectId"] = self.settings.domino_project_id
        if model_api_id:
            params["modelApiId"] = model_api_id

        try:
            response = await client.get(
                "/api/modelServing/v1/modelDeployments",
                params=params
            )
            response.raise_for_status()

            # Check if response is HTML (authentication error)
            content_type = response.headers.get("content-type", "")
            if "text/html" in content_type:
                logger.error("Received HTML response - likely authentication issue")
                return {"success": True, "data": [], "warning": "Authentication required for Domino API"}

            # Domino API returns {"items": [...], "metadata": {...}}
            result = response.json()
            items = result.get("items", []) if isinstance(result, dict) else result
            return {"success": True, "data": items}
        except Exception as e:
            logger.error(f"Error listing deployments: {e}")
            return {"success": True, "data": [], "error": str(e)}

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
        client = await self._get_client()

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

        try:
            response = await client.post(
                "/api/modelServing/v1/modelDeployments",
                json=payload
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error creating deployment: {e}")
            return {"success": False, "error": str(e)}

    async def get_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Get a specific Model Deployment.

        GET /api/modelServing/v1/modelDeployments/{modelDeploymentId}
        """
        client = await self._get_client()

        try:
            response = await client.get(
                f"/api/modelServing/v1/modelDeployments/{deployment_id}"
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error getting deployment: {e}")
            return {"success": False, "error": str(e)}

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
        client = await self._get_client()

        payload = {}
        if min_replicas is not None:
            payload["minReplicas"] = min_replicas
        if max_replicas is not None:
            payload["maxReplicas"] = max_replicas
        if model_api_version_id:
            payload["modelApiVersionId"] = model_api_version_id

        try:
            response = await client.patch(
                f"/api/modelServing/v1/modelDeployments/{deployment_id}",
                json=payload
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error updating deployment: {e}")
            return {"success": False, "error": str(e)}

    async def delete_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Delete a Model Deployment.

        DELETE /api/modelServing/v1/modelDeployments/{modelDeploymentId}
        """
        client = await self._get_client()

        try:
            response = await client.delete(
                f"/api/modelServing/v1/modelDeployments/{deployment_id}"
            )
            response.raise_for_status()
            return {"success": True, "message": f"Deployment {deployment_id} deleted"}
        except Exception as e:
            logger.error(f"Error deleting deployment: {e}")
            return {"success": False, "error": str(e)}

    async def start_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Start a stopped Model Deployment.

        POST /api/modelServing/v1/modelDeployments/{modelDeploymentId}/start
        """
        client = await self._get_client()

        try:
            response = await client.post(
                f"/api/modelServing/v1/modelDeployments/{deployment_id}/start"
            )
            response.raise_for_status()
            return {
                "success": True,
                "deployment_id": deployment_id,
                "status": "starting",
                "message": "Deployment start initiated"
            }
        except Exception as e:
            logger.error(f"Error starting deployment: {e}")
            return {"success": False, "error": str(e)}

    async def stop_deployment(self, deployment_id: str) -> Dict[str, Any]:
        """Stop a running Model Deployment.

        POST /api/modelServing/v1/modelDeployments/{modelDeploymentId}/stop
        """
        client = await self._get_client()

        try:
            response = await client.post(
                f"/api/modelServing/v1/modelDeployments/{deployment_id}/stop"
            )
            response.raise_for_status()
            return {
                "success": True,
                "deployment_id": deployment_id,
                "status": "stopping",
                "message": "Deployment stop initiated"
            }
        except Exception as e:
            logger.error(f"Error stopping deployment: {e}")
            return {"success": False, "error": str(e)}

    async def get_deployment_logs(
        self,
        deployment_id: str,
        log_suffix: str = "stdout"
    ) -> Dict[str, Any]:
        """Get logs for a Model Deployment.

        GET /api/modelServing/v1/modelDeployments/{modelDeploymentId}/logs/{logSuffix}

        logSuffix can be 'stdout', 'stderr', etc.
        """
        client = await self._get_client()

        try:
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
        client = await self._get_client()

        try:
            response = await client.get(
                f"/api/modelServing/v1/modelDeployments/{deployment_id}/versions"
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error getting deployment versions: {e}")
            return {"success": False, "error": str(e)}

    async def get_deployment_credentials(
        self,
        deployment_id: str,
        operation_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get temporary credentials for a Model Deployment.

        GET /api/modelServing/v1/modelDeployments/{modelDeploymentId}/credentials
        GET /api/modelServing/v1/modelDeployments/{modelDeploymentId}/credentials/{operationType}
        """
        client = await self._get_client()

        try:
            if operation_type:
                url = f"/api/modelServing/v1/modelDeployments/{deployment_id}/credentials/{operation_type}"
            else:
                url = f"/api/modelServing/v1/modelDeployments/{deployment_id}/credentials"

            response = await client.get(url)
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except Exception as e:
            logger.error(f"Error getting deployment credentials: {e}")
            return {"success": False, "error": str(e)}

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


# Singleton instance
_domino_model_api: Optional[DominoModelAPI] = None


def get_domino_model_api() -> DominoModelAPI:
    """Get the Domino Model API singleton."""
    global _domino_model_api
    if _domino_model_api is None:
        _domino_model_api = DominoModelAPI()
    return _domino_model_api
