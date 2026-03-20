from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NewDeploymentTargetConfiguration")


@_attrs_define
class NewDeploymentTargetConfiguration:
    r"""Configuration of this Deployment Target following the schema in its Deployment Target Type

    Example:
        {'credentials': {'account': 1234, 'credentials': 'AWS_ACCESS_KEY_ID: 1234\nAWS_SECRET_ACCESS_KEY:
            itsasecret\n'}, 'sagemaker': {'ecrUrl': 'anURL', 'region': 'us-east-1', 'sagemakerS3ModelsBucket': 'domino-
            sagemaker'}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_deployment_target_configuration = cls()

        new_deployment_target_configuration.additional_properties = d
        return new_deployment_target_configuration

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
