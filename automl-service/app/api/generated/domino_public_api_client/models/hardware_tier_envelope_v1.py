from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hardware_tier_v1 import HardwareTierV1
    from ..models.metadata_v1 import MetadataV1


T = TypeVar("T", bound="HardwareTierEnvelopeV1")


@_attrs_define
class HardwareTierEnvelopeV1:
    """
    Attributes:
        hardware_tier (HardwareTierV1):
        metadata (MetadataV1):
    """

    hardware_tier: HardwareTierV1
    metadata: MetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hardware_tier = self.hardware_tier.to_dict()

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hardwareTier": hardware_tier,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hardware_tier_v1 import HardwareTierV1
        from ..models.metadata_v1 import MetadataV1

        d = dict(src_dict)
        hardware_tier = HardwareTierV1.from_dict(d.pop("hardwareTier"))

        metadata = MetadataV1.from_dict(d.pop("metadata"))

        hardware_tier_envelope_v1 = cls(
            hardware_tier=hardware_tier,
            metadata=metadata,
        )

        hardware_tier_envelope_v1.additional_properties = d
        return hardware_tier_envelope_v1

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
