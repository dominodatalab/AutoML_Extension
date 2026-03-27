from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsWebTransferProjectOwnership")


@_attrs_define
class DominoProjectsWebTransferProjectOwnership:
    """
    Attributes:
        project_id (str):
        new_owner_username_or_email (str):
    """

    project_id: str
    new_owner_username_or_email: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        new_owner_username_or_email = self.new_owner_username_or_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "newOwnerUsernameOrEmail": new_owner_username_or_email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        new_owner_username_or_email = d.pop("newOwnerUsernameOrEmail")

        domino_projects_web_transfer_project_ownership = cls(
            project_id=project_id,
            new_owner_username_or_email=new_owner_username_or_email,
        )

        domino_projects_web_transfer_project_ownership.additional_properties = d
        return domino_projects_web_transfer_project_ownership

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
