from enum import Enum


class ModelEndpointModelTypeV1(str, Enum):
    EMBEDDING = "Embedding"
    LLM = "LLM"
    OTHERGENAI = "OtherGenAI"

    def __str__(self) -> str:
        return str(self.value)
