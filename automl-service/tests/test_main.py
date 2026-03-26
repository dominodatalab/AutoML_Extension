"""Tests for request handling in app.main."""

import ast
import logging

import pytest


@pytest.mark.asyncio
async def test_capture_request_context_redacts_sensitive_headers_in_logs(app_client, caplog):
    with caplog.at_level(logging.DEBUG, logger="app.main"):
        response = await app_client.get(
            "/svc/v1/health",
            headers={
                "x-api-key": "secret-api-key",
                "authorization": "Bearer super-secret-token",
                "x-domino-api-key": "domino-secret-key",
                "cookie": "session=super-secret-cookie",
                "x-visible-header": "visible-value",
            },
        )

    assert response.status_code == 200

    log_message = next(
        record.message
        for record in reversed(caplog.records)
        if record.name == "app.main" and "Capture request metadata" in record.message
    )
    logged_headers = dict(ast.literal_eval(log_message[log_message.index("["):]))

    assert logged_headers["x-api-key"] == "<REDACTED>"
    assert logged_headers["authorization"] == "<REDACTED>"
    assert logged_headers["x-domino-api-key"] == "<REDACTED>"
    assert logged_headers["cookie"] == "<REDACTED>"
    assert logged_headers["x-visible-header"] == "visible-value"

    assert "secret-api-key" not in log_message
    assert "super-secret-token" not in log_message
    assert "domino-secret-key" not in log_message
    assert "super-secret-cookie" not in log_message
