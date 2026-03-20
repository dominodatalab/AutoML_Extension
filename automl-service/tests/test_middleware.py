"""Tests for app.api.middleware — _truncate, _safe_headers, DebugLoggingMiddleware."""

import logging

import pytest
from httpx import ASGITransport, AsyncClient
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.api.middleware import DebugLoggingMiddleware, _safe_headers, _truncate


# ---------------------------------------------------------------------------
# _truncate
# ---------------------------------------------------------------------------

class TestTruncate:
    def test_short_text_unchanged(self):
        assert _truncate("hello", limit=10) == "hello"

    def test_exact_limit_unchanged(self):
        text = "a" * 50
        assert _truncate(text, limit=50) == text

    def test_long_text_truncated_with_byte_count(self):
        text = "x" * 100
        result = _truncate(text, limit=40)
        assert result.startswith("x" * 40)
        assert result.endswith("... (60 more bytes)")

    def test_default_limit(self):
        short = "a" * 2000
        assert _truncate(short) == short

        over = "b" * 2500
        result = _truncate(over)
        assert "500 more bytes" in result


# ---------------------------------------------------------------------------
# _safe_headers
# ---------------------------------------------------------------------------

class TestSafeHeaders:
    def test_non_sensitive_headers_pass_through(self):
        headers = {"content-type": "application/json", "accept": "*/*"}
        assert _safe_headers(headers) == headers

    def test_sensitive_headers_redacted(self):
        headers = {
            "authorization": "Bearer secret",
            "cookie": "session=abc",
            "x-api-key": "key123",
            "domino-api-key": "domkey",
        }
        result = _safe_headers(headers)
        for key in headers:
            assert result[key] == "***"

    def test_case_insensitive_redaction(self):
        headers = {"Authorization": "Bearer tok", "COOKIE": "val"}
        result = _safe_headers(headers)
        assert result["Authorization"] == "***"
        assert result["COOKIE"] == "***"

    def test_mixed_headers(self):
        headers = {
            "content-type": "text/html",
            "Authorization": "Bearer x",
            "x-request-id": "abc",
        }
        result = _safe_headers(headers)
        assert result["content-type"] == "text/html"
        assert result["Authorization"] == "***"
        assert result["x-request-id"] == "abc"

    def test_empty_dict(self):
        assert _safe_headers({}) == {}


# ---------------------------------------------------------------------------
# DebugLoggingMiddleware
# ---------------------------------------------------------------------------

def _make_app():
    """Create a minimal Starlette app with the middleware attached."""
    app = Starlette()

    async def homepage(request: Request):
        return JSONResponse({"ok": True})

    async def echo_body(request: Request):
        body = await request.body()
        return JSONResponse({"echo": body.decode()})

    from starlette.routing import Route

    app = Starlette(
        routes=[
            Route("/", homepage),
            Route("/echo", echo_body, methods=["POST"]),
        ],
    )
    app.add_middleware(DebugLoggingMiddleware)
    return app


@pytest.fixture
def app():
    return _make_app()


@pytest.mark.asyncio
class TestDebugLoggingMiddleware:
    async def test_get_request_passes_through(self, app):
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            resp = await client.get("/")
        assert resp.status_code == 200
        assert resp.json() == {"ok": True}

    async def test_post_request_passes_through(self, app):
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            resp = await client.post("/echo", content="hello")
        assert resp.status_code == 200
        assert resp.json() == {"echo": "hello"}

    async def test_get_logs_request_and_response(self, app, caplog):
        with caplog.at_level(logging.INFO, logger="automl.debug"):
            async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
            ) as client:
                await client.get("/")

        messages = [r.message for r in caplog.records if r.name == "automl.debug"]
        assert len(messages) == 2
        assert ">>> GET /" in messages[0]
        assert "(empty)" in messages[0]
        assert "<<< GET /" in messages[1]
        assert "status=200" in messages[1]
        assert "elapsed=" in messages[1]

    async def test_post_logs_body(self, app, caplog):
        with caplog.at_level(logging.INFO, logger="automl.debug"):
            async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
            ) as client:
                await client.post("/echo", content="payload123")

        messages = [r.message for r in caplog.records if r.name == "automl.debug"]
        request_log = messages[0]
        assert ">>> POST /echo" in request_log
        assert "payload123" in request_log

    async def test_get_does_not_log_body(self, app, caplog):
        with caplog.at_level(logging.INFO, logger="automl.debug"):
            async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
            ) as client:
                await client.get("/")

        request_log = [
            r.message for r in caplog.records if r.name == "automl.debug"
        ][0]
        # GET should show "(empty)" body, not any body content
        assert "(empty)" in request_log

    async def test_sensitive_headers_redacted_in_log(self, app, caplog):
        with caplog.at_level(logging.INFO, logger="automl.debug"):
            async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
            ) as client:
                await client.get("/", headers={"authorization": "Bearer secret"})

        request_log = [
            r.message for r in caplog.records if r.name == "automl.debug"
        ][0]
        assert "Bearer secret" not in request_log
        assert "***" in request_log

    async def test_query_string_logged(self, app, caplog):
        with caplog.at_level(logging.INFO, logger="automl.debug"):
            async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
            ) as client:
                await client.get("/", params={"foo": "bar"})

        request_log = [
            r.message for r in caplog.records if r.name == "automl.debug"
        ][0]
        assert "foo=bar" in request_log

    async def test_404_still_logged(self, app, caplog):
        with caplog.at_level(logging.INFO, logger="automl.debug"):
            async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
            ) as client:
                resp = await client.get("/nonexistent")

        assert resp.status_code in (404, 405)
        messages = [r.message for r in caplog.records if r.name == "automl.debug"]
        assert len(messages) == 2
