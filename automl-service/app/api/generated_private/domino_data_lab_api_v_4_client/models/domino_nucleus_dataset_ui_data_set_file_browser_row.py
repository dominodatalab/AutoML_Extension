from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_nucleus_dataset_ui_data_set_file_browser_entry import (
        DominoNucleusDatasetUiDataSetFileBrowserEntry,
    )


T = TypeVar("T", bound="DominoNucleusDatasetUiDataSetFileBrowserRow")


@_attrs_define
class DominoNucleusDatasetUiDataSetFileBrowserRow:
    """
    Attributes:
        name (DominoNucleusDatasetUiDataSetFileBrowserEntry):
        size (DominoNucleusDatasetUiDataSetFileBrowserEntry):
    """

    name: DominoNucleusDatasetUiDataSetFileBrowserEntry
    size: DominoNucleusDatasetUiDataSetFileBrowserEntry
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.to_dict()

        size = self.size.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_dataset_ui_data_set_file_browser_entry import (
            DominoNucleusDatasetUiDataSetFileBrowserEntry,
        )

        d = dict(src_dict)
        name = DominoNucleusDatasetUiDataSetFileBrowserEntry.from_dict(d.pop("name"))

        size = DominoNucleusDatasetUiDataSetFileBrowserEntry.from_dict(d.pop("size"))

        domino_nucleus_dataset_ui_data_set_file_browser_row = cls(
            name=name,
            size=size,
        )

        domino_nucleus_dataset_ui_data_set_file_browser_row.additional_properties = d
        return domino_nucleus_dataset_ui_data_set_file_browser_row

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
