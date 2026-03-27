from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_credential_api_full_credential_dto_auth_type import DominoCredentialApiFullCredentialDtoAuthType
from ..models.domino_credential_api_full_credential_dto_credential_type import (
    DominoCredentialApiFullCredentialDtoCredentialType,
)

if TYPE_CHECKING:
    from ..models.domino_credential_api_full_credential_dto_secret_credentials import (
        DominoCredentialApiFullCredentialDtoSecretCredentials,
    )
    from ..models.domino_credential_api_full_credential_dto_visible_credentials import (
        DominoCredentialApiFullCredentialDtoVisibleCredentials,
    )


T = TypeVar("T", bound="DominoCredentialApiFullCredentialDto")


@_attrs_define
class DominoCredentialApiFullCredentialDto:
    """
    Attributes:
        secret_credentials (DominoCredentialApiFullCredentialDtoSecretCredentials):
        credential_type (DominoCredentialApiFullCredentialDtoCredentialType):
        auth_type (DominoCredentialApiFullCredentialDtoAuthType):
        visible_credentials (DominoCredentialApiFullCredentialDtoVisibleCredentials):
    """

    secret_credentials: DominoCredentialApiFullCredentialDtoSecretCredentials
    credential_type: DominoCredentialApiFullCredentialDtoCredentialType
    auth_type: DominoCredentialApiFullCredentialDtoAuthType
    visible_credentials: DominoCredentialApiFullCredentialDtoVisibleCredentials
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_credentials = self.secret_credentials.to_dict()

        credential_type = self.credential_type.value

        auth_type = self.auth_type.value

        visible_credentials = self.visible_credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secretCredentials": secret_credentials,
                "credentialType": credential_type,
                "authType": auth_type,
                "visibleCredentials": visible_credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_credential_api_full_credential_dto_secret_credentials import (
            DominoCredentialApiFullCredentialDtoSecretCredentials,
        )
        from ..models.domino_credential_api_full_credential_dto_visible_credentials import (
            DominoCredentialApiFullCredentialDtoVisibleCredentials,
        )

        d = dict(src_dict)
        secret_credentials = DominoCredentialApiFullCredentialDtoSecretCredentials.from_dict(d.pop("secretCredentials"))

        credential_type = DominoCredentialApiFullCredentialDtoCredentialType(d.pop("credentialType"))

        auth_type = DominoCredentialApiFullCredentialDtoAuthType(d.pop("authType"))

        visible_credentials = DominoCredentialApiFullCredentialDtoVisibleCredentials.from_dict(
            d.pop("visibleCredentials")
        )

        domino_credential_api_full_credential_dto = cls(
            secret_credentials=secret_credentials,
            credential_type=credential_type,
            auth_type=auth_type,
            visible_credentials=visible_credentials,
        )

        domino_credential_api_full_credential_dto.additional_properties = d
        return domino_credential_api_full_credential_dto

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
