from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoHardwaretierApiHwtFlags")


@_attrs_define
class DominoHardwaretierApiHwtFlags:
    """
    Attributes:
        is_default (bool):
        is_visible (bool):
        is_global (bool):
        is_archived (bool):
        is_free (bool):
        is_data_analyst_tier (bool):
        is_allowed_during_trial (bool):
        is_model_api_tier (bool | None | Unset):
        is_default_for_model_api (bool | None | Unset):
    """

    is_default: bool
    is_visible: bool
    is_global: bool
    is_archived: bool
    is_free: bool
    is_data_analyst_tier: bool
    is_allowed_during_trial: bool
    is_model_api_tier: bool | None | Unset = UNSET
    is_default_for_model_api: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_default = self.is_default

        is_visible = self.is_visible

        is_global = self.is_global

        is_archived = self.is_archived

        is_free = self.is_free

        is_data_analyst_tier = self.is_data_analyst_tier

        is_allowed_during_trial = self.is_allowed_during_trial

        is_model_api_tier: bool | None | Unset
        if isinstance(self.is_model_api_tier, Unset):
            is_model_api_tier = UNSET
        else:
            is_model_api_tier = self.is_model_api_tier

        is_default_for_model_api: bool | None | Unset
        if isinstance(self.is_default_for_model_api, Unset):
            is_default_for_model_api = UNSET
        else:
            is_default_for_model_api = self.is_default_for_model_api

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isDefault": is_default,
                "isVisible": is_visible,
                "isGlobal": is_global,
                "isArchived": is_archived,
                "isFree": is_free,
                "isDataAnalystTier": is_data_analyst_tier,
                "isAllowedDuringTrial": is_allowed_during_trial,
            }
        )
        if is_model_api_tier is not UNSET:
            field_dict["isModelApiTier"] = is_model_api_tier
        if is_default_for_model_api is not UNSET:
            field_dict["isDefaultForModelApi"] = is_default_for_model_api

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_default = d.pop("isDefault")

        is_visible = d.pop("isVisible")

        is_global = d.pop("isGlobal")

        is_archived = d.pop("isArchived")

        is_free = d.pop("isFree")

        is_data_analyst_tier = d.pop("isDataAnalystTier")

        is_allowed_during_trial = d.pop("isAllowedDuringTrial")

        def _parse_is_model_api_tier(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_model_api_tier = _parse_is_model_api_tier(d.pop("isModelApiTier", UNSET))

        def _parse_is_default_for_model_api(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_default_for_model_api = _parse_is_default_for_model_api(d.pop("isDefaultForModelApi", UNSET))

        domino_hardwaretier_api_hwt_flags = cls(
            is_default=is_default,
            is_visible=is_visible,
            is_global=is_global,
            is_archived=is_archived,
            is_free=is_free,
            is_data_analyst_tier=is_data_analyst_tier,
            is_allowed_during_trial=is_allowed_during_trial,
            is_model_api_tier=is_model_api_tier,
            is_default_for_model_api=is_default_for_model_api,
        )

        domino_hardwaretier_api_hwt_flags.additional_properties = d
        return domino_hardwaretier_api_hwt_flags

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
