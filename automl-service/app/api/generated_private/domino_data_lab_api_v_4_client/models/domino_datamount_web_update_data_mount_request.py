from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatamountWebUpdateDataMountRequest")


@_attrs_define
class DominoDatamountWebUpdateDataMountRequest:
    """
    Attributes:
        id (str):
        name (str):
        mount_path (str):
        users (list[str]):
        projects (list[str]):
        read_only (bool):
        is_public (bool):
        is_registered (bool):
        data_plane_ids (list[str]):
        description (None | str | Unset):
        status (None | str | Unset):
    """

    id: str
    name: str
    mount_path: str
    users: list[str]
    projects: list[str]
    read_only: bool
    is_public: bool
    is_registered: bool
    data_plane_ids: list[str]
    description: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        mount_path = self.mount_path

        users = self.users

        projects = self.projects

        read_only = self.read_only

        is_public = self.is_public

        is_registered = self.is_registered

        data_plane_ids = self.data_plane_ids

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "mountPath": mount_path,
                "users": users,
                "projects": projects,
                "readOnly": read_only,
                "isPublic": is_public,
                "isRegistered": is_registered,
                "dataPlaneIds": data_plane_ids,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        mount_path = d.pop("mountPath")

        users = cast(list[str], d.pop("users"))

        projects = cast(list[str], d.pop("projects"))

        read_only = d.pop("readOnly")

        is_public = d.pop("isPublic")

        is_registered = d.pop("isRegistered")

        data_plane_ids = cast(list[str], d.pop("dataPlaneIds"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        domino_datamount_web_update_data_mount_request = cls(
            id=id,
            name=name,
            mount_path=mount_path,
            users=users,
            projects=projects,
            read_only=read_only,
            is_public=is_public,
            is_registered=is_registered,
            data_plane_ids=data_plane_ids,
            description=description,
            status=status,
        )

        domino_datamount_web_update_data_mount_request.additional_properties = d
        return domino_datamount_web_update_data_mount_request

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
