from enum import Enum


class DominoDatasourceModelStorageType(str, Enum):
    OBJECTSTORE = "ObjectStore"
    TABULAR = "Tabular"
    VECTOR = "Vector"

    def __str__(self) -> str:
        return str(self.value)
