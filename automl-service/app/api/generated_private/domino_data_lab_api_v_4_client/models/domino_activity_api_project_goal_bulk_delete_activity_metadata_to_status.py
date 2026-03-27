from enum import Enum


class DominoActivityApiProjectGoalBulkDeleteActivityMetadataToStatus(str, Enum):
    COMPLETE = "complete"
    DELETE = "delete"
    INCOMPLETE = "incomplete"

    def __str__(self) -> str:
        return str(self.value)
