from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoCommonGatewaySearchSearchProjectDetails")


@_attrs_define
class DominoCommonGatewaySearchSearchProjectDetails:
    """
    Attributes:
        id (str):
        project_name (str):
        project_link (str):
    """

    id: str
    project_name: str
    project_link: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_name = self.project_name

        project_link = self.project_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "projectName": project_name,
                "projectLink": project_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        project_name = d.pop("projectName")

        project_link = d.pop("projectLink")

        domino_common_gateway_search_search_project_details = cls(
            id=id,
            project_name=project_name,
            project_link=project_link,
        )

        domino_common_gateway_search_search_project_details.additional_properties = d
        return domino_common_gateway_search_search_project_details

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
