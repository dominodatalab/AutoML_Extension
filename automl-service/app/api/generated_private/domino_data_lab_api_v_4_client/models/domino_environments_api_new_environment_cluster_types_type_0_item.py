from enum import Enum


class DominoEnvironmentsApiNewEnvironmentClusterTypesType0Item(str, Enum):
    DASK = "Dask"
    MPI = "MPI"
    RAY = "Ray"
    SPARK = "Spark"

    def __str__(self) -> str:
        return str(self.value)
