from enum import Enum


class DominoEnvironmentsApiVisibilityUpdateRequestVisibility(str, Enum):
    GLOBAL = "Global"
    ORGANIZATION = "Organization"
    PRIVATE = "Private"

    def __str__(self) -> str:
        return str(self.value)
