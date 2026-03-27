from __future__ import annotations
from enum import Enum


class TargetRangeV1Condition(str, Enum):
    BETWEEN = "between"
    GREATERTHAN = "greaterThan"
    GREATERTHANEQUAL = "greaterThanEqual"
    LESSTHAN = "lessThan"
    LESSTHANEQUAL = "lessThanEqual"

    def __str__(self) -> str:
        return str(self.value)
