from enum import Enum


class DominoActivityApiCommentActivityMetaDataOperation(str, Enum):
    ARCHIVED = "Archived"
    CREATED = "Created"
    UPDATED = "Updated"

    def __str__(self) -> str:
        return str(self.value)
