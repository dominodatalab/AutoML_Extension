from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_type import FieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldStateChange")


@_attrs_define
class FieldStateChange:
    """
    Attributes:
        field_name (str | Unset):
        field_type (FieldType | Unset):
    """

    field_name: str | Unset = UNSET
    field_type: FieldType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        field_type: str | Unset = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("fieldName", UNSET)

        _field_type = d.pop("fieldType", UNSET)
        field_type: FieldType | Unset
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = FieldType(_field_type)

        field_state_change = cls(
            field_name=field_name,
            field_type=field_type,
        )

        field_state_change.additional_properties = d
        return field_state_change

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
