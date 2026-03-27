from enum import Enum


class DominoNucleusGatewayUsersModelsProjectDependencyViewProjectType(str, Enum):
    ANALYTIC = "Analytic"
    DATASET = "DataSet"
    TEMPLATE = "Template"

    def __str__(self) -> str:
        return str(self.value)
