from __future__ import annotations
from enum import Enum


class GitReferenceTypeV1(str, Enum):
    BRANCH = "branch"
    COMMIT = "commit"
    HEAD = "head"
    TAG = "tag"

    def __str__(self) -> str:
        return str(self.value)
