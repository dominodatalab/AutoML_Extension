from __future__ import annotations
from enum import Enum


class ModelDeploymentCollaboratorRole(str, Enum):
    CONSUMER = "CONSUMER"
    OWNER = "OWNER"

    def __str__(self) -> str:
        return str(self.value)
