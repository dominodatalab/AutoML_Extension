from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoAdminInterfaceConfigSettingDto")


@_attrs_define
class DominoAdminInterfaceConfigSettingDto:
    """
    Attributes:
        namespace (str):
        key (str):
        value (str):
        name_maybe (None | str | Unset):
    """

    namespace: str
    key: str
    value: str
    name_maybe: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace = self.namespace

        key = self.key

        value = self.value

        name_maybe: None | str | Unset
        if isinstance(self.name_maybe, Unset):
            name_maybe = UNSET
        else:
            name_maybe = self.name_maybe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace": namespace,
                "key": key,
                "value": value,
            }
        )
        if name_maybe is not UNSET:
            field_dict["nameMaybe"] = name_maybe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        namespace = d.pop("namespace")

        key = d.pop("key")

        value = d.pop("value")

        def _parse_name_maybe(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_maybe = _parse_name_maybe(d.pop("nameMaybe", UNSET))

        domino_admin_interface_config_setting_dto = cls(
            namespace=namespace,
            key=key,
            value=value,
            name_maybe=name_maybe,
        )

        domino_admin_interface_config_setting_dto.additional_properties = d
        return domino_admin_interface_config_setting_dto

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
