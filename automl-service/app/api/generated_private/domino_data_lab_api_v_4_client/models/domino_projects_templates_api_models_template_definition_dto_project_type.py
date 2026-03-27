from enum import Enum


class DominoProjectsTemplatesApiModelsTemplateDefinitionDtoProjectType(str, Enum):
    DFS = "dfs"
    GIT_BASED = "git_based"

    def __str__(self) -> str:
        return str(self.value)
