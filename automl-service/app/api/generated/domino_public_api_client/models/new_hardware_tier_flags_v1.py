from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewHardwareTierFlagsV1")


@_attrs_define
class NewHardwareTierFlagsV1:
    """Boolean flags for creating a new hardware tier

    Attributes:
        is_data_analyst_tier (bool | Unset):  Default: False.
        is_default (bool | Unset):  Default: False.
        is_default_for_model_api (bool | Unset):
        is_global (bool | Unset):  Default: True.
        is_model_api_tier (bool | Unset):
        is_visible (bool | Unset):  Default: True.
    """

    is_data_analyst_tier: bool | Unset = False
    is_default: bool | Unset = False
    is_default_for_model_api: bool | Unset = UNSET
    is_global: bool | Unset = True
    is_model_api_tier: bool | Unset = UNSET
    is_visible: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_data_analyst_tier = self.is_data_analyst_tier

        is_default = self.is_default

        is_default_for_model_api = self.is_default_for_model_api

        is_global = self.is_global

        is_model_api_tier = self.is_model_api_tier

        is_visible = self.is_visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_data_analyst_tier is not UNSET:
            field_dict["isDataAnalystTier"] = is_data_analyst_tier
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_default_for_model_api is not UNSET:
            field_dict["isDefaultForModelApi"] = is_default_for_model_api
        if is_global is not UNSET:
            field_dict["isGlobal"] = is_global
        if is_model_api_tier is not UNSET:
            field_dict["isModelApiTier"] = is_model_api_tier
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_data_analyst_tier = d.pop("isDataAnalystTier", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_default_for_model_api = d.pop("isDefaultForModelApi", UNSET)

        is_global = d.pop("isGlobal", UNSET)

        is_model_api_tier = d.pop("isModelApiTier", UNSET)

        is_visible = d.pop("isVisible", UNSET)

        new_hardware_tier_flags_v1 = cls(
            is_data_analyst_tier=is_data_analyst_tier,
            is_default=is_default,
            is_default_for_model_api=is_default_for_model_api,
            is_global=is_global,
            is_model_api_tier=is_model_api_tier,
            is_visible=is_visible,
        )

        new_hardware_tier_flags_v1.additional_properties = d
        return new_hardware_tier_flags_v1

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
