from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.net_app_volume_mount_v1_other_mounts_item import NetAppVolumeMountV1OtherMountsItem


T = TypeVar("T", bound="NetAppVolumeMountV1")


@_attrs_define
class NetAppVolumeMountV1:
    """
    Attributes:
        name (str): Name of Domino NetApp Volume to mount. Example: MyVolume.
        snapshot_mount_path (str): Path to mount the Snapshot directory of the Volume at. Example: /path/to/my/snapshot.
        snapshot_read_only (bool): Whether to mount the Snapshot directory as read only.
        volume_mount_path (str): Path to mount the Domino NetApp Volume at. Example: /path/to/my/volume.
        volume_read_only (bool): Whether to mount the Volume as read only.
        other_mounts (list[NetAppVolumeMountV1OtherMountsItem] | Unset): Additional mounts for the NetApp Volume.
        snapshot_sub_path (str | Unset): Path within the Snapshot directory to mount. The entire Snapshot directory will
            be mounted if not specified. Example: /my/snapshot/subPath.
        volume_sub_path (str | Unset): Path within the Domino NetApp Volume to mount. The entire Volume will be mounted
            if not specified. Example: /my/volume/subPath.
    """

    name: str
    snapshot_mount_path: str
    snapshot_read_only: bool
    volume_mount_path: str
    volume_read_only: bool
    other_mounts: list[NetAppVolumeMountV1OtherMountsItem] | Unset = UNSET
    snapshot_sub_path: str | Unset = UNSET
    volume_sub_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        snapshot_mount_path = self.snapshot_mount_path

        snapshot_read_only = self.snapshot_read_only

        volume_mount_path = self.volume_mount_path

        volume_read_only = self.volume_read_only

        other_mounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.other_mounts, Unset):
            other_mounts = []
            for other_mounts_item_data in self.other_mounts:
                other_mounts_item = other_mounts_item_data.to_dict()
                other_mounts.append(other_mounts_item)

        snapshot_sub_path = self.snapshot_sub_path

        volume_sub_path = self.volume_sub_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "snapshotMountPath": snapshot_mount_path,
                "snapshotReadOnly": snapshot_read_only,
                "volumeMountPath": volume_mount_path,
                "volumeReadOnly": volume_read_only,
            }
        )
        if other_mounts is not UNSET:
            field_dict["otherMounts"] = other_mounts
        if snapshot_sub_path is not UNSET:
            field_dict["snapshotSubPath"] = snapshot_sub_path
        if volume_sub_path is not UNSET:
            field_dict["volumeSubPath"] = volume_sub_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.net_app_volume_mount_v1_other_mounts_item import NetAppVolumeMountV1OtherMountsItem

        d = dict(src_dict)
        name = d.pop("name")

        snapshot_mount_path = d.pop("snapshotMountPath")

        snapshot_read_only = d.pop("snapshotReadOnly")

        volume_mount_path = d.pop("volumeMountPath")

        volume_read_only = d.pop("volumeReadOnly")

        _other_mounts = d.pop("otherMounts", UNSET)
        other_mounts: list[NetAppVolumeMountV1OtherMountsItem] | Unset = UNSET
        if _other_mounts is not UNSET:
            other_mounts = []
            for other_mounts_item_data in _other_mounts:
                other_mounts_item = NetAppVolumeMountV1OtherMountsItem.from_dict(other_mounts_item_data)

                other_mounts.append(other_mounts_item)

        snapshot_sub_path = d.pop("snapshotSubPath", UNSET)

        volume_sub_path = d.pop("volumeSubPath", UNSET)

        net_app_volume_mount_v1 = cls(
            name=name,
            snapshot_mount_path=snapshot_mount_path,
            snapshot_read_only=snapshot_read_only,
            volume_mount_path=volume_mount_path,
            volume_read_only=volume_read_only,
            other_mounts=other_mounts,
            snapshot_sub_path=snapshot_sub_path,
            volume_sub_path=volume_sub_path,
        )

        net_app_volume_mount_v1.additional_properties = d
        return net_app_volume_mount_v1

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
