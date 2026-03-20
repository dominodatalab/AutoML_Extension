from enum import Enum


class RegisteredModelForUIV1LatestVersionModelType(str, Enum):
    EMBEDDING = "embedding"
    LLM = "llm"
    ML = "ml"
    OTHER_GENAI = "other-genai"

    def __str__(self) -> str:
        return str(self.value)
