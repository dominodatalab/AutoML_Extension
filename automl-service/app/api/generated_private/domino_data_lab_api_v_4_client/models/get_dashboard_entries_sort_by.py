from enum import Enum


class GetDashboardEntriesSortBy(str, Enum):
    CREATED = "created"
    NAME = "name"
    OWNERID = "ownerId"

    def __str__(self) -> str:
        return str(self.value)
