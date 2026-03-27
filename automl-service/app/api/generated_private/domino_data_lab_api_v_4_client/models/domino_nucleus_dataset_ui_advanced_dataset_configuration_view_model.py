from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoNucleusDatasetUiAdvancedDatasetConfigurationViewModel")


@_attrs_define
class DominoNucleusDatasetUiAdvancedDatasetConfigurationViewModel:
    """
    Attributes:
        name (str):
        yaml (str):
    """

    name: str
    yaml: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        yaml = self.yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "yaml": yaml,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        yaml = d.pop("yaml")

        domino_nucleus_dataset_ui_advanced_dataset_configuration_view_model = cls(
            name=name,
            yaml=yaml,
        )

        domino_nucleus_dataset_ui_advanced_dataset_configuration_view_model.additional_properties = d
        return domino_nucleus_dataset_ui_advanced_dataset_configuration_view_model

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
