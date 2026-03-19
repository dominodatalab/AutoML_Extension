from enum import Enum


class NewEnvironmentVisibilityV1(str, Enum):
    GLOBAL = "global"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
