from enum import Enum


class DominoDatasetrwApiDatasetRwProjectMountDtoSizeStatus(str, Enum):
    ACTIVE = "Active"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
