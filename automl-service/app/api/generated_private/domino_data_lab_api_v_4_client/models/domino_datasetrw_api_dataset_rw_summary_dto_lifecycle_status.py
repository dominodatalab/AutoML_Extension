from enum import Enum


class DominoDatasetrwApiDatasetRwSummaryDtoLifecycleStatus(str, Enum):
    ACTIVE = "Active"
    DELETED = "Deleted"
    DELETIONINPROGRESS = "DeletionInProgress"
    FAILED = "Failed"
    MARKEDFORDELETION = "MarkedForDeletion"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
