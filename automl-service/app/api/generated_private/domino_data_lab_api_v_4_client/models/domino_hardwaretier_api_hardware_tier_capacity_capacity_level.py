from enum import Enum


class DominoHardwaretierApiHardwareTierCapacityCapacityLevel(str, Enum):
    CAN_EXECUTE_WITH_CURRENT_INSTANCES = "CAN_EXECUTE_WITH_CURRENT_INSTANCES"
    FULL = "FULL"
    REQUIRES_LAUNCHING_INSTANCE = "REQUIRES_LAUNCHING_INSTANCE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
