from enum import Enum


class ModelSource(str, Enum):
    MODELREGISTRY = "MODELREGISTRY"

    def __str__(self) -> str:
        return str(self.value)
