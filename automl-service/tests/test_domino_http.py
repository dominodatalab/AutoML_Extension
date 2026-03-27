"""Tests for app.core.domino_http.

Covers:
- domino_download() — streaming file download to disk
- domino_request() — retry logic, auth headers
- get_user_auth_headers() / get_user_auth_headers_async() — strict user token
- resolve_domino_api_host() — priority chain
"""

import os
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from app.core.domino_http import (
    MissingUserTokenError,
    domino_download,
    domino_get_dataset_rw_snapshots,
    domino_get_dataset_snapshot_file_metadata,
    domino_get_dataset_snapshot_file_raw,
    domino_request,
    get_user_auth_headers,
    get_user_auth_headers_async,
    resolve_domino_api_host,
    resolve_domino_v4_api_base_url,
)


@pytest.fixture(autouse=True)
async def reset_domino_http_state():
    from app.core.context.auth import set_request_auth_header
    set_request_auth_header(None)
    yield
    set_request_auth_header(None)


@pytest.fixture()
def with_user_token():
    """Set a forwarded user token for tests that need one."""
    from app.core.context.auth import set_request_auth_header
    set_request_auth_header("Bearer test-user-token")
    yield "Bearer test-user-token"
    set_request_auth_header(None)


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


class TestResolveDominoV4ApiBaseUrl:

    def test_appends_v4_suffix(self, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://proxy.example.com/")
        assert resolve_domino_v4_api_base_url() == "https://proxy.example.com/v4"


# ---------------------------------------------------------------------------
# get_domino_auth_headers
# ---------------------------------------------------------------------------


class TestGetUserAuthHeaders:

    def test_raises_when_no_token(self):
        """Must raise MissingUserTokenError when no forwarded token exists."""
        with pytest.raises(MissingUserTokenError):
            get_user_auth_headers()

    @pytest.mark.asyncio
    async def test_async_raises_when_no_token(self):
        """Async variant must also raise when no forwarded token exists."""
        with pytest.raises(MissingUserTokenError):
            await get_user_auth_headers_async()

    def test_returns_forwarded_token(self, with_user_token):
        """Returns the forwarded user token as Authorization header."""
        headers = get_user_auth_headers()
        assert headers == {"Authorization": "Bearer test-user-token"}

    @pytest.mark.asyncio
    async def test_async_returns_forwarded_token(self, with_user_token):
        """Async variant returns the forwarded user token."""
        headers = await get_user_auth_headers_async()
        assert headers == {"Authorization": "Bearer test-user-token"}

    def test_no_api_key_fallback(self, monkeypatch):
        """API key env vars must NOT be used as fallback."""
        monkeypatch.setenv("DOMINO_API_KEY", "should-not-appear")
        monkeypatch.setenv("DOMINO_USER_API_KEY", "should-not-appear")
        with pytest.raises(MissingUserTokenError):
            get_user_auth_headers()

    @pytest.mark.asyncio
    async def test_no_sidecar_fallback(self):
        """Sidecar token must NOT be fetched as fallback."""
        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("httpx.AsyncClient", return_value=mock_client):
            with pytest.raises(MissingUserTokenError):
                await get_user_auth_headers_async()
        # Sidecar should never be called
        assert mock_client.get.await_count == 0


# ---------------------------------------------------------------------------
# domino_request — retry logic
# ---------------------------------------------------------------------------


class TestDominoRequest:

    @pytest.mark.asyncio
    async def test_raises_without_user_token(self, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")
        with pytest.raises(MissingUserTokenError):
            await domino_request("GET", "/api/test", max_retries=0)

    @pytest.mark.asyncio
    async def test_successful_get(self, monkeypatch, with_user_token):
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
    async def test_raises_on_client_error(self, monkeypatch, with_user_token):
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
    async def test_retries_on_503(self, monkeypatch, with_user_token):
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
        assert call_count >= 3

    @pytest.mark.asyncio
    async def test_creates_fresh_client_per_request(self, monkeypatch, with_user_token):
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

        # Each domino_request call creates a fresh client.
        assert len(client_instances) >= 2

    @pytest.mark.asyncio
    async def test_retries_after_transport_error(self, monkeypatch, with_user_token):
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


class TestDatasetRwHelpers:

    @pytest.mark.asyncio
    async def test_get_dataset_rw_snapshots_uses_v4_helper(self, monkeypatch):
        seen = {}

        class FakeResponse:
            def json(self):
                return [{"id": "snap-1"}]

        async def fake_domino_request(method, path, **kwargs):
            seen["call"] = (method, path, kwargs)
            return FakeResponse()

        monkeypatch.setattr("app.core.domino_http.domino_request", fake_domino_request)
        monkeypatch.setattr(
            "app.core.domino_http.resolve_domino_v4_api_base_url",
            lambda: "https://domino.example/v4",
        )

        result = await domino_get_dataset_rw_snapshots("ds-1")

        assert result == [{"id": "snap-1"}]
        assert seen["call"] == (
            "GET",
            "/datasetrw/snapshots/ds-1",
            {"base_url": "https://domino.example/v4"},
        )

    @pytest.mark.asyncio
    async def test_get_dataset_snapshot_file_metadata_uses_v4_helper(self, monkeypatch):
        seen = {}

        class FakeResponse:
            def json(self):
                return {"fileSize": 123}

        async def fake_domino_request(method, path, **kwargs):
            seen["call"] = (method, path, kwargs)
            return FakeResponse()

        monkeypatch.setattr("app.core.domino_http.domino_request", fake_domino_request)
        monkeypatch.setattr(
            "app.core.domino_http.resolve_domino_v4_api_base_url",
            lambda: "https://domino.example/v4",
        )

        result = await domino_get_dataset_snapshot_file_metadata("snap-1", "folder/train.csv")

        assert result == {"fileSize": 123}
        assert seen["call"] == (
            "GET",
            "/datasetrw/snapshot/snap-1/file/meta",
            {
                "params": {"path": "folder/train.csv"},
                "base_url": "https://domino.example/v4",
            },
        )

    @pytest.mark.asyncio
    async def test_get_dataset_snapshot_file_raw_uses_v4_helper(self, monkeypatch):
        seen = {}

        class FakeResponse:
            content = b"abc"

        async def fake_domino_request(method, path, **kwargs):
            seen["call"] = (method, path, kwargs)
            return FakeResponse()

        monkeypatch.setattr("app.core.domino_http.domino_request", fake_domino_request)
        monkeypatch.setattr(
            "app.core.domino_http.resolve_domino_v4_api_base_url",
            lambda: "https://domino.example/v4",
        )

        result = await domino_get_dataset_snapshot_file_raw("snap-1", "folder/train.csv")

        assert result == b"abc"
        assert seen["call"] == (
            "GET",
            "/datasetrw/snapshot/snap-1/file/raw",
            {
                "params": {"path": "folder/train.csv"},
                "headers": {"Accept": "application/octet-stream"},
                "base_url": "https://domino.example/v4",
            },
        )


# ---------------------------------------------------------------------------
# domino_download — streaming file download
# ---------------------------------------------------------------------------


class TestDominoDownload:

    @pytest.mark.asyncio
    async def test_raises_without_user_token(self, tmp_path, monkeypatch):
        monkeypatch.setenv("DOMINO_API_PROXY", "https://api.test.com")
        dest = str(tmp_path / "fail.csv")
        with pytest.raises(MissingUserTokenError):
            await domino_download("/api/files/test.csv", dest)

    @pytest.mark.asyncio
    async def test_downloads_file_to_dest(self, tmp_path, monkeypatch, with_user_token):
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
    async def test_creates_parent_directories(self, tmp_path, monkeypatch, with_user_token):
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
    async def test_raises_on_http_error(self, tmp_path, monkeypatch, with_user_token):
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
