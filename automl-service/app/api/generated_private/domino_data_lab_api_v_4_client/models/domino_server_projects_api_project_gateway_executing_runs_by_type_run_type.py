from enum import Enum


class DominoServerProjectsApiProjectGatewayExecutingRunsByTypeRunType(str, Enum):
    APP = "App"
    BATCH = "Batch"
    ENDPOINT = "Endpoint"
    LAUNCHER = "Launcher"
    OTHER = "Other"
    SCHEDULED = "Scheduled"
    SSHPROXY = "SSHProxy"
    WORKSPACE = "Workspace"

    def __str__(self) -> str:
        return str(self.value)
