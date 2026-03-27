from enum import Enum


class DominoComputegridMonitoredResourceExecutionCheckpointStatus(str, Enum):
    COMPLETED = "Completed"
    ERROR = "Error"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
