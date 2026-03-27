from enum import Enum


class CountMetricsMetricType(str, Enum):
    COUNTER = "Counter"
    GAUGE = "Gauge"
    HISTOGRAM = "Histogram"
    TIMER = "Timer"

    def __str__(self) -> str:
        return str(self.value)
