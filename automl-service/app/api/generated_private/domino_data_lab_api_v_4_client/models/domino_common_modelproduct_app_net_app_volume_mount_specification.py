from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_modelproduct_app_volume_mount import DominoCommonModelproductAppVolumeMount


T = TypeVar("T", bound="DominoCommonModelproductAppNetAppVolumeMountSpecification")


@_attrs_define
class DominoCommonModelproductAppNetAppVolumeMountSpecification:
    """
    Attributes:
        pvc_name (str):
        volume_id (str):
        volume_name (str):
        volume_mount (DominoCommonModelproductAppVolumeMount | Unset):
        snapshot_mount (DominoCommonModelproductAppVolumeMount | Unset):
        other_mounts (list[DominoCommonModelproductAppVolumeMount] | None | Unset):
    """

    pvc_name: str
    volume_id: str
    volume_name: str
    volume_mount: DominoCommonModelproductAppVolumeMount | Unset = UNSET
    snapshot_mount: DominoCommonModelproductAppVolumeMount | Unset = UNSET
    other_mounts: list[DominoCommonModelproductAppVolumeMount] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pvc_name = self.pvc_name

        volume_id = self.volume_id

        volume_name = self.volume_name

        volume_mount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.volume_mount, Unset):
            volume_mount = self.volume_mount.to_dict()

        snapshot_mount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot_mount, Unset):
            snapshot_mount = self.snapshot_mount.to_dict()

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
        if volume_mount is not UNSET:
            field_dict["volumeMount"] = volume_mount
        if snapshot_mount is not UNSET:
            field_dict["snapshotMount"] = snapshot_mount
        if other_mounts is not UNSET:
            field_dict["otherMounts"] = other_mounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_modelproduct_app_volume_mount import DominoCommonModelproductAppVolumeMount

        d = dict(src_dict)
        pvc_name = d.pop("pvcName")

        volume_id = d.pop("volumeId")

        volume_name = d.pop("volumeName")

        _volume_mount = d.pop("volumeMount", UNSET)
        volume_mount: DominoCommonModelproductAppVolumeMount | Unset
        if isinstance(_volume_mount, Unset):
            volume_mount = UNSET
        else:
            volume_mount = DominoCommonModelproductAppVolumeMount.from_dict(_volume_mount)

        _snapshot_mount = d.pop("snapshotMount", UNSET)
        snapshot_mount: DominoCommonModelproductAppVolumeMount | Unset
        if isinstance(_snapshot_mount, Unset):
            snapshot_mount = UNSET
        else:
            snapshot_mount = DominoCommonModelproductAppVolumeMount.from_dict(_snapshot_mount)

        def _parse_other_mounts(data: object) -> list[DominoCommonModelproductAppVolumeMount] | None | Unset:
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
                    other_mounts_type_0_item = DominoCommonModelproductAppVolumeMount.from_dict(
                        other_mounts_type_0_item_data
                    )

                    other_mounts_type_0.append(other_mounts_type_0_item)

                return other_mounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoCommonModelproductAppVolumeMount] | None | Unset, data)

        other_mounts = _parse_other_mounts(d.pop("otherMounts", UNSET))

        domino_common_modelproduct_app_net_app_volume_mount_specification = cls(
            pvc_name=pvc_name,
            volume_id=volume_id,
            volume_name=volume_name,
            volume_mount=volume_mount,
            snapshot_mount=snapshot_mount,
            other_mounts=other_mounts,
        )

        domino_common_modelproduct_app_net_app_volume_mount_specification.additional_properties = d
        return domino_common_modelproduct_app_net_app_volume_mount_specification

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
