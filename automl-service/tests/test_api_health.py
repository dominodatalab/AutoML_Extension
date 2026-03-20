"""Tests for the health check API endpoints.

Covers:
- GET /svc/v1/health — basic health check
- GET /svc/v1/health/ready — readiness check (DB + Domino)
- GET /svc/v1/health/user — current user info from headers/env
"""

import pytest

from app.core.context import user as user_ctx

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


def _set_viewing_user_roles(monkeypatch, roles: list[str]):
    """Override the viewing user returned by the user context."""
    def fake_get_viewing_user():
        return user_ctx.User(id="test-id", user_name="test-user", roles=roles)

    monkeypatch.setattr(user_ctx, "get_viewing_user", fake_get_viewing_user, raising=True)


@pytest.mark.asyncio
async def test_capabilities_include_storage_cleanup_for_sysadmin(app_client):
    """Storage cleanup capability should follow the SysAdmin storage policy."""
    response = await app_client.get("/svc/v1/health/capabilities")

    assert response.status_code == 200
    body = response.json()
    assert body["storage_cleanup"] is True


@pytest.mark.asyncio
async def test_capabilities_disable_storage_cleanup_for_non_sysadmin(app_client, monkeypatch):
    """Roles without storage-modify permission should not receive capability."""
    _set_viewing_user_roles(monkeypatch, ["Practitioner"])

    response = await app_client.get("/svc/v1/health/capabilities")

    assert response.status_code == 200
    body = response.json()
    assert body["storage_cleanup"] is False
