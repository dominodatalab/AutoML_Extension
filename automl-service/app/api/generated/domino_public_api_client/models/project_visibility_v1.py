from __future__ import annotations
from enum import Enum


class ProjectVisibilityV1(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"
    SEARCHABLE = "searchable"

    def __str__(self) -> str:
        return str(self.value)
