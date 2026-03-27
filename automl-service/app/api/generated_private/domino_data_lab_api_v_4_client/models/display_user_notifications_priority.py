from enum import Enum


class DisplayUserNotificationsPriority(str, Enum):
    CRITICAL = "Critical"
    DEFAULT = "Default"

    def __str__(self) -> str:
        return str(self.value)
