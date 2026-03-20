from __future__ import annotations
from enum import Enum


class ModelApiSourceType(str, Enum):
    FILE = "File"
    REGISTRY = "Registry"

    def __str__(self) -> str:
        return str(self.value)
