"""Per-request context helpers for forwarded auth headers."""
from __future__ import annotations

from contextvars import ContextVar
import logging
from typing import Optional
import re

logger = logging.getLogger(__name__)

AUTH_TOKEN_EXTRACT_PATTERN = r'bearer\s+(.*)'

_auth_header_var: ContextVar[Optional[str]] = ContextVar("forwarded_authorization_header", default=None)
_token_var: ContextVar[Optional[str]] = ContextVar("forwarded_authorization_token", default=None)


def set_request_auth_header(value: Optional[str]) -> None:
    _auth_header_var.set(value)

    if value is None:
        _token_var.set(None)
        return

    found = re.search(AUTH_TOKEN_EXTRACT_PATTERN, value.strip(), re.IGNORECASE)
    if not found:
        logger.debug("Could not extract token from auth header")
        _token_var.set(None)
        return

    _token_var.set(found.group(1))


def get_request_auth_header() -> Optional[str]:
    return _auth_header_var.get()

def get_request_auth_token() -> Optional[str]:
    return _token_var.get()
