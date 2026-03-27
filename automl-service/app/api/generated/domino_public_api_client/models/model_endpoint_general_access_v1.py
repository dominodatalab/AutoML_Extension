from __future__ import annotations
from enum import Enum


class ModelEndpointGeneralAccessV1(str, Enum):
    CONSUMER = "Consumer"
    RESTRICTED = "Restricted"
    VIEWER = "Viewer"

    def __str__(self) -> str:
        return str(self.value)
