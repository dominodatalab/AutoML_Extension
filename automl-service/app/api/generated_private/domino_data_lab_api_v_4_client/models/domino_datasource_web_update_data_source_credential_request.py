from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasource_web_update_data_source_credential_request_auth_type import (
    DominoDatasourceWebUpdateDataSourceCredentialRequestAuthType,
)
from ..models.domino_datasource_web_update_data_source_credential_request_credential_type import (
    DominoDatasourceWebUpdateDataSourceCredentialRequestCredentialType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasource_web_update_data_source_credential_request_secret_credentials_type_0 import (
        DominoDatasourceWebUpdateDataSourceCredentialRequestSecretCredentialsType0,
    )


T = TypeVar("T", bound="DominoDatasourceWebUpdateDataSourceCredentialRequest")


@_attrs_define
class DominoDatasourceWebUpdateDataSourceCredentialRequest:
    """
    Attributes:
        auth_type (DominoDatasourceWebUpdateDataSourceCredentialRequestAuthType):
        credential_type (DominoDatasourceWebUpdateDataSourceCredentialRequestCredentialType):
        visible_credential (None | str | Unset):
        secret_credential (None | str | Unset):
        secret_credentials (DominoDatasourceWebUpdateDataSourceCredentialRequestSecretCredentialsType0 | None | Unset):
    """

    auth_type: DominoDatasourceWebUpdateDataSourceCredentialRequestAuthType
    credential_type: DominoDatasourceWebUpdateDataSourceCredentialRequestCredentialType
    visible_credential: None | str | Unset = UNSET
    secret_credential: None | str | Unset = UNSET
    secret_credentials: DominoDatasourceWebUpdateDataSourceCredentialRequestSecretCredentialsType0 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_datasource_web_update_data_source_credential_request_secret_credentials_type_0 import (
            DominoDatasourceWebUpdateDataSourceCredentialRequestSecretCredentialsType0,
        )

        auth_type = self.auth_type.value

        credential_type = self.credential_type.value

        visible_credential: None | str | Unset
        if isinstance(self.visible_credential, Unset):
            visible_credential = UNSET
        else:
            visible_credential = self.visible_credential

        secret_credential: None | str | Unset
        if isinstance(self.secret_credential, Unset):
            secret_credential = UNSET
        else:
            secret_credential = self.secret_credential

        secret_credentials: dict[str, Any] | None | Unset
        if isinstance(self.secret_credentials, Unset):
            secret_credentials = UNSET
        elif isinstance(
            self.secret_credentials, DominoDatasourceWebUpdateDataSourceCredentialRequestSecretCredentialsType0
        ):
            secret_credentials = self.secret_credentials.to_dict()
        else:
            secret_credentials = self.secret_credentials

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authType": auth_type,
                "credentialType": credential_type,
            }
        )
        if visible_credential is not UNSET:
            field_dict["visibleCredential"] = visible_credential
        if secret_credential is not UNSET:
            field_dict["secretCredential"] = secret_credential
        if secret_credentials is not UNSET:
            field_dict["secretCredentials"] = secret_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_web_update_data_source_credential_request_secret_credentials_type_0 import (
            DominoDatasourceWebUpdateDataSourceCredentialRequestSecretCredentialsType0,
        )

        d = dict(src_dict)
        auth_type = DominoDatasourceWebUpdateDataSourceCredentialRequestAuthType(d.pop("authType"))

        credential_type = DominoDatasourceWebUpdateDataSourceCredentialRequestCredentialType(d.pop("credentialType"))

        def _parse_visible_credential(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visible_credential = _parse_visible_credential(d.pop("visibleCredential", UNSET))

        def _parse_secret_credential(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_credential = _parse_secret_credential(d.pop("secretCredential", UNSET))

        def _parse_secret_credentials(
            data: object,
        ) -> DominoDatasourceWebUpdateDataSourceCredentialRequestSecretCredentialsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secret_credentials_type_0 = (
                    DominoDatasourceWebUpdateDataSourceCredentialRequestSecretCredentialsType0.from_dict(data)
                )

                return secret_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoDatasourceWebUpdateDataSourceCredentialRequestSecretCredentialsType0 | None | Unset, data)

        secret_credentials = _parse_secret_credentials(d.pop("secretCredentials", UNSET))

        domino_datasource_web_update_data_source_credential_request = cls(
            auth_type=auth_type,
            credential_type=credential_type,
            visible_credential=visible_credential,
            secret_credential=secret_credential,
            secret_credentials=secret_credentials,
        )

        domino_datasource_web_update_data_source_credential_request.additional_properties = d
        return domino_datasource_web_update_data_source_credential_request

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
