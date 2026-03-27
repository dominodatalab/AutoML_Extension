from enum import Enum


class DominoQuotaApiQuotaActionType(str, Enum):
    EMAIL = "Email"
    NOTIFICATION = "Notification"

    def __str__(self) -> str:
        return str(self.value)
