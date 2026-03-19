from enum import Enum


class GetVllmTokenMetricsAggregationWindow(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"

    def __str__(self) -> str:
        return str(self.value)
