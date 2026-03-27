from enum import Enum


class DocumentType(str, Enum):
    APP = "app"
    COMMENT = "comment"
    DATASET = "dataset"
    ENVIRONMENT = "environment"
    FILE = "file"
    MODEL = "model"
    PROJECT = "project"
    RUN = "run"

    def __str__(self) -> str:
        return str(self.value)
