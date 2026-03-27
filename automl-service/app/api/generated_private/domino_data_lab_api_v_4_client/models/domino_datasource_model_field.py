from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasourceModelField")


@_attrs_define
class DominoDatasourceModelField:
    """
    Attributes:
        is_optional (bool):
        is_overridable (bool):
        name (str):
        alias (str | Unset):
        initial_value (str | Unset):
        is_secret (bool | Unset):
        placeholder (str | Unset):
        regexp (str | Unset):
        regexp_error_message (str | Unset):
    """

    is_optional: bool
    is_overridable: bool
    name: str
    alias: str | Unset = UNSET
    initial_value: str | Unset = UNSET
    is_secret: bool | Unset = UNSET
    placeholder: str | Unset = UNSET
    regexp: str | Unset = UNSET
    regexp_error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_optional = self.is_optional

        is_overridable = self.is_overridable

        name = self.name

        alias = self.alias

        initial_value = self.initial_value

        is_secret = self.is_secret

        placeholder = self.placeholder

        regexp = self.regexp

        regexp_error_message = self.regexp_error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isOptional": is_optional,
                "isOverridable": is_overridable,
                "name": name,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if initial_value is not UNSET:
            field_dict["initialValue"] = initial_value
        if is_secret is not UNSET:
            field_dict["isSecret"] = is_secret
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if regexp is not UNSET:
            field_dict["regexp"] = regexp
        if regexp_error_message is not UNSET:
            field_dict["regexpErrorMessage"] = regexp_error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_optional = d.pop("isOptional")

        is_overridable = d.pop("isOverridable")

        name = d.pop("name")

        alias = d.pop("alias", UNSET)

        initial_value = d.pop("initialValue", UNSET)

        is_secret = d.pop("isSecret", UNSET)

        placeholder = d.pop("placeholder", UNSET)

        regexp = d.pop("regexp", UNSET)

        regexp_error_message = d.pop("regexpErrorMessage", UNSET)

        domino_datasource_model_field = cls(
            is_optional=is_optional,
            is_overridable=is_overridable,
            name=name,
            alias=alias,
            initial_value=initial_value,
            is_secret=is_secret,
            placeholder=placeholder,
            regexp=regexp,
            regexp_error_message=regexp_error_message,
        )

        domino_datasource_model_field.additional_properties = d
        return domino_datasource_model_field

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
