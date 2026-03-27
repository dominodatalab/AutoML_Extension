from enum import Enum


class DominoProjectsApiProjectStageStageCreationSource(str, Enum):
    DOMINO = "Domino"
    JIRA = "Jira"

    def __str__(self) -> str:
        return str(self.value)
