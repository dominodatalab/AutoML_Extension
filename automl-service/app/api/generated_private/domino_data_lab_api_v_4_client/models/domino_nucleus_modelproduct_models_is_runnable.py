from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoNucleusModelproductModelsIsRunnable")


@_attrs_define
class DominoNucleusModelproductModelsIsRunnable:
    """
    Attributes:
        is_runnable (bool):
    """

    is_runnable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_runnable = self.is_runnable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isRunnable": is_runnable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_runnable = d.pop("isRunnable")

        domino_nucleus_modelproduct_models_is_runnable = cls(
            is_runnable=is_runnable,
        )

        domino_nucleus_modelproduct_models_is_runnable.additional_properties = d
        return domino_nucleus_modelproduct_models_is_runnable

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
