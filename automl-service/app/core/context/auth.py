"""Per-request context helpers for forwarded request headers."""
from __future__ import annotations

from contextvars import ContextVar
from typing import Optional

_auth_header_var: ContextVar[Optional[str]] = ContextVar("forwarded_authorization_header", default=None)
_project_id_var: ContextVar[Optional[str]] = ContextVar("forwarded_project_id", default=None)


def set_request_auth_header(value: Optional[str]) -> None:
    _auth_header_var.set(value)


def get_request_auth_header() -> Optional[str]:
    return _auth_header_var.get()


def set_request_project_id(value: Optional[str]) -> None:
    _project_id_var.set(value)


def get_request_project_id() -> Optional[str]:
    return _project_id_var.get()
