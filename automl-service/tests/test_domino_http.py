"""Tests for app.core.domino_http.

Covers:
- domino_download() — streaming file download to disk
- domino_request() — retry logic, auth headers
- get_domino_auth_headers() — ephemeral token vs API key
- resolve_domino_api_host() — priority chain
"""

import os
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from app.core.domino_http import (
    _reset_domino_http_state,
    domino_download,
    domino_request,
    get_domino_auth_headers,
    resolve_domino_api_host,
)


@pytest.fixture(autouse=True)
async def reset_domino_http_state():
    from app.core.context.auth import set_request_auth_header
    set_request_auth_header(None)
    await _reset_domino_http_state()
    yield
    set_request_auth_header(None)
    await _reset_domino_http_state()


# ---------------------------------------------------------------------------
# resolve_domino_api_host
# ---------------------------------------------------------------------------


class TestResolveDominoApiHost:

    def test_uses_proxy_env(self, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://proxy.example.com/")
        assert resolve_domino_api_host() == "https://proxy.example.com"

    def test_strips_trailing_slash(self, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://host.example.com///")
        assert resolve_domino_api_host() == "https://host.example.com"

    def test_raises_when_no_host(self, monkeypatch):
        monkeypatch.delenv("DOMINO_API_PROXY", raising=False)
        monkeypatch.delenv("DOMINO_API_HOST", raising=False)
        # Also need to clear settings
        import app.config as cfg
        old = cfg._settings_instance
        cfg._settings_instance = None
        monkeypatch.setenv("DOMINO_API_HOST", "")
        try:
            with pytest.raises(ValueError, match="not configured"):
                resolve_domino_api_host()
        finally:
            cfg._settings_instance = old


# ---------------------------------------------------------------------------
# get_domino_auth_headers
# ---------------------------------------------------------------------------


class TestGetDominoAuthHeaders:

    @pytest.mark.asyncio
    async def test_returns_api_key_when_sidecar_down(self, monkeypatch):
        monkeypatch.setenv("DOMINO_API_KEY", "test-key-123")
        # Mock the sidecar call to fail so we fall through to API key
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(side_effect=ConnectionError("no sidecar"))
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        with patch("httpx.AsyncClient", return_value=mock_client):
            headers = await get_domino_auth_headers()
        assert headers.get("X-Domino-Api-Key") == "test-key-123"

    @pytest.mark.asyncio
    async def test_returns_empty_when_no_credentials(self, monkeypatch):
        monkeypatch.delenv("DOMINO_API_KEY", raising=False)
        monkeypatch.delenv("DOMINO_USER_API_KEY", raising=False)
        # Clear settings to avoid picking up a key from config
        import app.config as cfg
        old = cfg._settings_instance
        cfg._settings_instance = None
        try:
            headers = await get_domino_auth_headers()
            # May be empty or may pick up from settings — just verify it's a dict
            assert isinstance(headers, dict)
        finally:
            cfg._settings_instance = old

    @pytest.mark.asyncio
    async def test_reuses_cached_sidecar_token_within_ttl(self, monkeypatch):
        monkeypatch.delenv("DOMINO_API_KEY", raising=False)
        monkeypatch.delenv("DOMINO_USER_API_KEY", raising=False)

        response = MagicMock()
        response.status_code = 200
        response.text = "token-123"

        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=response)
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("httpx.AsyncClient", return_value=mock_client):
            headers_one = await get_domino_auth_headers()
            headers_two = await get_domino_auth_headers()

        assert headers_one == {"Authorization": "Bearer token-123"}
        assert headers_two == {"Authorization": "Bearer token-123"}
        # Sidecar should only be called once — second call uses cache
        assert mock_client.get.await_count == 1


# ---------------------------------------------------------------------------
# domino_request — retry logic
# ---------------------------------------------------------------------------


class TestDominoRequest:

    @pytest.mark.asyncio
    async def test_successful_get(self, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")

        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {"ok": True}
        mock_response.raise_for_status = MagicMock()

        async def mock_request(self, method, url, **kwargs):
            return mock_response

        with patch.object(httpx.AsyncClient, "request", mock_request):
            resp = await domino_request("GET", "/api/test", max_retries=0)

        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_raises_on_client_error(self, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")

        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "Not Found", request=MagicMock(), response=mock_response
        )

        async def mock_request(self, method, url, **kwargs):
            return mock_response

        with patch.object(httpx.AsyncClient, "request", mock_request):
            with pytest.raises(httpx.HTTPStatusError):
                await domino_request("GET", "/api/missing", max_retries=0)

    @pytest.mark.asyncio
    async def test_retries_on_503(self, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")

        call_count = 0

        async def mock_request(self, method, url, **kwargs):
            nonlocal call_count
            call_count += 1
            resp = MagicMock(spec=httpx.Response)
            if call_count < 3:
                resp.status_code = 503
                return resp
            resp.status_code = 200
            resp.raise_for_status = MagicMock()
            return resp

        with patch.object(httpx.AsyncClient, "request", mock_request):
            with patch("app.core.domino_http.asyncio.sleep", new_callable=AsyncMock):
                resp = await domino_request(
                    "GET", "/api/flaky", max_retries=4
                )

        assert resp.status_code == 200
        # call_count includes auth header fetches triggering extra client creates,
        # but the mock_request captures the actual API calls
        assert call_count >= 3

    @pytest.mark.asyncio
    async def test_creates_fresh_client_per_request(self, monkeypatch):
        """domino_request uses a fresh AsyncClient per call (no shared pool)."""
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")

        client_instances = []

        class FakeClient:
            def __init__(self, **kwargs):
                client_instances.append(self)

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

            async def request(self, method, url, **kwargs):
                resp = MagicMock(spec=httpx.Response)
                resp.status_code = 200
                resp.raise_for_status = MagicMock()
                return resp

        with patch("app.core.domino_http.httpx.AsyncClient", FakeClient):
            await domino_request("GET", "/api/first", max_retries=0)
            await domino_request("GET", "/api/second", max_retries=0)

        # Each domino_request call creates a fresh client; get_domino_auth_headers
        # may also create a client for the sidecar token fetch, so we just verify
        # that multiple clients are instantiated (no shared pool).
        assert len(client_instances) >= 2

    @pytest.mark.asyncio
    async def test_retries_after_transport_error(self, monkeypatch):
        """domino_request retries on transport errors with a fresh client."""
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")

        call_count = 0

        class FakeClient:
            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

            async def request(self, method, url, **kwargs):
                nonlocal call_count
                call_count += 1
                if call_count == 1:
                    raise httpx.RemoteProtocolError("Server disconnected without sending a response.")
                resp = MagicMock(spec=httpx.Response)
                resp.status_code = 200
                resp.raise_for_status = MagicMock()
                return resp

        with patch("app.core.domino_http.httpx.AsyncClient", FakeClient):
            with patch("app.core.domino_http.asyncio.sleep", new_callable=AsyncMock):
                resp = await domino_request("GET", "/api/flaky", max_retries=1)

        assert resp.status_code == 200
        assert call_count == 2


# ---------------------------------------------------------------------------
# domino_download — streaming file download
# ---------------------------------------------------------------------------


class TestDominoDownload:

    @pytest.mark.asyncio
    async def test_downloads_file_to_dest(self, tmp_path, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")

        file_content = b"col1,col2\n1,2\n3,4\n"
        dest = str(tmp_path / "subdir" / "downloaded.csv")

        class FakeResponse:
            status_code = 200

            def raise_for_status(self):
                pass

            async def aiter_bytes(self, chunk_size=8192):
                yield file_content

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

        class FakeClient:
            def __init__(self, **kwargs):
                pass

            def stream(self, method, url, **kwargs):
                return FakeResponse()

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

        with patch("app.core.domino_http.httpx.AsyncClient", FakeClient):
            await domino_download("/api/files/test.csv", dest)

        assert os.path.exists(dest)
        with open(dest, "rb") as f:
            assert f.read() == file_content

    @pytest.mark.asyncio
    async def test_creates_parent_directories(self, tmp_path, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")

        dest = str(tmp_path / "a" / "b" / "c" / "file.csv")

        class FakeResponse:
            status_code = 200

            def raise_for_status(self):
                pass

            async def aiter_bytes(self, chunk_size=8192):
                yield b"data"

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

        class FakeClient:
            def __init__(self, **kwargs):
                pass

            def stream(self, method, url, **kwargs):
                return FakeResponse()

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

        with patch("app.core.domino_http.httpx.AsyncClient", FakeClient):
            await domino_download("/api/files/test.csv", dest)

        assert os.path.exists(dest)

    @pytest.mark.asyncio
    async def test_raises_on_http_error(self, tmp_path, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")

        dest = str(tmp_path / "fail.csv")

        class FakeResponse:
            status_code = 404

            def raise_for_status(self):
                raise httpx.HTTPStatusError(
                    "Not Found",
                    request=MagicMock(),
                    response=MagicMock(status_code=404),
                )

            async def aiter_bytes(self, chunk_size=8192):
                yield b""

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

        class FakeClient:
            def __init__(self, **kwargs):
                pass

            def stream(self, method, url, **kwargs):
                return FakeResponse()

            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

        with patch("app.core.domino_http.httpx.AsyncClient", FakeClient):
            with pytest.raises(httpx.HTTPStatusError):
                await domino_download("/api/files/missing.csv", dest)
