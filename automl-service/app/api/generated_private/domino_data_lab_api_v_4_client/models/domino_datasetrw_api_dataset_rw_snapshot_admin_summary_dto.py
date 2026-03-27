from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_rw_snapshot_dto import DominoDatasetrwApiDatasetRwSnapshotDto


T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwSnapshotAdminSummaryDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwSnapshotAdminSummaryDto:
    """
    Attributes:
        snapshot (DominoDatasetrwApiDatasetRwSnapshotDto):
        dataset_name (str):
        project_name (str):
        owner_username (None | str | Unset):
        storage_name (None | str | Unset):
    """

    snapshot: DominoDatasetrwApiDatasetRwSnapshotDto
    dataset_name: str
    project_name: str
    owner_username: None | str | Unset = UNSET
    storage_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot = self.snapshot.to_dict()

        dataset_name = self.dataset_name

        project_name = self.project_name

        owner_username: None | str | Unset
        if isinstance(self.owner_username, Unset):
            owner_username = UNSET
        else:
            owner_username = self.owner_username

        storage_name: None | str | Unset
        if isinstance(self.storage_name, Unset):
            storage_name = UNSET
        else:
            storage_name = self.storage_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshot": snapshot,
                "datasetName": dataset_name,
                "projectName": project_name,
            }
        )
        if owner_username is not UNSET:
            field_dict["ownerUsername"] = owner_username
        if storage_name is not UNSET:
            field_dict["storageName"] = storage_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_rw_snapshot_dto import DominoDatasetrwApiDatasetRwSnapshotDto

        d = dict(src_dict)
        snapshot = DominoDatasetrwApiDatasetRwSnapshotDto.from_dict(d.pop("snapshot"))

        dataset_name = d.pop("datasetName")

        project_name = d.pop("projectName")

        def _parse_owner_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_username = _parse_owner_username(d.pop("ownerUsername", UNSET))

        def _parse_storage_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_name = _parse_storage_name(d.pop("storageName", UNSET))

        domino_datasetrw_api_dataset_rw_snapshot_admin_summary_dto = cls(
            snapshot=snapshot,
            dataset_name=dataset_name,
            project_name=project_name,
            owner_username=owner_username,
            storage_name=storage_name,
        )

        domino_datasetrw_api_dataset_rw_snapshot_admin_summary_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_snapshot_admin_summary_dto

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
