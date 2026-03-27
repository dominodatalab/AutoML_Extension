from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoNucleusDatasetUiDatasetProjectMountSummaryViewModel")


@_attrs_define
class DominoNucleusDatasetUiDatasetProjectMountSummaryViewModel:
    """
    Attributes:
        dataset_id (str):
        name (str):
        owner_name (str):
        project_name (str):
        is_partial_size (bool):
        request_latest (bool):
        total_available_versions (int):
        path (str):
        snapshot_id (None | str | Unset):
        description (None | str | Unset):
        storage_size (int | None | Unset):
        requested_tag (None | str | Unset):
        requested_version_number (int | None | Unset):
        latest_version_number (int | None | Unset):
    """

    dataset_id: str
    name: str
    owner_name: str
    project_name: str
    is_partial_size: bool
    request_latest: bool
    total_available_versions: int
    path: str
    snapshot_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    storage_size: int | None | Unset = UNSET
    requested_tag: None | str | Unset = UNSET
    requested_version_number: int | None | Unset = UNSET
    latest_version_number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        name = self.name

        owner_name = self.owner_name

        project_name = self.project_name

        is_partial_size = self.is_partial_size

        request_latest = self.request_latest

        total_available_versions = self.total_available_versions

        path = self.path

        snapshot_id: None | str | Unset
        if isinstance(self.snapshot_id, Unset):
            snapshot_id = UNSET
        else:
            snapshot_id = self.snapshot_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        storage_size: int | None | Unset
        if isinstance(self.storage_size, Unset):
            storage_size = UNSET
        else:
            storage_size = self.storage_size

        requested_tag: None | str | Unset
        if isinstance(self.requested_tag, Unset):
            requested_tag = UNSET
        else:
            requested_tag = self.requested_tag

        requested_version_number: int | None | Unset
        if isinstance(self.requested_version_number, Unset):
            requested_version_number = UNSET
        else:
            requested_version_number = self.requested_version_number

        latest_version_number: int | None | Unset
        if isinstance(self.latest_version_number, Unset):
            latest_version_number = UNSET
        else:
            latest_version_number = self.latest_version_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "name": name,
                "ownerName": owner_name,
                "projectName": project_name,
                "isPartialSize": is_partial_size,
                "requestLatest": request_latest,
                "totalAvailableVersions": total_available_versions,
                "path": path,
            }
        )
        if snapshot_id is not UNSET:
            field_dict["snapshotId"] = snapshot_id
        if description is not UNSET:
            field_dict["description"] = description
        if storage_size is not UNSET:
            field_dict["storageSize"] = storage_size
        if requested_tag is not UNSET:
            field_dict["requestedTag"] = requested_tag
        if requested_version_number is not UNSET:
            field_dict["requestedVersionNumber"] = requested_version_number
        if latest_version_number is not UNSET:
            field_dict["latestVersionNumber"] = latest_version_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        name = d.pop("name")

        owner_name = d.pop("ownerName")

        project_name = d.pop("projectName")

        is_partial_size = d.pop("isPartialSize")

        request_latest = d.pop("requestLatest")

        total_available_versions = d.pop("totalAvailableVersions")

        path = d.pop("path")

        def _parse_snapshot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snapshot_id = _parse_snapshot_id(d.pop("snapshotId", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_storage_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_size = _parse_storage_size(d.pop("storageSize", UNSET))

        def _parse_requested_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_tag = _parse_requested_tag(d.pop("requestedTag", UNSET))

        def _parse_requested_version_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requested_version_number = _parse_requested_version_number(d.pop("requestedVersionNumber", UNSET))

        def _parse_latest_version_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_version_number = _parse_latest_version_number(d.pop("latestVersionNumber", UNSET))

        domino_nucleus_dataset_ui_dataset_project_mount_summary_view_model = cls(
            dataset_id=dataset_id,
            name=name,
            owner_name=owner_name,
            project_name=project_name,
            is_partial_size=is_partial_size,
            request_latest=request_latest,
            total_available_versions=total_available_versions,
            path=path,
            snapshot_id=snapshot_id,
            description=description,
            storage_size=storage_size,
            requested_tag=requested_tag,
            requested_version_number=requested_version_number,
            latest_version_number=latest_version_number,
        )

        domino_nucleus_dataset_ui_dataset_project_mount_summary_view_model.additional_properties = d
        return domino_nucleus_dataset_ui_dataset_project_mount_summary_view_model

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
