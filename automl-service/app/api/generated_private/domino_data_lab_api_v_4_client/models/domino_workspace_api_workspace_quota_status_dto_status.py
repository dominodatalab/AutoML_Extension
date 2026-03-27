from enum import Enum


class DominoWorkspaceApiWorkspaceQuotaStatusDtoStatus(str, Enum):
    OVERQUOTAFORMAXALLOCATEDVOLUMESIZEACROSSALLWORKSPACES = "OverQuotaForMaxAllocatedVolumeSizeAcrossAllWorkspaces"
    OVERQUOTAFORMAXWORKSPACES = "OverQuotaForMaxWorkspaces"
    OVERQUOTAFORMAXWORKSPACESPERUSER = "OverQuotaForMaxWorkspacesPerUser"
    OVERQUOTAFORMAXWORKSPACESPERUSERPERPROJECT = "OverQuotaForMaxWorkspacesPerUserPerProject"
    QUOTANOTEXCEEDED = "QuotaNotExceeded"

    def __str__(self) -> str:
        return str(self.value)
