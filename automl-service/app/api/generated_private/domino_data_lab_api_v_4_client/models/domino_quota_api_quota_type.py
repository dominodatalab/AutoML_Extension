from enum import Enum


class DominoQuotaApiQuotaType(str, Enum):
    GLOBAL = "Global"
    OVERRIDE = "Override"

    def __str__(self) -> str:
        return str(self.value)
