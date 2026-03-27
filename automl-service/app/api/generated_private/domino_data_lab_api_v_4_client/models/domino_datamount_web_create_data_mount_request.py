from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datamount_web_create_data_mount_request_volume_type import (
    DominoDatamountWebCreateDataMountRequestVolumeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatamountWebCreateDataMountRequest")


@_attrs_define
class DominoDatamountWebCreateDataMountRequest:
    """
    Attributes:
        name (str):
        volume_type (DominoDatamountWebCreateDataMountRequestVolumeType):
        pvc_name (str):
        mount_path (str):
        users (list[str]):
        read_only (bool):
        is_public (bool):
        data_plane_ids (list[str]):
        description (None | str | Unset):
        pv_id (None | str | Unset):
    """

    name: str
    volume_type: DominoDatamountWebCreateDataMountRequestVolumeType
    pvc_name: str
    mount_path: str
    users: list[str]
    read_only: bool
    is_public: bool
    data_plane_ids: list[str]
    description: None | str | Unset = UNSET
    pv_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        volume_type = self.volume_type.value

        pvc_name = self.pvc_name

        mount_path = self.mount_path

        users = self.users

        read_only = self.read_only

        is_public = self.is_public

        data_plane_ids = self.data_plane_ids

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        pv_id: None | str | Unset
        if isinstance(self.pv_id, Unset):
            pv_id = UNSET
        else:
            pv_id = self.pv_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "volumeType": volume_type,
                "pvcName": pvc_name,
                "mountPath": mount_path,
                "users": users,
                "readOnly": read_only,
                "isPublic": is_public,
                "dataPlaneIds": data_plane_ids,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if pv_id is not UNSET:
            field_dict["pvId"] = pv_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        volume_type = DominoDatamountWebCreateDataMountRequestVolumeType(d.pop("volumeType"))

        pvc_name = d.pop("pvcName")

        mount_path = d.pop("mountPath")

        users = cast(list[str], d.pop("users"))

        read_only = d.pop("readOnly")

        is_public = d.pop("isPublic")

        data_plane_ids = cast(list[str], d.pop("dataPlaneIds"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_pv_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pv_id = _parse_pv_id(d.pop("pvId", UNSET))

        domino_datamount_web_create_data_mount_request = cls(
            name=name,
            volume_type=volume_type,
            pvc_name=pvc_name,
            mount_path=mount_path,
            users=users,
            read_only=read_only,
            is_public=is_public,
            data_plane_ids=data_plane_ids,
            description=description,
            pv_id=pv_id,
        )

        domino_datamount_web_create_data_mount_request.additional_properties = d
        return domino_datamount_web_create_data_mount_request

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
