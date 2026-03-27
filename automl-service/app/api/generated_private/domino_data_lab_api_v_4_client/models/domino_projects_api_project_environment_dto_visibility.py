from enum import Enum


class DominoProjectsApiProjectEnvironmentDTOVisibility(str, Enum):
    GLOBAL = "Global"
    ORGANIZATION = "Organization"
    PRIVATE = "Private"

    def __str__(self) -> str:
        return str(self.value)
