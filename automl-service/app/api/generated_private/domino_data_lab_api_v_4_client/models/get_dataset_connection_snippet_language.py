from enum import Enum


class GetDatasetConnectionSnippetLanguage(str, Enum):
    PYTHON = "Python"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
