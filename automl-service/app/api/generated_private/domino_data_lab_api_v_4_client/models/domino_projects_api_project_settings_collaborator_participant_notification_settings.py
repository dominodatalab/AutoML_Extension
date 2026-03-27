from enum import Enum


class DominoProjectsApiProjectSettingsCollaboratorParticipantNotificationSettings(str, Enum):
    ALLRUNS = "AllRuns"
    NEVER = "Never"
    RUNSSTARTEDBYUSER = "RunsStartedByUser"
    RUNSSTARTEDBYUSERTHATFAILED = "RunsStartedByUserThatFailed"
    RUNSTHATFAILED = "RunsThatFailed"

    def __str__(self) -> str:
        return str(self.value)
