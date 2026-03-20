from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserSummary")


@_attrs_define
class UserSummary:
    """Information about a Domino user including id and names.

    Attributes:
        first_name (str): The first name of the user.
        id (str): The id of the user.
        last_name (str): The last name of the user.
        user_name (str): The username of the user.
    """

    first_name: str
    id: str
    last_name: str
    user_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        id = self.id

        last_name = self.last_name

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstName": first_name,
                "id": id,
                "lastName": last_name,
                "userName": user_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("firstName")

        id = d.pop("id")

        last_name = d.pop("lastName")

        user_name = d.pop("userName")

        user_summary = cls(
            first_name=first_name,
            id=id,
            last_name=last_name,
            user_name=user_name,
        )

        user_summary.additional_properties = d
        return user_summary

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
