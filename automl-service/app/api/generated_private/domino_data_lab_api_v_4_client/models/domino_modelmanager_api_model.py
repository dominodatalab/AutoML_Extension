from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_modelmanager_api_model_active_version_status import DominoModelmanagerApiModelActiveVersionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_modelmanager_api_model_owner import DominoModelmanagerApiModelOwner
    from ..models.domino_modelmanager_api_model_version_summary import DominoModelmanagerApiModelVersionSummary


T = TypeVar("T", bound="DominoModelmanagerApiModel")


@_attrs_define
class DominoModelmanagerApiModel:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        last_modified (int):
        owners (list[DominoModelmanagerApiModelOwner]):
        is_async (bool):
        active_version (DominoModelmanagerApiModelVersionSummary | Unset):
        active_version_number (int | None | Unset):
        active_model_version_id (None | str | Unset):
        active_version_data_plane_id (None | str | Unset):
        active_version_status (DominoModelmanagerApiModelActiveVersionStatus | Unset):
        project_id (None | str | Unset):
        project_name (None | str | Unset):
        project_owner_username (None | str | Unset):
        bundle_id (None | str | Unset):
    """

    id: str
    name: str
    description: str
    last_modified: int
    owners: list[DominoModelmanagerApiModelOwner]
    is_async: bool
    active_version: DominoModelmanagerApiModelVersionSummary | Unset = UNSET
    active_version_number: int | None | Unset = UNSET
    active_model_version_id: None | str | Unset = UNSET
    active_version_data_plane_id: None | str | Unset = UNSET
    active_version_status: DominoModelmanagerApiModelActiveVersionStatus | Unset = UNSET
    project_id: None | str | Unset = UNSET
    project_name: None | str | Unset = UNSET
    project_owner_username: None | str | Unset = UNSET
    bundle_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        last_modified = self.last_modified

        owners = []
        for owners_item_data in self.owners:
            owners_item = owners_item_data.to_dict()
            owners.append(owners_item)

        is_async = self.is_async

        active_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_version, Unset):
            active_version = self.active_version.to_dict()

        active_version_number: int | None | Unset
        if isinstance(self.active_version_number, Unset):
            active_version_number = UNSET
        else:
            active_version_number = self.active_version_number

        active_model_version_id: None | str | Unset
        if isinstance(self.active_model_version_id, Unset):
            active_model_version_id = UNSET
        else:
            active_model_version_id = self.active_model_version_id

        active_version_data_plane_id: None | str | Unset
        if isinstance(self.active_version_data_plane_id, Unset):
            active_version_data_plane_id = UNSET
        else:
            active_version_data_plane_id = self.active_version_data_plane_id

        active_version_status: str | Unset = UNSET
        if not isinstance(self.active_version_status, Unset):
            active_version_status = self.active_version_status.value

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        project_name: None | str | Unset
        if isinstance(self.project_name, Unset):
            project_name = UNSET
        else:
            project_name = self.project_name

        project_owner_username: None | str | Unset
        if isinstance(self.project_owner_username, Unset):
            project_owner_username = UNSET
        else:
            project_owner_username = self.project_owner_username

        bundle_id: None | str | Unset
        if isinstance(self.bundle_id, Unset):
            bundle_id = UNSET
        else:
            bundle_id = self.bundle_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "lastModified": last_modified,
                "owners": owners,
                "isAsync": is_async,
            }
        )
        if active_version is not UNSET:
            field_dict["activeVersion"] = active_version
        if active_version_number is not UNSET:
            field_dict["activeVersionNumber"] = active_version_number
        if active_model_version_id is not UNSET:
            field_dict["activeModelVersionId"] = active_model_version_id
        if active_version_data_plane_id is not UNSET:
            field_dict["activeVersionDataPlaneId"] = active_version_data_plane_id
        if active_version_status is not UNSET:
            field_dict["activeVersionStatus"] = active_version_status
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if project_owner_username is not UNSET:
            field_dict["projectOwnerUsername"] = project_owner_username
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_modelmanager_api_model_owner import DominoModelmanagerApiModelOwner
        from ..models.domino_modelmanager_api_model_version_summary import DominoModelmanagerApiModelVersionSummary

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        last_modified = d.pop("lastModified")

        owners = []
        _owners = d.pop("owners")
        for owners_item_data in _owners:
            owners_item = DominoModelmanagerApiModelOwner.from_dict(owners_item_data)

            owners.append(owners_item)

        is_async = d.pop("isAsync")

        _active_version = d.pop("activeVersion", UNSET)
        active_version: DominoModelmanagerApiModelVersionSummary | Unset
        if isinstance(_active_version, Unset):
            active_version = UNSET
        else:
            active_version = DominoModelmanagerApiModelVersionSummary.from_dict(_active_version)

        def _parse_active_version_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        active_version_number = _parse_active_version_number(d.pop("activeVersionNumber", UNSET))

        def _parse_active_model_version_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        active_model_version_id = _parse_active_model_version_id(d.pop("activeModelVersionId", UNSET))

        def _parse_active_version_data_plane_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        active_version_data_plane_id = _parse_active_version_data_plane_id(d.pop("activeVersionDataPlaneId", UNSET))

        _active_version_status = d.pop("activeVersionStatus", UNSET)
        active_version_status: DominoModelmanagerApiModelActiveVersionStatus | Unset
        if isinstance(_active_version_status, Unset):
            active_version_status = UNSET
        else:
            active_version_status = DominoModelmanagerApiModelActiveVersionStatus(_active_version_status)

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        def _parse_project_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_name = _parse_project_name(d.pop("projectName", UNSET))

        def _parse_project_owner_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_owner_username = _parse_project_owner_username(d.pop("projectOwnerUsername", UNSET))

        def _parse_bundle_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bundle_id = _parse_bundle_id(d.pop("bundleId", UNSET))

        domino_modelmanager_api_model = cls(
            id=id,
            name=name,
            description=description,
            last_modified=last_modified,
            owners=owners,
            is_async=is_async,
            active_version=active_version,
            active_version_number=active_version_number,
            active_model_version_id=active_model_version_id,
            active_version_data_plane_id=active_version_data_plane_id,
            active_version_status=active_version_status,
            project_id=project_id,
            project_name=project_name,
            project_owner_username=project_owner_username,
            bundle_id=bundle_id,
        )

        domino_modelmanager_api_model.additional_properties = d
        return domino_modelmanager_api_model

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
