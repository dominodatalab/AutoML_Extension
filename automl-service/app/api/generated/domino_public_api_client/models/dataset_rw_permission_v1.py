from __future__ import annotations
from enum import Enum


class DatasetRwPermissionV1(str, Enum):
    DELETEDATASETRWV2 = "DeleteDatasetRwV2"
    EDITSECURITYDATASETRWV2 = "EditSecurityDatasetRwV2"
    LISTDATASETRWV2 = "ListDatasetRwV2"
    PERFORMDATASETRWACTIONSASADMINV2 = "PerformDatasetRwActionsAsAdminV2"
    PERFORMDATASETRWACTIONSINPROJECTV2 = "PerformDatasetRwActionsInProjectV2"
    PERMANENTDELETEDATASETRWV2 = "PermanentDeleteDatasetRwV2"
    READDATASETRWV2 = "ReadDatasetRwV2"
    UPDATEDATASETRWV2 = "UpdateDatasetRwV2"

    def __str__(self) -> str:
        return str(self.value)
