from __future__ import annotations
from enum import Enum


class UIMountPointType(str, Enum):
    DATASETFILECONTEXT = "datasetFileContext"
    PROJECTSIDEBAR = "projectSidebar"
    TOPBAR = "topBar"

    def __str__(self) -> str:
        return str(self.value)
