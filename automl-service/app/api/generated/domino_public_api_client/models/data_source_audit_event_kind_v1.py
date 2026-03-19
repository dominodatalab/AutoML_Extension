from enum import Enum


class DataSourceAuditEventKindV1(str, Enum):
    ACCESSDATASOURCE = "AccessDataSource"
    CREATEDATASOURCE = "CreateDataSource"
    DATASOURCEASSOCIATEDTOPROJECT = "DataSourceAssociatedToProject"
    DATASOURCECHANGEOFOWNERSHIP = "DataSourceChangeOfOwnership"
    DATASOURCECHANGEOFPERMISSIONS = "DataSourceChangeOfPermissions"
    DATASOURCEDISSOCIATEDFROMPROJECT = "DataSourceDissociatedFromProject"
    DELETEDATASOURCE = "DeleteDataSource"

    def __str__(self) -> str:
        return str(self.value)
