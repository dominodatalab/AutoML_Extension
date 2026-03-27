from enum import Enum


class DominoDatasourceWebUpdateDataSourceCredentialRequestCredentialType(str, Enum):
    INDIVIDUAL = "Individual"
    SHARED = "Shared"

    def __str__(self) -> str:
        return str(self.value)
