from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_rw_snapshot_dto import DominoDatasetrwApiDatasetRwSnapshotDto
    from ..models.domino_datasetrw_api_dataset_rw_storage_info_dto import DominoDatasetrwApiDatasetRwStorageInfoDto


T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwSnapshotSummaryDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwSnapshotSummaryDto:
    """
    Attributes:
        snapshot (DominoDatasetrwApiDatasetRwSnapshotDto):
        is_read_write (bool):
        author_username (None | str | Unset):
        dataset_description (None | str | Unset):
        storage_info (DominoDatasetrwApiDatasetRwStorageInfoDto | Unset):
    """

    snapshot: DominoDatasetrwApiDatasetRwSnapshotDto
    is_read_write: bool
    author_username: None | str | Unset = UNSET
    dataset_description: None | str | Unset = UNSET
    storage_info: DominoDatasetrwApiDatasetRwStorageInfoDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot = self.snapshot.to_dict()

        is_read_write = self.is_read_write

        author_username: None | str | Unset
        if isinstance(self.author_username, Unset):
            author_username = UNSET
        else:
            author_username = self.author_username

        dataset_description: None | str | Unset
        if isinstance(self.dataset_description, Unset):
            dataset_description = UNSET
        else:
            dataset_description = self.dataset_description

        storage_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_info, Unset):
            storage_info = self.storage_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshot": snapshot,
                "isReadWrite": is_read_write,
            }
        )
        if author_username is not UNSET:
            field_dict["authorUsername"] = author_username
        if dataset_description is not UNSET:
            field_dict["datasetDescription"] = dataset_description
        if storage_info is not UNSET:
            field_dict["storageInfo"] = storage_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_rw_snapshot_dto import DominoDatasetrwApiDatasetRwSnapshotDto
        from ..models.domino_datasetrw_api_dataset_rw_storage_info_dto import DominoDatasetrwApiDatasetRwStorageInfoDto

        d = dict(src_dict)
        snapshot = DominoDatasetrwApiDatasetRwSnapshotDto.from_dict(d.pop("snapshot"))

        is_read_write = d.pop("isReadWrite")

        def _parse_author_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_username = _parse_author_username(d.pop("authorUsername", UNSET))

        def _parse_dataset_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_description = _parse_dataset_description(d.pop("datasetDescription", UNSET))

        _storage_info = d.pop("storageInfo", UNSET)
        storage_info: DominoDatasetrwApiDatasetRwStorageInfoDto | Unset
        if isinstance(_storage_info, Unset):
            storage_info = UNSET
        else:
            storage_info = DominoDatasetrwApiDatasetRwStorageInfoDto.from_dict(_storage_info)

        domino_datasetrw_api_dataset_rw_snapshot_summary_dto = cls(
            snapshot=snapshot,
            is_read_write=is_read_write,
            author_username=author_username,
            dataset_description=dataset_description,
            storage_info=storage_info,
        )

        domino_datasetrw_api_dataset_rw_snapshot_summary_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_snapshot_summary_dto

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
