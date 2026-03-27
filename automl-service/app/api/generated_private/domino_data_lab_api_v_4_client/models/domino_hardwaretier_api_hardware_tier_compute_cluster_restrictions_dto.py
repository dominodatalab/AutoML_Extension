from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoHardwaretierApiHardwareTierComputeClusterRestrictionsDto")


@_attrs_define
class DominoHardwaretierApiHardwareTierComputeClusterRestrictionsDto:
    """
    Attributes:
        restrict_to_spark (bool):
        restrict_to_ray (bool):
        restrict_to_dask (bool):
        restrict_to_mpi (bool):
    """

    restrict_to_spark: bool
    restrict_to_ray: bool
    restrict_to_dask: bool
    restrict_to_mpi: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restrict_to_spark = self.restrict_to_spark

        restrict_to_ray = self.restrict_to_ray

        restrict_to_dask = self.restrict_to_dask

        restrict_to_mpi = self.restrict_to_mpi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "restrictToSpark": restrict_to_spark,
                "restrictToRay": restrict_to_ray,
                "restrictToDask": restrict_to_dask,
                "restrictToMpi": restrict_to_mpi,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        restrict_to_spark = d.pop("restrictToSpark")

        restrict_to_ray = d.pop("restrictToRay")

        restrict_to_dask = d.pop("restrictToDask")

        restrict_to_mpi = d.pop("restrictToMpi")

        domino_hardwaretier_api_hardware_tier_compute_cluster_restrictions_dto = cls(
            restrict_to_spark=restrict_to_spark,
            restrict_to_ray=restrict_to_ray,
            restrict_to_dask=restrict_to_dask,
            restrict_to_mpi=restrict_to_mpi,
        )

        domino_hardwaretier_api_hardware_tier_compute_cluster_restrictions_dto.additional_properties = d
        return domino_hardwaretier_api_hardware_tier_compute_cluster_restrictions_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
