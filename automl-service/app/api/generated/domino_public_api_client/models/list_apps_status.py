from __future__ import annotations
from enum import Enum


class ListAppsStatus(str, Enum):
    BUILDING = "Building"
    ERROR = "Error"
    FAILED = "Failed"
    FINISHING = "Finishing"
    PENDING = "Pending"
    PREPARING = "Preparing"
    PULLING = "Pulling"
    QUEUED = "Queued"
    RUNNING = "Running"
    SCHEDULED = "Scheduled"
    SERVING = "Serving"
    STOPANDDISCARDREQUESTED = "StopAndDiscardRequested"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    STOPREQUESTED = "StopRequested"
    SUCCEEDED = "Succeeded"

    def __str__(self) -> str:
        return str(self.value)
