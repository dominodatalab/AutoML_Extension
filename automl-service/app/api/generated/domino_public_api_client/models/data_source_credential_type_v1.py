from __future__ import annotations
from enum import Enum


class DataSourceCredentialTypeV1(str, Enum):
    INDIVIDUAL = "Individual"
    SHARED = "Shared"

    def __str__(self) -> str:
        return str(self.value)
