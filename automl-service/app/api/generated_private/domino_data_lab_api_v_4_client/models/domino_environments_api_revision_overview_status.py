from enum import Enum


class DominoEnvironmentsApiRevisionOverviewStatus(str, Enum):
    BUILDING = "Building"
    FAILED = "Failed"
    KILLED = "Killed"
    PULLING = "Pulling"
    PUSHING = "Pushing"
    QUEUED = "Queued"
    STARTING = "Starting"
    SUCCEEDED = "Succeeded"

    def __str__(self) -> str:
        return str(self.value)
