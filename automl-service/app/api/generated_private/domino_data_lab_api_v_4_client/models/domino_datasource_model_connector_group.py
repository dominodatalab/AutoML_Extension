from enum import Enum


class DominoDatasourceModelConnectorGroup(str, Enum):
    NATIVE = "Native"
    REVERSEPROXY = "ReverseProxy"
    STARBURST = "Starburst"
    STARBURSTSELFSERVICE = "StarburstSelfService"

    def __str__(self) -> str:
        return str(self.value)
