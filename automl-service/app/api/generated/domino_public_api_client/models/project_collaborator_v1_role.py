from enum import Enum


class ProjectCollaboratorV1Role(str, Enum):
    CONTRIBUTOR = "contributor"
    LAUNCHERUSER = "launcherUser"
    PROJECTIMPORTER = "projectImporter"
    RESULTSCONSUMER = "resultsConsumer"

    def __str__(self) -> str:
        return str(self.value)
