from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchRegisteredModelV1")


@_attrs_define
class PatchRegisteredModelV1:
    """
    Attributes:
        description (str | Unset): The description of the registered model Example: Logistic regression model.
        discoverable (bool | Unset): Whether this registered model is discoverable
    """

    description: str | Unset = UNSET
    discoverable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        discoverable = self.discoverable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if discoverable is not UNSET:
            field_dict["discoverable"] = discoverable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        discoverable = d.pop("discoverable", UNSET)

        patch_registered_model_v1 = cls(
            description=description,
            discoverable=discoverable,
        )

        patch_registered_model_v1.additional_properties = d
        return patch_registered_model_v1

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
