from enum import Enum


class GetGoalsSortField(str, Enum):
    CREATEDAT = "createdAt"
    LASTUPDATEDAT = "lastUpdatedAt"

    def __str__(self) -> str:
        return str(self.value)
