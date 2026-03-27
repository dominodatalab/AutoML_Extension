from __future__ import annotations
from enum import Enum


class AggregationWindowV1(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"
    VALUE_0 = "5min"

    def __str__(self) -> str:
        return str(self.value)
