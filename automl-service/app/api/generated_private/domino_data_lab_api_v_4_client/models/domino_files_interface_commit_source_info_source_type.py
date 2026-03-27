from enum import Enum


class DominoFilesInterfaceCommitSourceInfoSourceType(str, Enum):
    JOB = "job"
    USER = "user"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
