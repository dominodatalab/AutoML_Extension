from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_admin_usermanagement_api_admin_user_management_user_metadata import (
        DominoAdminUsermanagementApiAdminUserManagementUserMetadata,
    )


T = TypeVar("T", bound="DominoAdminUsermanagementApiAdminUserManagementUser")


@_attrs_define
class DominoAdminUsermanagementApiAdminUserManagementUser:
    """
    Attributes:
        idp_id (str):
        first_name (str):
        last_name (str):
        full_name (str):
        username (str):
        roles (list[str]):
        is_active (bool):
        is_domino_employee (bool):
        is_sso (bool):
        license_name (str):
        created_at_timestamp_ms (int):
        metadata (DominoAdminUsermanagementApiAdminUserManagementUserMetadata):
        id (None | str | Unset):
        email (None | str | Unset):
    """

    idp_id: str
    first_name: str
    last_name: str
    full_name: str
    username: str
    roles: list[str]
    is_active: bool
    is_domino_employee: bool
    is_sso: bool
    license_name: str
    created_at_timestamp_ms: int
    metadata: DominoAdminUsermanagementApiAdminUserManagementUserMetadata
    id: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idp_id = self.idp_id

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        username = self.username

        roles = self.roles

        is_active = self.is_active

        is_domino_employee = self.is_domino_employee

        is_sso = self.is_sso

        license_name = self.license_name

        created_at_timestamp_ms = self.created_at_timestamp_ms

        metadata = self.metadata.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idpId": idp_id,
                "firstName": first_name,
                "lastName": last_name,
                "fullName": full_name,
                "username": username,
                "roles": roles,
                "isActive": is_active,
                "isDominoEmployee": is_domino_employee,
                "isSSO": is_sso,
                "licenseName": license_name,
                "createdAtTimestampMs": created_at_timestamp_ms,
                "metadata": metadata,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_usermanagement_api_admin_user_management_user_metadata import (
            DominoAdminUsermanagementApiAdminUserManagementUserMetadata,
        )

        d = dict(src_dict)
        idp_id = d.pop("idpId")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        full_name = d.pop("fullName")

        username = d.pop("username")

        roles = cast(list[str], d.pop("roles"))

        is_active = d.pop("isActive")

        is_domino_employee = d.pop("isDominoEmployee")

        is_sso = d.pop("isSSO")

        license_name = d.pop("licenseName")

        created_at_timestamp_ms = d.pop("createdAtTimestampMs")

        metadata = DominoAdminUsermanagementApiAdminUserManagementUserMetadata.from_dict(d.pop("metadata"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        domino_admin_usermanagement_api_admin_user_management_user = cls(
            idp_id=idp_id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            username=username,
            roles=roles,
            is_active=is_active,
            is_domino_employee=is_domino_employee,
            is_sso=is_sso,
            license_name=license_name,
            created_at_timestamp_ms=created_at_timestamp_ms,
            metadata=metadata,
            id=id,
            email=email,
        )

        domino_admin_usermanagement_api_admin_user_management_user.additional_properties = d
        return domino_admin_usermanagement_api_admin_user_management_user

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
