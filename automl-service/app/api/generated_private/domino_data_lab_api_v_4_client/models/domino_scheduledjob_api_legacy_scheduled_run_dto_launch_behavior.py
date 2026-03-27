from enum import Enum


class DominoScheduledjobApiLegacyScheduledRunDTOLaunchBehavior(str, Enum):
    CONCURRENT = "Concurrent"
    SEQUENTIAL = "Sequential"

    def __str__(self) -> str:
        return str(self.value)
