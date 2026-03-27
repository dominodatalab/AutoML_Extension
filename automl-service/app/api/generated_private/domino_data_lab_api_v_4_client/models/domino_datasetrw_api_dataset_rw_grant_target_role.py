from enum import Enum


class DominoDatasetrwApiDatasetRwGrantTargetRole(str, Enum):
    DATASETRWEDITOR = "DatasetRwEditor"
    DATASETRWOWNER = "DatasetRwOwner"
    DATASETRWREADER = "DatasetRwReader"

    def __str__(self) -> str:
        return str(self.value)
