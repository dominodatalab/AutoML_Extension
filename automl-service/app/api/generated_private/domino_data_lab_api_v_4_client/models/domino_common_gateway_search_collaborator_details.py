from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoCommonGatewaySearchCollaboratorDetails")


@_attrs_define
class DominoCommonGatewaySearchCollaboratorDetails:
    """
    Attributes:
        username (str):
        highlighted_username (str):
    """

    username: str
    highlighted_username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        highlighted_username = self.highlighted_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "highlightedUsername": highlighted_username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        highlighted_username = d.pop("highlightedUsername")

        domino_common_gateway_search_collaborator_details = cls(
            username=username,
            highlighted_username=highlighted_username,
        )

        domino_common_gateway_search_collaborator_details.additional_properties = d
        return domino_common_gateway_search_collaborator_details

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
