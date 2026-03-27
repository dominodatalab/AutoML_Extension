from enum import Enum


class DominoComputegridComputeClusterFileSyncStatusResponseReason(str, Enum):
    CLUSTERNOTREADY = "ClusterNotReady"
    NOSYNCDETECTED = "NoSyncDetected"
    STILLSYNCING = "StillSyncing"
    SYNCED = "Synced"
    TIMEOUT = "Timeout"
    UNKNOWN = "Unknown"
    WORKERSYNCFAILURE = "WorkerSyncFailure"

    def __str__(self) -> str:
        return str(self.value)
