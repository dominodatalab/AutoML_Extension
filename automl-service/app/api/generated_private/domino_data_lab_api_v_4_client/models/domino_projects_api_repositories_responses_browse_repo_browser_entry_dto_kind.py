from enum import Enum


class DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTOKind(str, Enum):
    DIR = "dir"
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
