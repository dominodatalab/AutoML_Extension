from __future__ import annotations
from enum import Enum


class AppProjectResponseProjectType(str, Enum):
    ANALYTIC = "Analytic"
    DATASET = "Dataset"
    TEMPLATE = "Template"

    def __str__(self) -> str:
        return str(self.value)
