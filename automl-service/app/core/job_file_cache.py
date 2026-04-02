"""App-Local cache for job-related file downloads.

The cache lives under ``settings.temp_path``, which is the app's project dataset
(``/mnt/data/{project}/temp/`` in Domino). This is the app's own persistent filesystem.

Cache layout:

    {settings.temp_path}/{job_id}/

The entire ``{settings.temp_path}/{job_id}/`` directory is deleted by the
cleanup service when the corresponding job is deleted, clearing all cached
files for that job in one operation.
"""

import logging
import os

from app.config import get_settings

logger = logging.getLogger(__name__)


def download_mlflow_artifact(uri: str, job_id: str) -> str:
    """Download any MLflow artifact to the app's local cache and return its path.

    Enforces that ``uri`` is a ``runs:/`` URI — raises ``ValueError`` otherwise.

    Args:
        uri: MLflow artifact URI, e.g. ``runs:/{run_id}/autogluon_model``
             or ``runs:/{run_id}/leaderboard.json``.
        job_id: App-internal job ID, used to scope the cache directory.

    Returns:
        Absolute local path to the cached artifact (file or directory).
    """
    if not uri.startswith("runs:/"):
        raise ValueError(
            f"MLflow artifact URI must start with 'runs:/', got: {uri!r}"
        )

    remainder = uri[len("runs:/"):]
    run_id, _, artifact_path = remainder.partition("/")
    if not run_id:
        raise ValueError(f"Cannot parse run_id from MLflow URI: {uri!r}")
    if not artifact_path:
        raise ValueError(f"Cannot parse artifact_path from MLflow URI: {uri!r}")

    cache_root = get_settings().temp_path
    local_path = os.path.join(cache_root, job_id, "mlflow_models", *artifact_path.split("/"))

    if os.path.exists(local_path):
        logger.debug("MLflow artifact cache hit: %s", local_path)
        return local_path

    import mlflow

    dest_dir = os.path.join(cache_root, job_id, "mlflow_models")
    os.makedirs(dest_dir, exist_ok=True)
    logger.info("Downloading MLflow artifact %s to %s", uri, dest_dir)
    client = mlflow.tracking.MlflowClient()
    client.download_artifacts(run_id, artifact_path, dest_dir)

    if not os.path.exists(local_path):
        raise FileNotFoundError(
            f"MLflow download completed but expected path does not exist: {local_path}"
        )

    return local_path


def cache_dir_for_job(job_id: str) -> str:
    """Return the cache directory for a given job_id."""
    return os.path.join(get_settings().temp_path, job_id)
