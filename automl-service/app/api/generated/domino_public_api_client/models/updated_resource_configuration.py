from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.updated_resource_configuration_configuration import UpdatedResourceConfigurationConfiguration


T = TypeVar("T", bound="UpdatedResourceConfiguration")


@_attrs_define
class UpdatedResourceConfiguration:
    """Resource Configuration update request

    Attributes:
        id (str): UUID for the Resource Configuration
        configuration (UpdatedResourceConfigurationConfiguration | Unset): Configuration of this Resource Configuration
            following the schema in its Deployment Target Type Example: {'instance_type': 'm5.large'}.
        description (str | Unset): Description for the Resource Configuration
        name (str | Unset): Internal name for the Resource Configuration Example: gpu_large.
    """

    id: str
    configuration: UpdatedResourceConfigurationConfiguration | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.updated_resource_configuration_configuration import UpdatedResourceConfigurationConfiguration

        d = dict(src_dict)
        id = d.pop("id")

        _configuration = d.pop("configuration", UNSET)
        configuration: UpdatedResourceConfigurationConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = UpdatedResourceConfigurationConfiguration.from_dict(_configuration)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        updated_resource_configuration = cls(
            id=id,
            configuration=configuration,
            description=description,
            name=name,
        )

        updated_resource_configuration.additional_properties = d
        return updated_resource_configuration

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
