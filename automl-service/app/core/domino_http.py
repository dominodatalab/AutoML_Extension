"""Shared Domino HTTP utilities for direct REST API calls.

Provides auth header acquisition, host resolution, project ID resolution,
and a retry-aware request helper used by domino_job_launcher and other
modules that call Domino platform APIs.
"""

import asyncio
import logging
import os
import time
from typing import Any, Optional

import httpx

from app.config import get_settings

logger = logging.getLogger(__name__)

_RETRYABLE_STATUS_CODES = (408, 502, 503, 504)
_DEFAULT_MAX_RETRIES = 4
_DEFAULT_TIMEOUT = 30.0
_AUTH_CACHE_TTL_SECONDS = 3.0

_auth_cache_headers: Optional[dict[str, str]] = None
_auth_cache_expires_at = 0.0
_auth_lock: Optional[asyncio.Lock] = None
_shared_request_client: Optional[httpx.AsyncClient] = None
_shared_request_client_lock: Optional[asyncio.Lock] = None


def _get_auth_lock() -> asyncio.Lock:
    global _auth_lock
    if _auth_lock is None:
        _auth_lock = asyncio.Lock()
    return _auth_lock


def _get_request_client_lock() -> asyncio.Lock:
    global _shared_request_client_lock
    if _shared_request_client_lock is None:
        _shared_request_client_lock = asyncio.Lock()
    return _shared_request_client_lock


def _get_cached_auth_headers() -> Optional[dict[str, str]]:
    if _auth_cache_headers and _auth_cache_expires_at > time.monotonic():
        return dict(_auth_cache_headers)
    return None


def _cache_auth_headers(headers: dict[str, str]) -> dict[str, str]:
    global _auth_cache_headers, _auth_cache_expires_at
    _auth_cache_headers = dict(headers)
    _auth_cache_expires_at = time.monotonic() + _AUTH_CACHE_TTL_SECONDS
    return dict(headers)


def _invalidate_auth_cache() -> None:
    global _auth_cache_headers, _auth_cache_expires_at
    _auth_cache_headers = None
    _auth_cache_expires_at = 0.0


async def _get_shared_request_client() -> httpx.AsyncClient:
    """Reuse one AsyncClient so recursive API calls share connections."""
    global _shared_request_client
    if _shared_request_client is None or getattr(_shared_request_client, "is_closed", False):
        async with _get_request_client_lock():
            if _shared_request_client is None or getattr(_shared_request_client, "is_closed", False):
                _shared_request_client = httpx.AsyncClient()
    return _shared_request_client


async def _reset_domino_http_state() -> None:
    """Test helper to clear auth/client caches between cases."""
    _invalidate_auth_cache()
    await _close_shared_request_client()


async def _close_shared_request_client() -> None:
    """Close and clear the shared request client."""
    global _shared_request_client
    if _shared_request_client is not None and not getattr(_shared_request_client, "is_closed", False):
        close = getattr(_shared_request_client, "aclose", None)
        if close is not None:
            await close()
    _shared_request_client = None


async def get_domino_auth_headers(force_refresh: bool = False) -> dict[str, str]:
    """Build Domino auth headers using the platform priority chain.

    Priority:
    1. Ephemeral token from Domino App/Run sidecar (localhost:8899)
    2. Static API key (DOMINO_API_KEY / DOMINO_USER_API_KEY / token file)
    """
    if not force_refresh:
        cached_headers = _get_cached_auth_headers()
        if cached_headers is not None:
            return cached_headers

    async with _get_auth_lock():
        if not force_refresh:
            cached_headers = _get_cached_auth_headers()
            if cached_headers is not None:
                return cached_headers

        try:
            client = await _get_shared_request_client()
            # TODO this url must be dynamically resolved
            resp = await client.get("http://localhost:8899/access-token", timeout=5.0)
            if resp.status_code == 200 and resp.text.strip():
                return _cache_auth_headers(
                    {"Authorization": f"Bearer {resp.text.strip()}"}
                )
        except Exception:
            pass

        api_key = (
            os.environ.get("DOMINO_API_KEY")
            or os.environ.get("DOMINO_USER_API_KEY")
            or get_settings().effective_api_key
        )
        if api_key:
            return _cache_auth_headers({"X-Domino-Api-Key": api_key})

        _invalidate_auth_cache()
        return {}


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
    client = await _get_shared_request_client()

    for attempt in range(max_retries + 1):
        auth_headers = await get_domino_auth_headers(force_refresh=attempt > 0)
        merged_headers = {**auth_headers, **(headers or {})}
        try:
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


def _get_api_key() -> Optional[str]:
    """Return the Domino API key from environment or settings."""
    key = (
        os.environ.get("DOMINO_API_KEY")
        or os.environ.get("DOMINO_USER_API_KEY")
        or get_settings().effective_api_key
    )
    return key or None


async def domino_download(
    path: str,
    dest_path: str,
    *,
    timeout: float = 300.0,
    base_url: Optional[str] = None,
    use_api_key: bool = False,
) -> None:
    """Stream a file from the Domino API to a local path.

    Uses the same auth and host resolution as ``domino_request`` but
    streams the response body to *dest_path* in chunks to avoid loading
    large files into memory.

    An explicit *base_url* can be passed to bypass the default proxy-first
    resolution (useful when the proxy does not support the endpoint).

    When *use_api_key* is True, the request uses ``X-Domino-Api-Key``
    header instead of the normal Bearer-token-first auth chain.  The v4
    datasetrw endpoints require this auth method.
    """
    base_url = (base_url or resolve_domino_api_host()).rstrip("/")
    url = f"{base_url}{path}"

    if use_api_key:
        api_key = _get_api_key()
        if api_key:
            auth_headers = {"X-Domino-Api-Key": api_key}
        else:
            auth_headers = await get_domino_auth_headers()
    else:
        auth_headers = await get_domino_auth_headers()

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    async with httpx.AsyncClient(timeout=timeout) as client:
        async with client.stream("GET", url, headers=auth_headers) as resp:
            resp.raise_for_status()
            with open(dest_path, "wb") as f:
                async for chunk in resp.aiter_bytes(chunk_size=8192):
                    f.write(chunk)

    logger.info("Downloaded %s -> %s", path, dest_path)
