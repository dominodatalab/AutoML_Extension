import pytest
from unittest.mock import AsyncMock


@pytest.fixture()
def clear_user_context():
    """Reset the per-request user ContextVar before and after each test."""
    from app.core.context import user as user_ctx

    token = user_ctx._user_ctx.set(None)
    try:
        yield
    finally:
        # Restore previous state to avoid cross-test leakage
        user_ctx._user_ctx.reset(token)


def _make_user_envelope(user_id: str, user_name: str, roles=None):
    from app.api.generated.domino_public_api_client.models.metadata_v1 import (
        MetadataV1,
    )
    from app.api.generated.domino_public_api_client.models.user_envelope_v1 import (
        UserEnvelopeV1,
    )
    from app.api.generated.domino_public_api_client.models.user_v1 import UserV1

    user = UserV1(
        avatar_url="",
        first_name="First",
        full_name="First Last",
        id=user_id,
        last_name="Last",
        user_name=user_name,
        roles=roles,
    )
    meta = MetadataV1(notices=[], request_id="req-1")
    return UserEnvelopeV1(metadata=meta, user=user)


def test_get_viewing_user_fetches_and_caches(monkeypatch, clear_user_context):
    clear_user_context

    """First call fetches from API, subsequent calls use cached user."""
    from app.core.context import user as user_ctx
    from app.api.generated.domino_public_api_client.api import users as users_api

    # Avoid real client construction/host resolution
    monkeypatch.setattr(user_ctx, "get_domino_public_api_client_sync", lambda: object())

    calls = {"n": 0}

    def fake_sync(*, client):  # signature must match get_current_user.sync
        calls["n"] += 1
        return _make_user_envelope("u-1", "alice", roles=["Admin", "Viewer"])

    monkeypatch.setattr(users_api.get_current_user, "sync", fake_sync)

    u1 = user_ctx.get_viewing_user()
    assert u1 is not None
    assert u1.id == "u-1"
    assert u1.user_name == "alice"
    assert u1.roles == ["Admin", "Viewer"]

    # Second call should hit cache, not the API
    u2 = user_ctx.get_viewing_user()
    assert u2 is u1
    assert calls["n"] == 1


def test_get_viewing_user_roles_unset_becomes_empty(monkeypatch, clear_user_context):
    clear_user_context

    """If roles are UNSET in API model, surface as empty list."""
    from app.core.context import user as user_ctx
    from app.api.generated.domino_public_api_client.api import users as users_api

    # Avoid real client construction/host resolution
    monkeypatch.setattr(user_ctx, "get_domino_public_api_client_sync", lambda: object())

    def fake_sync(*, client):
        # No roles passed -> remains UNSET on model
        return _make_user_envelope("u-2", "bob", roles=None)

    monkeypatch.setattr(users_api.get_current_user, "sync", fake_sync)

    u = user_ctx.get_viewing_user()
    assert u is not None
    assert u.id == "u-2"
    assert u.user_name == "bob"
    # The context wrapper normalizes UNSET/None -> []
    assert u.roles == []

@pytest.fixture()
def mock_viewing_user():
    """This override conftest's mock_viewing_user fixture which is used in app_client
    so that no user is mocked, and only for the context of this test"""
    yield


@pytest.mark.asyncio
async def test_per_request_user_context_isolation_via_api(app_client, monkeypatch):
    """Using real requests, verify refetch on the second request when _user_ctx is empty.

    We patch the underlying Domino API call used by get_viewing_user to return
    different users for successive invocations. Each HTTP request runs in an
    isolated context, so both requests trigger fetch and see different users.
    """
    from types import SimpleNamespace

    from app.core.context import user as user_ctx
    from app.api.generated.domino_public_api_client.api import users as users_api
    import app.services.job_service as job_service
    import app.services.project_resolver as project_resolver

    calls = {"n": 0}

    def fake_sync(*, client):
        calls["n"] += 1
        if calls["n"] == 1:
            return _make_user_envelope("u-1", "alice", roles=["Admin"])  # first request
        else:
            return _make_user_envelope("u-2", "bob", roles=["Viewer"])   # second request

    monkeypatch.setattr(users_api.get_current_user, "sync", fake_sync)

    async def fake_resolve_project(project_id: str):
        return SimpleNamespace(
            id=project_id,
            name="test-project",
            owner_username="test-owner",
        )

    class FakeLauncher:
        async def start_training_job(self, **kwargs):
            return {
                "success": True,
                "domino_job_id": f"domino-{kwargs['job_id']}",
                "domino_job_status": "Submitted",
            }

    monkeypatch.setattr(project_resolver, "resolve_project", fake_resolve_project, raising=True)
    monkeypatch.setattr(job_service, "get_domino_job_launcher", lambda: FakeLauncher(), raising=True)
    monkeypatch.setattr(job_service, "_attach_external_links", lambda job: job, raising=True)

    # First request has owner alice
    r1 = await app_client.post(
        "/svc/v1/jobs",
        params={"projectId": "test-project-id"},
        json={
            "execution_target": "domino_job",
            "name": "req1",
            "model_type": "tabular",
            "data_source": "upload",
            "file_path": "/tmp/dummy.csv",
            "target_column": "target",
        },
    )
    assert r1.status_code == 200, r1.text
    b1 = r1.json()
    assert b1["owner"] == "alice"

    # Second request has owner bob
    r2 = await app_client.post(
        "/svc/v1/jobs",
        params={"projectId": "test-project-id"},
        json={
            "execution_target": "domino_job",
            "name": "req2",
            "model_type": "tabular",
            "data_source": "upload",
            "file_path": "/tmp/dummy.csv",
            "target_column": "target",
        },
    )
    assert r2.status_code == 200, r2.text
    b2 = r2.json()
    assert b2["owner"] == "bob"
    assert calls["n"] == 2
