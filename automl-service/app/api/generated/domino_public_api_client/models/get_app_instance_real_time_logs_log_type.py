from __future__ import annotations
from enum import Enum


class GetAppInstanceRealTimeLogsLogType(str, Enum):
    COMPLETE = "complete"
    PREPAREOUTPUT = "prepareoutput"
    STDERR = "stderr"
    STDOUT = "stdout"

    def __str__(self) -> str:
        return str(self.value)
