from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoHardwaretierApiHardwareTierCapacityTypeRestrictionsDto")


@_attrs_define
class DominoHardwaretierApiHardwareTierCapacityTypeRestrictionsDto:
    """
    Attributes:
        enable_spot_instances (bool):
    """

    enable_spot_instances: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_spot_instances = self.enable_spot_instances

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enableSpotInstances": enable_spot_instances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_spot_instances = d.pop("enableSpotInstances")

        domino_hardwaretier_api_hardware_tier_capacity_type_restrictions_dto = cls(
            enable_spot_instances=enable_spot_instances,
        )

        domino_hardwaretier_api_hardware_tier_capacity_type_restrictions_dto.additional_properties = d
        return domino_hardwaretier_api_hardware_tier_capacity_type_restrictions_dto

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
