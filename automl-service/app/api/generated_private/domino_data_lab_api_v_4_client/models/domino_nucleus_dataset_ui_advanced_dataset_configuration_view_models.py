from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_nucleus_dataset_ui_advanced_dataset_configuration_view_model import (
        DominoNucleusDatasetUiAdvancedDatasetConfigurationViewModel,
    )


T = TypeVar("T", bound="DominoNucleusDatasetUiAdvancedDatasetConfigurationViewModels")


@_attrs_define
class DominoNucleusDatasetUiAdvancedDatasetConfigurationViewModels:
    """
    Attributes:
        models (list[DominoNucleusDatasetUiAdvancedDatasetConfigurationViewModel]):
    """

    models: list[DominoNucleusDatasetUiAdvancedDatasetConfigurationViewModel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "models": models,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_dataset_ui_advanced_dataset_configuration_view_model import (
            DominoNucleusDatasetUiAdvancedDatasetConfigurationViewModel,
        )

        d = dict(src_dict)
        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = DominoNucleusDatasetUiAdvancedDatasetConfigurationViewModel.from_dict(models_item_data)

            models.append(models_item)

        domino_nucleus_dataset_ui_advanced_dataset_configuration_view_models = cls(
            models=models,
        )

        domino_nucleus_dataset_ui_advanced_dataset_configuration_view_models.additional_properties = d
        return domino_nucleus_dataset_ui_advanced_dataset_configuration_view_models

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
