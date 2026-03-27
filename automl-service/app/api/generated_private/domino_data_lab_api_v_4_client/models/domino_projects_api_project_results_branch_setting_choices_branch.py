from enum import Enum


class DominoProjectsApiProjectResultsBranchSettingChoicesBranch(str, Enum):
    ISOLATED = "Isolated"
    MAIN = "Main"

    def __str__(self) -> str:
        return str(self.value)
