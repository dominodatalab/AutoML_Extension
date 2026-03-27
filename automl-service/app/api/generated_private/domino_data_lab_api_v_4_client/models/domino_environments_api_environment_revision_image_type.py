from enum import Enum


class DominoEnvironmentsApiEnvironmentRevisionImageType(str, Enum):
    CUSTOMIMAGE = "CustomImage"
    DEFAULTIMAGE = "DefaultImage"
    ENVIRONMENT = "Environment"

    def __str__(self) -> str:
        return str(self.value)
