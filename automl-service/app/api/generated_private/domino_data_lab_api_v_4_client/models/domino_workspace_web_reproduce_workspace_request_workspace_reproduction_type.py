from enum import Enum


class DominoWorkspaceWebReproduceWorkspaceRequestWorkspaceReproductionType(str, Enum):
    FROMMODEL = "FromModel"
    FROMMODELCOMMITS = "FromModelCommits"
    FROMWORKSPACE = "FromWorkspace"

    def __str__(self) -> str:
        return str(self.value)
