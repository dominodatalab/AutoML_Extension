from enum import Enum


class GetSupportedActionsQType0Item(str, Enum):
    AUTHONLY = "AuthOnly"
    CREATETEMPLATE = "CreateTemplate"
    PROJECTCOPY = "ProjectCopy"
    PROJECTFORK = "ProjectFork"

    def __str__(self) -> str:
        return str(self.value)
