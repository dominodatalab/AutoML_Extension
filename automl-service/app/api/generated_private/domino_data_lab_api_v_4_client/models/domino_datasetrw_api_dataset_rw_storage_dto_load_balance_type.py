from enum import Enum


class DominoDatasetrwApiDatasetRwStorageDtoLoadBalanceType(str, Enum):
    PRIMARY = "primary"

    def __str__(self) -> str:
        return str(self.value)
