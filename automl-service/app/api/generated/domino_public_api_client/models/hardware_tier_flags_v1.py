from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HardwareTierFlagsV1")


@_attrs_define
class HardwareTierFlagsV1:
    """Boolean flags for a hardware tier

    Attributes:
        is_archived (bool):
        is_data_analyst_tier (bool):
        is_default (bool):
        is_global (bool):
        is_visible (bool):
        is_default_for_model_api (bool | Unset):
        is_model_api_tier (bool | Unset):
    """

    is_archived: bool
    is_data_analyst_tier: bool
    is_default: bool
    is_global: bool
    is_visible: bool
    is_default_for_model_api: bool | Unset = UNSET
    is_model_api_tier: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_archived = self.is_archived

        is_data_analyst_tier = self.is_data_analyst_tier

        is_default = self.is_default

        is_global = self.is_global

        is_visible = self.is_visible

        is_default_for_model_api = self.is_default_for_model_api

        is_model_api_tier = self.is_model_api_tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isArchived": is_archived,
                "isDataAnalystTier": is_data_analyst_tier,
                "isDefault": is_default,
                "isGlobal": is_global,
                "isVisible": is_visible,
            }
        )
        if is_default_for_model_api is not UNSET:
            field_dict["isDefaultForModelApi"] = is_default_for_model_api
        if is_model_api_tier is not UNSET:
            field_dict["isModelApiTier"] = is_model_api_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_archived = d.pop("isArchived")

        is_data_analyst_tier = d.pop("isDataAnalystTier")

        is_default = d.pop("isDefault")

        is_global = d.pop("isGlobal")

        is_visible = d.pop("isVisible")

        is_default_for_model_api = d.pop("isDefaultForModelApi", UNSET)

        is_model_api_tier = d.pop("isModelApiTier", UNSET)

        hardware_tier_flags_v1 = cls(
            is_archived=is_archived,
            is_data_analyst_tier=is_data_analyst_tier,
            is_default=is_default,
            is_global=is_global,
            is_visible=is_visible,
            is_default_for_model_api=is_default_for_model_api,
            is_model_api_tier=is_model_api_tier,
        )

        hardware_tier_flags_v1.additional_properties = d
        return hardware_tier_flags_v1

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
