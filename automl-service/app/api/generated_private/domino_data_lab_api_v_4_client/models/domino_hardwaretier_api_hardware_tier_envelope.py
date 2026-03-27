from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_hardwaretier_api_hardware_tier_dto import DominoHardwaretierApiHardwareTierDto


T = TypeVar("T", bound="DominoHardwaretierApiHardwareTierEnvelope")


@_attrs_define
class DominoHardwaretierApiHardwareTierEnvelope:
    """
    Attributes:
        hardware_tiers (list[DominoHardwaretierApiHardwareTierDto]):
        is_data_analyst_enabled (bool):
    """

    hardware_tiers: list[DominoHardwaretierApiHardwareTierDto]
    is_data_analyst_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hardware_tiers = []
        for hardware_tiers_item_data in self.hardware_tiers:
            hardware_tiers_item = hardware_tiers_item_data.to_dict()
            hardware_tiers.append(hardware_tiers_item)

        is_data_analyst_enabled = self.is_data_analyst_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hardwareTiers": hardware_tiers,
                "isDataAnalystEnabled": is_data_analyst_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_hardwaretier_api_hardware_tier_dto import DominoHardwaretierApiHardwareTierDto

        d = dict(src_dict)
        hardware_tiers = []
        _hardware_tiers = d.pop("hardwareTiers")
        for hardware_tiers_item_data in _hardware_tiers:
            hardware_tiers_item = DominoHardwaretierApiHardwareTierDto.from_dict(hardware_tiers_item_data)

            hardware_tiers.append(hardware_tiers_item)

        is_data_analyst_enabled = d.pop("isDataAnalystEnabled")

        domino_hardwaretier_api_hardware_tier_envelope = cls(
            hardware_tiers=hardware_tiers,
            is_data_analyst_enabled=is_data_analyst_enabled,
        )

        domino_hardwaretier_api_hardware_tier_envelope.additional_properties = d
        return domino_hardwaretier_api_hardware_tier_envelope

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
