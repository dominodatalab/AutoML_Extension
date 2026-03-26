from __future__ import annotations
from enum import Enum


class CostActivationStatusV1(str, Enum):
    FULL = "Full"
    PARTIAL = "Partial"

    def __str__(self) -> str:
        return str(self.value)
