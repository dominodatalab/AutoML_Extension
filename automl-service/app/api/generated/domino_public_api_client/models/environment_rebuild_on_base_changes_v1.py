from enum import Enum


class EnvironmentRebuildOnBaseChangesV1(str, Enum):
    FOLLOWACTIVE = "followActive"
    NEVER = "never"

    def __str__(self) -> str:
        return str(self.value)
