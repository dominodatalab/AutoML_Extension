from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_filetask_copy_update_dto_snapshot_status import (
    DominoDatasetrwApiDatasetRwFiletaskCopyUpdateDtoSnapshotStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwFiletaskCopyUpdateDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwFiletaskCopyUpdateDto:
    """
    Attributes:
        progress (int):
        snapshot_id (str):
        snapshot_status (DominoDatasetrwApiDatasetRwFiletaskCopyUpdateDtoSnapshotStatus):
        time_remaining (int | None | Unset):
        error_code (int | None | Unset):
        error_message (None | str | Unset):
    """

    progress: int
    snapshot_id: str
    snapshot_status: DominoDatasetrwApiDatasetRwFiletaskCopyUpdateDtoSnapshotStatus
    time_remaining: int | None | Unset = UNSET
    error_code: int | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        progress = self.progress

        snapshot_id = self.snapshot_id

        snapshot_status = self.snapshot_status.value

        time_remaining: int | None | Unset
        if isinstance(self.time_remaining, Unset):
            time_remaining = UNSET
        else:
            time_remaining = self.time_remaining

        error_code: int | None | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "progress": progress,
                "snapshotId": snapshot_id,
                "snapshotStatus": snapshot_status,
            }
        )
        if time_remaining is not UNSET:
            field_dict["timeRemaining"] = time_remaining
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        progress = d.pop("progress")

        snapshot_id = d.pop("snapshotId")

        snapshot_status = DominoDatasetrwApiDatasetRwFiletaskCopyUpdateDtoSnapshotStatus(d.pop("snapshotStatus"))

        def _parse_time_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_remaining = _parse_time_remaining(d.pop("timeRemaining", UNSET))

        def _parse_error_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        error_code = _parse_error_code(d.pop("errorCode", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        domino_datasetrw_api_dataset_rw_filetask_copy_update_dto = cls(
            progress=progress,
            snapshot_id=snapshot_id,
            snapshot_status=snapshot_status,
            time_remaining=time_remaining,
            error_code=error_code,
            error_message=error_message,
        )

        domino_datasetrw_api_dataset_rw_filetask_copy_update_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_filetask_copy_update_dto

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
