from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_credential_api_visible_credential_dto_credential_type import (
    DominoCredentialApiVisibleCredentialDtoCredentialType,
)

if TYPE_CHECKING:
    from ..models.domino_credential_api_visible_credential_dto_visible_credentials import (
        DominoCredentialApiVisibleCredentialDtoVisibleCredentials,
    )


T = TypeVar("T", bound="DominoCredentialApiVisibleCredentialDto")


@_attrs_define
class DominoCredentialApiVisibleCredentialDto:
    """
    Attributes:
        visible_credentials (DominoCredentialApiVisibleCredentialDtoVisibleCredentials):
        credential_type (DominoCredentialApiVisibleCredentialDtoCredentialType):
    """

    visible_credentials: DominoCredentialApiVisibleCredentialDtoVisibleCredentials
    credential_type: DominoCredentialApiVisibleCredentialDtoCredentialType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        visible_credentials = self.visible_credentials.to_dict()

        credential_type = self.credential_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "visibleCredentials": visible_credentials,
                "credentialType": credential_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_credential_api_visible_credential_dto_visible_credentials import (
            DominoCredentialApiVisibleCredentialDtoVisibleCredentials,
        )

        d = dict(src_dict)
        visible_credentials = DominoCredentialApiVisibleCredentialDtoVisibleCredentials.from_dict(
            d.pop("visibleCredentials")
        )

        credential_type = DominoCredentialApiVisibleCredentialDtoCredentialType(d.pop("credentialType"))

        domino_credential_api_visible_credential_dto = cls(
            visible_credentials=visible_credentials,
            credential_type=credential_type,
        )

        domino_credential_api_visible_credential_dto.additional_properties = d
        return domino_credential_api_visible_credential_dto

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
