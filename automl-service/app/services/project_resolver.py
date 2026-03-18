"""Resolve Domino project metadata from the V4 projects API."""

import logging
import os
from dataclasses import dataclass
from typing import Optional

from app.config import get_settings
from app.core.context.auth import get_request_auth_header

logger = logging.getLogger(__name__)

# In-memory cache — project metadata is immutable for the app's lifetime.
_cache: dict[str, "ProjectInfo"] = {}


@dataclass(frozen=True)
class ProjectInfo:
    id: str
    name: str
    owner_username: str


async def _get_auth_headers() -> dict[str, str]:
    """Build Domino auth headers using the same priority chain as domino_model_api."""
    import httpx

    # forward the incoming request's auth header if present
    forwarded_auth = get_request_auth_header()
    if forwarded_auth:
        return {"Authorization": forwarded_auth}

    # fallbaack to the ephemeral token from Domino App/Run sidecar
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            # TODO this url should be dynamically resolved
            resp = await client.get("http://localhost:8899/access-token")
        if resp.status_code == 200 and resp.text.strip():
            return {"Authorization": f"Bearer {resp.text.strip()}"}
    except Exception:
        pass

    # Priority 2: static API key fallback
    api_key = (
        os.environ.get("DOMINO_API_KEY")
        or os.environ.get("DOMINO_USER_API_KEY")
        or get_settings().effective_api_key
    )
    if api_key:
        return {"X-Domino-Api-Key": api_key}

    return {}


def _resolve_api_host() -> Optional[str]:
    """Resolve Domino API host/proxy URL."""
    settings = get_settings()
    host = (
        os.environ.get("DOMINO_API_PROXY")
        or settings.domino_api_host
        or os.environ.get("DOMINO_API_HOST")
    )
    return host.rstrip("/") if host else None


async def resolve_project(project_id: str) -> Optional[ProjectInfo]:
    """Resolve project name and owner from the Domino V4 projects API.

    Returns cached ProjectInfo on success, None on any failure.
    """
    if project_id in _cache:
        return _cache[project_id]

    api_host = _resolve_api_host()
    if not api_host:
        logger.warning("Cannot resolve project %s: no Domino API host configured", project_id)
        return None

    try:
        import httpx

		# TODO should this use domino_http?
        headers = await _get_auth_headers()
        url = f"{api_host}/v4/projects/{project_id}"

        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(url, headers=headers)

        if resp.status_code != 200:
            logger.warning(
                "Failed to resolve project %s: HTTP %s", project_id, resp.status_code
            )
            return None

        data = resp.json()
        name = data.get("name")
        owner = data.get("ownerUsername") or data.get("owner", {}).get("userName")

        if not name or not owner:
            logger.warning(
                "Project %s response missing name/owner: %s",
                project_id,
                {k: data.get(k) for k in ("name", "ownerUsername", "owner")},
            )
            return None

        info = ProjectInfo(id=project_id, name=name, owner_username=owner)
        _cache[project_id] = info
        logger.info("Resolved project %s → %s/%s", project_id, owner, name)
        return info

    except Exception:
        logger.exception("Error resolving project %s", project_id)
        return None
