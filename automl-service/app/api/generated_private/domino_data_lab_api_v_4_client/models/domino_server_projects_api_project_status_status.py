from enum import Enum


class DominoServerProjectsApiProjectStatusStatus(str, Enum):
    ACTIVE = "active"
    COMPLETE = "complete"

    def __str__(self) -> str:
        return str(self.value)
