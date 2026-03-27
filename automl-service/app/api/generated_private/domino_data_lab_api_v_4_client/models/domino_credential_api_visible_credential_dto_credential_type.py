from enum import Enum


class DominoCredentialApiVisibleCredentialDtoCredentialType(str, Enum):
    INDIVIDUAL = "Individual"
    SHARED = "Shared"

    def __str__(self) -> str:
        return str(self.value)
