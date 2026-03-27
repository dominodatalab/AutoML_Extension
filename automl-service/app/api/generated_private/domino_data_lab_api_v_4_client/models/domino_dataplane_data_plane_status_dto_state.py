from enum import Enum


class DominoDataplaneDataPlaneStatusDtoState(str, Enum):
    DISCONNECTED = "Disconnected"
    ERROR = "Error"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"

    def __str__(self) -> str:
        return str(self.value)
