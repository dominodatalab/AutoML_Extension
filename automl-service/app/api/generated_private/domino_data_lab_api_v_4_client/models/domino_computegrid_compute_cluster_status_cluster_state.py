from enum import Enum


class DominoComputegridComputeClusterStatusClusterState(str, Enum):
    NONEXISTENT = "NonExistent"
    PENDING = "Pending"
    READY = "Ready"
    STARTING = "Starting"
    STOPPING = "Stopping"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
