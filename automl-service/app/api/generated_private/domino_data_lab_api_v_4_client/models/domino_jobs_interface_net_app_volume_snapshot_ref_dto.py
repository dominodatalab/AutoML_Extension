from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoJobsInterfaceNetAppVolumeSnapshotRefDto")


@_attrs_define
class DominoJobsInterfaceNetAppVolumeSnapshotRefDto:
    """
    Attributes:
        volume_id (str):
        snapshot_version (int):
        volume_name (None | str | Unset):
    """

    volume_id: str
    snapshot_version: int
    volume_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volume_id = self.volume_id

        snapshot_version = self.snapshot_version

        volume_name: None | str | Unset
        if isinstance(self.volume_name, Unset):
            volume_name = UNSET
        else:
            volume_name = self.volume_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volumeId": volume_id,
                "snapshotVersion": snapshot_version,
            }
        )
        if volume_name is not UNSET:
            field_dict["volumeName"] = volume_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume_id = d.pop("volumeId")

        snapshot_version = d.pop("snapshotVersion")

        def _parse_volume_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        volume_name = _parse_volume_name(d.pop("volumeName", UNSET))

        domino_jobs_interface_net_app_volume_snapshot_ref_dto = cls(
            volume_id=volume_id,
            snapshot_version=snapshot_version,
            volume_name=volume_name,
        )

        domino_jobs_interface_net_app_volume_snapshot_ref_dto.additional_properties = d
        return domino_jobs_interface_net_app_volume_snapshot_ref_dto

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
