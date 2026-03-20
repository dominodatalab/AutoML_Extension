from __future__ import annotations
from enum import Enum


class WriteTypeV1(str, Enum):
    CREATE = "Create"
    FORCEIMPORT = "ForceImport"
    IMPORT = "Import"

    def __str__(self) -> str:
        return str(self.value)
