from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_credential_api_full_credential_dto import DominoCredentialApiFullCredentialDto


T = TypeVar("T", bound="DominoCredentialApiFullDataSourceCredentialDto")


@_attrs_define
class DominoCredentialApiFullDataSourceCredentialDto:
    """
    Attributes:
        owner (str):
        data_source_id (str):
        is_everyone (bool):
        credential (DominoCredentialApiFullCredentialDto):
        id (str):
        users (list[str]):
    """

    owner: str
    data_source_id: str
    is_everyone: bool
    credential: DominoCredentialApiFullCredentialDto
    id: str
    users: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner = self.owner

        data_source_id = self.data_source_id

        is_everyone = self.is_everyone

        credential = self.credential.to_dict()

        id = self.id

        users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner": owner,
                "dataSourceId": data_source_id,
                "isEveryone": is_everyone,
                "credential": credential,
                "id": id,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_credential_api_full_credential_dto import DominoCredentialApiFullCredentialDto

        d = dict(src_dict)
        owner = d.pop("owner")

        data_source_id = d.pop("dataSourceId")

        is_everyone = d.pop("isEveryone")

        credential = DominoCredentialApiFullCredentialDto.from_dict(d.pop("credential"))

        id = d.pop("id")

        users = cast(list[str], d.pop("users"))

        domino_credential_api_full_data_source_credential_dto = cls(
            owner=owner,
            data_source_id=data_source_id,
            is_everyone=is_everyone,
            credential=credential,
            id=id,
            users=users,
        )

        domino_credential_api_full_data_source_credential_dto.additional_properties = d
        return domino_credential_api_full_data_source_credential_dto

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
