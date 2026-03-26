from __future__ import annotations
from enum import Enum


class UnregisteredModelV1Source(str, Enum):
    ARTIFACT_PATH = "artifact_path"
    LOGGED_MODEL = "logged_model"

    def __str__(self) -> str:
        return str(self.value)
