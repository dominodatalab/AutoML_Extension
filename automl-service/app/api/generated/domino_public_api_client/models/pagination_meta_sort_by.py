from __future__ import annotations
from enum import Enum


class PaginationMetaSortBy(str, Enum):
    CREATEDAT = "createdAt"

    def __str__(self) -> str:
        return str(self.value)
