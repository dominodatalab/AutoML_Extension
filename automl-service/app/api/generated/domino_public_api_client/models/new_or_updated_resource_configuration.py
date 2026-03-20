from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_or_updated_resource_configuration_configuration import (
        NewOrUpdatedResourceConfigurationConfiguration,
    )


T = TypeVar("T", bound="NewOrUpdatedResourceConfiguration")


@_attrs_define
class NewOrUpdatedResourceConfiguration:
    """Resource Configuration create or update request

    Attributes:
        configuration (NewOrUpdatedResourceConfigurationConfiguration | Unset): Configuration of this Resource
            Configuration following the schema in its Deployment Target Type Example: {'instance_type': 'm5.large'}.
        description (str | Unset): Description for the Resource Configuration
        id (str | Unset): UUID for the Resource Configuration. Must be included if updating an existing Resource
            Configuration. If missing, a new Resource Configuration is created.
        is_default (bool | Unset): Whether the resource configuration is the default one
        name (str | Unset): Internal name for the Resource Configuration Example: gpu_large.
    """

    configuration: NewOrUpdatedResourceConfigurationConfiguration | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        description = self.description

        id = self.id

        is_default = self.is_default

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_or_updated_resource_configuration_configuration import (
            NewOrUpdatedResourceConfigurationConfiguration,
        )

        d = dict(src_dict)
        _configuration = d.pop("configuration", UNSET)
        configuration: NewOrUpdatedResourceConfigurationConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = NewOrUpdatedResourceConfigurationConfiguration.from_dict(_configuration)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        is_default = d.pop("isDefault", UNSET)

        name = d.pop("name", UNSET)

        new_or_updated_resource_configuration = cls(
            configuration=configuration,
            description=description,
            id=id,
            is_default=is_default,
            name=name,
        )

        new_or_updated_resource_configuration.additional_properties = d
        return new_or_updated_resource_configuration

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
