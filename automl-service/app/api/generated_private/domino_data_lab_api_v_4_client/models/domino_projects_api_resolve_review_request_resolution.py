from enum import Enum


class DominoProjectsApiResolveReviewRequestResolution(str, Enum):
    ACCEPTED = "Accepted"
    OPEN = "Open"
    REJECTED = "Rejected"

    def __str__(self) -> str:
        return str(self.value)
