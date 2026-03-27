from enum import Enum


class DominoComputegridExecutionEventDtoExecutionType(str, Enum):
    APP = "App"
    BATCH = "Batch"
    ENDPOINT = "Endpoint"
    LAUNCHER = "Launcher"
    MODEL_API = "Model API"
    OTHER = "Other"
    SCHEDULED = "Scheduled"
    SSHPROXY = "SSHProxy"
    WORKSPACE = "Workspace"

    def __str__(self) -> str:
        return str(self.value)
