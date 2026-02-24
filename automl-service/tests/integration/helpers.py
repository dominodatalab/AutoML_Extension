"""Polling utilities for integration tests."""

import time
from typing import Optional

import httpx


def wait_for_service_ready(
    client: httpx.Client,
    timeout: float = 120.0,
    interval: float = 5.0,
) -> None:
    """Poll GET /svc/v1/health until the service is healthy or timeout."""
    deadline = time.monotonic() + timeout
    last_error: Optional[Exception] = None

    while time.monotonic() < deadline:
        try:
            resp = client.get("/svc/v1/health")
            if resp.status_code == 200 and resp.json().get("status") == "healthy":
                return
        except (httpx.ConnectError, httpx.ReadError, httpx.RemoteProtocolError) as exc:
            last_error = exc
        time.sleep(interval)

    raise TimeoutError(
        f"Service did not become healthy within {timeout}s. Last error: {last_error}"
    )


def poll_job_until_terminal(
    client: httpx.Client,
    job_id: str,
    timeout: float = 600.0,
    interval: float = 10.0,
) -> dict:
    """Poll GET /svc/v1/jobs/{job_id}/status until the job reaches a terminal state.

    Returns the final status response dict.
    Raises TimeoutError if the job doesn't finish in time.
    """
    terminal_statuses = {"completed", "failed", "cancelled"}
    deadline = time.monotonic() + timeout

    while time.monotonic() < deadline:
        resp = client.get(f"/svc/v1/jobs/{job_id}/status")
        resp.raise_for_status()
        data = resp.json()
        status = data.get("status")

        if status in terminal_statuses:
            return data

        time.sleep(interval)

    raise TimeoutError(
        f"Job {job_id} did not reach a terminal state within {timeout}s. "
        f"Last status: {data.get('status')}"
    )


def poll_deployment_until_running(
    client: httpx.Client,
    deployment_id: str,
    timeout: float = 600.0,
    interval: float = 15.0,
) -> dict:
    """Poll deployment status until running or timeout.

    Returns the final status response dict.
    """
    terminal_statuses = {"running", "failed", "stopped", "error"}
    deadline = time.monotonic() + timeout

    while time.monotonic() < deadline:
        resp = client.get(f"/svc/v1/deployments/{deployment_id}")
        resp.raise_for_status()
        data = resp.json()
        status = (data.get("status") or "").lower()

        if status in terminal_statuses:
            return data

        time.sleep(interval)

    raise TimeoutError(
        f"Deployment {deployment_id} did not become running within {timeout}s. "
        f"Last status: {data.get('status')}"
    )
