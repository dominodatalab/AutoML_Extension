from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAccountToken")


@_attrs_define
class ServiceAccountToken:
    """
    Attributes:
        created_at (datetime.datetime):  Example: 2025-08-21T23:51:54.075Z.
        is_valid (bool):
        name (str):
        service_account_idp_id (str):
        token (str):
        expires_at (datetime.datetime | Unset):  Example: 2025-08-21T23:51:54.075Z.
    """

    created_at: datetime.datetime
    is_valid: bool
    name: str
    service_account_idp_id: str
    token: str
    expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        is_valid = self.is_valid

        name = self.name

        service_account_idp_id = self.service_account_idp_id

        token = self.token

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "isValid": is_valid,
                "name": name,
                "serviceAccountIdpId": service_account_idp_id,
                "token": token,
            }
        )
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        is_valid = d.pop("isValid")

        name = d.pop("name")

        service_account_idp_id = d.pop("serviceAccountIdpId")

        token = d.pop("token")

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        service_account_token = cls(
            created_at=created_at,
            is_valid=is_valid,
            name=name,
            service_account_idp_id=service_account_idp_id,
            token=token,
            expires_at=expires_at,
        )

        service_account_token.additional_properties = d
        return service_account_token

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
