from __future__ import annotations
from enum import Enum


class ModelDetailSourceRegisteredModelType(str, Enum):
    MODELREGISTRY = "MODELREGISTRY"

    def __str__(self) -> str:
        return str(self.value)
