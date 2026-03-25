"""Tests for the job management API endpoints.

Covers:
- POST /svc/v1/jobs — create a tabular job (valid + validation error)
- POST /svc/v1/jobs/list — list jobs (empty then non-empty)
- GET  /svc/v1/jobs/{job_id} — get job by ID (found + 404)
- GET  /svc/v1/jobs/{job_id}/status — job status response
- GET  /svc/v1/jobs/{job_id}/metrics — job metrics response
- POST /svc/v1/jobs/{job_id}/cancel — cancel a pending job
- DELETE /svc/v1/jobs/{job_id} — delete a job

.. note:: Requires the ``domino`` package (available in Domino runtime).
- POST /svc/v1/jobs/bulk-delete — bulk delete
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

pytestmark = pytest.mark.domino


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

VALID_TABULAR_JOB = {
    "execution_target": "local",
    "name": "test-tabular-job",
    "model_type": "tabular",
    "data_source": "upload",
    "file_path": "/tmp/test.csv",
    "target_column": "target",
    "preset": "medium_quality_faster_train",
    "time_limit": 120,
}


def _mock_job_queue():
    """Return a mock JobQueueManager whose enqueue/cancel are async no-ops."""
    mock_queue = MagicMock()
    mock_queue.enqueue = AsyncMock()
    mock_queue.cancel = AsyncMock(return_value=True)
    mock_queue.get_queue_status = MagicMock(return_value={
        "max_concurrent": 1,
        "active": 0,
        "queued": 0,
    })
    mock_queue.get_total_tracked = MagicMock(return_value=0)
    return mock_queue

# ---------------------------------------------------------------------------
# POST /svc/v1/jobs — create job
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_create_tabular_job(app_client):
    """POST /svc/v1/jobs with valid tabular payload creates a job and returns 200."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        response = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "test-tabular-job"
    assert body["model_type"] == "tabular"
    assert body["status"] == "pending"
    assert body["target_column"] == "target"
    assert body["data_source"] == "upload"
    assert "id" in body
    assert "created_at" in body


@pytest.mark.asyncio
async def test_create_job_missing_target_column(app_client):
    """POST /svc/v1/jobs without target_column returns 422 validation error."""
    payload = {
        "name": "bad-job",
        "model_type": "tabular",
        "data_source": "upload",
        "file_path": "/tmp/test.csv",
        # target_column is missing
    }
    response = await app_client.post("/svc/v1/jobs", json=payload)

    assert response.status_code == 422
    body = response.json()
    assert "detail" in body


@pytest.mark.asyncio
async def test_create_job_missing_name(app_client):
    """POST /svc/v1/jobs without name returns 422 validation error."""
    payload = {
        "model_type": "tabular",
        "data_source": "upload",
        "file_path": "/tmp/test.csv",
        "target_column": "target",
    }
    response = await app_client.post("/svc/v1/jobs", json=payload)

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_timeseries_job_missing_time_column(app_client):
    """POST /svc/v1/jobs for timeseries without time_column returns 400."""
    payload = {
        "name": "ts-job",
        "model_type": "timeseries",
        "data_source": "upload",
        "file_path": "/tmp/test.csv",
        "target_column": "value",
        "prediction_length": 10,
        # time_column is missing
    }
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        response = await app_client.post("/svc/v1/jobs", json=payload)

    assert response.status_code == 400


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("method", "path", "payload"),
    [
        ("get", "/svc/v1/jobs/cleanup/preview", None),
        ("post", "/svc/v1/jobs/cleanup", {"statuses": ["failed"], "include_orphans": False}),
        ("post", "/svc/v1/jobs/cleanup/orphans", None),
        ("post", "/svcjobcleanuppreview", {}),
        ("post", "/svcjobcleanup", {"statuses": ["failed"], "include_orphans": False}),
        ("post", "/svcjoborphans", {}),
        ("post", "/svcjobcleanuporphans", {}),
    ],
)
async def test_cleanup_routes_allow_extension_editors(app_client, monkeypatch, method, path, payload):
    """Cleanup endpoints succeed when extension edit permission is granted."""
    from app.core import authorization

    def fake_fn(project_id: str):
        return True

    monkeypatch.setattr(
        authorization,
        "current_user_can_modify_storage",
        fake_fn,
        raising=True,
    )

    if method == "get":
        response = await app_client.get(path)
    else:
        response = await app_client.post(path, json=payload)

    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("method", "path", "payload"),
    [
        ("get", "/svc/v1/jobs/cleanup/preview", None),
        ("post", "/svc/v1/jobs/cleanup", {"statuses": ["failed"], "include_orphans": False}),
        ("post", "/svc/v1/jobs/cleanup/orphans", None),
        ("post", "/svcjobcleanuppreview", {}),
        ("post", "/svcjobcleanup", {"statuses": ["failed"], "include_orphans": False}),
        ("post", "/svcjoborphans", {}),
        ("post", "/svcjobcleanuporphans", {}),
    ],
)
async def test_cleanup_routes_reject_users_without_extension_edit(app_client, monkeypatch, method, path, payload):
    """Cleanup endpoints reject users without extension edit permission."""
    from app.core import authorization

    def fake_fn(project_id: str):
        return False

    monkeypatch.setattr(
        authorization,
        "current_user_can_modify_storage",
        fake_fn,
        raising=True,
    )

    if method == "get":
        response = await app_client.get(path)
    else:
        response = await app_client.post(path, json=payload)

    assert response.status_code == 403
    assert "edit the extension" in response.json()["detail"].lower()


# ---------------------------------------------------------------------------
# POST /svc/v1/jobs/list — list jobs
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_list_jobs_empty(app_client, monkeypatch):
    """POST /svc/v1/jobs/list on a fresh DB returns zero jobs."""
    from app.core import authorization as auth
    from tests.fake_domino_client import FakeResponse, FakeHttpxClient, FakeDominoClient

    fake_httpx = FakeHttpxClient(
        post_payload={"actions": [{"id": "job.project.list_jobs-1", "result": True}]},
    )
    fake_client = FakeDominoClient(fake_httpx)
    monkeypatch.setattr(
        auth,
        "get_domino_public_api_client_sync",
        lambda: fake_client,
        raising=True,
    )

    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        response = await app_client.post(
            "/svc/v1/jobs/list",
            json={"projectId": "1"},
        )

    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 0
    assert body["jobs"] == []


@pytest.mark.asyncio
async def test_list_jobs_after_creation(app_client):
    """POST /svc/v1/jobs/list returns the job created earlier in the same session."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        # Create a job first
        create_resp = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)
        assert create_resp.status_code == 200

        # List all jobs (empty owner/project to bypass filtering)
        list_resp = await app_client.post(
            "/svc/v1/jobs/list",
            json={"owner": "", "project_name": ""},
        )

    assert list_resp.status_code == 200
    body = list_resp.json()
    assert body["total"] >= 1
    job_names = [j["name"] for j in body["jobs"]]
    assert "test-tabular-job" in job_names


# ---------------------------------------------------------------------------
# GET /svc/v1/jobs/{job_id} — get job
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_get_job_by_id(app_client):
    """GET /svc/v1/jobs/{id} returns the created job."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        create_resp = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)
        job_id = create_resp.json()["id"]

    response = await app_client.get(f"/svc/v1/jobs/{job_id}")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == job_id
    assert body["name"] == "test-tabular-job"
    assert body["model_type"] == "tabular"


@pytest.mark.asyncio
async def test_get_job_not_found(app_client):
    """GET /svc/v1/jobs/{id} with nonexistent ID returns 404."""
    response = await app_client.get("/svc/v1/jobs/nonexistent-id-12345")

    assert response.status_code == 404
    body = response.json()
    assert "detail" in body


# ---------------------------------------------------------------------------
# GET /svc/v1/jobs/{job_id}/status
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_get_job_status(app_client):
    """GET /svc/v1/jobs/{id}/status returns status response shape."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        create_resp = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)
        job_id = create_resp.json()["id"]

    response = await app_client.get(f"/svc/v1/jobs/{job_id}/status")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == job_id
    assert body["status"] == "pending"
    assert "error_message" in body
    assert "started_at" in body
    assert "completed_at" in body


@pytest.mark.asyncio
async def test_get_job_status_not_found(app_client):
    """GET /svc/v1/jobs/{id}/status with nonexistent ID returns 404."""
    response = await app_client.get("/svc/v1/jobs/nonexistent-id/status")

    assert response.status_code == 404


# ---------------------------------------------------------------------------
# GET /svc/v1/jobs/{job_id}/metrics
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_get_job_metrics(app_client):
    """GET /svc/v1/jobs/{id}/metrics returns metrics response shape."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        create_resp = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)
        job_id = create_resp.json()["id"]

    response = await app_client.get(f"/svc/v1/jobs/{job_id}/metrics")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == job_id
    # A freshly created job has no metrics yet
    assert body["metrics"] is None
    assert body["leaderboard"] is None


@pytest.mark.asyncio
async def test_get_job_metrics_not_found(app_client):
    """GET /svc/v1/jobs/{id}/metrics with nonexistent ID returns 404."""
    response = await app_client.get("/svc/v1/jobs/nonexistent-id/metrics")

    assert response.status_code == 404


# ---------------------------------------------------------------------------
# POST /svc/v1/jobs/{job_id}/cancel
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_cancel_pending_job(app_client):
    """POST /svc/v1/jobs/{id}/cancel cancels a pending job."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        create_resp = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)
        job_id = create_resp.json()["id"]

        response = await app_client.post(f"/svc/v1/jobs/{job_id}/cancel")

    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Job cancelled"
    assert body["job_id"] == job_id


@pytest.mark.asyncio
async def test_cancel_already_cancelled_job(app_client):
    """POST /svc/v1/jobs/{id}/cancel on an already-cancelled job returns 400."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        create_resp = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)
        job_id = create_resp.json()["id"]

        # Cancel once
        await app_client.post(f"/svc/v1/jobs/{job_id}/cancel")

        # Try to cancel again
        response = await app_client.post(f"/svc/v1/jobs/{job_id}/cancel")

    assert response.status_code == 400
    body = response.json()
    assert "Cannot cancel" in body["detail"]


@pytest.mark.asyncio
async def test_cancel_nonexistent_job(app_client):
    """POST /svc/v1/jobs/{id}/cancel with nonexistent ID returns 404."""
    response = await app_client.post("/svc/v1/jobs/nonexistent-id/cancel")

    assert response.status_code == 404


# ---------------------------------------------------------------------------
# DELETE /svc/v1/jobs/{job_id}
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_delete_job(app_client):
    """DELETE /svc/v1/jobs/{id} deletes a job and returns confirmation."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        create_resp = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)
        job_id = create_resp.json()["id"]

    response = await app_client.delete(f"/svc/v1/jobs/{job_id}")

    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Job deleted"
    assert body["job_id"] == job_id

    # Verify the job is actually gone
    get_resp = await app_client.get(f"/svc/v1/jobs/{job_id}")
    assert get_resp.status_code == 404


@pytest.mark.asyncio
async def test_delete_nonexistent_job(app_client):
    """DELETE /svc/v1/jobs/{id} with nonexistent ID returns 404."""
    response = await app_client.delete("/svc/v1/jobs/nonexistent-id")

    assert response.status_code == 404


# ---------------------------------------------------------------------------
# POST /svc/v1/jobs/bulk-delete
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_bulk_delete_jobs(app_client):
    """POST /svc/v1/jobs/bulk-delete deletes multiple jobs at once."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        # Create two jobs with different names
        job1_payload = {**VALID_TABULAR_JOB, "name": "bulk-job-1"}
        job2_payload = {**VALID_TABULAR_JOB, "name": "bulk-job-2"}

        resp1 = await app_client.post("/svc/v1/jobs", json=job1_payload)
        resp2 = await app_client.post("/svc/v1/jobs", json=job2_payload)
        job_id_1 = resp1.json()["id"]
        job_id_2 = resp2.json()["id"]

        response = await app_client.post(
            "/svc/v1/jobs/bulk-delete",
            json={"job_ids": [job_id_1, job_id_2]},
        )

    assert response.status_code == 200
    body = response.json()
    assert job_id_1 in body["deleted_job_ids"]
    assert job_id_2 in body["deleted_job_ids"]
    assert body["failed"] == []


@pytest.mark.asyncio
async def test_bulk_delete_with_nonexistent_ids(app_client):
    """POST /svc/v1/jobs/bulk-delete with unknown IDs reports them in failed."""
    response = await app_client.post(
        "/svc/v1/jobs/bulk-delete",
        json={"job_ids": ["nonexistent-1", "nonexistent-2"]},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["deleted_job_ids"] == []
    assert len(body["failed"]) == 2
    failed_ids = [f["job_id"] for f in body["failed"]]
    assert "nonexistent-1" in failed_ids
    assert "nonexistent-2" in failed_ids


@pytest.mark.asyncio
async def test_bulk_delete_empty_list_returns_422(app_client):
    """POST /svc/v1/jobs/bulk-delete with empty list returns 422 validation error."""
    response = await app_client.post(
        "/svc/v1/jobs/bulk-delete",
        json={"job_ids": []},
    )

    assert response.status_code == 422


# ---------------------------------------------------------------------------
# Duplicate name validation
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_create_duplicate_job_name_returns_409(app_client):
    """POST /svc/v1/jobs with a duplicate name in the same scope returns 409."""
    with patch("app.core.job_queue.get_job_queue", return_value=_mock_job_queue()):
        resp1 = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)
        assert resp1.status_code == 200

        resp2 = await app_client.post("/svc/v1/jobs", json=VALID_TABULAR_JOB)

    assert resp2.status_code == 409
    body = resp2.json()
    assert "already exists" in body["detail"]
