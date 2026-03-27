from enum import Enum


class DominoActivityApiProjectLinkChangeActivityMetadataProjectLinkAction(str, Enum):
    LINK = "Link"
    UNLINK = "Unlink"

    def __str__(self) -> str:
        return str(self.value)
