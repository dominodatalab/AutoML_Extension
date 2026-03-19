from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_project_response_project_type import AppProjectResponseProjectType

T = TypeVar("T", bound="AppProjectResponse")


@_attrs_define
class AppProjectResponse:
    """
    Attributes:
        id (str):
        name (str):
        owner_id (str):
        owner_username (str):
        project_type (AppProjectResponseProjectType):
    """

    id: str
    name: str
    owner_id: str
    owner_username: str
    project_type: AppProjectResponseProjectType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        owner_id = self.owner_id

        owner_username = self.owner_username

        project_type = self.project_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ownerId": owner_id,
                "ownerUsername": owner_username,
                "projectType": project_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        owner_id = d.pop("ownerId")

        owner_username = d.pop("ownerUsername")

        project_type = AppProjectResponseProjectType(d.pop("projectType"))

        app_project_response = cls(
            id=id,
            name=name,
            owner_id=owner_id,
            owner_username=owner_username,
            project_type=project_type,
        )

        app_project_response.additional_properties = d
        return app_project_response

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
