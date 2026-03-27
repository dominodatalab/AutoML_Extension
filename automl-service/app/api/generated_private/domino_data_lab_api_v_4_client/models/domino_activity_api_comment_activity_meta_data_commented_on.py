from enum import Enum


class DominoActivityApiCommentActivityMetaDataCommentedOn(str, Enum):
    BUNDLE = "bundle"
    FILE = "file"
    GOAL = "goal"
    JOB = "job"
    PROJECT = "project"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
