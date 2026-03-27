from enum import Enum


class DominoComputegridLogContentLogType(str, Enum):
    COMPLETE = "complete"
    PREPAREOUTPUT = "prepareoutput"
    STDERR = "stderr"
    STDOUT = "stdout"
    STDOUTSTDERR = "stdoutstderr"

    def __str__(self) -> str:
        return str(self.value)
