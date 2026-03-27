from enum import Enum


class DominoDatasetrwApiDatasetRwGrantDetailsTargetRole(str, Enum):
    DATASETRWEDITOR = "DatasetRwEditor"
    DATASETRWOWNER = "DatasetRwOwner"
    DATASETRWREADER = "DatasetRwReader"

    def __str__(self) -> str:
        return str(self.value)
