from enum import Enum


class DominoProjectsTemplatesApiModelsTemplateBackingGitCodeSpecDtoWriteType(str, Enum):
    CREATE = "Create"
    FORCEIMPORT = "ForceImport"
    IMPORT = "Import"

    def __str__(self) -> str:
        return str(self.value)
