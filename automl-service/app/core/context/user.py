"""This is a per request cache for the viewing user"""

import logging
from dataclasses import dataclass
from typing import Optional
from contextvars import ContextVar

import httpx

from app.core.context.auth import get_request_auth_header
from app.core.domino_http import resolve_domino_api_host

logger = logging.getLogger(__name__)


@dataclass
class User:
    id: str
    user_name: str
    roles: list[str]


_user_ctx: ContextVar[Optional[User]] = ContextVar("viewing_user", default=None)


def _build_auth_headers() -> dict[str, str]:
    """Build auth headers using the exclusive cascade (same as get_domino_auth_headers)."""
    import os
    from app.config import get_settings

    forwarded_auth = get_request_auth_header()
    if forwarded_auth:
        return {"Authorization": forwarded_auth}

    api_key = (
        os.environ.get("DOMINO_API_KEY")
        or os.environ.get("DOMINO_USER_API_KEY")
        or get_settings().effective_api_key
    )
    if api_key:
        return {"X-Domino-Api-Key": api_key}

    return {}


async def _fetch_user() -> Optional[User]:
    """Fetch the current Domino user via a direct httpx call.

    Uses a simple async request with proper client cleanup instead of
    the generated API client, which leaks httpx connections.
    """
    try:
        base_url = resolve_domino_api_host()
        headers = _build_auth_headers()

        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{base_url}/api/users/v1/self", headers=headers)

        if resp.status_code != 200:
            logger.warning("GET /api/users/v1/self returned %s", resp.status_code)
            return None

        data = resp.json()
        u = data.get("user", {})
        return User(
            id=u.get("id", ""),
            user_name=u.get("userName", ""),
            roles=u.get("roles") or [],
        )
    except Exception:
        logger.debug("Could not fetch viewing user from Domino API", exc_info=True)
        return None


def clear_viewing_user() -> None:
    """Reset the per-request user cache. Must be called after each request."""
    _user_ctx.set(None)


async def resolve_viewing_user() -> Optional[User]:
    """Fetch and cache the viewing user for the current request.

    Called once per request from the auth middleware. Subsequent calls
    within the same request use the cached value via get_viewing_user().
    """
    fetched = await _fetch_user()
    _user_ctx.set(fetched)
    return fetched


def get_viewing_user() -> Optional[User]:
    """Get the current request's cached user. Returns None if not yet resolved."""
    return _user_ctx.get()
