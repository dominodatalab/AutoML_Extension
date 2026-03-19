from enum import Enum


class GetRegisteredModelsV2ModelCategory(str, Enum):
    GENAI = "genai"
    ML = "ml"

    def __str__(self) -> str:
        return str(self.value)
