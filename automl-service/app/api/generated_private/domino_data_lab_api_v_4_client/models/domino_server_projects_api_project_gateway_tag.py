from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoServerProjectsApiProjectGatewayTag")


@_attrs_define
class DominoServerProjectsApiProjectGatewayTag:
    """
    Attributes:
        id (str):
        name (str):
        is_approved (bool):
    """

    id: str
    name: str
    is_approved: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_approved = self.is_approved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "isApproved": is_approved,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_approved = d.pop("isApproved")

        domino_server_projects_api_project_gateway_tag = cls(
            id=id,
            name=name,
            is_approved=is_approved,
        )

        domino_server_projects_api_project_gateway_tag.additional_properties = d
        return domino_server_projects_api_project_gateway_tag

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
