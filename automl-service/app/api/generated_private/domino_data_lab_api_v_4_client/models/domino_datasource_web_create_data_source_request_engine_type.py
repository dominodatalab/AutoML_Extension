from enum import Enum


class DominoDatasourceWebCreateDataSourceRequestEngineType(str, Enum):
    DOMINO = "Domino"
    STARBURST = "Starburst"

    def __str__(self) -> str:
        return str(self.value)
