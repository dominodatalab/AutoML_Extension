from enum import Enum


class DominoComputegridMonitoredExecutionResourceStartupStatus(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    READY = "READY"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
