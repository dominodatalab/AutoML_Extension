from enum import Enum


class HardwareTierCapacityV1CapacityLevel(str, Enum):
    CANEXECUTEWITHCURRENTINSTANCES = "CanExecuteWithCurrentInstances"
    FULL = "Full"
    REQUIRESLAUNCHINGINSTANCE = "RequiresLaunchingInstance"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
