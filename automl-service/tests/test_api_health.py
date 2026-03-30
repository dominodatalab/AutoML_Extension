"""Tests for the health check API endpoints.

Covers:
- GET /svc/v1/health — basic health check
- GET /svc/v1/health/ready — readiness check (DB + Domino)
- GET /svc/v1/health/user — current user info from headers/env
"""

import pytest

pytestmark = pytest.mark.domino


@pytest.mark.asyncio
async def test_health_check_returns_200(app_client):
    """GET /svc/v1/health returns 200 with status 'healthy'."""
    response = await app_client.get("/svc/v1/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "healthy"
    assert "service" in body
    assert "version" in body


@pytest.mark.asyncio
async def test_health_check_includes_service_name(app_client):
    """GET /svc/v1/health returns the configured service name."""
    response = await app_client.get("/svc/v1/health")

    body = response.json()
    assert isinstance(body["service"], str)
    assert len(body["service"]) > 0


@pytest.mark.asyncio
async def test_health_check_includes_version(app_client):
    """GET /svc/v1/health returns a non-empty version string."""
    response = await app_client.get("/svc/v1/health")

    body = response.json()
    assert isinstance(body["version"], str)
    assert len(body["version"]) > 0


@pytest.mark.asyncio
async def test_readiness_check_returns_200(app_client):
    """GET /svc/v1/health/ready returns 200 with status and checks dict."""
    response = await app_client.get("/svc/v1/health/ready")

    assert response.status_code == 200
    body = response.json()
    assert "status" in body
    assert body["status"] in ("ready", "degraded")
    assert "checks" in body
    assert "database" in body["checks"]
    assert "domino" in body["checks"]


@pytest.mark.asyncio
async def test_readiness_check_database_is_healthy(app_client):
    """GET /svc/v1/health/ready — the database check should pass with the in-memory DB."""
    response = await app_client.get("/svc/v1/health/ready")

    body = response.json()
    assert body["checks"]["database"] is True


@pytest.mark.asyncio
async def test_user_endpoint_anonymous(app_client):
    """GET /svc/v1/health/user without domino-username header returns 'Anonymous'."""
    response = await app_client.get("/svc/v1/health/user")

    assert response.status_code == 200
    body = response.json()
    assert body["username"] == "Anonymous"
    assert body["initials"] == "?"


@pytest.mark.asyncio
async def test_user_endpoint_with_domino_username(app_client):
    """GET /svc/v1/health/user with domino-username header returns that user."""
    response = await app_client.get(
        "/svc/v1/health/user",
        headers={"domino-username": "jane.doe"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["username"] == "jane.doe"
    # jane.doe => initials "JD"
    assert body["initials"] == "JD"


@pytest.mark.asyncio
async def test_user_endpoint_single_name_initials(app_client):
    """GET /svc/v1/health/user with a single-word username derives 2-char initials."""
    response = await app_client.get(
        "/svc/v1/health/user",
        headers={"domino-username": "admin"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["username"] == "admin"
    assert body["initials"] == "AD"


@pytest.mark.asyncio
async def test_user_endpoint_contains_project_fields(app_client):
    """GET /svc/v1/health/user response includes project and environment fields."""
    response = await app_client.get("/svc/v1/health/user")

    body = response.json()
    assert "project_id" in body
    assert "project_name" in body
    assert "project_owner" in body
    assert "is_domino_environment" in body

@pytest.mark.asyncio
async def test_capabilities_include_storage_cleanup_for_extension_editors(app_client, monkeypatch):
    """Storage cleanup capability should follow extension edit permission."""
    from app.api.routes import health as health_routes

    seen = {}

    def fake_current_user_can_modify_storage(project_id=None):
        seen["project_id"] = project_id
        return True

    monkeypatch.setattr(
        health_routes,
        "current_user_can_modify_storage",
        fake_current_user_can_modify_storage,
        raising=True,
    )
    response = await app_client.get(
        "/svc/v1/health/capabilities",
        params={"projectId": "project-123"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["can_user_modify_storage"] is True
    assert seen["project_id"] == "project-123"


@pytest.mark.asyncio
async def test_capabilities_disable_storage_cleanup_without_extension_edit(app_client, monkeypatch):
    """Users without extension edit permission should not receive capability."""
    from app.api.routes import health as health_routes

    seen = {}

    def fake_current_user_can_modify_storage(project_id=None):
        seen["project_id"] = project_id
        return False

    monkeypatch.setattr(
        health_routes,
        "current_user_can_modify_storage",
        fake_current_user_can_modify_storage,
        raising=True,
    )

    response = await app_client.get(
        "/svc/v1/health/capabilities",
        params={"projectId": "project-456"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["can_user_modify_storage"] is False
    assert seen["project_id"] == "project-456"
