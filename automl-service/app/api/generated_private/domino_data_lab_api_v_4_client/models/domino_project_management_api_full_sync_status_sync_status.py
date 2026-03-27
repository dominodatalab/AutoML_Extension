from enum import Enum


class DominoProjectManagementApiFullSyncStatusSyncStatus(str, Enum):
    COMPLETED = "Completed"
    FAILED = "Failed"
    INPROGRESS = "InProgress"

    def __str__(self) -> str:
        return str(self.value)
