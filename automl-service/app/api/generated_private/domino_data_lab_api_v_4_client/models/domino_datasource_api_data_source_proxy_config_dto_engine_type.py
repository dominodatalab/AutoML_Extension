from enum import Enum


class DominoDatasourceApiDataSourceProxyConfigDtoEngineType(str, Enum):
    DOMINO = "Domino"
    STARBURST = "Starburst"

    def __str__(self) -> str:
        return str(self.value)
