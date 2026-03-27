from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_files_interface_project_release_dto import DominoFilesInterfaceProjectReleaseDto


T = TypeVar("T", bound="DominoFilesInterfaceProjectImportsDto")


@_attrs_define
class DominoFilesInterfaceProjectImportsDto:
    """
    Attributes:
        id (str):
        project_name (str):
        owner_username (str):
        variables_available (bool):
        is_active (bool):
        is_archived (bool):
        files_available (bool):
        package_available (bool):
        projects (list[str]):
        available_releases (list[DominoFilesInterfaceProjectReleaseDto]):
        mount_path (str):
    """

    id: str
    project_name: str
    owner_username: str
    variables_available: bool
    is_active: bool
    is_archived: bool
    files_available: bool
    package_available: bool
    projects: list[str]
    available_releases: list[DominoFilesInterfaceProjectReleaseDto]
    mount_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_name = self.project_name

        owner_username = self.owner_username

        variables_available = self.variables_available

        is_active = self.is_active

        is_archived = self.is_archived

        files_available = self.files_available

        package_available = self.package_available

        projects = self.projects

        available_releases = []
        for available_releases_item_data in self.available_releases:
            available_releases_item = available_releases_item_data.to_dict()
            available_releases.append(available_releases_item)

        mount_path = self.mount_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "projectName": project_name,
                "ownerUsername": owner_username,
                "variablesAvailable": variables_available,
                "isActive": is_active,
                "isArchived": is_archived,
                "filesAvailable": files_available,
                "packageAvailable": package_available,
                "projects": projects,
                "availableReleases": available_releases,
                "mountPath": mount_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_project_release_dto import DominoFilesInterfaceProjectReleaseDto

        d = dict(src_dict)
        id = d.pop("id")

        project_name = d.pop("projectName")

        owner_username = d.pop("ownerUsername")

        variables_available = d.pop("variablesAvailable")

        is_active = d.pop("isActive")

        is_archived = d.pop("isArchived")

        files_available = d.pop("filesAvailable")

        package_available = d.pop("packageAvailable")

        projects = cast(list[str], d.pop("projects"))

        available_releases = []
        _available_releases = d.pop("availableReleases")
        for available_releases_item_data in _available_releases:
            available_releases_item = DominoFilesInterfaceProjectReleaseDto.from_dict(available_releases_item_data)

            available_releases.append(available_releases_item)

        mount_path = d.pop("mountPath")

        domino_files_interface_project_imports_dto = cls(
            id=id,
            project_name=project_name,
            owner_username=owner_username,
            variables_available=variables_available,
            is_active=is_active,
            is_archived=is_archived,
            files_available=files_available,
            package_available=package_available,
            projects=projects,
            available_releases=available_releases,
            mount_path=mount_path,
        )

        domino_files_interface_project_imports_dto.additional_properties = d
        return domino_files_interface_project_imports_dto

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
