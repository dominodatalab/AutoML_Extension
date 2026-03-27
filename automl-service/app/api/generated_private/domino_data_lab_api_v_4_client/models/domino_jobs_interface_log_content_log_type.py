from enum import Enum


class DominoJobsInterfaceLogContentLogType(str, Enum):
    COMPLETE = "complete"
    PREPAREOUTPUT = "prepareoutput"
    STDERR = "stderr"
    STDOUT = "stdout"

    def __str__(self) -> str:
        return str(self.value)
