from enum import Enum


class ProjectTemplateTemplateType(str, Enum):
    CUSTOMER = "customer"
    ECOSYSTEM = "ecosystem"

    def __str__(self) -> str:
        return str(self.value)
