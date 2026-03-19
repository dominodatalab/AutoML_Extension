from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_update_request_visibility import AppUpdateRequestVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_access_status import AppAccessStatus
    from ..models.app_version_creation_request import AppVersionCreationRequest


T = TypeVar("T", bound="AppUpdateRequest")


@_attrs_define
class AppUpdateRequest:
    """
    Attributes:
        access_statuses (list[AppAccessStatus] | Unset):
        description (str | Unset):
        discoverable (bool | Unset):
        entry_point (str | Unset):
        mount_datasets (bool | Unset):
        mount_net_app_volumes (bool | Unset):
        name (str | Unset):
        render_i_frame (bool | Unset):
        version (AppVersionCreationRequest | Unset):
        visibility (AppUpdateRequestVisibility | Unset):
    """

    access_statuses: list[AppAccessStatus] | Unset = UNSET
    description: str | Unset = UNSET
    discoverable: bool | Unset = UNSET
    entry_point: str | Unset = UNSET
    mount_datasets: bool | Unset = UNSET
    mount_net_app_volumes: bool | Unset = UNSET
    name: str | Unset = UNSET
    render_i_frame: bool | Unset = UNSET
    version: AppVersionCreationRequest | Unset = UNSET
    visibility: AppUpdateRequestVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.access_statuses, Unset):
            access_statuses = []
            for access_statuses_item_data in self.access_statuses:
                access_statuses_item = access_statuses_item_data.to_dict()
                access_statuses.append(access_statuses_item)

        description = self.description

        discoverable = self.discoverable

        entry_point = self.entry_point

        mount_datasets = self.mount_datasets

        mount_net_app_volumes = self.mount_net_app_volumes

        name = self.name

        render_i_frame = self.render_i_frame

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_statuses is not UNSET:
            field_dict["accessStatuses"] = access_statuses
        if description is not UNSET:
            field_dict["description"] = description
        if discoverable is not UNSET:
            field_dict["discoverable"] = discoverable
        if entry_point is not UNSET:
            field_dict["entryPoint"] = entry_point
        if mount_datasets is not UNSET:
            field_dict["mountDatasets"] = mount_datasets
        if mount_net_app_volumes is not UNSET:
            field_dict["mountNetAppVolumes"] = mount_net_app_volumes
        if name is not UNSET:
            field_dict["name"] = name
        if render_i_frame is not UNSET:
            field_dict["renderIFrame"] = render_i_frame
        if version is not UNSET:
            field_dict["version"] = version
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_access_status import AppAccessStatus
        from ..models.app_version_creation_request import AppVersionCreationRequest

        d = dict(src_dict)
        _access_statuses = d.pop("accessStatuses", UNSET)
        access_statuses: list[AppAccessStatus] | Unset = UNSET
        if _access_statuses is not UNSET:
            access_statuses = []
            for access_statuses_item_data in _access_statuses:
                access_statuses_item = AppAccessStatus.from_dict(access_statuses_item_data)

                access_statuses.append(access_statuses_item)

        description = d.pop("description", UNSET)

        discoverable = d.pop("discoverable", UNSET)

        entry_point = d.pop("entryPoint", UNSET)

        mount_datasets = d.pop("mountDatasets", UNSET)

        mount_net_app_volumes = d.pop("mountNetAppVolumes", UNSET)

        name = d.pop("name", UNSET)

        render_i_frame = d.pop("renderIFrame", UNSET)

        _version = d.pop("version", UNSET)
        version: AppVersionCreationRequest | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = AppVersionCreationRequest.from_dict(_version)

        _visibility = d.pop("visibility", UNSET)
        visibility: AppUpdateRequestVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = AppUpdateRequestVisibility(_visibility)

        app_update_request = cls(
            access_statuses=access_statuses,
            description=description,
            discoverable=discoverable,
            entry_point=entry_point,
            mount_datasets=mount_datasets,
            mount_net_app_volumes=mount_net_app_volumes,
            name=name,
            render_i_frame=render_i_frame,
            version=version,
            visibility=visibility,
        )

        app_update_request.additional_properties = d
        return app_update_request

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
