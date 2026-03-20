from enum import Enum


class EnvironmentVisibilityV1(str, Enum):
    GLOBAL = "global"
    ORGANIZATION = "organization"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
