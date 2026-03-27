from enum import Enum


class DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoVisibility(str, Enum):
    INTERNAL = "Internal"
    PRIVATE = "Private"
    PUBLIC = "Public"

    def __str__(self) -> str:
        return str(self.value)
