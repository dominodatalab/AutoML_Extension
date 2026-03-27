from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwFileDetailsDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwFileDetailsDto:
    """
    Attributes:
        label (str):
        is_directory (bool | None | Unset):
        sortable_name (None | str | Unset):
        file_name (None | str | Unset):
        url (None | str | Unset):
        size_in_bytes (int | None | Unset):
    """

    label: str
    is_directory: bool | None | Unset = UNSET
    sortable_name: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    size_in_bytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        is_directory: bool | None | Unset
        if isinstance(self.is_directory, Unset):
            is_directory = UNSET
        else:
            is_directory = self.is_directory

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

        size_in_bytes: int | None | Unset
        if isinstance(self.size_in_bytes, Unset):
            size_in_bytes = UNSET
        else:
            size_in_bytes = self.size_in_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if is_directory is not UNSET:
            field_dict["isDirectory"] = is_directory
        if sortable_name is not UNSET:
            field_dict["sortableName"] = sortable_name
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if url is not UNSET:
            field_dict["url"] = url
        if size_in_bytes is not UNSET:
            field_dict["sizeInBytes"] = size_in_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        def _parse_is_directory(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_directory = _parse_is_directory(d.pop("isDirectory", UNSET))

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

        def _parse_size_in_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_in_bytes = _parse_size_in_bytes(d.pop("sizeInBytes", UNSET))

        domino_datasetrw_api_dataset_rw_file_details_dto = cls(
            label=label,
            is_directory=is_directory,
            sortable_name=sortable_name,
            file_name=file_name,
            url=url,
            size_in_bytes=size_in_bytes,
        )

        domino_datasetrw_api_dataset_rw_file_details_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_file_details_dto

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
