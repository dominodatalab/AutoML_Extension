from enum import Enum


class DisplayAdminNotificationsPriority(str, Enum):
    CRITICAL = "Critical"
    DEFAULT = "Default"

    def __str__(self) -> str:
        return str(self.value)
