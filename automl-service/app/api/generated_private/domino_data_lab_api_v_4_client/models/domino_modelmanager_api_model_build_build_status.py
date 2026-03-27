from enum import Enum


class DominoModelmanagerApiModelBuildBuildStatus(str, Enum):
    BUILDING = "building"
    COMPLETE = "complete"
    FAILED = "failed"
    PREPARING = "preparing"

    def __str__(self) -> str:
        return str(self.value)
