from enum import Enum


class DominoMlflowApiMlflowDataMlflowSourceType(str, Enum):
    JOB = "JOB"
    LOCAL = "LOCAL"
    NOTEBOOK = "NOTEBOOK"
    PIPELINE = "PIPELINE"
    PROJECT = "PROJECT"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
