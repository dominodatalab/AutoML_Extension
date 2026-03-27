from enum import Enum


class DominoProjectsTemplatesApiModelsTemplateCollaboratorDtoRole(str, Enum):
    TEMPLATE_USER = "template_user"

    def __str__(self) -> str:
        return str(self.value)
