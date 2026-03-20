from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_configuration_type import AppConfigurationType
from ..models.app_creation_request_visibility import AppCreationRequestVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_access_status import AppAccessStatus
    from ..models.app_version_creation_request import AppVersionCreationRequest


T = TypeVar("T", bound="AppCreationRequest")


@_attrs_define
class AppCreationRequest:
    """
    Attributes:
        name (str):
        project_id (str):
        version (AppVersionCreationRequest):
        visibility (AppCreationRequestVisibility):
        access_statuses (list[AppAccessStatus] | Unset):
        configuration_type (AppConfigurationType | Unset): Type of configuration for the app which determines different
            deployment resources and settings.
        description (str | Unset):
        discoverable (bool | Unset):
        entry_point (str | Unset):
        mount_datasets (bool | Unset):
        mount_net_app_volumes (bool | Unset):
        render_i_frame (bool | Unset):
    """

    name: str
    project_id: str
    version: AppVersionCreationRequest
    visibility: AppCreationRequestVisibility
    access_statuses: list[AppAccessStatus] | Unset = UNSET
    configuration_type: AppConfigurationType | Unset = UNSET
    description: str | Unset = UNSET
    discoverable: bool | Unset = UNSET
    entry_point: str | Unset = UNSET
    mount_datasets: bool | Unset = UNSET
    mount_net_app_volumes: bool | Unset = UNSET
    render_i_frame: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        project_id = self.project_id

        version = self.version.to_dict()

        visibility = self.visibility.value

        access_statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.access_statuses, Unset):
            access_statuses = []
            for access_statuses_item_data in self.access_statuses:
                access_statuses_item = access_statuses_item_data.to_dict()
                access_statuses.append(access_statuses_item)

        configuration_type: str | Unset = UNSET
        if not isinstance(self.configuration_type, Unset):
            configuration_type = self.configuration_type.value

        description = self.description

        discoverable = self.discoverable

        entry_point = self.entry_point

        mount_datasets = self.mount_datasets

        mount_net_app_volumes = self.mount_net_app_volumes

        render_i_frame = self.render_i_frame

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "projectId": project_id,
                "version": version,
                "visibility": visibility,
            }
        )
        if access_statuses is not UNSET:
            field_dict["accessStatuses"] = access_statuses
        if configuration_type is not UNSET:
            field_dict["configurationType"] = configuration_type
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
        if render_i_frame is not UNSET:
            field_dict["renderIFrame"] = render_i_frame

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_access_status import AppAccessStatus
        from ..models.app_version_creation_request import AppVersionCreationRequest

        d = dict(src_dict)
        name = d.pop("name")

        project_id = d.pop("projectId")

        version = AppVersionCreationRequest.from_dict(d.pop("version"))

        visibility = AppCreationRequestVisibility(d.pop("visibility"))

        _access_statuses = d.pop("accessStatuses", UNSET)
        access_statuses: list[AppAccessStatus] | Unset = UNSET
        if _access_statuses is not UNSET:
            access_statuses = []
            for access_statuses_item_data in _access_statuses:
                access_statuses_item = AppAccessStatus.from_dict(access_statuses_item_data)

                access_statuses.append(access_statuses_item)

        _configuration_type = d.pop("configurationType", UNSET)
        configuration_type: AppConfigurationType | Unset
        if isinstance(_configuration_type, Unset):
            configuration_type = UNSET
        else:
            configuration_type = AppConfigurationType(_configuration_type)

        description = d.pop("description", UNSET)

        discoverable = d.pop("discoverable", UNSET)

        entry_point = d.pop("entryPoint", UNSET)

        mount_datasets = d.pop("mountDatasets", UNSET)

        mount_net_app_volumes = d.pop("mountNetAppVolumes", UNSET)

        render_i_frame = d.pop("renderIFrame", UNSET)

        app_creation_request = cls(
            name=name,
            project_id=project_id,
            version=version,
            visibility=visibility,
            access_statuses=access_statuses,
            configuration_type=configuration_type,
            description=description,
            discoverable=discoverable,
            entry_point=entry_point,
            mount_datasets=mount_datasets,
            mount_net_app_volumes=mount_net_app_volumes,
            render_i_frame=render_i_frame,
        )

        app_creation_request.additional_properties = d
        return app_creation_request

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
