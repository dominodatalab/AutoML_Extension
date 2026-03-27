from enum import Enum


class DominoComputegridComputeClusterFileSyncStatusResponseStatus(str, Enum):
    FAILED = "Failed"
    NOSYNC = "NoSync"
    SYNCED = "Synced"
    SYNCING = "Syncing"

    def __str__(self) -> str:
        return str(self.value)
