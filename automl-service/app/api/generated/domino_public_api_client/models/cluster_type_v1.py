from __future__ import annotations
from enum import Enum


class ClusterTypeV1(str, Enum):
    DASK = "dask"
    MPI = "mpi"
    RAY = "ray"
    SPARK = "spark"

    def __str__(self) -> str:
        return str(self.value)
