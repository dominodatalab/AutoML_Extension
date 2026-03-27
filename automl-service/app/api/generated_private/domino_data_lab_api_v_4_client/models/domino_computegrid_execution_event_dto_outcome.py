from enum import Enum


class DominoComputegridExecutionEventDtoOutcome(str, Enum):
    ERROR = "Error"
    FAILURE = "Failure"
    IGNORED = "Ignored"
    RETRY = "Retry"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
