"""Tests for Casbin-backed authorization helpers."""

from app.core.context import user as user_ctx


def _make_user(*roles: str) -> user_ctx.User:
    """Create a test user with the provided roles."""
    return user_ctx.User(id="u-1", user_name="alice", roles=list(roles))


def test_sysadmin_role_can_modify_storage():
    """SysAdmin should receive storage-modify permission via Casbin policy."""
    from app.core.authorization import can_modify_storage

    assert can_modify_storage(_make_user("SysAdmin")) is True


def test_non_sysadmin_role_cannot_modify_storage():
    """Roles without the storage-admin capability should be denied."""
    from app.core.authorization import can_modify_storage

    assert can_modify_storage(_make_user("Practitioner")) is False


def test_any_matching_role_grants_permission():
    """Permission should be granted when any assigned role matches policy."""
    from app.core.authorization import can_modify_storage

    assert can_modify_storage(_make_user("Practitioner", "SysAdmin")) is True
