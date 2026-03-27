from enum import Enum


class DominoWorkspaceApiWorkspaceReproductionDetailsDtoWorkspaceReproductionType(str, Enum):
    FROMMODEL = "FromModel"
    FROMMODELCOMMITS = "FromModelCommits"
    FROMWORKSPACE = "FromWorkspace"

    def __str__(self) -> str:
        return str(self.value)
