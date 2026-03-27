from enum import Enum


class DominoComputegridMonitoredResourceExecutionCheckpointCombinedResourceStatus(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    READY = "READY"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
