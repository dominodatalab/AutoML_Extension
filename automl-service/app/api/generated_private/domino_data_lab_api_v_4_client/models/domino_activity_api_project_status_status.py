from enum import Enum


class DominoActivityApiProjectStatusStatus(str, Enum):
    ACTIVE = "active"
    COMPLETE = "complete"

    def __str__(self) -> str:
        return str(self.value)
