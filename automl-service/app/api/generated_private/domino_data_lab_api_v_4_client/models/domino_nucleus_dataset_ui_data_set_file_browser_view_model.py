from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_nucleus_dataset_ui_data_set_file_browser_row import DominoNucleusDatasetUiDataSetFileBrowserRow


T = TypeVar("T", bound="DominoNucleusDatasetUiDataSetFileBrowserViewModel")


@_attrs_define
class DominoNucleusDatasetUiDataSetFileBrowserViewModel:
    """
    Attributes:
        rows (list[DominoNucleusDatasetUiDataSetFileBrowserRow]):
        directory_size (None | str | Unset):
    """

    rows: list[DominoNucleusDatasetUiDataSetFileBrowserRow]
    directory_size: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        directory_size: None | str | Unset
        if isinstance(self.directory_size, Unset):
            directory_size = UNSET
        else:
            directory_size = self.directory_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rows": rows,
            }
        )
        if directory_size is not UNSET:
            field_dict["directorySize"] = directory_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_dataset_ui_data_set_file_browser_row import (
            DominoNucleusDatasetUiDataSetFileBrowserRow,
        )

        d = dict(src_dict)
        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = DominoNucleusDatasetUiDataSetFileBrowserRow.from_dict(rows_item_data)

            rows.append(rows_item)

        def _parse_directory_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directory_size = _parse_directory_size(d.pop("directorySize", UNSET))

        domino_nucleus_dataset_ui_data_set_file_browser_view_model = cls(
            rows=rows,
            directory_size=directory_size,
        )

        domino_nucleus_dataset_ui_data_set_file_browser_view_model.additional_properties = d
        return domino_nucleus_dataset_ui_data_set_file_browser_view_model

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
