from enum import Enum


class DominoServerProjectsApiProjectGatewaySummaryProjectType(str, Enum):
    ANALYTIC = "Analytic"
    DATASET = "DataSet"
    TEMPLATE = "Template"

    def __str__(self) -> str:
        return str(self.value)
