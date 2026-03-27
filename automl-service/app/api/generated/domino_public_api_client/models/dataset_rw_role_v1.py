from __future__ import annotations
from enum import Enum


class DatasetRwRoleV1(str, Enum):
    DATASETRWEDITOR = "DatasetRwEditor"
    DATASETRWOWNER = "DatasetRwOwner"
    DATASETRWREADER = "DatasetRwReader"

    def __str__(self) -> str:
        return str(self.value)
