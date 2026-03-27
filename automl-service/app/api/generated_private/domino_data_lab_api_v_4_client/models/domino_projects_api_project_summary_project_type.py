from enum import Enum


class DominoProjectsApiProjectSummaryProjectType(str, Enum):
    ANALYTIC = "Analytic"
    TEMPLATE = "Template"

    def __str__(self) -> str:
        return str(self.value)
