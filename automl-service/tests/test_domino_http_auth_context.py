import pytest


@pytest.mark.asyncio
async def test_get_domino_auth_headers_ignores_forwarded_auth(monkeypatch):
    """get_domino_auth_headers should NOT forward the per-request Authorization
    header to the sidecar proxy.  The sidecar injects its own auth; overriding
    it with the browser's token causes 500 errors.

    When no sidecar token is available, the function falls back to API key.
    """
    monkeypatch.setenv("DOMINO_API_KEY", "unit-test-key")

    from app.core.domino_http import get_domino_auth_headers
    from app.core.context.auth import set_request_auth_header

    # Simulate middleware capturing a browser auth header
    set_request_auth_header("Bearer token-A")

    # get_domino_auth_headers should NOT use the forwarded token —
    # it should fall through to sidecar token (which will fail in test)
    # then to API key
    headers = await get_domino_auth_headers()
    assert headers == {"X-Domino-Api-Key": "unit-test-key"}
    assert "Authorization" not in headers or "token-A" not in headers.get("Authorization", "")
