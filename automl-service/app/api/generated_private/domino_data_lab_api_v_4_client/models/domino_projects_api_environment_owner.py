from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_environment_owner_environment_owner_type import (
    DominoProjectsApiEnvironmentOwnerEnvironmentOwnerType,
)

T = TypeVar("T", bound="DominoProjectsApiEnvironmentOwner")


@_attrs_define
class DominoProjectsApiEnvironmentOwner:
    """
    Attributes:
        id (str):
        username (str):
        environment_owner_type (DominoProjectsApiEnvironmentOwnerEnvironmentOwnerType):
    """

    id: str
    username: str
    environment_owner_type: DominoProjectsApiEnvironmentOwnerEnvironmentOwnerType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        environment_owner_type = self.environment_owner_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "environmentOwnerType": environment_owner_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        environment_owner_type = DominoProjectsApiEnvironmentOwnerEnvironmentOwnerType(d.pop("environmentOwnerType"))

        domino_projects_api_environment_owner = cls(
            id=id,
            username=username,
            environment_owner_type=environment_owner_type,
        )

        domino_projects_api_environment_owner.additional_properties = d
        return domino_projects_api_environment_owner

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
