"""Domino Model Registry integration using MLflow."""

import os
import logging
import tempfile
from functools import lru_cache
from typing import Any, Dict, List, Optional

import mlflow
from mlflow import MlflowClient

from app.config import get_settings
from app.core.utils import utc_now

logger = logging.getLogger(__name__)


def _build_pyfunc_wrapper(model_type: str) -> mlflow.pyfunc.PythonModel:
    """Build a pyfunc wrapper using a local class for pickle portability.

    Defining the class in local scope makes cloudpickle serialize it by value
    instead of by module reference (`app.core...`). This avoids import errors
    when loading the model in Domino serving runtimes that don't ship this
    codebase.
    """
    if model_type == "timeseries":
        class AutoGluonTimeSeriesWrapper(mlflow.pyfunc.PythonModel):
            """MLflow PythonModel wrapper for AutoGluon TimeSeriesPredictor."""

            def load_context(self, context):
                """Load the AutoGluon model from artifacts."""
                from autogluon.timeseries import TimeSeriesPredictor
                self.predictor = TimeSeriesPredictor.load(context.artifacts["model_path"])

            def predict(self, context, model_input):
                """Make predictions using the loaded model."""
                predictions = self.predictor.predict(model_input)
                return {"predictions": predictions.to_dict('records')}

        return AutoGluonTimeSeriesWrapper()

    class AutoGluonTabularWrapper(mlflow.pyfunc.PythonModel):
        """MLflow PythonModel wrapper for AutoGluon TabularPredictor."""

        def load_context(self, context):
            """Load the AutoGluon model from artifacts."""
            from autogluon.tabular import TabularPredictor
            self.predictor = TabularPredictor.load(context.artifacts["model_path"])

        def predict(self, context, model_input):
            """Make predictions using the loaded model."""
            predictions = self.predictor.predict(model_input)
            try:
                probabilities = self.predictor.predict_proba(model_input)
                return {
                    "predictions": predictions.tolist(),
                    "probabilities": probabilities.to_dict('records')
                }
            except Exception:
                # For regression or when probabilities aren't available
                return {"predictions": predictions.tolist()}

    return AutoGluonTabularWrapper()


class DominoModelRegistry:
    """Integration with Domino Model Registry via MLflow."""

    def __init__(self):
        self.settings = get_settings()
        self._client: Optional[MlflowClient] = None
        self._setup_mlflow()

    def _setup_mlflow(self):
        """Configure MLflow for Domino integration."""
        # Set tracking URI
        tracking_uri = os.environ.get(
            "MLFLOW_TRACKING_URI",
            self.settings.mlflow_tracking_uri
        )
        if tracking_uri:
            mlflow.set_tracking_uri(tracking_uri)
            logger.info(f"MLflow tracking URI: {tracking_uri}")

        # Domino's proxy multipart endpoint can mis-handle MLflow logged-model artifact paths
        # (models:/m-...); keep multipart opt-in instead of forcing it on.
        if "MLFLOW_ENABLE_PROXY_MULTIPART_UPLOAD" not in os.environ:
            os.environ["MLFLOW_ENABLE_PROXY_MULTIPART_UPLOAD"] = "false"
        if os.environ.get("MLFLOW_ENABLE_PROXY_MULTIPART_UPLOAD", "").lower() == "true":
            os.environ.setdefault("MLFLOW_MULTIPART_UPLOAD_CHUNK_SIZE", "200000000")

    @property
    def client(self) -> MlflowClient:
        """Get MLflow client."""
        if self._client is None:
            self._client = MlflowClient()
        return self._client

    def register_model(
        self,
        model_path: str,
        model_name: str,
        model_type: str,
        description: str = "",
        tags: Optional[Dict[str, str]] = None,
        metrics: Optional[Dict[str, float]] = None,
        params: Optional[Dict[str, Any]] = None,
        experiment_name: Optional[str] = None,
        project_id: Optional[str] = None,
        project_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Register a trained model to the Domino Model Registry.

        Logs a pyfunc model under the active run artifacts, then registers that
        run artifact URI in the model registry.

        Args:
            experiment_name: The experiment name used during training. If not provided,
                           creates a new experiment with model name and timestamp.
        """
        result = {
            "success": False,
            "model_name": model_name,
            "model_version": None,
            "run_id": None,
            "artifact_uri": None,
        }

        try:
            # Use the same experiment as training, or create new one if not provided
            if not experiment_name:
                experiment_name = f"{model_name}__{utc_now().strftime('%Y%m%d_%H%M%S')}"
            mlflow.set_experiment(experiment_name)
            logger.info(f"Using MLflow experiment: {experiment_name}")

            # Define conda environment for the model
            conda_env = {
                "name": "autogluon_env",
                "channels": ["conda-forge"],
                "dependencies": [
                    "python=3.10",
                    "pip",
                    {
                        "pip": [
                            "autogluon>=1.1.0",
                            "mlflow>=2.10.0",
                            "pandas>=2.0.0",
                        ]
                    }
                ]
            }

            # Start a run to register the model
            with mlflow.start_run(run_name=f"register_{model_name}") as run:
                run_id = run.info.run_id
                result["run_id"] = run_id

                # Log parameters
                default_params = {
                    "model_type": model_type,
                    "framework": "autogluon",
                    "model_path": model_path,
                }
                if params:
                    default_params.update(params)

                for key, value in default_params.items():
                    try:
                        mlflow.log_param(key, str(value)[:250])
                    except Exception as e:
                        logger.warning(f"Could not log param {key}: {e}")

                # Log metrics
                if metrics:
                    for key, value in metrics.items():
                        try:
                            if isinstance(value, (int, float)):
                                mlflow.log_metric(key, float(value))
                        except Exception as e:
                            logger.warning(f"Could not log metric {key}: {e}")

                # Set tags — include Domino project context so the proxy
                # associates this run (and registered model) with the correct project.
                mlflow.set_tag("model_type", model_type)
                mlflow.set_tag("framework", "autogluon")
                mlflow.set_tag("registered_by", "automl-service")
                mlflow.set_tag("registration_time", utc_now().isoformat())
                mlflow.set_tag(
                    "domino.project_id",
                    project_id or os.environ.get("DOMINO_PROJECT_ID", ""),
                )
                mlflow.set_tag(
                    "domino.project_name",
                    project_name or os.environ.get("DOMINO_PROJECT_NAME", ""),
                )

                if tags:
                    for key, value in tags.items():
                        mlflow.set_tag(key, str(value))

                # Use a local-class wrapper so the serialized pyfunc does not
                # require importing this service module in serving environments.
                wrapper_model = _build_pyfunc_wrapper(model_type)

                # Use run artifacts + explicit model registration to stay compatible
                # with tracking servers that don't support logged-model artifact uploads.
                with tempfile.TemporaryDirectory(prefix="mlflow_model_") as tmp_dir:
                    local_model_dir = os.path.join(tmp_dir, "model")
                    mlflow.pyfunc.save_model(
                        path=local_model_dir,
                        python_model=wrapper_model,
                        artifacts={"model_path": model_path},
                        conda_env=conda_env,
                    )
                    mlflow.log_artifacts(local_model_dir, artifact_path="model")
                result["artifact_uri"] = f"runs:/{run_id}/model"
                created_version = mlflow.register_model(
                    model_uri=result["artifact_uri"],
                    name=model_name,
                    await_registration_for=300,
                )
                if created_version:
                    result["model_version"] = str(created_version.version)
                logger.info(f"Registered model from run artifact URI: {result['artifact_uri']}")

            # Resolve version and update metadata/tags
            try:
                version = result.get("model_version")
                if not version:
                    versions = self.client.search_model_versions(f"name='{model_name}'")
                    if versions:
                        latest = max(versions, key=lambda v: int(v.version))
                        version = str(latest.version)
                        result["model_version"] = version

                # Update description if provided
                if description:
                    self.client.update_registered_model(model_name, description=description)
                    if version:
                        self.client.update_model_version(
                            model_name,
                            version,
                            description=f"AutoGluon {model_type} model. {description}",
                        )

                # Set version tags with metrics
                if metrics and version:
                    for key, value in metrics.items():
                        if isinstance(value, (int, float)):
                            try:
                                self.client.set_model_version_tag(
                                    model_name, version, key, f"{value:.4f}"
                                )
                            except Exception:
                                pass

                result["success"] = True
                if version:
                    logger.info(f"Model {model_name} version {version} registered successfully")
                else:
                    logger.info(f"Model {model_name} registered successfully")

            except Exception as e:
                logger.warning(f"Could not get version info: {e}")
                result["success"] = True  # Model was registered, just couldn't get version

        except Exception as e:
            logger.error(f"Error in model registration: {e}")
            result["error"] = str(e)

        return result

    def list_registered_models(self) -> List[Dict[str, Any]]:
        """List all registered models."""
        models = []

        try:
            for rm in self.client.search_registered_models():
                model_info = {
                    "name": rm.name,
                    "description": rm.description,
                    "creation_timestamp": rm.creation_timestamp,
                    "last_updated_timestamp": rm.last_updated_timestamp,
                    "tags": dict(rm.tags) if rm.tags else {},
                    "latest_versions": []
                }

                # Get latest versions
                for mv in rm.latest_versions:
                    model_info["latest_versions"].append({
                        "version": mv.version,
                        "status": mv.status,
                        "stage": mv.current_stage,
                        "creation_timestamp": mv.creation_timestamp,
                        "run_id": mv.run_id,
                        "source": mv.source,
                    })

                models.append(model_info)

        except Exception as e:
            logger.error(f"Error listing registered models: {e}")

        return models

    def get_model_versions(self, model_name: str) -> List[Dict[str, Any]]:
        """Get all versions of a registered model."""
        versions = []

        try:
            for mv in self.client.search_model_versions(f"name='{model_name}'"):
                version_info = {
                    "version": mv.version,
                    "name": mv.name,
                    "status": mv.status,
                    "stage": mv.current_stage,
                    "description": mv.description,
                    "creation_timestamp": mv.creation_timestamp,
                    "last_updated_timestamp": mv.last_updated_timestamp,
                    "run_id": mv.run_id,
                    "source": mv.source,
                    "run_link": mv.run_link,
                    "tags": dict(mv.tags) if mv.tags else {},
                }
                versions.append(version_info)

        except Exception as e:
            logger.error(f"Error getting model versions: {e}")

        return versions

    def transition_model_stage(
        self,
        model_name: str,
        version: str,
        stage: str,
        archive_existing: bool = False
    ) -> Dict[str, Any]:
        """Transition a model version to a new stage."""
        valid_stages = ["None", "Staging", "Production", "Archived"]

        if stage not in valid_stages:
            return {
                "success": False,
                "error": f"Invalid stage. Must be one of: {valid_stages}"
            }

        try:
            result = self.client.transition_model_version_stage(
                name=model_name,
                version=version,
                stage=stage,
                archive_existing_versions=archive_existing
            )

            return {
                "success": True,
                "model_name": model_name,
                "version": version,
                "new_stage": stage,
                "previous_stage": result.current_stage
            }

        except Exception as e:
            logger.error(f"Error transitioning model stage: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def delete_model_version(self, model_name: str, version: str) -> Dict[str, Any]:
        """Delete a specific model version."""
        try:
            self.client.delete_model_version(name=model_name, version=version)
            return {
                "success": True,
                "model_name": model_name,
                "version": version,
                "message": f"Deleted version {version} of {model_name}"
            }
        except Exception as e:
            logger.error(f"Error deleting model version: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def delete_registered_model(self, model_name: str) -> Dict[str, Any]:
        """Delete a registered model and all its versions."""
        try:
            self.client.delete_registered_model(name=model_name)
            return {
                "success": True,
                "model_name": model_name,
                "message": f"Deleted registered model {model_name}"
            }
        except Exception as e:
            logger.error(f"Error deleting registered model: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def update_model_description(
        self,
        model_name: str,
        description: str,
        version: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update model or model version description."""
        try:
            if version:
                self.client.update_model_version(
                    name=model_name,
                    version=version,
                    description=description
                )
                return {
                    "success": True,
                    "model_name": model_name,
                    "version": version,
                    "description": description
                }
            else:
                self.client.update_registered_model(
                    name=model_name,
                    description=description
                )
                return {
                    "success": True,
                    "model_name": model_name,
                    "description": description
                }
        except Exception as e:
            logger.error(f"Error updating description: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def get_model_download_uri(self, model_name: str, version: str) -> Optional[str]:
        """Get the download URI for a model version."""
        try:
            mv = self.client.get_model_version(name=model_name, version=version)
            return mv.source
        except Exception as e:
            logger.error(f"Error getting model URI: {e}")
            return None

    def load_model_from_registry(
        self,
        model_name: str,
        version: Optional[str] = None,
        stage: Optional[str] = None
    ) -> Any:
        """Load a model from the registry."""
        try:
            if version:
                model_uri = f"models:/{model_name}/{version}"
            elif stage:
                model_uri = f"models:/{model_name}/{stage}"
            else:
                model_uri = f"models:/{model_name}/latest"

            # Download model artifacts
            local_path = mlflow.artifacts.download_artifacts(model_uri)
            return local_path

        except Exception as e:
            logger.error(f"Error loading model from registry: {e}")
            return None

    def create_model_card(
        self,
        model_name: str,
        version: str,
        job_info: Dict[str, Any],
        metrics: Dict[str, Any],
        feature_importance: Optional[List[Dict]] = None
    ) -> str:
        """Generate a model card markdown document."""
        card = f"""# Model Card: {model_name}

## Model Overview
- **Version**: {version}
- **Type**: {job_info.get('model_type', 'Unknown')}
- **Problem Type**: {job_info.get('problem_type', 'Unknown')}
- **Framework**: AutoGluon
- **Created**: {utc_now().isoformat()}

## Training Configuration
- **Dataset**: {job_info.get('dataset_id', 'Unknown')}
- **Target Column**: {job_info.get('target_column', 'Unknown')}
- **Preset**: {job_info.get('preset', 'Unknown')}
- **Time Limit**: {job_info.get('time_limit', 'Unknown')} seconds

## Performance Metrics
"""
        for metric_name, metric_value in metrics.items():
            if isinstance(metric_value, (int, float)):
                card += f"- **{metric_name}**: {metric_value:.4f}\n"

        if feature_importance:
            card += "\n## Feature Importance (Top 10)\n"
            card += "| Feature | Importance |\n|---------|------------|\n"
            for feat in feature_importance[:10]:
                card += f"| {feat['feature']} | {feat['importance']:.4f} |\n"

        card += f"""
## Usage

```python
from autogluon.tabular import TabularPredictor

# Load from MLflow registry
import mlflow
model_uri = "models:/{model_name}/{version}"
local_path = mlflow.artifacts.download_artifacts(model_uri)
predictor = TabularPredictor.load(local_path)

# Make predictions
predictions = predictor.predict(new_data)
```

## Intended Use
This model was trained using AutoML for {job_info.get('problem_type', 'prediction')} tasks.

## Limitations
- Model performance may vary on data significantly different from training data
- Regularly monitor model performance in production

---
*Generated by AutoML Service*
"""
        return card


@lru_cache()
def get_domino_registry() -> DominoModelRegistry:
    """Get the Domino registry singleton (cached)."""
    return DominoModelRegistry()
