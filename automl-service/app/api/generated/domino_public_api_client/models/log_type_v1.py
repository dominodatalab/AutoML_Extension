from enum import Enum


class LogTypeV1(str, Enum):
    COMPLETE = "complete"
    PREPAREOUTPUT = "prepareOutput"
    STDERR = "stdErr"
    STDOUT = "stdOut"

    def __str__(self) -> str:
        return str(self.value)
