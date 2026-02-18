"""Centralized error-handling decorator for FastAPI route handlers.

Eliminates repetitive try/except blocks across route files by providing
a decorator that catches exceptions, logs them, and returns appropriate
HTTP responses.
"""

import asyncio
import functools
import logging
from typing import Optional

from fastapi import HTTPException

logger = logging.getLogger(__name__)


def handle_errors(
    error_message_prefix: Optional[str] = None,
    detail_prefix: Optional[str] = None,
):
    """Decorator that wraps a route handler with standard error handling.

    Behavior:
    - Re-raises HTTPException as-is (no double-wrapping).
    - Converts FileNotFoundError to HTTPException(404).
    - Converts ValueError to HTTPException(400).
    - Converts all other exceptions to HTTPException(500) and logs them.
    - Works with both sync and async route handlers.

    Args:
        error_message_prefix: Optional prefix for the log message.
            If not provided, the function name is used.
        detail_prefix: Optional prefix prepended to the HTTPException detail
            for generic 500 errors. When set, the detail becomes
            ``f"{detail_prefix}: {e}"`` instead of just ``str(e)``.
            Also applied to FileNotFoundError (404) and ValueError (400)
            details when present.

    Usage::

        @router.get("/items")
        @handle_errors("Error fetching items")
        async def get_items():
            ...

        @router.get("/datasets")
        @handle_errors("Failed to list", detail_prefix="Failed to list datasets")
        async def list_datasets():
            ...
    """
    def decorator(func):
        log_prefix = error_message_prefix or func.__name__

        def _detail(e: Exception) -> str:
            if detail_prefix:
                return f"{detail_prefix}: {e}"
            return str(e)

        def _handle_exception(e: Exception) -> None:
            if isinstance(e, HTTPException):
                raise
            if isinstance(e, FileNotFoundError):
                raise HTTPException(status_code=404, detail=_detail(e))
            if isinstance(e, ValueError):
                raise HTTPException(status_code=400, detail=_detail(e))
            logger.error(f"{log_prefix}: {e}")
            raise HTTPException(status_code=500, detail=_detail(e))

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                _handle_exception(e)

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                _handle_exception(e)

        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return decorator
