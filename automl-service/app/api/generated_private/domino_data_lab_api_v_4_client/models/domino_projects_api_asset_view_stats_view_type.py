from enum import Enum


class DominoProjectsApiAssetViewStatsViewType(str, Enum):
    ALLVIEW = "allView"
    LAST24H = "last24H"

    def __str__(self) -> str:
        return str(self.value)
