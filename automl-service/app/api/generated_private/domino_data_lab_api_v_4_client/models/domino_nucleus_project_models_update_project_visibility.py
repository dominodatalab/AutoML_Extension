from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_nucleus_project_models_update_project_visibility_visibility import (
    DominoNucleusProjectModelsUpdateProjectVisibilityVisibility,
)

T = TypeVar("T", bound="DominoNucleusProjectModelsUpdateProjectVisibility")


@_attrs_define
class DominoNucleusProjectModelsUpdateProjectVisibility:
    """
    Attributes:
        visibility (DominoNucleusProjectModelsUpdateProjectVisibilityVisibility):
    """

    visibility: DominoNucleusProjectModelsUpdateProjectVisibilityVisibility
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibility": visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        visibility = DominoNucleusProjectModelsUpdateProjectVisibilityVisibility(d.pop("visibility"))

        domino_nucleus_project_models_update_project_visibility = cls(
            visibility=visibility,
        )

        domino_nucleus_project_models_update_project_visibility.additional_properties = d
        return domino_nucleus_project_models_update_project_visibility

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
