from enum import Enum


class DominoProjectsApiProjectPortfolioPaginationFilterStatusItem(str, Enum):
    ACTIVE = "active"
    COMPLETE = "complete"

    def __str__(self) -> str:
        return str(self.value)
