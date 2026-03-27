from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspace_api_volume_mount_dto import DominoWorkspaceApiVolumeMountDto


T = TypeVar("T", bound="DominoWorkspaceApiNetAppVolumeMountSpecificationDto")


@_attrs_define
class DominoWorkspaceApiNetAppVolumeMountSpecificationDto:
    """
    Attributes:
        pvc_name (str):
        volume_id (str):
        volume_name (str):
        snapshot_mount (DominoWorkspaceApiVolumeMountDto | Unset):
        volume_mount (DominoWorkspaceApiVolumeMountDto | Unset):
        other_mounts (list[DominoWorkspaceApiVolumeMountDto] | None | Unset):
    """

    pvc_name: str
    volume_id: str
    volume_name: str
    snapshot_mount: DominoWorkspaceApiVolumeMountDto | Unset = UNSET
    volume_mount: DominoWorkspaceApiVolumeMountDto | Unset = UNSET
    other_mounts: list[DominoWorkspaceApiVolumeMountDto] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pvc_name = self.pvc_name

        volume_id = self.volume_id

        volume_name = self.volume_name

        snapshot_mount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_mount, Unset):
            snapshot_mount = self.snapshot_mount.to_dict()

        volume_mount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.volume_mount, Unset):
            volume_mount = self.volume_mount.to_dict()

        other_mounts: list[dict[str, Any]] | None | Unset
        if isinstance(self.other_mounts, Unset):
            other_mounts = UNSET
        elif isinstance(self.other_mounts, list):
            other_mounts = []
            for other_mounts_type_0_item_data in self.other_mounts:
                other_mounts_type_0_item = other_mounts_type_0_item_data.to_dict()
                other_mounts.append(other_mounts_type_0_item)

        else:
            other_mounts = self.other_mounts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pvcName": pvc_name,
                "volumeId": volume_id,
                "volumeName": volume_name,
            }
        )
        if snapshot_mount is not UNSET:
            field_dict["snapshotMount"] = snapshot_mount
        if volume_mount is not UNSET:
            field_dict["volumeMount"] = volume_mount
        if other_mounts is not UNSET:
            field_dict["otherMounts"] = other_mounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_volume_mount_dto import DominoWorkspaceApiVolumeMountDto

        d = dict(src_dict)
        pvc_name = d.pop("pvcName")

        volume_id = d.pop("volumeId")

        volume_name = d.pop("volumeName")

        _snapshot_mount = d.pop("snapshotMount", UNSET)
        snapshot_mount: DominoWorkspaceApiVolumeMountDto | Unset
        if isinstance(_snapshot_mount, Unset):
            snapshot_mount = UNSET
        else:
            snapshot_mount = DominoWorkspaceApiVolumeMountDto.from_dict(_snapshot_mount)

        _volume_mount = d.pop("volumeMount", UNSET)
        volume_mount: DominoWorkspaceApiVolumeMountDto | Unset
        if isinstance(_volume_mount, Unset):
            volume_mount = UNSET
        else:
            volume_mount = DominoWorkspaceApiVolumeMountDto.from_dict(_volume_mount)

        def _parse_other_mounts(data: object) -> list[DominoWorkspaceApiVolumeMountDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                other_mounts_type_0 = []
                _other_mounts_type_0 = data
                for other_mounts_type_0_item_data in _other_mounts_type_0:
                    other_mounts_type_0_item = DominoWorkspaceApiVolumeMountDto.from_dict(other_mounts_type_0_item_data)

                    other_mounts_type_0.append(other_mounts_type_0_item)

                return other_mounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoWorkspaceApiVolumeMountDto] | None | Unset, data)

        other_mounts = _parse_other_mounts(d.pop("otherMounts", UNSET))

        domino_workspace_api_net_app_volume_mount_specification_dto = cls(
            pvc_name=pvc_name,
            volume_id=volume_id,
            volume_name=volume_name,
            snapshot_mount=snapshot_mount,
            volume_mount=volume_mount,
            other_mounts=other_mounts,
        )

        domino_workspace_api_net_app_volume_mount_specification_dto.additional_properties = d
        return domino_workspace_api_net_app_volume_mount_specification_dto

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
