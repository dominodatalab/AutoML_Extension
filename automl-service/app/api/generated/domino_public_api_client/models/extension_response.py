from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ui_mount_point_type_configs import UIMountPointTypeConfigs
    from ..models.user_summary import UserSummary


T = TypeVar("T", bound="ExtensionResponse")


@_attrs_define
class ExtensionResponse:
    """
    Attributes:
        app_id (str): The id of the App to associate the Extension with.
        app_version_id (str): The version of the App to associate the Extension with.
        created_at (datetime.datetime): The date and time when the Extension was created.
        created_by (UserSummary): Information about a Domino user including id and names.
        enabled (bool): Whether the Extension is globally enabled or disabled.
        id (str): The id of the Extension.
        name (str): The name of the Extension.
        ui_mount_point_type_configs (UIMountPointTypeConfigs): The configuration for the UI mount points of the
            Extension. Each property corresponds to a different mount point in the Domino UI where the Extension can be
            mounted.
        updated_at (datetime.datetime): The date and time when the Extension was last updated.
        updated_by (UserSummary): Information about a Domino user including id and names.
        deleted_at (datetime.datetime | Unset): The date and time when the Extension was deleted. If null, the Extension
            has not been deleted.
        deleted_by (UserSummary | Unset): Information about a Domino user including id and names.
        description (str | Unset): The description of the Extension.
    """

    app_id: str
    app_version_id: str
    created_at: datetime.datetime
    created_by: UserSummary
    enabled: bool
    id: str
    name: str
    ui_mount_point_type_configs: UIMountPointTypeConfigs
    updated_at: datetime.datetime
    updated_by: UserSummary
    deleted_at: datetime.datetime | Unset = UNSET
    deleted_by: UserSummary | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_version_id = self.app_version_id

        created_at = self.created_at.isoformat()

        created_by = self.created_by.to_dict()

        enabled = self.enabled

        id = self.id

        name = self.name

        ui_mount_point_type_configs = self.ui_mount_point_type_configs.to_dict()

        updated_at = self.updated_at.isoformat()

        updated_by = self.updated_by.to_dict()

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        deleted_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deleted_by, Unset):
            deleted_by = self.deleted_by.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appId": app_id,
                "appVersionId": app_version_id,
                "createdAt": created_at,
                "createdBy": created_by,
                "enabled": enabled,
                "id": id,
                "name": name,
                "uiMountPointTypeConfigs": ui_mount_point_type_configs,
                "updatedAt": updated_at,
                "updatedBy": updated_by,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if deleted_by is not UNSET:
            field_dict["deletedBy"] = deleted_by
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_mount_point_type_configs import UIMountPointTypeConfigs
        from ..models.user_summary import UserSummary

        d = dict(src_dict)
        app_id = d.pop("appId")

        app_version_id = d.pop("appVersionId")

        created_at = isoparse(d.pop("createdAt"))

        created_by = UserSummary.from_dict(d.pop("createdBy"))

        enabled = d.pop("enabled")

        id = d.pop("id")

        name = d.pop("name")

        ui_mount_point_type_configs = UIMountPointTypeConfigs.from_dict(d.pop("uiMountPointTypeConfigs"))

        updated_at = isoparse(d.pop("updatedAt"))

        updated_by = UserSummary.from_dict(d.pop("updatedBy"))

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _deleted_by = d.pop("deletedBy", UNSET)
        deleted_by: UserSummary | Unset
        if isinstance(_deleted_by, Unset):
            deleted_by = UNSET
        else:
            deleted_by = UserSummary.from_dict(_deleted_by)

        description = d.pop("description", UNSET)

        extension_response = cls(
            app_id=app_id,
            app_version_id=app_version_id,
            created_at=created_at,
            created_by=created_by,
            enabled=enabled,
            id=id,
            name=name,
            ui_mount_point_type_configs=ui_mount_point_type_configs,
            updated_at=updated_at,
            updated_by=updated_by,
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            description=description,
        )

        extension_response.additional_properties = d
        return extension_response

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
