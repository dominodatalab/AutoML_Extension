from enum import Enum


class DominoProjectsApiEntityLinkEntityLinkType(str, Enum):
    APP = "app"
    FILE = "file"
    JOB = "job"
    MODEL_API = "model_api"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
