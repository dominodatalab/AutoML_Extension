from enum import Enum


class DominoProjectsApiOnDemandSparkClusterStatusClusterState(str, Enum):
    NOTFOUND = "NotFound"
    PENDING = "Pending"
    READY = "Ready"
    STARTING = "Starting"
    STOPPING = "Stopping"

    def __str__(self) -> str:
        return str(self.value)
