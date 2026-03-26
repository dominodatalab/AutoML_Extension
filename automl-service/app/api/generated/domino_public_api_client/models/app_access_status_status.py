from __future__ import annotations
from enum import Enum


class AppAccessStatusStatus(str, Enum):
    ALLOWED = "ALLOWED"
    DENIED = "DENIED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
