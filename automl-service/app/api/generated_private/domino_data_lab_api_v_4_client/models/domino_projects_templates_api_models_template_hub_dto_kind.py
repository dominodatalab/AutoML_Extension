from enum import Enum


class DominoProjectsTemplatesApiModelsTemplateHubDtoKind(str, Enum):
    ECOSYSTEM = "ecosystem"
    MINE = "mine"
    SHARED = "shared"

    def __str__(self) -> str:
        return str(self.value)
