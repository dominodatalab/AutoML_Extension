from enum import Enum


class DominoModelmanagerApiModelVersionReproduceInWorkspaceDetailsStatus(str, Enum):
    FAILED = "failed"
    NOT_RUNNING = "not_running"
    RUNNING = "running"
    STARTING = "starting"

    def __str__(self) -> str:
        return str(self.value)
