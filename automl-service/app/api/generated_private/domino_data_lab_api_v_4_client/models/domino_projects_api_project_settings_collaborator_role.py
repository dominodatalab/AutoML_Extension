from enum import Enum


class DominoProjectsApiProjectSettingsCollaboratorRole(str, Enum):
    CONTRIBUTOR = "Contributor"
    LAUNCHERUSER = "LauncherUser"
    OWNER = "Owner"
    PROJECTIMPORTER = "ProjectImporter"
    RESULTSCONSUMER = "ResultsConsumer"

    def __str__(self) -> str:
        return str(self.value)
