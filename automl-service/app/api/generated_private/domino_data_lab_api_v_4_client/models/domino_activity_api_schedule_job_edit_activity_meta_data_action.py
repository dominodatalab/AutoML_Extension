from enum import Enum


class DominoActivityApiScheduleJobEditActivityMetaDataAction(str, Enum):
    EDITED = "edited"
    PAUSED = "paused"
    SCHEDULED = "scheduled"
    UNPAUSED = "unpaused"
    UNSCHEDULED = "unscheduled"

    def __str__(self) -> str:
        return str(self.value)
