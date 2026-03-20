from enum import Enum


class ProjectStatusV1Status(str, Enum):
    ACTIVE = "active"
    COMPLETE = "complete"

    def __str__(self) -> str:
        return str(self.value)
