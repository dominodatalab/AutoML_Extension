from enum import Enum


class RegisteredModelVersionDetailsV2BuildStatus(str, Enum):
    BUILDING = "Building"
    FAILED = "Failed"
    KILLED = "Killed"
    QUEUED = "Queued"
    STARTING = "Starting"
    SUCCEEDED = "Succeeded"

    def __str__(self) -> str:
        return str(self.value)
