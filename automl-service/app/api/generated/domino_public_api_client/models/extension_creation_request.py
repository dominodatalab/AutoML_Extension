from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ui_mount_point_type_configs import UIMountPointTypeConfigs


T = TypeVar("T", bound="ExtensionCreationRequest")


@_attrs_define
class ExtensionCreationRequest:
    """
    Attributes:
        app_id (str): The id of the App to associate the Extension with.
        app_version_id (str): The version of the App to associate the Extension with.
        enabled (bool): Whether the Extension is globally enabled or disabled.
        name (str): The name of the Extension.
        ui_mount_point_type_configs (UIMountPointTypeConfigs): The configuration for the UI mount points of the
            Extension. Each property corresponds to a different mount point in the Domino UI where the Extension can be
            mounted.
        description (str | Unset): The description of the Extension.
    """

    app_id: str
    app_version_id: str
    enabled: bool
    name: str
    ui_mount_point_type_configs: UIMountPointTypeConfigs
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_version_id = self.app_version_id

        enabled = self.enabled

        name = self.name

        ui_mount_point_type_configs = self.ui_mount_point_type_configs.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appId": app_id,
                "appVersionId": app_version_id,
                "enabled": enabled,
                "name": name,
                "uiMountPointTypeConfigs": ui_mount_point_type_configs,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_mount_point_type_configs import UIMountPointTypeConfigs

        d = dict(src_dict)
        app_id = d.pop("appId")

        app_version_id = d.pop("appVersionId")

        enabled = d.pop("enabled")

        name = d.pop("name")

        ui_mount_point_type_configs = UIMountPointTypeConfigs.from_dict(d.pop("uiMountPointTypeConfigs"))

        description = d.pop("description", UNSET)

        extension_creation_request = cls(
            app_id=app_id,
            app_version_id=app_version_id,
            enabled=enabled,
            name=name,
            ui_mount_point_type_configs=ui_mount_point_type_configs,
            description=description,
        )

        extension_creation_request.additional_properties = d
        return extension_creation_request

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
