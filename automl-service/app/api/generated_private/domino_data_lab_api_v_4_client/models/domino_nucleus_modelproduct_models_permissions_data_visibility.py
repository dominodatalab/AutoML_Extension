from enum import Enum


class DominoNucleusModelproductModelsPermissionsDataVisibility(str, Enum):
    AUTHENTICATED = "AUTHENTICATED"
    GRANT_BASED = "GRANT_BASED"
    GRANT_BASED_STRICT = "GRANT_BASED_STRICT"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
