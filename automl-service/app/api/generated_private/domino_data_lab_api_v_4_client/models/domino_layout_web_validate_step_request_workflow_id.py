from enum import Enum


class DominoLayoutWebValidateStepRequestWorkflowID(str, Enum):
    CREATEDATASET = "CreateDataset"
    CREATEDATASOURCE = "CreateDatasource"
    UPDATEDATASET = "UpdateDataset"
    UPDATEDATASOURCE = "UpdateDatasource"

    def __str__(self) -> str:
        return str(self.value)
