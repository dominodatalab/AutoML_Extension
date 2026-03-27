from enum import Enum


class DominoDatasetrwApiDatasetRwSummaryDtoSizeStatus(str, Enum):
    ACTIVE = "Active"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
