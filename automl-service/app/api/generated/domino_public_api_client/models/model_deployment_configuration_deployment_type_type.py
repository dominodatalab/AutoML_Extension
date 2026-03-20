from enum import Enum


class ModelDeploymentConfigurationDeploymentTypeType(str, Enum):
    ASYNC_ENDPOINT = "ASYNC_ENDPOINT"
    SYNC_ENDPOINT = "SYNC_ENDPOINT"

    def __str__(self) -> str:
        return str(self.value)
