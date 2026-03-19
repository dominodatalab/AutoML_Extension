from enum import Enum


class GetProjectTemplatesCollectionOrderBy(str, Enum):
    NAME = "name"
    RECOMMENDED = "recommended"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
