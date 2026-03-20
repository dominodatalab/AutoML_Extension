from __future__ import annotations
from enum import Enum


class AppConfigurationType(str, Enum):
    AISYSTEM = "AISYSTEM"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
