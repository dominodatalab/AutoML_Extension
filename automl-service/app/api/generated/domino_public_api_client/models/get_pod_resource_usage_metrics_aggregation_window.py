from enum import Enum


class GetPodResourceUsageMetricsAggregationWindow(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"

    def __str__(self) -> str:
        return str(self.value)
