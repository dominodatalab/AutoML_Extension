from enum import Enum


class DominoProjectsApiStatusStatName(str, Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    COMPLETE = "complete"

    def __str__(self) -> str:
        return str(self.value)
