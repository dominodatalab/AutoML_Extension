from enum import Enum


class DominoProjectsTemplatesApiModelsDependencyTemplateDtoKind(str, Enum):
    ENVIRONMENT = "Environment"
    PROJECT = "Project"

    def __str__(self) -> str:
        return str(self.value)
