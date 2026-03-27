from enum import Enum


class GetModelsForUISortBy(str, Enum):
    MODIFIED = "modified"
    NAME = "name"
    PROJECT = "project"

    def __str__(self) -> str:
        return str(self.value)
