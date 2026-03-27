from __future__ import annotations
from enum import Enum


class GetJobsSortBy(str, Enum):
    COMMAND = "command"
    COMMENTCOUNT = "commentCount"
    DOMINOSTATSFIELD = "dominoStatsField"
    DURATION = "duration"
    NUMBER = "number"
    STARTEDTIME = "startedTime"
    STATUS = "status"
    TITLE = "title"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
