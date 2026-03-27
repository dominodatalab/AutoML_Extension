from enum import Enum


class GetRealTimeLogsLogType(str, Enum):
    CONSOLE = "console"
    PREPAREOUTPUT = "prepareoutput"
    STDERR = "stderr"
    STDOUT = "stdout"
    STDOUTSTDERR = "stdoutstderr"

    def __str__(self) -> str:
        return str(self.value)
