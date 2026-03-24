"""Per-request context helpers for forwarded auth headers."""
from __future__ import annotations

from contextvars import ContextVar
from typing import Optional

_auth_header_var: ContextVar[Optional[str]] = ContextVar("forwarded_authorization_header", default=None)


def set_request_auth_header(value: Optional[str]) -> None:
    _auth_header_var.set(value)


def get_request_auth_header() -> Optional[str]:
    return _auth_header_var.get()
