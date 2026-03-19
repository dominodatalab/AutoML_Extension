from enum import Enum


class GetVllmLatencyMetricsAggregationWindow(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"

    def __str__(self) -> str:
        return str(self.value)
