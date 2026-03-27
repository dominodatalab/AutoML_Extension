from enum import Enum


class DominoModelmanagerApiModelActiveVersionStatus(str, Enum):
    BUILDING = "Building"
    FAILED = "Failed"
    PREPARING_TO_BUILD = "Preparing to build"
    READY_TO_RUN = "Ready to run"
    RUNNING = "Running"
    STALLED = "Stalled"
    STARTING = "Starting"
    STOPPED = "Stopped"
    UNREACHABLE = "Unreachable"

    def __str__(self) -> str:
        return str(self.value)
