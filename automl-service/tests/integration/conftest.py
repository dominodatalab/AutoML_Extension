"""Integration test fixtures: service startup, HTTP client, test data, cleanup."""

import os
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Generator

import httpx
import numpy as np
import pandas as pd
import pytest

from .helpers import wait_for_service_ready

# ---------------------------------------------------------------------------
# Unique run tag for collision-free resource names
# ---------------------------------------------------------------------------
RUN_TAG = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

# ---------------------------------------------------------------------------
# Markers
# ---------------------------------------------------------------------------
pytestmark = pytest.mark.integration


# ---------------------------------------------------------------------------
# Service process (session-scoped)
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def service_process() -> Generator[subprocess.Popen, None, None]:
    """Start the FastAPI service as a subprocess and wait until healthy."""
    service_dir = Path(__file__).resolve().parents[2]  # automl-service/

    env = {**os.environ}
    # Force single worker for local compute
    env["WORKERS"] = "1"
    env["ENABLE_LOCAL_COMPUTE"] = "true"

    proc = subprocess.Popen(
        [
            sys.executable, "-m", "uvicorn",
            "app.main:app",
            "--host", "0.0.0.0",
            "--port", "8000",
            "--workers", "1",
        ],
        cwd=str(service_dir),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    # Give the process a moment to start
    time.sleep(2)
    if proc.poll() is not None:
        stdout = proc.stdout.read().decode() if proc.stdout else ""
        raise RuntimeError(
            f"Service process exited immediately with code {proc.returncode}.\n{stdout}"
        )

    yield proc

    # Teardown: gracefully stop the service
    proc.send_signal(signal.SIGTERM)
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=5)


# ---------------------------------------------------------------------------
# HTTP client (session-scoped)
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def client(service_process) -> Generator[httpx.Client, None, None]:
    """Synchronous httpx client pointed at the running service."""
    username = os.environ.get("DOMINO_STARTING_USERNAME", "integration-test")
    c = httpx.Client(
        base_url="http://localhost:8000",
        headers={"domino-username": username},
        timeout=httpx.Timeout(60.0, connect=10.0),
    )

    # Wait for service to be ready
    wait_for_service_ready(c, timeout=120.0, interval=5.0)

    yield c
    c.close()


# ---------------------------------------------------------------------------
# Shared state dict (session-scoped)
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def shared_state() -> dict:
    """Mutable dict for passing resource IDs between ordered test files.

    Downstream tests should call ``pytest.skip()`` if a required key is missing.
    """
    return {}


# ---------------------------------------------------------------------------
# Cleanup registry (session-scoped, runs at teardown)
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session", autouse=True)
def cleanup_registry(client, shared_state) -> Generator[dict, None, None]:
    """Track created resources and delete them in reverse dependency order.

    Keys: deployments, model_apis, registered_models, job_ids, data_files
    Each value is a list of IDs/paths.
    """
    registry = {
        "deployments": [],
        "model_apis": [],
        "registered_models": [],
        "job_ids": [],
        "data_files": [],
    }

    yield registry

    # ── Teardown: best-effort cleanup in dependency order ──
    _cleanup_deployments(client, registry["deployments"])
    _cleanup_model_apis(client, registry["model_apis"])
    _cleanup_registered_models(client, registry["registered_models"])
    _cleanup_jobs(client, registry["job_ids"])
    _cleanup_data_files(registry["data_files"])


def _cleanup_deployments(client: httpx.Client, deployment_ids: list) -> None:
    for dep_id in reversed(deployment_ids):
        try:
            # Stop first, then delete
            client.post(f"/svc/v1/deployments/{dep_id}/stop")
            time.sleep(2)
            client.delete(f"/svc/v1/deployments/{dep_id}")
        except Exception as exc:
            print(f"[cleanup] Warning: failed to delete deployment {dep_id}: {exc}")


def _cleanup_model_apis(client: httpx.Client, model_api_ids: list) -> None:
    for api_id in reversed(model_api_ids):
        try:
            client.delete(f"/svc/v1/deployments/model-apis/{api_id}")
        except Exception as exc:
            print(f"[cleanup] Warning: failed to delete model API {api_id}: {exc}")


def _cleanup_registered_models(client: httpx.Client, model_names: list) -> None:
    for name in reversed(model_names):
        try:
            client.delete(f"/svc/v1/registry/models/{name}")
        except Exception as exc:
            print(f"[cleanup] Warning: failed to delete registered model {name}: {exc}")


def _cleanup_jobs(client: httpx.Client, job_ids: list) -> None:
    if not job_ids:
        return
    try:
        client.post(
            "/svc/v1/jobs/bulk-delete",
            json={"job_ids": list(set(job_ids))},
        )
    except Exception as exc:
        print(f"[cleanup] Warning: failed to bulk-delete jobs: {exc}")


def _cleanup_data_files(file_paths: list) -> None:
    for fp in reversed(file_paths):
        try:
            p = Path(fp)
            if p.is_file():
                p.unlink()
            elif p.is_dir():
                import shutil
                shutil.rmtree(p, ignore_errors=True)
        except Exception as exc:
            print(f"[cleanup] Warning: failed to remove {fp}: {exc}")


# ---------------------------------------------------------------------------
# Test data directory
# ---------------------------------------------------------------------------
def _resolve_test_data_dir() -> Path:
    """Return the directory where integration test data should be written.

    In Domino: /mnt/data/{project}/datasets/integration_test/
    Locally:   automl-service/local_data/datasets/integration_test/
    """
    project_name = os.environ.get("DOMINO_PROJECT_NAME", "")
    if os.path.isdir("/mnt/data") and project_name:
        base = Path(f"/mnt/data/{project_name}/datasets/integration_test")
    else:
        base = Path(__file__).resolve().parents[2] / "local_data" / "datasets" / "integration_test"
    base.mkdir(parents=True, exist_ok=True)
    return base


# ---------------------------------------------------------------------------
# Synthetic test CSV fixtures (session-scoped)
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def tabular_csv_path(cleanup_registry) -> str:
    """Generate a 500-row binary classification CSV and return its path."""
    rng = np.random.default_rng(42)
    n = 500

    df = pd.DataFrame({
        "customer_id": range(1, n + 1),
        "age": rng.integers(18, 75, size=n),
        "income": rng.normal(60_000, 20_000, size=n).round(2),
        "score": rng.uniform(0, 100, size=n).round(2),
        "category": rng.choice(["A", "B", "C", "D"], size=n),
        "tenure_months": rng.integers(1, 120, size=n),
        "monthly_spend": rng.exponential(200, size=n).round(2),
    })

    # Binary target with some signal
    prob = 1 / (1 + np.exp(-(df["score"] / 50 - 1 + df["income"] / 80_000 - 0.5)))
    df["target"] = (rng.random(n) < prob).astype(int)

    # Inject ~3% missing in income
    mask = rng.random(n) < 0.03
    df.loc[mask, "income"] = np.nan

    data_dir = _resolve_test_data_dir()
    path = data_dir / f"tabular_test_{RUN_TAG}.csv"
    df.to_csv(path, index=False)

    cleanup_registry["data_files"].append(str(path))
    return str(path)


@pytest.fixture(scope="session")
def timeseries_csv_path(cleanup_registry) -> str:
    """Generate a 2-series x 180-day time series CSV and return its path."""
    rng = np.random.default_rng(99)
    rows = []

    for series_id in ["item_A", "item_B"]:
        base = 100 if series_id == "item_A" else 200
        trend = np.linspace(0, 20, 180)
        seasonal = 10 * np.sin(np.linspace(0, 4 * np.pi, 180))
        noise = rng.normal(0, 3, 180)
        values = base + trend + seasonal + noise

        for i, val in enumerate(values):
            rows.append({
                "timestamp": (pd.Timestamp("2024-01-01") + pd.Timedelta(days=i)).strftime("%Y-%m-%d"),
                "item_id": series_id,
                "value": round(val, 2),
            })

    df = pd.DataFrame(rows)

    data_dir = _resolve_test_data_dir()
    path = data_dir / f"timeseries_test_{RUN_TAG}.csv"
    df.to_csv(path, index=False)

    cleanup_registry["data_files"].append(str(path))
    return str(path)


# ---------------------------------------------------------------------------
# Convenience: unique name generator
# ---------------------------------------------------------------------------
@pytest.fixture(scope="session")
def unique_name():
    """Return a callable that generates unique inttest-prefixed names."""
    def _make(label: str) -> str:
        return f"inttest_{RUN_TAG}_{label}"
    return _make
