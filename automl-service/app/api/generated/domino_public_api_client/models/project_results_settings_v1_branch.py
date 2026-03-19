from enum import Enum


class ProjectResultsSettingsV1Branch(str, Enum):
    ISOLATED = "isolated"
    MAIN = "main"

    def __str__(self) -> str:
        return str(self.value)
