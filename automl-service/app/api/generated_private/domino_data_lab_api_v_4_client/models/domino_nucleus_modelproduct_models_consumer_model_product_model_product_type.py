from enum import Enum


class DominoNucleusModelproductModelsConsumerModelProductModelProductType(str, Enum):
    APP = "APP"
    BATCH = "BATCH"
    REPORT = "REPORT"
    SCORER = "SCORER"

    def __str__(self) -> str:
        return str(self.value)
