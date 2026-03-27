from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_revision_summary import (
        DominoEnvironmentsApiEnvironmentRevisionSummary,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.information import Information


T = TypeVar("T", bound="DominoComputeclusterApiSparkClusterPropsDto")


@_attrs_define
class DominoComputeclusterApiSparkClusterPropsDto:
    """
    Attributes:
        compute_environment (DominoEnvironmentsApiEnvironmentRevisionSummary):
        executor_count (int):
        executor_hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        master_hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        volume_size (Information | Unset):
    """

    compute_environment: DominoEnvironmentsApiEnvironmentRevisionSummary
    executor_count: int
    executor_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    master_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    volume_size: Information | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compute_environment = self.compute_environment.to_dict()

        executor_count = self.executor_count

        executor_hardware_tier_id = self.executor_hardware_tier_id.to_dict()

        master_hardware_tier_id = self.master_hardware_tier_id.to_dict()

        volume_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.volume_size, Unset):
            volume_size = self.volume_size.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "computeEnvironment": compute_environment,
                "executorCount": executor_count,
                "executorHardwareTierId": executor_hardware_tier_id,
                "masterHardwareTierId": master_hardware_tier_id,
            }
        )
        if volume_size is not UNSET:
            field_dict["volumeSize"] = volume_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_revision_summary import (
            DominoEnvironmentsApiEnvironmentRevisionSummary,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_identifier import (
            DominoHardwaretierApiHardwareTierIdentifier,
        )
        from ..models.information import Information

        d = dict(src_dict)
        compute_environment = DominoEnvironmentsApiEnvironmentRevisionSummary.from_dict(d.pop("computeEnvironment"))

        executor_count = d.pop("executorCount")

        executor_hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(
            d.pop("executorHardwareTierId")
        )

        master_hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("masterHardwareTierId"))

        _volume_size = d.pop("volumeSize", UNSET)
        volume_size: Information | Unset
        if isinstance(_volume_size, Unset):
            volume_size = UNSET
        else:
            volume_size = Information.from_dict(_volume_size)

        domino_computecluster_api_spark_cluster_props_dto = cls(
            compute_environment=compute_environment,
            executor_count=executor_count,
            executor_hardware_tier_id=executor_hardware_tier_id,
            master_hardware_tier_id=master_hardware_tier_id,
            volume_size=volume_size,
        )

        domino_computecluster_api_spark_cluster_props_dto.additional_properties = d
        return domino_computecluster_api_spark_cluster_props_dto

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
