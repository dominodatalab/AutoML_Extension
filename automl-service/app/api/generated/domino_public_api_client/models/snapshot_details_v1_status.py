from enum import Enum


class SnapshotDetailsV1Status(str, Enum):
    ACTIVE = "active"
    COPYING = "copying"
    DELETED = "deleted"
    DELETIONINPROGRESS = "deletionInProgress"
    FAILED = "failed"
    MARKFORDELETION = "markForDeletion"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
