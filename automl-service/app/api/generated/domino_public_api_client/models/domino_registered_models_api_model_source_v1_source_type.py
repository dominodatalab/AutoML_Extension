from enum import Enum


class DominoRegisteredModelsApiModelSourceV1SourceType(str, Enum):
    HUGGINGFACE = "huggingface"
    MLFLOW = "mlflow"

    def __str__(self) -> str:
        return str(self.value)
