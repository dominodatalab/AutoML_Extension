from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ui_mount_point_type_configs import UIMountPointTypeConfigs


T = TypeVar("T", bound="ExtensionPatchRequest")


@_attrs_define
class ExtensionPatchRequest:
    """
    Attributes:
        app_version_id (str | Unset): The version of the App to associate the Extension with.
        description (str | Unset): The description of the Extension.
        enabled (bool | Unset): Whether the Extension is globally enabled or disabled.
        name (str | Unset): The name of the Extension.
        ui_mount_point_type_configs (UIMountPointTypeConfigs | Unset): The configuration for the UI mount points of the
            Extension. Each property corresponds to a different mount point in the Domino UI where the Extension can be
            mounted.
    """

    app_version_id: str | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    name: str | Unset = UNSET
    ui_mount_point_type_configs: UIMountPointTypeConfigs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_version_id = self.app_version_id

        description = self.description

        enabled = self.enabled

        name = self.name

        ui_mount_point_type_configs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ui_mount_point_type_configs, Unset):
            ui_mount_point_type_configs = self.ui_mount_point_type_configs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_version_id is not UNSET:
            field_dict["appVersionId"] = app_version_id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if ui_mount_point_type_configs is not UNSET:
            field_dict["uiMountPointTypeConfigs"] = ui_mount_point_type_configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_mount_point_type_configs import UIMountPointTypeConfigs

        d = dict(src_dict)
        app_version_id = d.pop("appVersionId", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        _ui_mount_point_type_configs = d.pop("uiMountPointTypeConfigs", UNSET)
        ui_mount_point_type_configs: UIMountPointTypeConfigs | Unset
        if isinstance(_ui_mount_point_type_configs, Unset):
            ui_mount_point_type_configs = UNSET
        else:
            ui_mount_point_type_configs = UIMountPointTypeConfigs.from_dict(_ui_mount_point_type_configs)

        extension_patch_request = cls(
            app_version_id=app_version_id,
            description=description,
            enabled=enabled,
            name=name,
            ui_mount_point_type_configs=ui_mount_point_type_configs,
        )

        extension_patch_request.additional_properties = d
        return extension_patch_request

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
