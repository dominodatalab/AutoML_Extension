from enum import Enum


class DominoProjectsApiEnvironmentOwnerEnvironmentOwnerType(str, Enum):
    INDIVIDUAL = "Individual"
    ORGANIZATION = "Organization"

    def __str__(self) -> str:
        return str(self.value)
