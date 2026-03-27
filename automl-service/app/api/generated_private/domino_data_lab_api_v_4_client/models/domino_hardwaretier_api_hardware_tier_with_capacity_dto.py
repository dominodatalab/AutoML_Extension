from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_dataplane_data_plane_dto import DominoDataplaneDataPlaneDto
    from ..models.domino_hardwaretier_api_hardware_tier_capacity import DominoHardwaretierApiHardwareTierCapacity
    from ..models.domino_hardwaretier_api_hardware_tier_dto import DominoHardwaretierApiHardwareTierDto


T = TypeVar("T", bound="DominoHardwaretierApiHardwareTierWithCapacityDto")


@_attrs_define
class DominoHardwaretierApiHardwareTierWithCapacityDto:
    """
    Attributes:
        hardware_tier (DominoHardwaretierApiHardwareTierDto):
        capacity (DominoHardwaretierApiHardwareTierCapacity):
        data_plane (DominoDataplaneDataPlaneDto):
    """

    hardware_tier: DominoHardwaretierApiHardwareTierDto
    capacity: DominoHardwaretierApiHardwareTierCapacity
    data_plane: DominoDataplaneDataPlaneDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hardware_tier = self.hardware_tier.to_dict()

        capacity = self.capacity.to_dict()

        data_plane = self.data_plane.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hardwareTier": hardware_tier,
                "capacity": capacity,
                "dataPlane": data_plane,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataplane_data_plane_dto import DominoDataplaneDataPlaneDto
        from ..models.domino_hardwaretier_api_hardware_tier_capacity import DominoHardwaretierApiHardwareTierCapacity
        from ..models.domino_hardwaretier_api_hardware_tier_dto import DominoHardwaretierApiHardwareTierDto

        d = dict(src_dict)
        hardware_tier = DominoHardwaretierApiHardwareTierDto.from_dict(d.pop("hardwareTier"))

        capacity = DominoHardwaretierApiHardwareTierCapacity.from_dict(d.pop("capacity"))

        data_plane = DominoDataplaneDataPlaneDto.from_dict(d.pop("dataPlane"))

        domino_hardwaretier_api_hardware_tier_with_capacity_dto = cls(
            hardware_tier=hardware_tier,
            capacity=capacity,
            data_plane=data_plane,
        )

        domino_hardwaretier_api_hardware_tier_with_capacity_dto.additional_properties = d
        return domino_hardwaretier_api_hardware_tier_with_capacity_dto

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
