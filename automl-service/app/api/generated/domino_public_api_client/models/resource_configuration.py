from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_configuration_configuration import ResourceConfigurationConfiguration


T = TypeVar("T", bound="ResourceConfiguration")


@_attrs_define
class ResourceConfiguration:
    """Resource Configuration

    Example:
        {'configuration': {'instanceType': 'm7g.medium'}, 'deploymentTargetId': 1, 'description': 'Medium AWS Instance',
            'id': 2, 'name': 'Medium'}

    Attributes:
        configuration (ResourceConfigurationConfiguration): Configuration of this Resource Configuration following the
            schema in its Deployment Target Type Example: {'instance_type': 'm5.large'}.
        deployment_target_id (str): ID of the Deployment Target this Resource Configuration belongs to
        id (str): UUID for the Resource Configuration
        last_modified (datetime.datetime): Timestamp of the last update to the resource configuration (will be the
            creation timestamp on creation)
        name (str): Internal name for the Resource Configuration Example: gpu_large.
        description (str | Unset): Description for the Resource Configuration
    """

    configuration: ResourceConfigurationConfiguration
    deployment_target_id: str
    id: str
    last_modified: datetime.datetime
    name: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        deployment_target_id = self.deployment_target_id

        id = self.id

        last_modified = self.last_modified.isoformat()

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "deploymentTargetId": deployment_target_id,
                "id": id,
                "lastModified": last_modified,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_configuration_configuration import ResourceConfigurationConfiguration

        d = dict(src_dict)
        configuration = ResourceConfigurationConfiguration.from_dict(d.pop("configuration"))

        deployment_target_id = d.pop("deploymentTargetId")

        id = d.pop("id")

        last_modified = isoparse(d.pop("lastModified"))

        name = d.pop("name")

        description = d.pop("description", UNSET)

        resource_configuration = cls(
            configuration=configuration,
            deployment_target_id=deployment_target_id,
            id=id,
            last_modified=last_modified,
            name=name,
            description=description,
        )

        resource_configuration.additional_properties = d
        return resource_configuration

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
