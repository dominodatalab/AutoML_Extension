"""Smoke tests: health, readiness, user context, root endpoint."""

import os

import pytest

pytestmark = pytest.mark.integration


class TestHealth:
    """Basic health and readiness checks."""

    def test_health_returns_healthy(self, client):
        resp = client.get("/svc/v1/health")
        assert resp.status_code == 200, f"Health check failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert body["status"] == "healthy"
        assert "service" in body
        assert "version" in body

    def test_readiness_check(self, client):
        resp = client.get("/svc/v1/health/ready")
        assert resp.status_code == 200, f"Readiness check failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert body["status"] in ("ready", "degraded")
        assert "checks" in body
        assert "database" in body["checks"]
        assert "domino" in body["checks"]
        # Database should always be reachable
        assert body["checks"]["database"] is True

    def test_user_context(self, client):
        resp = client.get("/svc/v1/health/user")
        assert resp.status_code == 200, f"User context failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert "username" in body
        assert "initials" in body
        assert body["username"] != ""
        # In Domino, project_id and project_name should match env vars
        if os.environ.get("DOMINO_PROJECT_ID"):
            assert body["project_id"] == os.environ["DOMINO_PROJECT_ID"]
        if os.environ.get("DOMINO_PROJECT_NAME"):
            assert body["project_name"] == os.environ["DOMINO_PROJECT_NAME"]

    def test_root_endpoint(self, client):
        resp = client.get("/")
        assert resp.status_code == 200, f"Root endpoint failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert "service" in body
        assert "version" in body
        assert "status" in body
        assert body["status"] == "running"
        assert "jobs" in body
