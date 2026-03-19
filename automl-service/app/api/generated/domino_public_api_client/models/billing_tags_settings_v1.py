from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_tags_setting_mode_v1 import BillingTagsSettingModeV1

T = TypeVar("T", bound="BillingTagsSettingsV1")


@_attrs_define
class BillingTagsSettingsV1:
    """
    Attributes:
        mode (BillingTagsSettingModeV1): Billing tags functionality mode
        notifications (bool): Billing tags notifications setting
    """

    mode: BillingTagsSettingModeV1
    notifications: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        notifications = self.notifications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "notifications": notifications,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = BillingTagsSettingModeV1(d.pop("mode"))

        notifications = d.pop("notifications")

        billing_tags_settings_v1 = cls(
            mode=mode,
            notifications=notifications,
        )

        billing_tags_settings_v1.additional_properties = d
        return billing_tags_settings_v1

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
