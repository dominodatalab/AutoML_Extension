from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_source_credential_type_v1 import DataSourceCredentialTypeV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_config_v1 import DataSourceConfigV1
    from ..models.data_source_permissions_v1 import DataSourcePermissionsV1


T = TypeVar("T", bound="DataSourceEnvelopeV1")


@_attrs_define
class DataSourceEnvelopeV1:
    """
    Attributes:
        auth_type (str): The type of Data Source authentication Example: AzureBasic.
        config (DataSourceConfigV1): A map of configuration name -> value Example: {'host': 'example-host.com'}.
        credential_type (DataSourceCredentialTypeV1): Whether the credentials is individual to a user or shared
        data_source_type (str): The configuration type of the Data Source Example: ADLSConfig.
        display_name (str): Data Source display name Example: Azure Data Lake Store.
        id (str): ID of the Data Source Example: 62604702b7e5d347dbe7a909.
        last_updated (datetime.datetime): ISO 8601 formatted time of when the Data Source was last updated Example:
            2022-04-23T18:25:43.511Z.
        name (str): User given name of the Data Source Example: data-source-name.
        owner_id (str): ID of the Data Source owner Example: 62604702b7e5d347dbe7a909.
        owner_username (str): Username of the owner of the Data Source Example: owner-username.
        permissions (DataSourcePermissionsV1):
        description (str | Unset): Description of the Data Source Example: My Data Source.
    """

    auth_type: str
    config: DataSourceConfigV1
    credential_type: DataSourceCredentialTypeV1
    data_source_type: str
    display_name: str
    id: str
    last_updated: datetime.datetime
    name: str
    owner_id: str
    owner_username: str
    permissions: DataSourcePermissionsV1
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type = self.auth_type

        config = self.config.to_dict()

        credential_type = self.credential_type.value

        data_source_type = self.data_source_type

        display_name = self.display_name

        id = self.id

        last_updated = self.last_updated.isoformat()

        name = self.name

        owner_id = self.owner_id

        owner_username = self.owner_username

        permissions = self.permissions.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authType": auth_type,
                "config": config,
                "credentialType": credential_type,
                "dataSourceType": data_source_type,
                "displayName": display_name,
                "id": id,
                "lastUpdated": last_updated,
                "name": name,
                "ownerId": owner_id,
                "ownerUsername": owner_username,
                "permissions": permissions,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_config_v1 import DataSourceConfigV1
        from ..models.data_source_permissions_v1 import DataSourcePermissionsV1

        d = dict(src_dict)
        auth_type = d.pop("authType")

        config = DataSourceConfigV1.from_dict(d.pop("config"))

        credential_type = DataSourceCredentialTypeV1(d.pop("credentialType"))

        data_source_type = d.pop("dataSourceType")

        display_name = d.pop("displayName")

        id = d.pop("id")

        last_updated = isoparse(d.pop("lastUpdated"))

        name = d.pop("name")

        owner_id = d.pop("ownerId")

        owner_username = d.pop("ownerUsername")

        permissions = DataSourcePermissionsV1.from_dict(d.pop("permissions"))

        description = d.pop("description", UNSET)

        data_source_envelope_v1 = cls(
            auth_type=auth_type,
            config=config,
            credential_type=credential_type,
            data_source_type=data_source_type,
            display_name=display_name,
            id=id,
            last_updated=last_updated,
            name=name,
            owner_id=owner_id,
            owner_username=owner_username,
            permissions=permissions,
            description=description,
        )

        data_source_envelope_v1.additional_properties = d
        return data_source_envelope_v1

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
