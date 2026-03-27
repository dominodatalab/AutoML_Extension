from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentChildrenDetails")


@_attrs_define
class DominoEnvironmentsApiEnvironmentChildrenDetails:
    """
    Attributes:
        total (int):
        following_active (int):
    """

    total: int
    following_active: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        following_active = self.following_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "followingActive": following_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        following_active = d.pop("followingActive")

        domino_environments_api_environment_children_details = cls(
            total=total,
            following_active=following_active,
        )

        domino_environments_api_environment_children_details.additional_properties = d
        return domino_environments_api_environment_children_details

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
