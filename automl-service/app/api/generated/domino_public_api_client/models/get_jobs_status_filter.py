from enum import Enum


class GetJobsStatusFilter(str, Enum):
    ACTIVE = "active"
    ALL = "all"
    ARCHIVED = "archived"
    COMPLETED = "completed"
    QUEUED = "queued"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
