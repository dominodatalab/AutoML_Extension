from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoGruzApiDatasetMount")


@_attrs_define
class DominoGruzApiDatasetMount:
    """
    Attributes:
        container_path (str):
        is_read_only (bool):
        dataset_id (None | str | Unset):
        snapshot_id (None | str | Unset):
        storage_mode (None | str | Unset):
        claim_name (None | str | Unset):
        resource_id (None | str | Unset):
        sub_dir (None | str | Unset):
    """

    container_path: str
    is_read_only: bool
    dataset_id: None | str | Unset = UNSET
    snapshot_id: None | str | Unset = UNSET
    storage_mode: None | str | Unset = UNSET
    claim_name: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    sub_dir: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_path = self.container_path

        is_read_only = self.is_read_only

        dataset_id: None | str | Unset
        if isinstance(self.dataset_id, Unset):
            dataset_id = UNSET
        else:
            dataset_id = self.dataset_id

        snapshot_id: None | str | Unset
        if isinstance(self.snapshot_id, Unset):
            snapshot_id = UNSET
        else:
            snapshot_id = self.snapshot_id

        storage_mode: None | str | Unset
        if isinstance(self.storage_mode, Unset):
            storage_mode = UNSET
        else:
            storage_mode = self.storage_mode

        claim_name: None | str | Unset
        if isinstance(self.claim_name, Unset):
            claim_name = UNSET
        else:
            claim_name = self.claim_name

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        sub_dir: None | str | Unset
        if isinstance(self.sub_dir, Unset):
            sub_dir = UNSET
        else:
            sub_dir = self.sub_dir

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerPath": container_path,
                "isReadOnly": is_read_only,
            }
        )
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if snapshot_id is not UNSET:
            field_dict["snapshotId"] = snapshot_id
        if storage_mode is not UNSET:
            field_dict["storageMode"] = storage_mode
        if claim_name is not UNSET:
            field_dict["claimName"] = claim_name
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if sub_dir is not UNSET:
            field_dict["subDir"] = sub_dir

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        container_path = d.pop("containerPath")

        is_read_only = d.pop("isReadOnly")

        def _parse_dataset_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_id = _parse_dataset_id(d.pop("datasetId", UNSET))

        def _parse_snapshot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snapshot_id = _parse_snapshot_id(d.pop("snapshotId", UNSET))

        def _parse_storage_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_mode = _parse_storage_mode(d.pop("storageMode", UNSET))

        def _parse_claim_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        claim_name = _parse_claim_name(d.pop("claimName", UNSET))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        def _parse_sub_dir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_dir = _parse_sub_dir(d.pop("subDir", UNSET))

        domino_gruz_api_dataset_mount = cls(
            container_path=container_path,
            is_read_only=is_read_only,
            dataset_id=dataset_id,
            snapshot_id=snapshot_id,
            storage_mode=storage_mode,
            claim_name=claim_name,
            resource_id=resource_id,
            sub_dir=sub_dir,
        )

        domino_gruz_api_dataset_mount.additional_properties = d
        return domino_gruz_api_dataset_mount

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
