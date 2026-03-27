from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoNucleusDatasetUiDataSetFileBrowserEntry")


@_attrs_define
class DominoNucleusDatasetUiDataSetFileBrowserEntry:
    """
    Attributes:
        label (str):
        is_dir (bool | None | Unset):
        sortable_name (None | str | Unset):
        file_name (None | str | Unset):
        url (None | str | Unset):
        in_bytes (int | None | Unset):
    """

    label: str
    is_dir: bool | None | Unset = UNSET
    sortable_name: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    in_bytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        is_dir: bool | None | Unset
        if isinstance(self.is_dir, Unset):
            is_dir = UNSET
        else:
            is_dir = self.is_dir

        sortable_name: None | str | Unset
        if isinstance(self.sortable_name, Unset):
            sortable_name = UNSET
        else:
            sortable_name = self.sortable_name

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        in_bytes: int | None | Unset
        if isinstance(self.in_bytes, Unset):
            in_bytes = UNSET
        else:
            in_bytes = self.in_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if is_dir is not UNSET:
            field_dict["isDir"] = is_dir
        if sortable_name is not UNSET:
            field_dict["sortableName"] = sortable_name
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if url is not UNSET:
            field_dict["url"] = url
        if in_bytes is not UNSET:
            field_dict["inBytes"] = in_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        def _parse_is_dir(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_dir = _parse_is_dir(d.pop("isDir", UNSET))

        def _parse_sortable_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sortable_name = _parse_sortable_name(d.pop("sortableName", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_in_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        in_bytes = _parse_in_bytes(d.pop("inBytes", UNSET))

        domino_nucleus_dataset_ui_data_set_file_browser_entry = cls(
            label=label,
            is_dir=is_dir,
            sortable_name=sortable_name,
            file_name=file_name,
            url=url,
            in_bytes=in_bytes,
        )

        domino_nucleus_dataset_ui_data_set_file_browser_entry.additional_properties = d
        return domino_nucleus_dataset_ui_data_set_file_browser_entry

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
