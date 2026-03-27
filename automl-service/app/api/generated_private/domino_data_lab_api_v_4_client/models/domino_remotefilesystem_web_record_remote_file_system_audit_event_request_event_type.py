from enum import Enum


class DominoRemotefilesystemWebRecordRemoteFileSystemAuditEventRequestEventType(str, Enum):
    ADDGRANTVOLUME = "AddGrantVolume"
    ADDVOLUMETOPROJECT = "AddVolumeToProject"
    CREATEFILESYSTEM = "CreateFilesystem"
    CREATESNAPSHOT = "CreateSnapshot"
    CREATEVOLUME = "CreateVolume"
    DELETEFILESVOLUME = "DeleteFilesVolume"
    DELETEFILESYSTEM = "DeleteFilesystem"
    DELETESNAPSHOT = "DeleteSnapshot"
    DELETEVOLUME = "DeleteVolume"
    DOWNLOADFILESSNAPSHOT = "DownloadFilesSnapshot"
    DOWNLOADFILESVOLUME = "DownloadFilesVolume"
    MARKSNAPSHOTFORDELETION = "MarkSnapshotForDeletion"
    MARKVOLUMEFORDELETION = "MarkVolumeForDeletion"
    PREVIEWFILESNAPSHOT = "PreviewFileSnapshot"
    PREVIEWFILEVOLUME = "PreviewFileVolume"
    REMOVEGRANTVOLUME = "RemoveGrantVolume"
    REMOVEVOLUMEFROMPROJECT = "RemoveVolumeFromProject"
    RENAMEFILEORDIRECTORYVOLUME = "RenameFileOrDirectoryVolume"
    RESTORESNAPSHOT = "RestoreSnapshot"
    RESTOREVOLUME = "RestoreVolume"
    UPDATEFILESYSTEMNAME = "UpdateFilesystemName"
    UPDATESNAPSHOTDESCRIPTION = "UpdateSnapshotDescription"
    UPDATEVOLUMEDESCRIPTION = "UpdateVolumeDescription"
    UPDATEVOLUMENAME = "UpdateVolumeName"
    UPLOADFILESVOLUME = "UploadFilesVolume"

    def __str__(self) -> str:
        return str(self.value)
