from enum import Enum


class DominoProjectsApiCollaboratorForGovernanceApproversRole(str, Enum):
    CONTRIBUTOR = "Contributor"
    LAUNCHERUSER = "LauncherUser"
    OWNER = "Owner"
    PROJECTIMPORTER = "ProjectImporter"
    RESULTSCONSUMER = "ResultsConsumer"

    def __str__(self) -> str:
        return str(self.value)
