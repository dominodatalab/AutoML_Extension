from enum import Enum


class DominoWorkspaceApiWorkspaceSessionEndDtoExitStatus(str, Enum):
    ERROR = "Error"
    FAILED = "Failed"
    STOPPED = "Stopped"
    SUCCEEDED = "Succeeded"

    def __str__(self) -> str:
        return str(self.value)
