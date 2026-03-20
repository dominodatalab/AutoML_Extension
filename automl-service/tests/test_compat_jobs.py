"""Tests for app.api.compat.custom_jobs routes.

Verifies that the compat job routes correctly parse request bodies
and delegate to the appropriate service functions with the right arguments.
Uses a minimal FastAPI app with mocked service layer and DB session.
"""

from contextlib import asynccontextmanager
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

pytestmark = pytest.mark.domino


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


@asynccontextmanager
async def _fake_db_session():
    """Yield a MagicMock that stands in for an AsyncSession."""
    yield MagicMock(name="fake_db_session")


def _build_app() -> FastAPI:
    """Create a minimal FastAPI app with the custom job compat routes."""
    from app.api.compat.custom_jobs import register_custom_job_routes

    app = FastAPI()
    register_custom_job_routes(app)
    return app


# ---------------------------------------------------------------------------
# POST /svcjobcleanup
# ---------------------------------------------------------------------------


class TestSvcJobCleanup:
    """Tests for POST /svcjobcleanup."""

    @patch("app.api.compat.custom_jobs.get_db_session", new=_fake_db_session)
    @patch("app.api.compat.custom_jobs.get_request_owner", return_value="testuser")
    def test_calls_bulk_cleanup_with_parsed_body(self, mock_owner):
        """Body fields are parsed into a CleanupRequest and forwarded correctly."""
        app = _build_app()

        fake_result = {"jobs_deleted": 2, "deleted_job_ids": ["a", "b"]}
        with patch(
            "app.services.job_service.bulk_cleanup",
            new_callable=AsyncMock,
            return_value=fake_result,
        ) as mock_cleanup, patch(
            "app.services.job_service.get_request_project_id",
            return_value="proj-123",
        ):
            client = TestClient(app)
            resp = client.post(
                "/svcjobcleanup",
                json={
                    "statuses": ["failed"],
                    "older_than_days": 30,
                    "include_orphans": True,
                },
            )

        assert resp.status_code == 200
        assert resp.json() == fake_result

        mock_cleanup.assert_called_once()
        call_kwargs = mock_cleanup.call_args.kwargs
        assert call_kwargs["statuses"] == ["failed"]
        assert call_kwargs["older_than_days"] == 30
        assert call_kwargs["include_orphans"] is True
        assert call_kwargs["project_id"] == "proj-123"
        assert call_kwargs["owner"] == "testuser"

    @patch("app.api.compat.custom_jobs.get_db_session", new=_fake_db_session)
    @patch("app.api.compat.custom_jobs.get_request_owner", return_value="someone")
    def test_uses_default_cleanup_request_values(self, mock_owner):
        """An empty body produces the CleanupRequest defaults."""
        app = _build_app()

        with patch(
            "app.services.job_service.bulk_cleanup",
            new_callable=AsyncMock,
            return_value={"jobs_deleted": 0},
        ) as mock_cleanup, patch(
            "app.services.job_service.get_request_project_id",
            return_value=None,
        ):
            client = TestClient(app)
            resp = client.post("/svcjobcleanup", json={})

        assert resp.status_code == 200

        call_kwargs = mock_cleanup.call_args.kwargs
        assert call_kwargs["statuses"] == ["failed", "cancelled"]
        assert call_kwargs["older_than_days"] is None
        assert call_kwargs["include_orphans"] is False


# ---------------------------------------------------------------------------
# POST /svcjoblogs
# ---------------------------------------------------------------------------


class TestSvcJobLogs:
    """Tests for POST /svcjoblogs."""

    @patch("app.api.compat.custom_jobs.get_db_session", new=_fake_db_session)
    def test_calls_get_job_logs_with_body_params(self):
        """job_id and limit are extracted from the request body."""
        app = _build_app()

        fake_log = MagicMock()
        fake_log.id = 1
        fake_log.job_id = "job-abc"
        fake_log.level = "INFO"
        fake_log.message = "Hello"
        fake_log.timestamp = datetime(2025, 1, 1, tzinfo=timezone.utc)

        with patch(
            "app.api.compat.custom_jobs.get_job_logs_service",
            new_callable=AsyncMock,
            return_value=[fake_log],
        ) as mock_logs:
            client = TestClient(app)
            resp = client.post(
                "/svcjoblogs",
                json={"job_id": "job-abc", "limit": 50},
            )

        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["job_id"] == "job-abc"
        assert data[0]["message"] == "Hello"

        mock_logs.assert_called_once()
        call_kwargs = mock_logs.call_args.kwargs
        assert call_kwargs["job_id"] == "job-abc"
        assert call_kwargs["limit"] == 50

    @patch("app.api.compat.custom_jobs.get_db_session", new=_fake_db_session)
    def test_uses_default_limit(self):
        """When limit is omitted, the default of 100 is used."""
        app = _build_app()

        with patch(
            "app.api.compat.custom_jobs.get_job_logs_service",
            new_callable=AsyncMock,
            return_value=[],
        ) as mock_logs:
            client = TestClient(app)
            resp = client.post("/svcjoblogs", json={"job_id": "job-xyz"})

        assert resp.status_code == 200
        call_kwargs = mock_logs.call_args.kwargs
        assert call_kwargs["limit"] == 100

    @patch("app.api.compat.custom_jobs.get_db_session", new=_fake_db_session)
    def test_job_id_none_when_omitted(self):
        """When job_id is omitted, None is passed to the service."""
        app = _build_app()

        with patch(
            "app.api.compat.custom_jobs.get_job_logs_service",
            new_callable=AsyncMock,
            return_value=[],
        ) as mock_logs:
            client = TestClient(app)
            resp = client.post("/svcjoblogs", json={})

        assert resp.status_code == 200
        call_kwargs = mock_logs.call_args.kwargs
        assert call_kwargs["job_id"] is None


# ---------------------------------------------------------------------------
# Route existence / method checks
# ---------------------------------------------------------------------------


class TestRouteRegistration:
    """Verify routes are registered with the correct HTTP methods."""

    @patch("app.api.compat.custom_jobs.get_db_session", new=_fake_db_session)
    def test_svcjobcleanup_rejects_get(self):
        app = _build_app()
        client = TestClient(app)
        resp = client.get("/svcjobcleanup")
        assert resp.status_code == 405

    @patch("app.api.compat.custom_jobs.get_db_session", new=_fake_db_session)
    def test_svcjoblogs_rejects_get(self):
        app = _build_app()
        client = TestClient(app)
        resp = client.get("/svcjoblogs")
        assert resp.status_code == 405
