from enum import Enum


class DominoWorkspacesApiExecutionCheckpointStatusStatus(str, Enum):
    COMPLETED = "Completed"
    ERROR = "Error"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
