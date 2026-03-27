from enum import Enum


class DominoProjectsApiProjectSettingsExportExportPackageType(str, Enum):
    PYTHON = "Python"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
