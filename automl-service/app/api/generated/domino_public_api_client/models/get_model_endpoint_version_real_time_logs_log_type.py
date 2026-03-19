from enum import Enum


class GetModelEndpointVersionRealTimeLogsLogType(str, Enum):
    COMPLETE = "complete"
    PREPAREOUTPUT = "prepareoutput"
    STDERR = "stderr"
    STDOUT = "stdout"

    def __str__(self) -> str:
        return str(self.value)
