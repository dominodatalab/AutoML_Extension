"""Request/response logging middleware.

Enabled by AUTOML_DEBUG_LOGGING=true. Logs every request with method, URL,
headers, body (truncated), response status, and timing. Designed to be
turned off in production.
"""

import json
import logging
import time
from typing import Optional

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger("automl.debug")

# Max bytes of request/response body to log
_MAX_BODY_LOG = 2000


def _truncate(text: str, limit: int = _MAX_BODY_LOG) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"... ({len(text) - limit} more bytes)"


def _safe_headers(headers: dict) -> dict:
    """Redact sensitive header values."""
    sensitive = {"authorization", "cookie", "x-api-key", "x-domino-api-key"}
    return {
        k: ("***" if k.lower() in sensitive else v)
        for k, v in headers.items()
    }


class DebugLoggingMiddleware(BaseHTTPMiddleware):
    """Logs request and response details when debug logging is enabled."""

    async def dispatch(self, request: Request, call_next) -> Response:
        start = time.perf_counter()
        request_id = f"{request.method} {request.url.path}"

        # --- Log request ---
        headers = _safe_headers(dict(request.headers))
        query = str(request.url.query) if request.url.query else None

        # Read body (only for non-GET and when content exists)
        body_text: Optional[str] = None
        if request.method not in ("GET", "HEAD", "OPTIONS"):
            try:
                body_bytes = await request.body()
                if body_bytes:
                    body_text = _truncate(body_bytes.decode("utf-8", errors="replace"))
            except Exception:
                body_text = "(could not read body)"

        logger.info(
            ">>> %s  query=%s  headers=%s  body=%s",
            request_id,
            query,
            json.dumps(headers, default=str),
            body_text or "(empty)",
        )

        # --- Call handler ---
        response = await call_next(request)
        elapsed_ms = (time.perf_counter() - start) * 1000

        # --- Log response ---
        logger.info(
            "<<< %s  status=%d  elapsed=%.1fms  content-type=%s",
            request_id,
            response.status_code,
            elapsed_ms,
            response.headers.get("content-type", "unknown"),
        )

        return response
