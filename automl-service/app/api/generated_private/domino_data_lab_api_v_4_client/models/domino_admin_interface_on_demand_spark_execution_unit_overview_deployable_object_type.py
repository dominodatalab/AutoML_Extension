from enum import Enum


class DominoAdminInterfaceOnDemandSparkExecutionUnitOverviewDeployableObjectType(str, Enum):
    CONTAINER = "Container"
    POD = "Pod"

    def __str__(self) -> str:
        return str(self.value)
