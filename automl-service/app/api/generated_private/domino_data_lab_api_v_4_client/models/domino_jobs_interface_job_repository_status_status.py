from enum import Enum


class DominoJobsInterfaceJobRepositoryStatusStatus(str, Enum):
    CLEAN = "Clean"
    MODIFIED = "Modified"
    UNKNOWN = "Unknown"
    UNPUSHED = "Unpushed"
    UNPUSHED_AND_DIRTY = "Unpushed and Dirty"

    def __str__(self) -> str:
        return str(self.value)
