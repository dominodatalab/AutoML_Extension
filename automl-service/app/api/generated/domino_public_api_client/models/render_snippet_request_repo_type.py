from enum import Enum


class RenderSnippetRequestRepoType(str, Enum):
    BIOCONDUCTOR = "Bioconductor"
    PYTHON = "Python"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
