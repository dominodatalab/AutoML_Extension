from enum import Enum


class ModelDeploymentStatusState(str, Enum):
    DELETED = "DELETED"
    DELETING = "DELETING"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    STARTING = "STARTING"
    STOPPED = "STOPPED"
    STOPPING = "STOPPING"
    UPDATING = "UPDATING"

    def __str__(self) -> str:
        return str(self.value)
