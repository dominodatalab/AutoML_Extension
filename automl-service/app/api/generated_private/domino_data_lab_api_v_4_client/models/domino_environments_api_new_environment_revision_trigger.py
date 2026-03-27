from enum import Enum


class DominoEnvironmentsApiNewEnvironmentRevisionTrigger(str, Enum):
    BASEACTIVECHANGE = "BaseActiveChange"
    DEFINITIONEDIT = "DefinitionEdit"

    def __str__(self) -> str:
        return str(self.value)
