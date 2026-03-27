from enum import Enum


class OwnerProvisionedWorkspacesAllProjectsSortField(str, Enum):
    HARDWARETIERNAME = "HardwareTierName"
    LASTSTARTED = "LastStarted"
    NAME = "Name"
    PROJECTNAME = "ProjectName"
    STATUS = "Status"

    def __str__(self) -> str:
        return str(self.value)
