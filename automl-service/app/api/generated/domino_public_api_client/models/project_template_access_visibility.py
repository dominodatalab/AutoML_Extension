from __future__ import annotations
from enum import Enum


class ProjectTemplateAccessVisibility(str, Enum):
    ALL_NON_ANONYMOUS_USERS = "all_non_anonymous_users"
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
