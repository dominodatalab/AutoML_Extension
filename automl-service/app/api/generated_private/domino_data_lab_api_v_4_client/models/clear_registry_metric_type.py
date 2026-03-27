from enum import Enum


class ClearRegistryMetricType(str, Enum):
    COUNTER = "Counter"
    GAUGE = "Gauge"
    HISTOGRAM = "Histogram"
    TIMER = "Timer"

    def __str__(self) -> str:
        return str(self.value)
