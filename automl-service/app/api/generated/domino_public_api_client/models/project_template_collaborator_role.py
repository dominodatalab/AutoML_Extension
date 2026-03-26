from __future__ import annotations
from enum import Enum


class ProjectTemplateCollaboratorRole(str, Enum):
    TEMPLATE_USER = "template_user"

    def __str__(self) -> str:
        return str(self.value)
