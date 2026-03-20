from enum import Enum


class RepoStatusStatus(str, Enum):
    FAILED = "Failed"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
