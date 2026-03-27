from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_credential_api_visible_credential_dto import DominoCredentialApiVisibleCredentialDto


T = TypeVar("T", bound="DominoCredentialApiVisibleDataSourceCredentialDto")


@_attrs_define
class DominoCredentialApiVisibleDataSourceCredentialDto:
    """
    Attributes:
        id (str):
        data_source_id (str):
        credential (DominoCredentialApiVisibleCredentialDto):
        owner (str):
        users (list[str]):
        is_everyone (bool):
    """

    id: str
    data_source_id: str
    credential: DominoCredentialApiVisibleCredentialDto
    owner: str
    users: list[str]
    is_everyone: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        data_source_id = self.data_source_id

        credential = self.credential.to_dict()

        owner = self.owner

        users = self.users

        is_everyone = self.is_everyone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "dataSourceId": data_source_id,
                "credential": credential,
                "owner": owner,
                "users": users,
                "isEveryone": is_everyone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_credential_api_visible_credential_dto import DominoCredentialApiVisibleCredentialDto

        d = dict(src_dict)
        id = d.pop("id")

        data_source_id = d.pop("dataSourceId")

        credential = DominoCredentialApiVisibleCredentialDto.from_dict(d.pop("credential"))

        owner = d.pop("owner")

        users = cast(list[str], d.pop("users"))

        is_everyone = d.pop("isEveryone")

        domino_credential_api_visible_data_source_credential_dto = cls(
            id=id,
            data_source_id=data_source_id,
            credential=credential,
            owner=owner,
            users=users,
            is_everyone=is_everyone,
        )

        domino_credential_api_visible_data_source_credential_dto.additional_properties = d
        return domino_credential_api_visible_data_source_credential_dto

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
