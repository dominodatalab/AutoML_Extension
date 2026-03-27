from enum import Enum


class GetCurrentExecutionsSortBy(str, Enum):
    EXECUTIONID = "executionId"
    HARDWARETIER = "hardwareTier"
    PROJECT = "project"
    STARTED = "started"
    STATUS = "status"
    TITLE = "title"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
