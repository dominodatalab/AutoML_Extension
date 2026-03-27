from enum import Enum


class DominoNucleusModelproductModelsPermissionsDataAppAccessStatus(str, Enum):
    ALLOWED = "ALLOWED"
    NOT_ALLOWED = "NOT_ALLOWED"
    PENDING = "PENDING"
    REQUESTABLE = "REQUESTABLE"

    def __str__(self) -> str:
        return str(self.value)
