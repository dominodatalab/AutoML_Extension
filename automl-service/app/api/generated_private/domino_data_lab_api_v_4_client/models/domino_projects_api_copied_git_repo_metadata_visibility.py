from enum import Enum


class DominoProjectsApiCopiedGitRepoMetadataVisibility(str, Enum):
    INTERNAL = "Internal"
    PRIVATE = "Private"
    PUBLIC = "Public"

    def __str__(self) -> str:
        return str(self.value)
