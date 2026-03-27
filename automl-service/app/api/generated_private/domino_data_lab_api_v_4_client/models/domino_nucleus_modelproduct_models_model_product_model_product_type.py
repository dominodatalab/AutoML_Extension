from enum import Enum


class DominoNucleusModelproductModelsModelProductModelProductType(str, Enum):
    APP = "APP"
    BATCH = "BATCH"
    REPORT = "REPORT"
    SCORER = "SCORER"

    def __str__(self) -> str:
        return str(self.value)
