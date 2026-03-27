from enum import Enum


class GetBranchesSort(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
