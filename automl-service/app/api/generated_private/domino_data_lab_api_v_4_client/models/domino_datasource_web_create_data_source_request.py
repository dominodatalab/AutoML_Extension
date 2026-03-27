from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasource_web_create_data_source_request_auth_type import (
    DominoDatasourceWebCreateDataSourceRequestAuthType,
)
from ..models.domino_datasource_web_create_data_source_request_credential_type import (
    DominoDatasourceWebCreateDataSourceRequestCredentialType,
)
from ..models.domino_datasource_web_create_data_source_request_data_source_type import (
    DominoDatasourceWebCreateDataSourceRequestDataSourceType,
)
from ..models.domino_datasource_web_create_data_source_request_engine_type import (
    DominoDatasourceWebCreateDataSourceRequestEngineType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasource_web_create_data_source_request_config import (
        DominoDatasourceWebCreateDataSourceRequestConfig,
    )


T = TypeVar("T", bound="DominoDatasourceWebCreateDataSourceRequest")


@_attrs_define
class DominoDatasourceWebCreateDataSourceRequest:
    """
    Attributes:
        auth_type (DominoDatasourceWebCreateDataSourceRequestAuthType):
        credential_type (DominoDatasourceWebCreateDataSourceRequestCredentialType):
        config (DominoDatasourceWebCreateDataSourceRequestConfig):
        data_source_type (DominoDatasourceWebCreateDataSourceRequestDataSourceType):
        is_everyone (bool):
        name (str):
        user_ids (list[str]):
        description (None | str | Unset):
        engine_type (DominoDatasourceWebCreateDataSourceRequestEngineType | Unset):
        project_id (None | str | Unset):
        secret_credential (None | str | Unset):
        visible_credential (None | str | Unset):
    """

    auth_type: DominoDatasourceWebCreateDataSourceRequestAuthType
    credential_type: DominoDatasourceWebCreateDataSourceRequestCredentialType
    config: DominoDatasourceWebCreateDataSourceRequestConfig
    data_source_type: DominoDatasourceWebCreateDataSourceRequestDataSourceType
    is_everyone: bool
    name: str
    user_ids: list[str]
    description: None | str | Unset = UNSET
    engine_type: DominoDatasourceWebCreateDataSourceRequestEngineType | Unset = UNSET
    project_id: None | str | Unset = UNSET
    secret_credential: None | str | Unset = UNSET
    visible_credential: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type = self.auth_type.value

        credential_type = self.credential_type.value

        config = self.config.to_dict()

        data_source_type = self.data_source_type.value

        is_everyone = self.is_everyone

        name = self.name

        user_ids = self.user_ids

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        engine_type: str | Unset = UNSET
        if not isinstance(self.engine_type, Unset):
            engine_type = self.engine_type.value

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        secret_credential: None | str | Unset
        if isinstance(self.secret_credential, Unset):
            secret_credential = UNSET
        else:
            secret_credential = self.secret_credential

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
                "config": config,
                "dataSourceType": data_source_type,
                "isEveryone": is_everyone,
                "name": name,
                "userIds": user_ids,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if engine_type is not UNSET:
            field_dict["engineType"] = engine_type
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if secret_credential is not UNSET:
            field_dict["secretCredential"] = secret_credential
        if visible_credential is not UNSET:
            field_dict["visibleCredential"] = visible_credential

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_web_create_data_source_request_config import (
            DominoDatasourceWebCreateDataSourceRequestConfig,
        )

        d = dict(src_dict)
        auth_type = DominoDatasourceWebCreateDataSourceRequestAuthType(d.pop("authType"))

        credential_type = DominoDatasourceWebCreateDataSourceRequestCredentialType(d.pop("credentialType"))

        config = DominoDatasourceWebCreateDataSourceRequestConfig.from_dict(d.pop("config"))

        data_source_type = DominoDatasourceWebCreateDataSourceRequestDataSourceType(d.pop("dataSourceType"))

        is_everyone = d.pop("isEveryone")

        name = d.pop("name")

        user_ids = cast(list[str], d.pop("userIds"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _engine_type = d.pop("engineType", UNSET)
        engine_type: DominoDatasourceWebCreateDataSourceRequestEngineType | Unset
        if isinstance(_engine_type, Unset):
            engine_type = UNSET
        else:
            engine_type = DominoDatasourceWebCreateDataSourceRequestEngineType(_engine_type)

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        def _parse_secret_credential(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_credential = _parse_secret_credential(d.pop("secretCredential", UNSET))

        def _parse_visible_credential(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visible_credential = _parse_visible_credential(d.pop("visibleCredential", UNSET))

        domino_datasource_web_create_data_source_request = cls(
            auth_type=auth_type,
            credential_type=credential_type,
            config=config,
            data_source_type=data_source_type,
            is_everyone=is_everyone,
            name=name,
            user_ids=user_ids,
            description=description,
            engine_type=engine_type,
            project_id=project_id,
            secret_credential=secret_credential,
            visible_credential=visible_credential,
        )

        domino_datasource_web_create_data_source_request.additional_properties = d
        return domino_datasource_web_create_data_source_request

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
