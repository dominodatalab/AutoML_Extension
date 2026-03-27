from enum import Enum


class DominoWorkspaceApiWorkspaceAdminPageTableRowWorkspaceState(str, Enum):
    CREATED = "Created"
    DELETED = "Deleted"
    INITIALIZING = "Initializing"
    STARTED = "Started"
    STARTING = "Starting"
    STOPPED = "Stopped"
    STOPPING = "Stopping"

    def __str__(self) -> str:
        return str(self.value)
