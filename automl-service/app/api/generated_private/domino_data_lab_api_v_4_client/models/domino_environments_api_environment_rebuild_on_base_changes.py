from enum import Enum


class DominoEnvironmentsApiEnvironmentRebuildOnBaseChanges(str, Enum):
    FOLLOWACTIVE = "FollowActive"
    NEVER = "Never"

    def __str__(self) -> str:
        return str(self.value)
