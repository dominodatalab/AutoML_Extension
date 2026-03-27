from enum import Enum


class DominoActivityApiScheduleJobActivityMetaDataAction(str, Enum):
    EDITED = "edited"
    PAUSED = "paused"
    SCHEDULED = "scheduled"
    UNPAUSED = "unpaused"
    UNSCHEDULED = "unscheduled"

    def __str__(self) -> str:
        return str(self.value)
