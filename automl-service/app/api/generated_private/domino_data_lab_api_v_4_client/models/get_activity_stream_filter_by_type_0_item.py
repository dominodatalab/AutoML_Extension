from enum import Enum


class GetActivityStreamFilterByType0Item(str, Enum):
    APP = "app"
    COMMENT = "comment"
    FILES = "files"
    GOALS = "goals"
    JOB = "job"
    MODEL_API = "model_api"
    PROJECT = "project"
    REGISTERED_MODEL = "registered_model"
    SCHEDULE_JOB = "schedule_job"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
