from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.credentials_type import CredentialsType

T = TypeVar("T", bound="ModelDeploymentStatusOperationCredentials")


@_attrs_define
class ModelDeploymentStatusOperationCredentials:
    """
    Attributes:
        expiration_time (datetime.datetime):
        keys (list[str]): This field provides the names of properties provided by this credential.
        type_ (CredentialsType): This field identifies the type of credential.  The `enum` value limits the
            possibilities to what this model deployment supports.
    """

    expiration_time: datetime.datetime
    keys: list[str]
    type_: CredentialsType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiration_time = self.expiration_time.isoformat()

        keys = self.keys

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expirationTime": expiration_time,
                "keys": keys,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expiration_time = isoparse(d.pop("expirationTime"))

        keys = cast(list[str], d.pop("keys"))

        type_ = CredentialsType(d.pop("type"))

        model_deployment_status_operation_credentials = cls(
            expiration_time=expiration_time,
            keys=keys,
            type_=type_,
        )

        model_deployment_status_operation_credentials.additional_properties = d
        return model_deployment_status_operation_credentials

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
