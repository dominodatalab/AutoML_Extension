from enum import Enum


class DominoDatasetrwApiDatasetRwSnapshotDtoLifecycleStatus(str, Enum):
    ACTIVE = "Active"
    COPYING = "Copying"
    DELETED = "Deleted"
    DELETIONINPROGRESS = "DeletionInProgress"
    FAILED = "Failed"
    MARKEDFORDELETION = "MarkedForDeletion"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
