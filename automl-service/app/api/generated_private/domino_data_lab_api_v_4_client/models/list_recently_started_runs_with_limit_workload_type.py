from enum import Enum


class ListRecentlyStartedRunsWithLimitWorkloadType(str, Enum):
    JOB = "job"
    OTHER = "other"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
