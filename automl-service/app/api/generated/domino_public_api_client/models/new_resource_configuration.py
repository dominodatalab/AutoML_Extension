from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_resource_configuration_configuration import NewResourceConfigurationConfiguration


T = TypeVar("T", bound="NewResourceConfiguration")


@_attrs_define
class NewResourceConfiguration:
    """Resource Configuration creation request

    Attributes:
        configuration (NewResourceConfigurationConfiguration): Configuration of this Resource Configuration following
            the schema in its Deployment Target Type Example: {'instance_type': 'm5.large'}.
        name (str): Internal name for the Resource Configuration Example: gpu_large.
        deployment_target_id (str | Unset): ID of the Deployment Target this Resource Configuration belongs to
        description (str | Unset): Description for the Resource Configuration
        is_default (bool | Unset): Whether the resource configuration is the default one
    """

    configuration: NewResourceConfigurationConfiguration
    name: str
    deployment_target_id: str | Unset = UNSET
    description: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        name = self.name

        deployment_target_id = self.deployment_target_id

        description = self.description

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "name": name,
            }
        )
        if deployment_target_id is not UNSET:
            field_dict["deploymentTargetId"] = deployment_target_id
        if description is not UNSET:
            field_dict["description"] = description
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_resource_configuration_configuration import NewResourceConfigurationConfiguration

        d = dict(src_dict)
        configuration = NewResourceConfigurationConfiguration.from_dict(d.pop("configuration"))

        name = d.pop("name")

        deployment_target_id = d.pop("deploymentTargetId", UNSET)

        description = d.pop("description", UNSET)

        is_default = d.pop("isDefault", UNSET)

        new_resource_configuration = cls(
            configuration=configuration,
            name=name,
            deployment_target_id=deployment_target_id,
            description=description,
            is_default=is_default,
        )

        new_resource_configuration.additional_properties = d
        return new_resource_configuration

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
