from enum import Enum


class DominoModelmanagerApiModelBuildLogsV2Status(str, Enum):
    BUILDING = "building"
    COMPLETE = "complete"
    FAILED = "failed"
    PREPARING = "preparing"

    def __str__(self) -> str:
        return str(self.value)
