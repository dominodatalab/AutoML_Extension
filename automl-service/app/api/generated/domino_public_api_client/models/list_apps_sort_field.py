from enum import Enum


class ListAppsSortField(str, Enum):
    LASTUPDATED = "lastUpdated"
    LASTVIEWED = "lastViewed"
    NAME = "name"
    STATUS = "status"
    VIEWS = "views"

    def __str__(self) -> str:
        return str(self.value)
