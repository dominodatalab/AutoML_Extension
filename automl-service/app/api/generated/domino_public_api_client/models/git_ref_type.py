from enum import Enum


class GitRefType(str, Enum):
    BRANCHES = "branches"
    COMMITID = "commitId"
    CUSTOM = "custom"
    HEAD = "head"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)
