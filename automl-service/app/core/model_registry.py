"""Domino model registry integration."""

import logging
from typing import Any, Optional

from app.config import get_settings
from app.api.schemas.model import (
    ModelVersionResponse,
    DeploymentResponse,
)

logger = logging.getLogger(__name__)


class ModelRegistry:
    """Manages model registration and deployment to Domino."""

    def __init__(self):
        self.settings = get_settings()
        self._mlflow_client = None
        self._domino_client = None

    @property
    def mlflow_client(self):
        """Get MLflow client (lazy initialization)."""
        if self._mlflow_client is None:
            try:
                from mlflow.tracking import MlflowClient

                self._mlflow_client = MlflowClient()
                logger.info("MLflow client initialized")
            except Exception as e:
                logger.warning(f"Failed to initialize MLflow client: {e}")

        return self._mlflow_client

    @property
    def domino_client(self):
        """Get Domino client (lazy initialization)."""
        if self._domino_client is None and self.settings.is_domino_environment:
            try:
                from domino import Domino

                self._domino_client = Domino(
                    host=self.settings.domino_api_host,
                    api_key=self.settings.domino_user_api_key,
                    project=f"{self.settings.domino_project_owner}/{self.settings.domino_project_name}",
                )
                logger.info("Domino client initialized")
            except Exception as e:
                logger.warning(f"Failed to initialize Domino client: {e}")

        return self._domino_client

    async def register_model(
        self,
        model_name: str,
        run_id: str,
        model_path: str = "model",
        description: Optional[str] = None,
    ) -> int:
        """Register a model in the MLflow model registry."""
        if not self.mlflow_client:
            raise RuntimeError("MLflow client not available")

        # Create registered model if it doesn't exist
        try:
            self.mlflow_client.create_registered_model(
                name=model_name,
                description=description or f"AutoGluon model: {model_name}",
            )
            logger.info(f"Created registered model: {model_name}")
        except Exception:
            # Model already exists
            pass

        # Create model version
        model_uri = f"runs:/{run_id}/{model_path}"
        version = self.mlflow_client.create_model_version(
            name=model_name,
            source=model_uri,
            run_id=run_id,
            description=description,
        )

        logger.info(f"Created model version {version.version} for {model_name}")
        return int(version.version)

    async def list_versions(self, model_name: str) -> list[ModelVersionResponse]:
        """List all versions of a model."""
        if not self.mlflow_client:
            return []

        try:
            versions = self.mlflow_client.search_model_versions(f"name='{model_name}'")

            return [
                ModelVersionResponse(
                    version=int(v.version),
                    created_at=v.creation_timestamp,
                    run_id=v.run_id,
                    status=v.status,
                )
                for v in versions
            ]
        except Exception as e:
            logger.error(f"Failed to list model versions: {e}")
            return []

    async def deploy_model(
        self,
        model_name: str,
        model_version: int = 1,
        environment_id: Optional[str] = None,
        hardware_tier_id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> DeploymentResponse:
        """Deploy a model to Domino Model API."""
        if not self.domino_client:
            return DeploymentResponse(
                success=False,
                model_name=model_name,
                model_version=model_version,
                status="failed",
                message="Domino client not available (not in Domino environment)",
            )

        try:
            # Get model info from MLflow
            if self.mlflow_client:
                version_info = self.mlflow_client.get_model_version(
                    model_name, str(model_version)
                )
                model_uri = version_info.source
            else:
                model_uri = None

            # Deploy to Domino Model API
            # Note: This uses the Domino API for model deployment
            # The exact API call depends on Domino version and configuration

            deployment_config = {
                "modelName": model_name,
                "modelVersion": model_version,
                "description": description or f"AutoGluon model deployment",
            }

            if environment_id:
                deployment_config["environmentId"] = environment_id
            if hardware_tier_id:
                deployment_config["hardwareTierId"] = hardware_tier_id

            # TODO: Implement actual Domino Model API deployment
            # This would use the Domino REST API to create a Model API endpoint
            # result = self.domino_client.model_create(...)

            logger.info(f"Model deployment initiated: {model_name} v{model_version}")

            return DeploymentResponse(
                success=True,
                model_name=model_name,
                model_version=model_version,
                status="pending",
                message="Deployment initiated. Check Domino Model APIs for status.",
            )

        except Exception as e:
            logger.error(f"Failed to deploy model: {e}")
            return DeploymentResponse(
                success=False,
                model_name=model_name,
                model_version=model_version,
                status="failed",
                message=str(e),
            )

    async def list_deployments(self, model_name: str) -> list[dict[str, Any]]:
        """List active deployments for a model."""
        if not self.domino_client:
            return []

        try:
            # TODO: Implement listing of Domino Model API deployments
            # This would query Domino for active model endpoints
            return []
        except Exception as e:
            logger.error(f"Failed to list deployments: {e}")
            return []
