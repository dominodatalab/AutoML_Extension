from enum import Enum


class DominoNucleusProjectProjectSettingsDtoSparkClusterMode(str, Enum):
    LOCAL = "Local"
    ONDEMAND = "OnDemand"
    STANDALONE = "Standalone"
    YARN = "Yarn"

    def __str__(self) -> str:
        return str(self.value)
