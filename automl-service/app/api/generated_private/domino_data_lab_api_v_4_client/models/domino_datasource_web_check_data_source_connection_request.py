from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasource_web_check_data_source_connection_request_auth_type import (
    DominoDatasourceWebCheckDataSourceConnectionRequestAuthType,
)
from ..models.domino_datasource_web_check_data_source_connection_request_credential_type import (
    DominoDatasourceWebCheckDataSourceConnectionRequestCredentialType,
)
from ..models.domino_datasource_web_check_data_source_connection_request_data_source_type import (
    DominoDatasourceWebCheckDataSourceConnectionRequestDataSourceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasource_api_data_source_data_plane_info import DominoDatasourceApiDataSourceDataPlaneInfo
    from ..models.domino_datasource_web_check_data_source_connection_request_config import (
        DominoDatasourceWebCheckDataSourceConnectionRequestConfig,
    )
    from ..models.domino_datasource_web_check_data_source_connection_request_secret_credentials_type_0 import (
        DominoDatasourceWebCheckDataSourceConnectionRequestSecretCredentialsType0,
    )


T = TypeVar("T", bound="DominoDatasourceWebCheckDataSourceConnectionRequest")


@_attrs_define
class DominoDatasourceWebCheckDataSourceConnectionRequest:
    """
    Attributes:
        auth_type (DominoDatasourceWebCheckDataSourceConnectionRequestAuthType):
        credential_type (DominoDatasourceWebCheckDataSourceConnectionRequestCredentialType):
        data_source_type (DominoDatasourceWebCheckDataSourceConnectionRequestDataSourceType):
        config (DominoDatasourceWebCheckDataSourceConnectionRequestConfig):
        data_planes (list[DominoDatasourceApiDataSourceDataPlaneInfo]):
        use_all_data_planes (bool):
        secret_credential (None | str | Unset):
        secret_credentials (DominoDatasourceWebCheckDataSourceConnectionRequestSecretCredentialsType0 | None | Unset):
        visible_credential (None | str | Unset):
    """

    auth_type: DominoDatasourceWebCheckDataSourceConnectionRequestAuthType
    credential_type: DominoDatasourceWebCheckDataSourceConnectionRequestCredentialType
    data_source_type: DominoDatasourceWebCheckDataSourceConnectionRequestDataSourceType
    config: DominoDatasourceWebCheckDataSourceConnectionRequestConfig
    data_planes: list[DominoDatasourceApiDataSourceDataPlaneInfo]
    use_all_data_planes: bool
    secret_credential: None | str | Unset = UNSET
    secret_credentials: DominoDatasourceWebCheckDataSourceConnectionRequestSecretCredentialsType0 | None | Unset = UNSET
    visible_credential: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_datasource_web_check_data_source_connection_request_secret_credentials_type_0 import (
            DominoDatasourceWebCheckDataSourceConnectionRequestSecretCredentialsType0,
        )

        auth_type = self.auth_type.value

        credential_type = self.credential_type.value

        data_source_type = self.data_source_type.value

        config = self.config.to_dict()

        data_planes = []
        for data_planes_item_data in self.data_planes:
            data_planes_item = data_planes_item_data.to_dict()
            data_planes.append(data_planes_item)

        use_all_data_planes = self.use_all_data_planes

        secret_credential: None | str | Unset
        if isinstance(self.secret_credential, Unset):
            secret_credential = UNSET
        else:
            secret_credential = self.secret_credential

        secret_credentials: dict[str, Any] | None | Unset
        if isinstance(self.secret_credentials, Unset):
            secret_credentials = UNSET
        elif isinstance(
            self.secret_credentials, DominoDatasourceWebCheckDataSourceConnectionRequestSecretCredentialsType0
        ):
            secret_credentials = self.secret_credentials.to_dict()
        else:
            secret_credentials = self.secret_credentials

        visible_credential: None | str | Unset
        if isinstance(self.visible_credential, Unset):
            visible_credential = UNSET
        else:
            visible_credential = self.visible_credential

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authType": auth_type,
                "credentialType": credential_type,
                "dataSourceType": data_source_type,
                "config": config,
                "dataPlanes": data_planes,
                "useAllDataPlanes": use_all_data_planes,
            }
        )
        if secret_credential is not UNSET:
            field_dict["secretCredential"] = secret_credential
        if secret_credentials is not UNSET:
            field_dict["secretCredentials"] = secret_credentials
        if visible_credential is not UNSET:
            field_dict["visibleCredential"] = visible_credential

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_api_data_source_data_plane_info import (
            DominoDatasourceApiDataSourceDataPlaneInfo,
        )
        from ..models.domino_datasource_web_check_data_source_connection_request_config import (
            DominoDatasourceWebCheckDataSourceConnectionRequestConfig,
        )
        from ..models.domino_datasource_web_check_data_source_connection_request_secret_credentials_type_0 import (
            DominoDatasourceWebCheckDataSourceConnectionRequestSecretCredentialsType0,
        )

        d = dict(src_dict)
        auth_type = DominoDatasourceWebCheckDataSourceConnectionRequestAuthType(d.pop("authType"))

        credential_type = DominoDatasourceWebCheckDataSourceConnectionRequestCredentialType(d.pop("credentialType"))

        data_source_type = DominoDatasourceWebCheckDataSourceConnectionRequestDataSourceType(d.pop("dataSourceType"))

        config = DominoDatasourceWebCheckDataSourceConnectionRequestConfig.from_dict(d.pop("config"))

        data_planes = []
        _data_planes = d.pop("dataPlanes")
        for data_planes_item_data in _data_planes:
            data_planes_item = DominoDatasourceApiDataSourceDataPlaneInfo.from_dict(data_planes_item_data)

            data_planes.append(data_planes_item)

        use_all_data_planes = d.pop("useAllDataPlanes")

        def _parse_secret_credential(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_credential = _parse_secret_credential(d.pop("secretCredential", UNSET))

        def _parse_secret_credentials(
            data: object,
        ) -> DominoDatasourceWebCheckDataSourceConnectionRequestSecretCredentialsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secret_credentials_type_0 = (
                    DominoDatasourceWebCheckDataSourceConnectionRequestSecretCredentialsType0.from_dict(data)
                )

                return secret_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoDatasourceWebCheckDataSourceConnectionRequestSecretCredentialsType0 | None | Unset, data)

        secret_credentials = _parse_secret_credentials(d.pop("secretCredentials", UNSET))

        def _parse_visible_credential(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visible_credential = _parse_visible_credential(d.pop("visibleCredential", UNSET))

        domino_datasource_web_check_data_source_connection_request = cls(
            auth_type=auth_type,
            credential_type=credential_type,
            data_source_type=data_source_type,
            config=config,
            data_planes=data_planes,
            use_all_data_planes=use_all_data_planes,
            secret_credential=secret_credential,
            secret_credentials=secret_credentials,
            visible_credential=visible_credential,
        )

        domino_datasource_web_check_data_source_connection_request.additional_properties = d
        return domino_datasource_web_check_data_source_connection_request

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
