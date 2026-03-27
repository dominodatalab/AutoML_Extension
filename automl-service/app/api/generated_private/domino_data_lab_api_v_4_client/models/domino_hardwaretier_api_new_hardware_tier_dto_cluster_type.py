from enum import Enum


class DominoHardwaretierApiNewHardwareTierDtoClusterType(str, Enum):
    CLASSICAWS = "ClassicAWS"
    CLASSICONPREMISES = "ClassicOnPremises"
    KUBERNETES = "Kubernetes"

    def __str__(self) -> str:
        return str(self.value)
