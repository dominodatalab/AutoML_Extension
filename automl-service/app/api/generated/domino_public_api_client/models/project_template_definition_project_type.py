from enum import Enum


class ProjectTemplateDefinitionProjectType(str, Enum):
    DFS = "dfs"
    GIT_BASED = "git_based"

    def __str__(self) -> str:
        return str(self.value)
