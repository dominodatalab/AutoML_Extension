from enum import Enum


class DominoAdminInterfaceComputeClusterPodOverviewDeployableObjectType(str, Enum):
    CONTAINER = "Container"
    POD = "Pod"

    def __str__(self) -> str:
        return str(self.value)
