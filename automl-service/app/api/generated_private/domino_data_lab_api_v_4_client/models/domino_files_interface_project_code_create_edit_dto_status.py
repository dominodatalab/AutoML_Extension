from enum import Enum


class DominoFilesInterfaceProjectCodeCreateEditDtoStatus(str, Enum):
    ACTIVE = "Active"
    DELETED = "Deleted"
    LARGE = "Large"
    NEW = "New"

    def __str__(self) -> str:
        return str(self.value)
