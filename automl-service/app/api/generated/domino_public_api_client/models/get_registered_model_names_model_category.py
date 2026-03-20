from __future__ import annotations
from enum import Enum


class GetRegisteredModelNamesModelCategory(str, Enum):
    GENAI = "genai"
    ML = "ml"

    def __str__(self) -> str:
        return str(self.value)
