from enum import Enum


class DominoWorkspaceApiWorkspaceConfigDtoCapacityType(str, Enum):
    ON_DEMAND = "on-demand"
    SPOT = "spot"

    def __str__(self) -> str:
        return str(self.value)
