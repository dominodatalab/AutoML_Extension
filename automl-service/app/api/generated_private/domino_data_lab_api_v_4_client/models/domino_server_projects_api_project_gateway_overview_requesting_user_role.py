from enum import Enum


class DominoServerProjectsApiProjectGatewayOverviewRequestingUserRole(str, Enum):
    ADMIN = "Admin"
    CONTRIBUTOR = "Contributor"
    LAUNCHERUSER = "LauncherUser"
    OWNER = "Owner"
    PROJECTIMPORTER = "ProjectImporter"
    RESULTSCONSUMER = "ResultsConsumer"
    VIEWER = "Viewer"

    def __str__(self) -> str:
        return str(self.value)
