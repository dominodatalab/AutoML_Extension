from enum import Enum


class ListRelationship(str, Enum):
    COLLABORATING = "Collaborating"
    OWNED = "Owned"
    OWNEDANDCOLLABORATING = "OwnedAndCollaborating"
    POPULAR = "Popular"
    SUGGESTED = "Suggested"

    def __str__(self) -> str:
        return str(self.value)
