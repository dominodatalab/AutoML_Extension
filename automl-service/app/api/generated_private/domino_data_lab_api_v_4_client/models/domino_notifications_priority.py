from enum import Enum


class DominoNotificationsPriority(str, Enum):
    CRITICAL = "Critical"
    DEFAULT = "Default"

    def __str__(self) -> str:
        return str(self.value)
