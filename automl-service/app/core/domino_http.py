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

from app.core.context.auth import get_request_auth_header
from app.config import get_settings
from app.api.generated.domino_public_api_client.client import Client as DominoApiClient

logger = logging.getLogger(__name__)

_RETRYABLE_STATUS_CODES = (408, 502, 503, 504)
_DEFAULT_MAX_RETRIES = 4
_DEFAULT_TIMEOUT = 30.0

def get_sync_auth_headers() -> dict[str, str]:
    forwarded_auth = get_request_auth_header()
    headers = {}
    if forwarded_auth:
        headers = {**headers, **{"Authorization": forwarded_auth}}

    api_key = (
        os.environ.get("DOMINO_API_KEY")
        or os.environ.get("DOMINO_USER_API_KEY")
        or get_settings().effective_api_key
    )
    if api_key:
        headers = {**headers, **{"X-Domino-Api-Key": api_key}}

    return headers

async def get_domino_auth_headers() -> dict[str, str]:
    """Build Domino auth headers using the platform priority chain.

    Priority:
    0. Get auth header from auth context
    1. Fallback to the ephemeral token from Domino App/Run sidecar (localhost:8899)
    2. Static API key (DOMINO_API_KEY / DOMINO_USER_API_KEY / token file)
    """
    # forward the incoming request's auth header if present
    headers = get_sync_auth_headers()

    # fallbaack to the ephemeral token from Domino App/Run sidecar
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            # TODO this url must be dynamically resolved
            resp = await client.get("http://localhost:8899/access-token")
        if resp.status_code == 200 and resp.text.strip():
            headers = {**headers, **{"Authorization": f"Bearer {resp.text.strip()}"} }
    except Exception:
        pass

    return headers


def get_domino_public_api_client_sync() -> DominoApiClient:
    """Create a Domino Public API client with auth, which uses the
    Authorization header if present, fallsback to DOMINO_API_KEY/DOMINO_USER_API_KEY/token file
    If none is available, none is set.
    """
    headers = get_sync_auth_headers()

    # Base URL
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
    timeout: float = _DEFAULT_TIMEOUT,
    max_retries: int = _DEFAULT_MAX_RETRIES,
    retry_statuses: tuple[int, ...] = _RETRYABLE_STATUS_CODES,
) -> httpx.Response:
    """Send an HTTP request to the Domino API with retry logic.

    Builds the full URL from ``resolve_domino_api_host() + path``, acquires
    auth headers on each attempt (ephemeral tokens may expire between retries),
    and retries on transient server errors with exponential backoff.
    """
    base_url = resolve_domino_api_host()
    url = f"{base_url}{path}"
    last_exc: Optional[Exception] = None

    for attempt in range(max_retries + 1):
        headers = await get_domino_auth_headers()
        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                resp = await client.request(method, url, json=json, headers=headers)
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
