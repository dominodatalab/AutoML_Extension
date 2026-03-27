from enum import Enum


class DominoNucleusProjectModelsNewProjectVisibility(str, Enum):
    PRIVATE = "Private"
    PUBLIC = "Public"
    SEARCHABLE = "Searchable"

    def __str__(self) -> str:
        return str(self.value)
