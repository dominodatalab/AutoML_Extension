from __future__ import annotations
from enum import Enum


class EnvironmentOwnerTypeV1(str, Enum):
    INDIVIDUAL = "individual"
    ORGANIZATION = "organization"

    def __str__(self) -> str:
        return str(self.value)
