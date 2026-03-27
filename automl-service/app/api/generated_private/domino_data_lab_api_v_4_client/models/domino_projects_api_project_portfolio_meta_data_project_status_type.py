from enum import Enum


class DominoProjectsApiProjectPortfolioMetaDataProjectStatusType(str, Enum):
    ACTIVE = "active"
    COMPLETE = "complete"

    def __str__(self) -> str:
        return str(self.value)
