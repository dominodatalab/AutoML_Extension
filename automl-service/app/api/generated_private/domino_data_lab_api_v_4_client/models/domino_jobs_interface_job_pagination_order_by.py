from enum import Enum


class DominoJobsInterfaceJobPaginationOrderBy(str, Enum):
    COMMAND = "command"
    COMMENTCOUNT = "commentCount"
    DOMINOSTATSFIELD = "dominoStatsField"
    DURATION = "duration"
    NUMBER = "number"
    NUMBERASDOUBLE = "numberAsDouble"
    QUEUED = "queued"
    STATUS = "status"
    TITLE = "title"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
