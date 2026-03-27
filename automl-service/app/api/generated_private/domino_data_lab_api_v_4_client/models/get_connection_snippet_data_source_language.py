from enum import Enum


class GetConnectionSnippetDataSourceLanguage(str, Enum):
    PYTHON = "Python"
    R = "R"
    SAS = "Sas"

    def __str__(self) -> str:
        return str(self.value)
