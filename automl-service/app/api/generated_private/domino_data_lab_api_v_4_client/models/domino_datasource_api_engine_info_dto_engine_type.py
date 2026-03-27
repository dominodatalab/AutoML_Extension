from enum import Enum


class DominoDatasourceApiEngineInfoDtoEngineType(str, Enum):
    DOMINO = "Domino"
    STARBURST = "Starburst"

    def __str__(self) -> str:
        return str(self.value)
