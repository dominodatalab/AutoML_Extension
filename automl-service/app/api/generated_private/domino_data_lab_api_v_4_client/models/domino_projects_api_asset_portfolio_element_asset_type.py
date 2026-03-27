from enum import Enum


class DominoProjectsApiAssetPortfolioElementAssetType(str, Enum):
    APP = "App"
    LAUNCHER = "Launcher"
    MODELAPI = "ModelAPI"
    SCHEDULES = "Schedules"

    def __str__(self) -> str:
        return str(self.value)
