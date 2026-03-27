"""Shared Domino HTTP utilities for direct REST API calls.

Provides auth header acquisition, host resolution, project ID resolution,
and a retry-aware request helper used by domino_job_launcher and other
modules that call Domino platform APIs.

Auth strategy
~~~~~~~~~~~~~
All outbound Domino API calls MUST use the visiting user's forwarded JWT
so that Domino enforces its own RBAC.  The sidecar token and static API
keys are **never** used as silent fallbacks — if no user token is present,
the request fails loudly.

``get_user_auth_headers`` / ``get_user_auth_headers_async``
    Strict user-identity auth.  Raises ``RuntimeError`` when no forwarded
    token is available.  Used by every user-facing code path.

The previous fallback chain (sidecar → API key) has been removed to
prevent accidental privilege escalation to the App-owner identity.
"""

import asyncio
import logging
import os
from typing import Any, Optional

import httpx

from app.api.generated.domino_public_api_client.client import Client as DominoApiClient
from app.api.generated_private.domino_data_lab_api_v_4_client.client import Client as DominoPrivateApiClient
from app.core.context.auth import get_request_auth_header
from app.config import get_settings

logger = logging.getLogger(__name__)

_RETRYABLE_STATUS_CODES = (408, 502, 503, 504)
_DEFAULT_MAX_RETRIES = 4
_DEFAULT_TIMEOUT = 30.0


class MissingUserTokenError(RuntimeError):
    """Raised when a Domino API call requires a forwarded user token but none is available."""


def get_user_auth_headers() -> dict[str, str]:
    """Build auth headers from the forwarded user token.

    Raises ``MissingUserTokenError`` if no token was forwarded by the
    middleware, preventing silent escalation to the App-owner identity.
    """
    forwarded_auth = get_request_auth_header()
    if not forwarded_auth:
        raise MissingUserTokenError(
            "No forwarded user token available. "
            "Domino API calls require a user token from the incoming request."
        )
    return {"Authorization": forwarded_auth}


async def get_user_auth_headers_async() -> dict[str, str]:
    """Async version of ``get_user_auth_headers``.

    Identical behaviour — exists so ``domino_request`` / ``domino_download``
    can await it symmetrically.
    """
    return get_user_auth_headers()


# ── Backward-compatible aliases ──────────────────────────────────────
# These preserve the old function names so that callers outside this
# module (and tests that mock them) continue to work without a rename
# sweep.  They now enforce user-token-only semantics.
get_sync_auth_headers = get_user_auth_headers
get_domino_auth_headers = get_user_auth_headers_async


def get_domino_private_api_client_sync() -> DominoPrivateApiClient:
    """Create a Domino Private API client authenticated as the visiting user."""
    headers = {**get_user_auth_headers(), 'Content-Type': 'application/json', 'Accept': 'application/json'}

    return DominoPrivateApiClient(
        base_url=resolve_domino_v4_api_base_url(),
        raise_on_unexpected_status=True,
    ).with_headers(headers)


def get_domino_public_api_client_sync() -> DominoApiClient:
    """Create a Domino Public API client authenticated as the visiting user.

    Raises ``MissingUserTokenError`` if no forwarded token is available.
    """
    headers = {**get_user_auth_headers(), 'Content-Type': 'application/json', 'Accept': 'application/json'}
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


def resolve_domino_v4_api_base_url() -> str:
    """Resolve the Domino private v4 API base URL."""
    return f"{resolve_domino_api_host()}/v4"


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

    Uses the forwarded user token for authentication.  Raises
    ``MissingUserTokenError`` if no token is available.

    Builds the full URL from ``base_url`` when provided, otherwise from
    ``resolve_domino_api_host() + path``, and retries on transient server
    errors with exponential backoff.
    """
    resolved_base_url = (base_url or resolve_domino_api_host()).rstrip("/")
    url = f"{resolved_base_url}{path}"
    last_exc: Optional[Exception] = None

    for attempt in range(max_retries + 1):
        auth_headers = await get_user_auth_headers_async()
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


async def domino_get_dataset_rw_snapshots(dataset_id: str) -> list[dict[str, Any]]:
    """Fetch Dataset RW snapshots for a dataset from the Domino v4 API."""
    response = await domino_request(
        "GET",
        f"/datasetrw/snapshots/{dataset_id}",
        base_url=resolve_domino_v4_api_base_url(),
    )
    payload = response.json()
    if not isinstance(payload, list):
        raise ValueError(f"Unexpected snapshot payload for dataset {dataset_id}")
    return payload


async def domino_get_dataset_snapshot_file_metadata(
    snapshot_id: str,
    path: str,
) -> dict[str, Any]:
    """Fetch Dataset RW snapshot file metadata from the Domino v4 API."""
    response = await domino_request(
        "GET",
        f"/datasetrw/snapshot/{snapshot_id}/file/meta",
        params={"path": path},
        base_url=resolve_domino_v4_api_base_url(),
    )
    payload = response.json()
    if not isinstance(payload, dict):
        raise ValueError(f"Unexpected metadata payload for snapshot {snapshot_id} path {path}")
    return payload


async def domino_get_dataset_snapshot_file_raw(
    snapshot_id: str,
    path: str,
) -> bytes:
    """Fetch raw Dataset RW snapshot file bytes from the Domino v4 API."""
    response = await domino_request(
        "GET",
        f"/datasetrw/snapshot/{snapshot_id}/file/raw",
        params={"path": path},
        headers={"Accept": "application/octet-stream"},
        base_url=resolve_domino_v4_api_base_url(),
    )
    return response.content


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

    Uses the forwarded user token for authentication.  Raises
    ``MissingUserTokenError`` if no token is available.

    An explicit *base_url* can be passed to bypass the default proxy-first
    resolution (useful when the proxy does not support the endpoint).
    """
    base_url = (base_url or resolve_domino_api_host()).rstrip("/")
    url = f"{base_url}{path}"

    auth_headers = await get_user_auth_headers_async()

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    async with httpx.AsyncClient(timeout=timeout) as client:
        async with client.stream("GET", url, headers=auth_headers) as resp:
            resp.raise_for_status()
            with open(dest_path, "wb") as f:
                async for chunk in resp.aiter_bytes(chunk_size=8192):
                    f.write(chunk)

    logger.info("Downloaded %s -> %s", path, dest_path)
