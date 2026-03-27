from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatamountApiDataMountProjectInfoDto")


@_attrs_define
class DominoDatamountApiDataMountProjectInfoDto:
    """
    Attributes:
        project_id (str):
        project_name (str):
        project_owner_username (str):
        is_project_archived (bool):
    """

    project_id: str
    project_name: str
    project_owner_username: str
    is_project_archived: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_name = self.project_name

        project_owner_username = self.project_owner_username

        is_project_archived = self.is_project_archived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "projectName": project_name,
                "projectOwnerUsername": project_owner_username,
                "isProjectArchived": is_project_archived,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        project_owner_username = d.pop("projectOwnerUsername")

        is_project_archived = d.pop("isProjectArchived")

        domino_datamount_api_data_mount_project_info_dto = cls(
            project_id=project_id,
            project_name=project_name,
            project_owner_username=project_owner_username,
            is_project_archived=is_project_archived,
        )

        domino_datamount_api_data_mount_project_info_dto.additional_properties = d
        return domino_datamount_api_data_mount_project_info_dto

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
