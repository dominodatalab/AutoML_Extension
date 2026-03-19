from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAccount")


@_attrs_define
class ServiceAccount:
    """
    Attributes:
        id (str): the Domino id of the service account
        username (str): the username of the service account
        email (str | Unset): the email that should receive notifications on behalf of the service account
        idp_id (str | Unset): the identity provider id of the service account
    """

    id: str
    username: str
    email: str | Unset = UNSET
    idp_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        email = self.email

        idp_id = self.idp_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if idp_id is not UNSET:
            field_dict["idpId"] = idp_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        email = d.pop("email", UNSET)

        idp_id = d.pop("idpId", UNSET)

        service_account = cls(
            id=id,
            username=username,
            email=email,
            idp_id=idp_id,
        )

        service_account.additional_properties = d
        return service_account

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
