from enum import Enum


class DominoEnvironmentsApiEnvironmentRevisionSummaryRevisionType(str, Enum):
    ACTIVE = "Active"
    LATEST = "Latest"
    PINNED = "Pinned"
    RESTRICTED = "Restricted"

    def __str__(self) -> str:
        return str(self.value)
