from enum import Enum


class GetAvailablePvcsByTypeVolumeType(str, Enum):
    EFS = "Efs"
    GENERIC = "Generic"
    NFS = "Nfs"
    SMB = "Smb"

    def __str__(self) -> str:
        return str(self.value)
