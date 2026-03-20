from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_configuration_type import AppConfigurationType
from ..models.app_response_visibility import AppResponseVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_access_status import AppAccessStatus
    from ..models.app_project_response import AppProjectResponse
    from ..models.app_user_response import AppUserResponse
    from ..models.app_version_response import AppVersionResponse


T = TypeVar("T", bound="AppResponse")


@_attrs_define
class AppResponse:
    """
    Attributes:
        access_statuses (list[AppAccessStatus]):
        configuration_type (AppConfigurationType): Type of configuration for the app which determines different
            deployment resources and settings.
        discoverable (bool):
        entry_point (str):
        id (str):
        mount_datasets (bool):
        mount_net_app_volumes (bool):
        name (str):
        project (AppProjectResponse):
        render_i_frame (bool):
        url (str):
        views (float):
        visibility (AppResponseVisibility):
        current_version (AppVersionResponse | Unset):
        description (str | Unset):
        publisher (AppUserResponse | Unset):
        thumbnail_etag (str | Unset):
        updated_at (float | Unset):
        vanity_url (str | Unset):
    """

    access_statuses: list[AppAccessStatus]
    configuration_type: AppConfigurationType
    discoverable: bool
    entry_point: str
    id: str
    mount_datasets: bool
    mount_net_app_volumes: bool
    name: str
    project: AppProjectResponse
    render_i_frame: bool
    url: str
    views: float
    visibility: AppResponseVisibility
    current_version: AppVersionResponse | Unset = UNSET
    description: str | Unset = UNSET
    publisher: AppUserResponse | Unset = UNSET
    thumbnail_etag: str | Unset = UNSET
    updated_at: float | Unset = UNSET
    vanity_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_statuses = []
        for access_statuses_item_data in self.access_statuses:
            access_statuses_item = access_statuses_item_data.to_dict()
            access_statuses.append(access_statuses_item)

        configuration_type = self.configuration_type.value

        discoverable = self.discoverable

        entry_point = self.entry_point

        id = self.id

        mount_datasets = self.mount_datasets

        mount_net_app_volumes = self.mount_net_app_volumes

        name = self.name

        project = self.project.to_dict()

        render_i_frame = self.render_i_frame

        url = self.url

        views = self.views

        visibility = self.visibility.value

        current_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_version, Unset):
            current_version = self.current_version.to_dict()

        description = self.description

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        thumbnail_etag = self.thumbnail_etag

        updated_at = self.updated_at

        vanity_url = self.vanity_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessStatuses": access_statuses,
                "configurationType": configuration_type,
                "discoverable": discoverable,
                "entryPoint": entry_point,
                "id": id,
                "mountDatasets": mount_datasets,
                "mountNetAppVolumes": mount_net_app_volumes,
                "name": name,
                "project": project,
                "renderIFrame": render_i_frame,
                "url": url,
                "views": views,
                "visibility": visibility,
            }
        )
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version
        if description is not UNSET:
            field_dict["description"] = description
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if thumbnail_etag is not UNSET:
            field_dict["thumbnailEtag"] = thumbnail_etag
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if vanity_url is not UNSET:
            field_dict["vanityUrl"] = vanity_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_access_status import AppAccessStatus
        from ..models.app_project_response import AppProjectResponse
        from ..models.app_user_response import AppUserResponse
        from ..models.app_version_response import AppVersionResponse

        d = dict(src_dict)
        access_statuses = []
        _access_statuses = d.pop("accessStatuses")
        for access_statuses_item_data in _access_statuses:
            access_statuses_item = AppAccessStatus.from_dict(access_statuses_item_data)

            access_statuses.append(access_statuses_item)

        configuration_type = AppConfigurationType(d.pop("configurationType"))

        discoverable = d.pop("discoverable")

        entry_point = d.pop("entryPoint")

        id = d.pop("id")

        mount_datasets = d.pop("mountDatasets")

        mount_net_app_volumes = d.pop("mountNetAppVolumes")

        name = d.pop("name")

        project = AppProjectResponse.from_dict(d.pop("project"))

        render_i_frame = d.pop("renderIFrame")

        url = d.pop("url")

        views = d.pop("views")

        visibility = AppResponseVisibility(d.pop("visibility"))

        _current_version = d.pop("currentVersion", UNSET)
        current_version: AppVersionResponse | Unset
        if isinstance(_current_version, Unset):
            current_version = UNSET
        else:
            current_version = AppVersionResponse.from_dict(_current_version)

        description = d.pop("description", UNSET)

        _publisher = d.pop("publisher", UNSET)
        publisher: AppUserResponse | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = AppUserResponse.from_dict(_publisher)

        thumbnail_etag = d.pop("thumbnailEtag", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        vanity_url = d.pop("vanityUrl", UNSET)

        app_response = cls(
            access_statuses=access_statuses,
            configuration_type=configuration_type,
            discoverable=discoverable,
            entry_point=entry_point,
            id=id,
            mount_datasets=mount_datasets,
            mount_net_app_volumes=mount_net_app_volumes,
            name=name,
            project=project,
            render_i_frame=render_i_frame,
            url=url,
            views=views,
            visibility=visibility,
            current_version=current_version,
            description=description,
            publisher=publisher,
            thumbnail_etag=thumbnail_etag,
            updated_at=updated_at,
            vanity_url=vanity_url,
        )

        app_response.additional_properties = d
        return app_response

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
