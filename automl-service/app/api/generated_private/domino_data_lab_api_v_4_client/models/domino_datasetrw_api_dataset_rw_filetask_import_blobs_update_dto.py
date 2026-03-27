from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_filetask_import_blobs_update_dto_snapshot_status import (
    DominoDatasetrwApiDatasetRwFiletaskImportBlobsUpdateDtoSnapshotStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwFiletaskImportBlobsUpdateDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwFiletaskImportBlobsUpdateDto:
    """
    Attributes:
        progress (int):
        error_code (int | None | Unset):
        error_message (None | str | Unset):
        snapshot_id (None | str | Unset):
        snapshot_status (DominoDatasetrwApiDatasetRwFiletaskImportBlobsUpdateDtoSnapshotStatus | Unset):
    """

    progress: int
    error_code: int | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    snapshot_id: None | str | Unset = UNSET
    snapshot_status: DominoDatasetrwApiDatasetRwFiletaskImportBlobsUpdateDtoSnapshotStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        progress = self.progress

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

        snapshot_id: None | str | Unset
        if isinstance(self.snapshot_id, Unset):
            snapshot_id = UNSET
        else:
            snapshot_id = self.snapshot_id

        snapshot_status: str | Unset = UNSET
        if not isinstance(self.snapshot_status, Unset):
            snapshot_status = self.snapshot_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "progress": progress,
            }
        )
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if snapshot_id is not UNSET:
            field_dict["snapshotId"] = snapshot_id
        if snapshot_status is not UNSET:
            field_dict["snapshotStatus"] = snapshot_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        progress = d.pop("progress")

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

        def _parse_snapshot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snapshot_id = _parse_snapshot_id(d.pop("snapshotId", UNSET))

        _snapshot_status = d.pop("snapshotStatus", UNSET)
        snapshot_status: DominoDatasetrwApiDatasetRwFiletaskImportBlobsUpdateDtoSnapshotStatus | Unset
        if isinstance(_snapshot_status, Unset):
            snapshot_status = UNSET
        else:
            snapshot_status = DominoDatasetrwApiDatasetRwFiletaskImportBlobsUpdateDtoSnapshotStatus(_snapshot_status)

        domino_datasetrw_api_dataset_rw_filetask_import_blobs_update_dto = cls(
            progress=progress,
            error_code=error_code,
            error_message=error_message,
            snapshot_id=snapshot_id,
            snapshot_status=snapshot_status,
        )

        domino_datasetrw_api_dataset_rw_filetask_import_blobs_update_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_filetask_import_blobs_update_dto

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
