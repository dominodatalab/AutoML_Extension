from enum import Enum


class DominoProjectsApiProjectPortfolioPaginationFilterSortBy(str, Enum):
    CENTSPERMINUTE = "centsPerMinute"
    COLLABORATORS = "collaborators"
    CREATEDON = "createdOn"
    DURATION = "duration"
    LASTACTIVITY = "lastActivity"
    PROJECTNAME = "projectName"
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
