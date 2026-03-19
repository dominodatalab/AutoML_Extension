"""This is a per request cache for the viewing user"""

import logging
from dataclasses import dataclass
from typing import Optional
from contextvars import ContextVar

from app.core.domino_http import get_domino_public_api_client_sync
from app.api.generated.domino_public_api_client.api.users import get_current_user
from app.api.generated.domino_public_api_client.models.user_envelope_v1 import (
    UserEnvelopeV1,
)

logger = logging.getLogger(__name__)


@dataclass
class User:
    id: str
    user_name: str
    roles: list[str]


_user_ctx: ContextVar[Optional[User]] = ContextVar("viewing_user", default=None)


async def _fetch_user() -> Optional[User]:
    """Fetch the current Domino user via the public API client.
    Uses the per-request Authorization header if present; otherwise falls back
    to a configured Domino API key. Returns None if user info cannot be fetched.
    """
    try:
        client = get_domino_public_api_client_sync()

        resp = await get_current_user.asyncio(client=client)
        if not isinstance(resp, UserEnvelopeV1):
            logger.warning("Unexpected response from get_current_user: %s", type(resp).__name__)
            return None

        u = resp.user
        roles: list[str] = u.roles or []
        return User(id=u.id, user_name=u.user_name, roles=roles)
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
