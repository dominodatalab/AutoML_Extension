from enum import Enum


class DominoModelmanagerApiModelExportTarget(str, Enum):
    DOMINO = "Domino"
    NVIDIAFLEETCOMMAND = "NvidiaFleetcommand"
    SAGEMAKER = "Sagemaker"
    SNOWFLAKE = "Snowflake"

    def __str__(self) -> str:
        return str(self.value)
