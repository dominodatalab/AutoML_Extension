from __future__ import annotations
from enum import Enum


class GetJobLogsLogType(str, Enum):
    COMPLETE = "complete"
    PREPAREOUTPUT = "prepareOutput"
    STDERR = "stdErr"
    STDOUT = "stdOut"

    def __str__(self) -> str:
        return str(self.value)
