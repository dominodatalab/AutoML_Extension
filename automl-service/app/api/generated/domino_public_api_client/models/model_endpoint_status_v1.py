from enum import Enum


class ModelEndpointStatusV1(str, Enum):
    BUILDFAILED = "BuildFailed"
    BUILDING = "Building"
    FAILED = "Failed"
    RUNNING = "Running"
    STARTING = "Starting"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
