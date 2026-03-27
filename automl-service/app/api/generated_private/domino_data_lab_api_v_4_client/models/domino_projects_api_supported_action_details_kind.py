from enum import Enum


class DominoProjectsApiSupportedActionDetailsKind(str, Enum):
    AUTHONLY = "AuthOnly"
    CREATETEMPLATE = "CreateTemplate"
    PROJECTCOPY = "ProjectCopy"
    PROJECTFORK = "ProjectFork"

    def __str__(self) -> str:
        return str(self.value)
