from enum import Enum


class SyncOperationType(str, Enum):
    GITANDDFS = "gitAndDfs"
    ONLYDFS = "onlyDfs"
    ONLYGIT = "onlyGit"

    def __str__(self) -> str:
        return str(self.value)
