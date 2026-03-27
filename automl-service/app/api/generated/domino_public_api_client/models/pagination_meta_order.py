from __future__ import annotations
from enum import Enum


class PaginationMetaOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"

    def __str__(self) -> str:
        return str(self.value)
