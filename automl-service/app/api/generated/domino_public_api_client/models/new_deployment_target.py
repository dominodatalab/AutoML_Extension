from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.new_deployment_target_configuration import NewDeploymentTargetConfiguration
    from ..models.new_resource_configuration import NewResourceConfiguration


T = TypeVar("T", bound="NewDeploymentTarget")


@_attrs_define
class NewDeploymentTarget:
    r"""Deployment Target creation request

    Attributes:
        configuration (NewDeploymentTargetConfiguration): Configuration of this Deployment Target following the schema
            in its Deployment Target Type Example: {'credentials': {'account': 1234, 'credentials': 'AWS_ACCESS_KEY_ID:
            1234\nAWS_SECRET_ACCESS_KEY: itsasecret\n'}, 'sagemaker': {'ecrUrl': 'anURL', 'region': 'us-east-1',
            'sagemakerS3ModelsBucket': 'domino-sagemaker'}}.
        deployment_target_type_id (str): ID of the Deployment Target Type this Deployment Target belongs to
        is_globally_accessible (bool): Whether or not the Deployment Target is globally accessible
        name (str): Internal name for the Deployment Target Example: Production.
        resource_configurations (list[NewResourceConfiguration]):
        user_and_organization_ids (list[str]): User and Organization IDs that can use this Deployment Target
    """

    configuration: NewDeploymentTargetConfiguration
    deployment_target_type_id: str
    is_globally_accessible: bool
    name: str
    resource_configurations: list[NewResourceConfiguration]
    user_and_organization_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        deployment_target_type_id = self.deployment_target_type_id

        is_globally_accessible = self.is_globally_accessible

        name = self.name

        resource_configurations = []
        for resource_configurations_item_data in self.resource_configurations:
            resource_configurations_item = resource_configurations_item_data.to_dict()
            resource_configurations.append(resource_configurations_item)

        user_and_organization_ids = self.user_and_organization_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "deploymentTargetTypeId": deployment_target_type_id,
                "isGloballyAccessible": is_globally_accessible,
                "name": name,
                "resourceConfigurations": resource_configurations,
                "userAndOrganizationIds": user_and_organization_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_deployment_target_configuration import NewDeploymentTargetConfiguration
        from ..models.new_resource_configuration import NewResourceConfiguration

        d = dict(src_dict)
        configuration = NewDeploymentTargetConfiguration.from_dict(d.pop("configuration"))

        deployment_target_type_id = d.pop("deploymentTargetTypeId")

        is_globally_accessible = d.pop("isGloballyAccessible")

        name = d.pop("name")

        resource_configurations = []
        _resource_configurations = d.pop("resourceConfigurations")
        for resource_configurations_item_data in _resource_configurations:
            resource_configurations_item = NewResourceConfiguration.from_dict(resource_configurations_item_data)

            resource_configurations.append(resource_configurations_item)

        user_and_organization_ids = cast(list[str], d.pop("userAndOrganizationIds"))

        new_deployment_target = cls(
            configuration=configuration,
            deployment_target_type_id=deployment_target_type_id,
            is_globally_accessible=is_globally_accessible,
            name=name,
            resource_configurations=resource_configurations,
            user_and_organization_ids=user_and_organization_ids,
        )

        new_deployment_target.additional_properties = d
        return new_deployment_target

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
