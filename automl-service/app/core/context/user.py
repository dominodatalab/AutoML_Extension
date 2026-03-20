"""This is a per request cache for the viewing user"""

from dataclasses import dataclass
from typing import Optional
from contextvars import ContextVar

from app.core.domino_http import get_domino_public_api_client_sync
from app.api.generated.domino_public_api_client.api.users import get_current_user
from app.api.generated.domino_public_api_client.models.user_envelope_v1 import (
    UserEnvelopeV1,
)


@dataclass
class User:
    id: str
    user_name: str
    roles: list[str]


_user_ctx: ContextVar[Optional[User]] = ContextVar("viewing_user", default=None)


def _fetch_user() -> Optional[User]:
    """fetch the current Domino user via the public API client.
    Uses the per-request Authorization header if present; otherwise falls back
    to a configured Domino API key. Returns None if user info cannot be fetched.
    """

    client = get_domino_public_api_client_sync()

    resp = get_current_user.sync(client=client)
    if not isinstance(resp, UserEnvelopeV1):
        raise Exception(str(resp))

    u = resp.user
    roles: list[str] = u.roles or []
    return User(id=u.id, user_name=u.user_name, roles=roles)


def clear_viewing_user() -> None:
    """Clear the cached user so the next request starts fresh."""
    _user_ctx.set(None)


def get_viewing_user() -> Optional[User]:
    """Get the current request's user, fetching once per context."""
    cached = _user_ctx.get()
    if cached is not None:
        return cached

    fetched = _fetch_user()
    _user_ctx.set(fetched)
    return fetched
