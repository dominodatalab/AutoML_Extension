from enum import Enum


class DominoDatasetrwWebFileCollisionRequestFileCollisionSetting(str, Enum):
    IGNORE = "Ignore"
    OVERWRITE = "Overwrite"
    RENAME = "Rename"

    def __str__(self) -> str:
        return str(self.value)
