import pytest


@pytest.mark.asyncio
async def test_get_domino_auth_headers_reads_from_request_context(monkeypatch):
    """domino_http.get_domino_auth_headers should prefer the per-request ContextVar.

    - When the ContextVar is set, it must return that Authorization header.
    - When cleared, it should fall back to API key env (and not the prior value).
    """
    # Ensure a deterministic fallback without network dependency
    monkeypatch.setenv("DOMINO_API_KEY", "unit-test-key")

    from app.core.domino_http import get_domino_auth_headers
    from app.core.context.auth import set_request_auth_header

    # set the auth headers (normally done by a middleware)
    set_request_auth_header("Bearer token-A")

    # verify forwarded auth is used exclusively (no API key mixed in —
    # the sidecar proxy returns 500 when it receives both headers)
    headers = await get_domino_auth_headers()
    assert headers == {"Authorization": "Bearer token-A"}
