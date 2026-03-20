from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_source_credentials_v1_secret_credentials import DataSourceCredentialsV1SecretCredentials
    from ..models.data_source_credentials_v1_visible_credentials import DataSourceCredentialsV1VisibleCredentials


T = TypeVar("T", bound="DataSourceCredentialsV1")


@_attrs_define
class DataSourceCredentialsV1:
    """
    Attributes:
        secret_credentials (DataSourceCredentialsV1SecretCredentials): Map of secret credentials fields -> value
        visible_credentials (DataSourceCredentialsV1VisibleCredentials): Map of non-secret credentials fields -> value
    """

    secret_credentials: DataSourceCredentialsV1SecretCredentials
    visible_credentials: DataSourceCredentialsV1VisibleCredentials
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_credentials = self.secret_credentials.to_dict()

        visible_credentials = self.visible_credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secretCredentials": secret_credentials,
                "visibleCredentials": visible_credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_credentials_v1_secret_credentials import DataSourceCredentialsV1SecretCredentials
        from ..models.data_source_credentials_v1_visible_credentials import DataSourceCredentialsV1VisibleCredentials

        d = dict(src_dict)
        secret_credentials = DataSourceCredentialsV1SecretCredentials.from_dict(d.pop("secretCredentials"))

        visible_credentials = DataSourceCredentialsV1VisibleCredentials.from_dict(d.pop("visibleCredentials"))

        data_source_credentials_v1 = cls(
            secret_credentials=secret_credentials,
            visible_credentials=visible_credentials,
        )

        data_source_credentials_v1.additional_properties = d
        return data_source_credentials_v1

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
