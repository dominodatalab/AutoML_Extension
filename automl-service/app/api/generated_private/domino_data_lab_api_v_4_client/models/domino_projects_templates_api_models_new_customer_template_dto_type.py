from enum import Enum


class DominoProjectsTemplatesApiModelsNewCustomerTemplateDtoType(str, Enum):
    CUSTOMER = "customer"
    ECOSYSTEM = "ecosystem"

    def __str__(self) -> str:
        return str(self.value)
