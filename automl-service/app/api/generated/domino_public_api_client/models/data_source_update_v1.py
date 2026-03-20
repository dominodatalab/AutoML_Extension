from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_config_v1 import DataSourceConfigV1
    from ..models.data_source_credentials_v1 import DataSourceCredentialsV1
    from ..models.data_source_permissions_v1 import DataSourcePermissionsV1


T = TypeVar("T", bound="DataSourceUpdateV1")


@_attrs_define
class DataSourceUpdateV1:
    """
    Attributes:
        config (DataSourceConfigV1 | Unset): A map of configuration name -> value Example: {'host': 'example-host.com'}.
        credentials (DataSourceCredentialsV1 | Unset):
        permissions (DataSourcePermissionsV1 | Unset):
    """

    config: DataSourceConfigV1 | Unset = UNSET
    credentials: DataSourceCredentialsV1 | Unset = UNSET
    permissions: DataSourcePermissionsV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_config_v1 import DataSourceConfigV1
        from ..models.data_source_credentials_v1 import DataSourceCredentialsV1
        from ..models.data_source_permissions_v1 import DataSourcePermissionsV1

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: DataSourceConfigV1 | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = DataSourceConfigV1.from_dict(_config)

        _credentials = d.pop("credentials", UNSET)
        credentials: DataSourceCredentialsV1 | Unset
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = DataSourceCredentialsV1.from_dict(_credentials)

        _permissions = d.pop("permissions", UNSET)
        permissions: DataSourcePermissionsV1 | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = DataSourcePermissionsV1.from_dict(_permissions)

        data_source_update_v1 = cls(
            config=config,
            credentials=credentials,
            permissions=permissions,
        )

        data_source_update_v1.additional_properties = d
        return data_source_update_v1

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
