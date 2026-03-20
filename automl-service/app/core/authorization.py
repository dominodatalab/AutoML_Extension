"""Casbin-backed authorization helpers for role-gated features."""

from __future__ import annotations

import logging
from functools import lru_cache
from pathlib import Path
from typing import Optional

import casbin
from fastapi import HTTPException

from app.core.context import user as user_ctx

logger = logging.getLogger(__name__)

AUTHZ_MODEL_PATH = Path(__file__).with_name("authorization_model.conf")
AUTHZ_POLICY_PATH = Path(__file__).with_name("authorization_policy.csv")

STORAGE_RESOURCE = "storage"
MODIFY_ACTION = "modify"


def _role_subject(role: str) -> str:
    """Normalize external Domino role names into Casbin subjects."""
    return f"role:{role}"


@lru_cache(maxsize=1)
def get_authorization_enforcer() -> casbin.Enforcer:
    """Create the shared Casbin enforcer for application authorization checks."""
    return casbin.Enforcer(str(AUTHZ_MODEL_PATH), str(AUTHZ_POLICY_PATH))


def user_has_permission(
    user: Optional[user_ctx.User],
    resource: str,
    action: str,
) -> bool:
    """Return True when any assigned role grants the requested permission."""
    if user is None:
        return False

    enforcer = get_authorization_enforcer()
    return any(
        enforcer.enforce(_role_subject(role), resource, action)
        for role in (user.roles or [])
    )


def current_user_can(resource: str, action: str) -> bool:
    """Return True when the current viewing user may perform the action."""
    try:
        return user_has_permission(user_ctx.get_viewing_user(), resource, action)
    except Exception:
        logger.exception(
            "Failed to resolve current user permissions for %s:%s",
            resource,
            action,
        )
        return False


def can_modify_storage(user: Optional[user_ctx.User]) -> bool:
    """Return True when the given user may modify storage."""
    return user_has_permission(user, STORAGE_RESOURCE, MODIFY_ACTION)


def current_user_can_modify_storage() -> bool:
    """Return True when the current viewing user may modify storage."""
    return current_user_can(STORAGE_RESOURCE, MODIFY_ACTION)


def require_permission(resource: str, action: str) -> None:
    """Raise 403 unless the current viewing user has the requested permission."""
    if not current_user_can(resource, action):
        raise HTTPException(
            status_code=403,
            detail=f"This operation requires permission to {action} {resource}.",
        )


def require_storage_modify() -> None:
    """Raise 403 unless the current viewing user may modify storage."""
    require_permission(STORAGE_RESOURCE, MODIFY_ACTION)
