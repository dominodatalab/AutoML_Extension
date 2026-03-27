from enum import Enum


class DominoProjectManagementApiPmEntityEntityType(str, Enum):
    PMCOMMENT = "PmComment"
    PMSTAGE = "PmStage"
    PMSUBTICKET = "PmSubTicket"
    PMTICKET = "PmTicket"

    def __str__(self) -> str:
        return str(self.value)
