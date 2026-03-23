"""Shared Domino HTTP utilities for direct REST API calls.

Provides auth header acquisition, host resolution, project ID resolution,
and a retry-aware request helper used by domino_job_launcher and other
modules that call Domino platform APIs.
"""

import asyncio
import logging
import os
from typing import Any, Optional

import httpx

from app.api.generated.domino_public_api_client.client import Client as DominoApiClient
from app.core.context.auth import get_request_auth_header
from app.config import get_settings

logger = logging.getLogger(__name__)

_RETRYABLE_STATUS_CODES = (408, 502, 503, 504)
_DEFAULT_MAX_RETRIES = 4
_DEFAULT_TIMEOUT = 30.0

def get_sync_auth_headers() -> dict[str, str]:
    forwarded_auth = get_request_auth_header()
    headers = {}
    if forwarded_auth:
        headers["Authorization"] = forwarded_auth

    api_key = (
        os.environ.get("DOMINO_API_KEY")
        or os.environ.get("DOMINO_USER_API_KEY")
        or get_settings().effective_api_key
    )
    if api_key:
        headers["X-Domino-Api-Key"] = api_key

    return headers

async def get_domino_auth_headers() -> dict[str, str]:
    """Build Domino auth headers using the platform priority chain.

    Priority:
    1. Forwarded user token from the incoming request (per-request context)
    2. Ephemeral token from the Domino App/Run sidecar (localhost:8899)
    3. Static API key (DOMINO_API_KEY / DOMINO_USER_API_KEY)

    When a forwarded user token is present, it is preserved so that
    outbound Domino API calls (datasetrw, jobs, model registry) run as
    the visiting user, not the App owner.  The sidecar token is only
    used as a fallback when no user token was forwarded (e.g. background
    tasks, health checks).
    """
    headers = get_sync_auth_headers()

    # Only fetch the sidecar token when no user token was forwarded.
    # The forwarded token carries the visiting user's identity; overwriting
    # it with the sidecar token would make all API calls run as the App owner.
    if "Authorization" not in headers:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                resp = await client.get("http://localhost:8899/access-token")
            if resp.status_code == 200 and resp.text.strip():
                headers["Authorization"] = f"Bearer {resp.text.strip()}"
        except Exception:
            pass

    return headers

def get_domino_public_api_client_sync() -> DominoApiClient:
    """Create a Domino Public API client with auth.

    When a forwarded user JWT is present (i.e. during a browser request),
    call nucleus-frontend directly with the JWT so that RBAC is honoured.
    The sidecar proxy at localhost:8899 does not correctly forward user
    JWTs to downstream services like datasetrw.

    When no user JWT is available (background tasks, health checks), fall
    back to the sidecar proxy which injects its own service auth.
    """
    forwarded_auth = get_request_auth_header()

    if forwarded_auth:
        # User JWT present — call nucleus-frontend directly
        nucleus_host = resolve_domino_nucleus_host()
        if nucleus_host:
            base_url = nucleus_host.rstrip("/")
            headers = {"Authorization": forwarded_auth}
            return DominoApiClient(base_url=base_url).with_headers(headers)

    # No user JWT or no direct host — use sidecar proxy with API key
    headers = get_sync_auth_headers()
    base_url = resolve_domino_api_host()
    return DominoApiClient(base_url=base_url).with_headers(headers)

def resolve_domino_api_host() -> str:
    """Resolve the Domino API base URL.

    Priority: DOMINO_API_PROXY > settings.domino_api_host > DOMINO_API_HOST.
    Raises ValueError when no host is configured.
    """
    settings = get_settings()
    host = (
        os.environ.get("DOMINO_API_PROXY")
        or settings.domino_api_host
        or os.environ.get("DOMINO_API_HOST")
    )
    if not host:
        raise ValueError(
            "Domino API host is not configured. "
            "Set DOMINO_API_PROXY or DOMINO_API_HOST."
        )
    return host.rstrip("/")


def resolve_domino_project_id() -> str:
    """Resolve the current Domino project ID from settings or env.

    Raises ValueError when no project ID is available.
    """
    settings = get_settings()
    project_id = settings.domino_project_id or os.environ.get("DOMINO_PROJECT_ID")
    if not project_id:
        raise ValueError(
            "DOMINO_PROJECT_ID is not configured. "
            "Set the DOMINO_PROJECT_ID environment variable."
        )
    return project_id


async def domino_request(
    method: str,
    path: str,
    *,
    json: Any = None,
    params: Optional[dict[str, Any]] = None,
    files: Optional[dict] = None,
    headers: Optional[dict[str, str]] = None,
    base_url: Optional[str] = None,
    timeout: float = _DEFAULT_TIMEOUT,
    max_retries: int = _DEFAULT_MAX_RETRIES,
    retry_statuses: tuple[int, ...] = _RETRYABLE_STATUS_CODES,
) -> httpx.Response:
    """Send an HTTP request to the Domino API with retry logic.

    Builds the full URL from ``base_url`` when provided, otherwise from
    ``resolve_domino_api_host() + path``, acquires auth headers on each
    attempt (ephemeral tokens may expire between retries), and retries on
    transient server errors with exponential backoff.
    """
    resolved_base_url = (base_url or resolve_domino_api_host()).rstrip("/")
    url = f"{resolved_base_url}{path}"
    last_exc: Optional[Exception] = None

    for attempt in range(max_retries + 1):
        auth_headers = await get_domino_auth_headers()
        merged_headers = {**auth_headers, **(headers or {})}
        try:
            # Fresh client per request — the Domino App proxy closes idle
            # connections server-side, causing "Server disconnected" errors
            # with a shared connection pool.  This matches the behaviour of
            # the python-domino SDK (which used synchronous requests).
            async with httpx.AsyncClient() as client:
                resp = await client.request(
                    method,
                    url,
                    json=json,
                    params=params,
                    files=files,
                    headers=merged_headers,
                    timeout=timeout,
                )
            if resp.status_code in retry_statuses and attempt < max_retries:
                backoff = 2**attempt  # 1, 2, 4, 8
                logger.warning(
                    "Domino API %s %s returned %s, retrying in %ss (attempt %s/%s)",
                    method,
                    path,
                    resp.status_code,
                    backoff,
                    attempt + 1,
                    max_retries,
                )
                await asyncio.sleep(backoff)
                continue
            resp.raise_for_status()
            return resp
        except httpx.HTTPStatusError:
            raise
        except Exception as exc:
            last_exc = exc
            if attempt < max_retries:
                backoff = 2**attempt
                logger.warning(
                    "Domino API %s %s failed (%s), retrying in %ss (attempt %s/%s)",
                    method,
                    path,
                    exc,
                    backoff,
                    attempt + 1,
                    max_retries,
                )
                await asyncio.sleep(backoff)
                continue
            raise

    # Should not reach here, but satisfy type checker.
    raise last_exc or RuntimeError("Domino request failed after retries")


def resolve_domino_nucleus_host() -> Optional[str]:
    """Return the nucleus-frontend host, bypassing the local proxy.

    Returns ``None`` when no direct host is configured (i.e. only the
    proxy is available).
    """
    settings = get_settings()
    return (
        settings.domino_api_host
        or os.environ.get("DOMINO_API_HOST")
    ) or None


async def domino_download(
    path: str,
    dest_path: str,
    *,
    timeout: float = 300.0,
    base_url: Optional[str] = None,
) -> None:
    """Stream a file from the Domino API to a local path.

    Uses the same auth and host resolution as ``domino_request`` but
    streams the response body to *dest_path* in chunks to avoid loading
    large files into memory.

    An explicit *base_url* can be passed to bypass the default proxy-first
    resolution (useful when the proxy does not support the endpoint).
    """
    base_url = (base_url or resolve_domino_api_host()).rstrip("/")
    url = f"{base_url}{path}"

    auth_headers = await get_domino_auth_headers()

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    async with httpx.AsyncClient(timeout=timeout) as client:
        async with client.stream("GET", url, headers=auth_headers) as resp:
            resp.raise_for_status()
            with open(dest_path, "wb") as f:
                async for chunk in resp.aiter_bytes(chunk_size=8192):
                    f.write(chunk)

    logger.info("Downloaded %s -> %s", path, dest_path)
