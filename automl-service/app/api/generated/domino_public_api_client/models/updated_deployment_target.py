from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_or_updated_resource_configuration import NewOrUpdatedResourceConfiguration
    from ..models.updated_deployment_target_configuration import UpdatedDeploymentTargetConfiguration


T = TypeVar("T", bound="UpdatedDeploymentTarget")


@_attrs_define
class UpdatedDeploymentTarget:
    r"""Deployment Target update request

    Attributes:
        configuration (UpdatedDeploymentTargetConfiguration | Unset): Configuration of this Deployment Target following
            the schema in its Deployment Target Type Example: {'credentials': {'account': 1234, 'credentials':
            'AWS_ACCESS_KEY_ID: 1234\nAWS_SECRET_ACCESS_KEY: itsasecret\n'}, 'sagemaker': {'ecrUrl': 'anURL', 'region': 'us-
            east-1', 'sagemakerS3ModelsBucket': 'domino-sagemaker'}}.
        is_globally_accessible (bool | Unset): Whether or not the Deployment Target is globally accessible
        name (str | Unset): Internal name for the Deployment Target Example: Production.
        resource_configurations (list[NewOrUpdatedResourceConfiguration] | Unset): Updated Resource Configurations -
            updates existing resource configurations for values with specified id fields - creates new resource
            configurations for values without specified id fields - deletes existing resource configurations not specified
            in the array
        user_and_organization_ids (list[str] | Unset): User and Organization IDs that can use this Deployment Target
    """

    configuration: UpdatedDeploymentTargetConfiguration | Unset = UNSET
    is_globally_accessible: bool | Unset = UNSET
    name: str | Unset = UNSET
    resource_configurations: list[NewOrUpdatedResourceConfiguration] | Unset = UNSET
    user_and_organization_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        is_globally_accessible = self.is_globally_accessible

        name = self.name

        resource_configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resource_configurations, Unset):
            resource_configurations = []
            for resource_configurations_item_data in self.resource_configurations:
                resource_configurations_item = resource_configurations_item_data.to_dict()
                resource_configurations.append(resource_configurations_item)

        user_and_organization_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_and_organization_ids, Unset):
            user_and_organization_ids = self.user_and_organization_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if is_globally_accessible is not UNSET:
            field_dict["isGloballyAccessible"] = is_globally_accessible
        if name is not UNSET:
            field_dict["name"] = name
        if resource_configurations is not UNSET:
            field_dict["resourceConfigurations"] = resource_configurations
        if user_and_organization_ids is not UNSET:
            field_dict["userAndOrganizationIds"] = user_and_organization_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_or_updated_resource_configuration import NewOrUpdatedResourceConfiguration
        from ..models.updated_deployment_target_configuration import UpdatedDeploymentTargetConfiguration

        d = dict(src_dict)
        _configuration = d.pop("configuration", UNSET)
        configuration: UpdatedDeploymentTargetConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = UpdatedDeploymentTargetConfiguration.from_dict(_configuration)

        is_globally_accessible = d.pop("isGloballyAccessible", UNSET)

        name = d.pop("name", UNSET)

        _resource_configurations = d.pop("resourceConfigurations", UNSET)
        resource_configurations: list[NewOrUpdatedResourceConfiguration] | Unset = UNSET
        if _resource_configurations is not UNSET:
            resource_configurations = []
            for resource_configurations_item_data in _resource_configurations:
                resource_configurations_item = NewOrUpdatedResourceConfiguration.from_dict(
                    resource_configurations_item_data
                )

                resource_configurations.append(resource_configurations_item)

        user_and_organization_ids = cast(list[str], d.pop("userAndOrganizationIds", UNSET))

        updated_deployment_target = cls(
            configuration=configuration,
            is_globally_accessible=is_globally_accessible,
            name=name,
            resource_configurations=resource_configurations,
            user_and_organization_ids=user_and_organization_ids,
        )

        updated_deployment_target.additional_properties = d
        return updated_deployment_target

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
