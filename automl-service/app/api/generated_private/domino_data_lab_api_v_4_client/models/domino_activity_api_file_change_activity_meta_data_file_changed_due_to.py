from enum import Enum


class DominoActivityApiFileChangeActivityMetaDataFileChangedDueTo(str, Enum):
    USER = "user"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
