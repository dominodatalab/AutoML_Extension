"""Shared utility helpers."""

import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


def utc_now() -> datetime:
    """Return the current time as a timezone-aware UTC datetime."""
    return datetime.now(timezone.utc)
