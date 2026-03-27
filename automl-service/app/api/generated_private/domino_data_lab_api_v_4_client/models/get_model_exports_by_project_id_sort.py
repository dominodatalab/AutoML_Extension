from enum import Enum


class GetModelExportsByProjectIdSort(str, Enum):
    CREATED = "created"
    MODELNAME = "modelName"
    TARGET = "target"

    def __str__(self) -> str:
        return str(self.value)
