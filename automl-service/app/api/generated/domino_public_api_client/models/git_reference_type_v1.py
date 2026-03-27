from enum import Enum


class GitReferenceTypeV1(str, Enum):
    BRANCH = "Branch"
    COMMIT = "Commit"
    HEAD = "Head"
    TAG = "Tag"

    def __str__(self) -> str:
        return str(self.value)
