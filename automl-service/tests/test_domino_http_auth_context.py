import pytest

from app.core.domino_http import MissingUserTokenError


@pytest.mark.asyncio
async def test_get_user_auth_headers_uses_forwarded_token():
    """get_user_auth_headers_async returns only the forwarded user token.

    No API key or sidecar fallback — the forwarded JWT is the sole
    credential for outbound Domino API calls.
    """
    from app.core.domino_http import get_user_auth_headers_async
    from app.core.context.auth import set_request_auth_header

    set_request_auth_header("Bearer token-A")
    try:
        headers = await get_user_auth_headers_async()
        assert headers == {"Authorization": "Bearer token-A"}
    finally:
        set_request_auth_header(None)


@pytest.mark.asyncio
async def test_get_user_auth_headers_raises_without_token(monkeypatch):
    """When no forwarded token exists, MissingUserTokenError is raised
    instead of silently falling back to sidecar/API key."""
    monkeypatch.setenv("DOMINO_API_KEY", "unit-test-key")

    from app.core.domino_http import get_user_auth_headers_async
    from app.core.context.auth import set_request_auth_header

    set_request_auth_header(None)
    with pytest.raises(MissingUserTokenError):
        await get_user_auth_headers_async()
