from enum import Enum


class DominoComputegridComputeClusterFileSyncResponseReason(str, Enum):
    ALREADYSYNCING = "AlreadySyncing"
    CLUSTERNOTREADY = "ClusterNotReady"
    FAILEDTOSTART = "FailedToStart"
    STARTED = "Started"

    def __str__(self) -> str:
        return str(self.value)
