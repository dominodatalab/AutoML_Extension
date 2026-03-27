from enum import Enum


class DominoActivityApiProjectGoalFileLinkActivityMetadataAction(str, Enum):
    ADDED = "added"
    REMOVED = "removed"

    def __str__(self) -> str:
        return str(self.value)
