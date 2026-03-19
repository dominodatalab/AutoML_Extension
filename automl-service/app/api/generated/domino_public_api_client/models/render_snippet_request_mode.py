from enum import Enum


class RenderSnippetRequestMode(str, Enum):
    BASH = "bash"
    R = "r"

    def __str__(self) -> str:
        return str(self.value)
