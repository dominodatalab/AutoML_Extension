from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.credentials_type import CredentialsType

if TYPE_CHECKING:
    from ..models.model_deployment_credentials_credentials import ModelDeploymentCredentialsCredentials


T = TypeVar("T", bound="ModelDeploymentCredentials")


@_attrs_define
class ModelDeploymentCredentials:
    """Model Deployment Credentials

    Attributes:
        credentials (ModelDeploymentCredentialsCredentials): The actual credentials represented as key value pairs
            Example: {'AWS_ACCESS_KEY_ID': 1234, 'AWS_SECRET_ACCESS_KEY': 5678, 'AWS_SESSION_TOKEN': '0123token'}.
        credentials_type (CredentialsType): This field identifies the type of credential.  The `enum` value limits the
            possibilities to what this model deployment supports.
        expiration_time (datetime.datetime):  Example: 2023-07-15T14:35:47.89Z.
        operation_type (str):  Example: INVOKE_ENDPOINT.
    """

    credentials: ModelDeploymentCredentialsCredentials
    credentials_type: CredentialsType
    expiration_time: datetime.datetime
    operation_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials = self.credentials.to_dict()

        credentials_type = self.credentials_type.value

        expiration_time = self.expiration_time.isoformat()

        operation_type = self.operation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
                "credentialsType": credentials_type,
                "expirationTime": expiration_time,
                "operationType": operation_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_deployment_credentials_credentials import ModelDeploymentCredentialsCredentials

        d = dict(src_dict)
        credentials = ModelDeploymentCredentialsCredentials.from_dict(d.pop("credentials"))

        credentials_type = CredentialsType(d.pop("credentialsType"))

        expiration_time = isoparse(d.pop("expirationTime"))

        operation_type = d.pop("operationType")

        model_deployment_credentials = cls(
            credentials=credentials,
            credentials_type=credentials_type,
            expiration_time=expiration_time,
            operation_type=operation_type,
        )

        model_deployment_credentials.additional_properties = d
        return model_deployment_credentials

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
