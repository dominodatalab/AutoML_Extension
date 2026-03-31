from enum import Enum


class LogTypeV1(str, Enum):
    COMPLETE = "Complete"
    PREPAREOUTPUT = "PrepareOutput"
    STDERR = "StdErr"
    STDOUT = "StdOut"

    def __str__(self) -> str:
        return str(self.value)
