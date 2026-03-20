from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_configuration_info_configuration import ResourceConfigurationInfoConfiguration


T = TypeVar("T", bound="ResourceConfigurationInfo")


@_attrs_define
class ResourceConfigurationInfo:
    """Information about a Resource Configuration

    Attributes:
        configuration (ResourceConfigurationInfoConfiguration): Configuration of the Resource Configuration following
            the schema in its Deployment Target Type Example: {'instance_type': 'm5.large'}.
        id (str): Id of the Resource Configuration Example: ABC-123.
        name (str): Name of the Resource Configuration Example: Large.
    """

    configuration: ResourceConfigurationInfoConfiguration
    id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_configuration_info_configuration import ResourceConfigurationInfoConfiguration

        d = dict(src_dict)
        configuration = ResourceConfigurationInfoConfiguration.from_dict(d.pop("configuration"))

        id = d.pop("id")

        name = d.pop("name")

        resource_configuration_info = cls(
            configuration=configuration,
            id=id,
            name=name,
        )

        resource_configuration_info.additional_properties = d
        return resource_configuration_info

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
