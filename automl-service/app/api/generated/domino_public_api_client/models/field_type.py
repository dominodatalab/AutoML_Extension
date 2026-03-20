from __future__ import annotations
from enum import Enum


class FieldType(str, Enum):
    SCALAR = "scalar"
    SEQUENCE = "sequence"

    def __str__(self) -> str:
        return str(self.value)
