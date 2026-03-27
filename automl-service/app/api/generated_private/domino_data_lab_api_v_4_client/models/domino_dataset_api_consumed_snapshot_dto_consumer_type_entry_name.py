from enum import Enum


class DominoDatasetApiConsumedSnapshotDtoConsumerTypeEntryName(str, Enum):
    RUN = "run"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
