from enum import Enum


class DominoComputegridExecutionEventDtoSource(str, Enum):
    DOMINO = "Domino"
    KUBERNETES = "Kubernetes"
    METRICS = "Metrics"

    def __str__(self) -> str:
        return str(self.value)
