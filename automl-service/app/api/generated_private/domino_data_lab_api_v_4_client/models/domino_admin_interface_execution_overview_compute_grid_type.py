from enum import Enum


class DominoAdminInterfaceExecutionOverviewComputeGridType(str, Enum):
    CLASSICAWS = "ClassicAWS"
    CLASSICONPREMISES = "ClassicOnPremises"
    KUBERNETES = "Kubernetes"

    def __str__(self) -> str:
        return str(self.value)
