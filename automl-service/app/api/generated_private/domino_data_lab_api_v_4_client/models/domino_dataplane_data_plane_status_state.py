from enum import Enum


class DominoDataplaneDataPlaneStatusState(str, Enum):
    DISCONNECTED = "Disconnected"
    ERROR = "Error"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"

    def __str__(self) -> str:
        return str(self.value)
