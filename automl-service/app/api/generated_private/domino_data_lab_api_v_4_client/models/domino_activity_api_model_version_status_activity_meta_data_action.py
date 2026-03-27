from enum import Enum


class DominoActivityApiModelVersionStatusActivityMetaDataAction(str, Enum):
    DESTROYED = "destroyed"
    PUBLISHED = "published"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
