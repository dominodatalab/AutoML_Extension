from enum import Enum


class DominoProjectManagementApiDominoGoalToPmSubTicketMetadataMapType(str, Enum):
    DOMINOCOMMENT = "DominoComment"
    DOMINOGOAL = "DominoGoal"
    DOMINOPROJECT = "DominoProject"
    DOMINOSTAGE = "DominoStage"

    def __str__(self) -> str:
        return str(self.value)
