from __future__ import annotations
from enum import Enum


class InformationV1Units(str, Enum):
    GB = "GB"
    GIB = "GiB"
    MB = "MB"
    MIB = "MiB"

    def __str__(self) -> str:
        return str(self.value)
