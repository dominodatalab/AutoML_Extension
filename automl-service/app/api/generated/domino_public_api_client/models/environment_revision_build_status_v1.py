from enum import Enum


class EnvironmentRevisionBuildStatusV1(str, Enum):
    BUILDING = "building"
    FAILED = "failed"
    KILLED = "killed"
    PULLING = "pulling"
    PUSHING = "pushing"
    QUEUED = "queued"
    STARTING = "starting"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
