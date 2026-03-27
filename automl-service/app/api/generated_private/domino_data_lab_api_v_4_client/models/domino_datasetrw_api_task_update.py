from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiTaskUpdate")


@_attrs_define
class DominoDatasetrwApiTaskUpdate:
    """
    Attributes:
        time_remaining (int | None | Unset):
        progress (int | None | Unset):
        deleted_files (int | None | Unset):
        file_count (int | None | Unset):
        total_size (int | None | Unset):
    """

    time_remaining: int | None | Unset = UNSET
    progress: int | None | Unset = UNSET
    deleted_files: int | None | Unset = UNSET
    file_count: int | None | Unset = UNSET
    total_size: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_remaining: int | None | Unset
        if isinstance(self.time_remaining, Unset):
            time_remaining = UNSET
        else:
            time_remaining = self.time_remaining

        progress: int | None | Unset
        if isinstance(self.progress, Unset):
            progress = UNSET
        else:
            progress = self.progress

        deleted_files: int | None | Unset
        if isinstance(self.deleted_files, Unset):
            deleted_files = UNSET
        else:
            deleted_files = self.deleted_files

        file_count: int | None | Unset
        if isinstance(self.file_count, Unset):
            file_count = UNSET
        else:
            file_count = self.file_count

        total_size: int | None | Unset
        if isinstance(self.total_size, Unset):
            total_size = UNSET
        else:
            total_size = self.total_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_remaining is not UNSET:
            field_dict["timeRemaining"] = time_remaining
        if progress is not UNSET:
            field_dict["progress"] = progress
        if deleted_files is not UNSET:
            field_dict["deletedFiles"] = deleted_files
        if file_count is not UNSET:
            field_dict["fileCount"] = file_count
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_time_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_remaining = _parse_time_remaining(d.pop("timeRemaining", UNSET))

        def _parse_progress(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress = _parse_progress(d.pop("progress", UNSET))

        def _parse_deleted_files(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        deleted_files = _parse_deleted_files(d.pop("deletedFiles", UNSET))

        def _parse_file_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_count = _parse_file_count(d.pop("fileCount", UNSET))

        def _parse_total_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_size = _parse_total_size(d.pop("totalSize", UNSET))

        domino_datasetrw_api_task_update = cls(
            time_remaining=time_remaining,
            progress=progress,
            deleted_files=deleted_files,
            file_count=file_count,
            total_size=total_size,
        )

        domino_datasetrw_api_task_update.additional_properties = d
        return domino_datasetrw_api_task_update

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
