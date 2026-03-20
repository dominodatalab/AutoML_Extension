from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonalAccessTokenDetails")


@_attrs_define
class PersonalAccessTokenDetails:
    """
    Attributes:
        created_at (datetime.datetime):  Example: 2025-08-21T23:51:54.075Z.
        expires_at (datetime.datetime):  Example: 2025-08-21T23:51:54.075Z.
        is_valid (bool):
        name (str):
        pat_id (str):
        user_id (str):
        description (str | Unset):
    """

    created_at: datetime.datetime
    expires_at: datetime.datetime
    is_valid: bool
    name: str
    pat_id: str
    user_id: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        is_valid = self.is_valid

        name = self.name

        pat_id = self.pat_id

        user_id = self.user_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "expiresAt": expires_at,
                "isValid": is_valid,
                "name": name,
                "patId": pat_id,
                "userId": user_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        expires_at = isoparse(d.pop("expiresAt"))

        is_valid = d.pop("isValid")

        name = d.pop("name")

        pat_id = d.pop("patId")

        user_id = d.pop("userId")

        description = d.pop("description", UNSET)

        personal_access_token_details = cls(
            created_at=created_at,
            expires_at=expires_at,
            is_valid=is_valid,
            name=name,
            pat_id=pat_id,
            user_id=user_id,
            description=description,
        )

        personal_access_token_details.additional_properties = d
        return personal_access_token_details

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
