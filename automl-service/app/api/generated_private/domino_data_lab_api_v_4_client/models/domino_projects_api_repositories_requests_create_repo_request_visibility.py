from enum import Enum


class DominoProjectsApiRepositoriesRequestsCreateRepoRequestVisibility(str, Enum):
    INTERNAL = "Internal"
    PRIVATE = "Private"
    PUBLIC = "Public"

    def __str__(self) -> str:
        return str(self.value)
