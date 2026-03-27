from enum import Enum


class DominoProjectsApiProjectTemplateDetailsTemplateType(str, Enum):
    CUSTOMER = "customer"
    ECOSYSTEM = "ecosystem"

    def __str__(self) -> str:
        return str(self.value)
