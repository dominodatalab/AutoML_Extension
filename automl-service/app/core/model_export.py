"""Model export utilities for deployment."""

import os
import json
import logging
import shutil
from typing import Any, Dict, List, Optional
from pathlib import Path

from app.config import get_settings

logger = logging.getLogger(__name__)


class ModelExporter:
    """Handles model export to various formats for deployment."""

    def __init__(self, output_dir: Optional[str] = None):
        self.output_dir = output_dir or os.path.join(
            get_settings().temp_path, "model_exports"
        )
        os.makedirs(self.output_dir, exist_ok=True)

    @staticmethod
    def _remove_path_if_exists(path: str) -> None:
        """Remove an existing file, symlink, or directory."""
        if os.path.islink(path) or os.path.isfile(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

    def export_for_deployment(
        self,
        model_path: str,
        model_type: str,
        output_dir: str,
    ) -> Dict[str, Any]:
        """
        Export model with all files needed for deployment.

        Creates a deployment package with:
        - Model artifacts
        - Inference script
        - Requirements file
        - Model metadata
        """
        result = {
            "success": False,
            "output_dir": None,
            "files": [],
            "error": None
        }

        try:
            # Create deployment directory
            deploy_dir = os.path.join(output_dir, "deployment_package")
            os.makedirs(deploy_dir, exist_ok=True)

            # Copy model
            model_dest = os.path.join(deploy_dir, "model")
            self._remove_path_if_exists(model_dest)
            if os.path.isdir(model_path):
                shutil.copytree(model_path, model_dest)
            else:
                os.makedirs(model_dest, exist_ok=True)
                shutil.copy(model_path, model_dest)

            result["files"].append("model/")

            # Generate inference script
            inference_script = self._generate_inference_script(model_type)
            script_path = os.path.join(deploy_dir, "inference.py")
            with open(script_path, "w") as f:
                f.write(inference_script)
            result["files"].append("inference.py")

            # Generate requirements
            requirements = self._generate_requirements(model_type)
            req_path = os.path.join(deploy_dir, "requirements.txt")
            with open(req_path, "w") as f:
                f.write(requirements)
            result["files"].append("requirements.txt")

            # Generate model metadata
            metadata = {
                "model_type": model_type,
                "framework": "autogluon",
            }
            meta_path = os.path.join(deploy_dir, "model_metadata.json")
            with open(meta_path, "w") as f:
                json.dump(metadata, f, indent=2)
            result["files"].append("model_metadata.json")

            # Generate Dockerfile
            dockerfile = self._generate_dockerfile(model_type)
            docker_path = os.path.join(deploy_dir, "Dockerfile")
            with open(docker_path, "w") as f:
                f.write(dockerfile)
            result["files"].append("Dockerfile")

            result["success"] = True
            result["output_dir"] = deploy_dir

        except Exception as e:
            logger.error(f"Deployment export failed: {e}")
            result["error"] = str(e)

        return result

    def _generate_inference_script(self, model_type: str) -> str:
        """Generate inference script based on model type."""
        if model_type == "tabular":
            return '''"""AutoGluon Tabular inference script."""
import json
import pandas as pd
from autogluon.tabular import TabularPredictor

# Load model
predictor = TabularPredictor.load("./model")

def predict(data):
    """Make predictions on input data."""
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    elif isinstance(data, list):
        df = pd.DataFrame(data)
    else:
        df = data

    predictions = predictor.predict(df)
    probabilities = None

    try:
        probabilities = predictor.predict_proba(df)
    except Exception:
        pass

    return {
        "predictions": predictions.tolist(),
        "probabilities": probabilities.to_dict() if probabilities is not None else None
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = json.load(f)
        result = predict(data)
        print(json.dumps(result))
'''
        elif model_type == "timeseries":
            return '''"""AutoGluon TimeSeries inference script."""
import json
import pandas as pd
from autogluon.timeseries import TimeSeriesPredictor

# Load model
predictor = TimeSeriesPredictor.load("./model")

def predict(data, prediction_length=None):
    """Make forecasts on input data."""
    if isinstance(data, dict):
        df = pd.DataFrame(data)
    else:
        df = data

    predictions = predictor.predict(df)

    return {
        "predictions": predictions.to_dict()
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = json.load(f)
        result = predict(data)
        print(json.dumps(result))
'''
        else:
            raise ValueError(f"Unsupported model type for deployment script: {model_type}")

    def _generate_requirements(self, model_type: str) -> str:
        """Generate requirements.txt based on model type."""
        base_reqs = [
            "autogluon>=1.0.0",
            "pandas>=1.5.0",
            "numpy>=1.21.0",
        ]

        if model_type == "tabular":
            base_reqs.append("autogluon.tabular")
        elif model_type == "timeseries":
            base_reqs.append("autogluon.timeseries")
        else:
            raise ValueError(f"Unsupported model type for deployment requirements: {model_type}")

        return "\n".join(base_reqs)

    def _generate_dockerfile(self, model_type: str) -> str:
        """Generate Dockerfile for deployment."""
        return f'''FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    build-essential \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model and inference script
COPY model/ ./model/
COPY inference.py .
COPY model_metadata.json .

# Expose port for API
EXPOSE 8080

# Run inference server
CMD ["python", "inference.py"]
'''


# Singleton instance
_model_exporter: Optional[ModelExporter] = None


def get_model_exporter() -> ModelExporter:
    """Get the model exporter singleton."""
    global _model_exporter
    if _model_exporter is None:
        _model_exporter = ModelExporter()
    return _model_exporter
