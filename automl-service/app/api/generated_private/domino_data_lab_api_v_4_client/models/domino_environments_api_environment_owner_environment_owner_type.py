from enum import Enum


class DominoEnvironmentsApiEnvironmentOwnerEnvironmentOwnerType(str, Enum):
    INDIVIDUAL = "Individual"
    ORGANIZATION = "Organization"

    def __str__(self) -> str:
        return str(self.value)
