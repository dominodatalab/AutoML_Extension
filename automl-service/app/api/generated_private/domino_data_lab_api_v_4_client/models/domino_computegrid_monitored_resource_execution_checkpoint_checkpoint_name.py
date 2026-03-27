from enum import Enum


class DominoComputegridMonitoredResourceExecutionCheckpointCheckpointName(str, Enum):
    ACKNOWLEDGED = "Acknowledged"
    EXECUTIONAVAILABLE = "ExecutionAvailable"
    FILESPREPARED = "FilesPrepared"
    IMAGESPULLED = "ImagesPulled"
    NODEASSIGNED = "NodeAssigned"
    QUOTACHECKED = "QuotaChecked"
    RESOURCESCREATED = "ResourcesCreated"
    RESOURCESDELETED = "ResourcesDeleted"
    USERCODELAUNCHED = "UserCodeLaunched"
    USERFILESSAVED = "UserFilesSaved"
    VOLUMESMOUNTED = "VolumesMounted"
    VOLUMESRELEASED = "VolumesReleased"

    def __str__(self) -> str:
        return str(self.value)
