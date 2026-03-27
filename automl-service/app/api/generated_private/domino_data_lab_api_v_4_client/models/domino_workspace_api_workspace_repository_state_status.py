from enum import Enum


class DominoWorkspaceApiWorkspaceRepositoryStateStatus(str, Enum):
    CLEAN = "Clean"
    MODIFIED = "Modified"
    UNKNOWN = "Unknown"
    UNPUSHED = "Unpushed"
    UNPUSHEDDIRTY = "UnpushedDirty"

    def __str__(self) -> str:
        return str(self.value)
