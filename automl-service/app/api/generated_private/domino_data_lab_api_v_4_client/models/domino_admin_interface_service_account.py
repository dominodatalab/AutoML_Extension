from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoAdminInterfaceServiceAccount")


@_attrs_define
class DominoAdminInterfaceServiceAccount:
    """
    Attributes:
        username (str):
        id (str):
        email (None | str | Unset):
        idp_id (None | str | Unset):
    """

    username: str
    id: str
    email: None | str | Unset = UNSET
    idp_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        id = self.id

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        idp_id: None | str | Unset
        if isinstance(self.idp_id, Unset):
            idp_id = UNSET
        else:
            idp_id = self.idp_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "id": id,
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
        username = d.pop("username")

        id = d.pop("id")

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_idp_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        idp_id = _parse_idp_id(d.pop("idpId", UNSET))

        domino_admin_interface_service_account = cls(
            username=username,
            id=id,
            email=email,
            idp_id=idp_id,
        )

        domino_admin_interface_service_account.additional_properties = d
        return domino_admin_interface_service_account

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
