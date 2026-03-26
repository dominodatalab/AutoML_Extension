from __future__ import annotations
"""A client library for accessing Domino Public API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
