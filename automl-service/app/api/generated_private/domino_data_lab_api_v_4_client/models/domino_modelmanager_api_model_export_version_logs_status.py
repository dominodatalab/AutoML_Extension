from enum import Enum


class DominoModelmanagerApiModelExportVersionLogsStatus(str, Enum):
    COMPLETE = "complete"
    EXPORTING = "exporting"
    FAILED = "failed"
    NOT_TRIGGERED = "not_triggered"
    PREPARING = "preparing"

    def __str__(self) -> str:
        return str(self.value)
