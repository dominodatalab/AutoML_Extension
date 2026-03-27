from enum import Enum


class DominoModelmanagerApiModelBuildLogsStatus(str, Enum):
    BUILDING = "building"
    COMPLETE = "complete"
    FAILED = "failed"
    PREPARING = "preparing"

    def __str__(self) -> str:
        return str(self.value)
