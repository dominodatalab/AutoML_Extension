from enum import Enum


class DominoWorkspacesApiEnvironmentEnvironmentRevisionSpecType0(str, Enum):
    ACTIVEREVISION = "ActiveRevision"
    LATESTREVISION = "LatestRevision"
    RESTRICTEDREVISION = "RestrictedRevision"

    def __str__(self) -> str:
        return str(self.value)
