from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_source_credential_type_v1 import DataSourceCredentialTypeV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_config_v1 import DataSourceConfigV1
    from ..models.data_source_credentials_v1 import DataSourceCredentialsV1
    from ..models.data_source_permissions_v1 import DataSourcePermissionsV1


T = TypeVar("T", bound="NewDataSourceV1")


@_attrs_define
class NewDataSourceV1:
    """
    Attributes:
        auth_type (str): The type of Data Source authentication Example: AzureBasic.
        config (DataSourceConfigV1): A map of configuration name -> value Example: {'host': 'example-host.com'}.
        credential_type (DataSourceCredentialTypeV1): Whether the credentials is individual to a user or shared
        credentials (DataSourceCredentialsV1):
        data_source_type (str): The configuration type of the Data Source Example: ADLSConfig.
        name (str): User given name of the Data Source Example: data-source-name.
        permissions (DataSourcePermissionsV1):
        description (str | Unset): Description of the Data Source Example: My Data Source.
    """

    auth_type: str
    config: DataSourceConfigV1
    credential_type: DataSourceCredentialTypeV1
    credentials: DataSourceCredentialsV1
    data_source_type: str
    name: str
    permissions: DataSourcePermissionsV1
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type = self.auth_type

        config = self.config.to_dict()

        credential_type = self.credential_type.value

        credentials = self.credentials.to_dict()

        data_source_type = self.data_source_type

        name = self.name

        permissions = self.permissions.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authType": auth_type,
                "config": config,
                "credentialType": credential_type,
                "credentials": credentials,
                "dataSourceType": data_source_type,
                "name": name,
                "permissions": permissions,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_config_v1 import DataSourceConfigV1
        from ..models.data_source_credentials_v1 import DataSourceCredentialsV1
        from ..models.data_source_permissions_v1 import DataSourcePermissionsV1

        d = dict(src_dict)
        auth_type = d.pop("authType")

        config = DataSourceConfigV1.from_dict(d.pop("config"))

        credential_type = DataSourceCredentialTypeV1(d.pop("credentialType"))

        credentials = DataSourceCredentialsV1.from_dict(d.pop("credentials"))

        data_source_type = d.pop("dataSourceType")

        name = d.pop("name")

        permissions = DataSourcePermissionsV1.from_dict(d.pop("permissions"))

        description = d.pop("description", UNSET)

        new_data_source_v1 = cls(
            auth_type=auth_type,
            config=config,
            credential_type=credential_type,
            credentials=credentials,
            data_source_type=data_source_type,
            name=name,
            permissions=permissions,
            description=description,
        )

        new_data_source_v1.additional_properties = d
        return new_data_source_v1

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
