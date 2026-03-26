from __future__ import annotations
from enum import Enum


class SearchRequestRepoType(str, Enum):
    BIOCONDUCTOR = "Bioconductor"
    PYTHON = "Python"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
