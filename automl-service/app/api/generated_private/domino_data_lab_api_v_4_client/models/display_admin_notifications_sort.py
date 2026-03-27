from enum import Enum


class DisplayAdminNotificationsSort(str, Enum):
    CREATED = "created"
    END = "end"
    MESSAGE = "message"
    PRIORITY = "priority"
    START = "start"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
