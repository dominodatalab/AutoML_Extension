from enum import Enum


class DominoDatasourceApiDataSourceDtoStatus(str, Enum):
    ACTIVE = "Active"
    DELETED = "Deleted"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
