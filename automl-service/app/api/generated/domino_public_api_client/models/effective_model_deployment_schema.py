from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.model_source import ModelSource

if TYPE_CHECKING:
    from ..models.deployment_custom_resource_definition import DeploymentCustomResourceDefinition
    from ..models.deployment_target_configuration import DeploymentTargetConfiguration
    from ..models.deployment_type_specific_schemas import DeploymentTypeSpecificSchemas
    from ..models.shared_and_model_specific_schemas import SharedAndModelSpecificSchemas


T = TypeVar("T", bound="EffectiveModelDeploymentSchema")


@_attrs_define
class EffectiveModelDeploymentSchema:
    """Effective Model Deployment Schema

    Attributes:
        data_plane_id (str): ID of the data plane where the operator is deployed
        deployment_target_configuration (DeploymentTargetConfiguration): The Deployment Target configuration values for
            the Deployment Target and Resource Configuration
        deployment_target_last_modified (datetime.datetime): Timestamp of the last update to the deployment target (will
            be the creation timestamp on creation)
        deployment_target_type_id (str): UUID for the Deployment Target Type
        deployment_target_type_name (str): Internal name for the Deployment Target Type Example: aws.
        deployment_target_type_operator_version (str): Version of the operator Example: 1.0.2.
        model_deployment_configuration_schemas (SharedAndModelSpecificSchemas): Shared and Model Specific configs.
        model_deployment_custom_resource_definition (DeploymentCustomResourceDefinition): Custom Resource Definition for
            Model Deployment
        model_deployment_state_schemas (SharedAndModelSpecificSchemas): Shared and Model Specific configs.
        model_deployment_supported_model_sources (list[ModelSource]): Model sources supported by Domino Example:
            ['MODELREGISTRY'].
        model_deployment_type_configuration_schemas (DeploymentTypeSpecificSchemas): The supported deployment types.
            There must be one property present for each deployment type.
        model_deployment_type_state_schemas (DeploymentTypeSpecificSchemas): The supported deployment types.  There must
            be one property present for each deployment type.
        resource_configuration_last_modified (datetime.datetime): Timestamp of the last update to the resource
            configuration (will be the creation timestamp on creation)
    """

    data_plane_id: str
    deployment_target_configuration: DeploymentTargetConfiguration
    deployment_target_last_modified: datetime.datetime
    deployment_target_type_id: str
    deployment_target_type_name: str
    deployment_target_type_operator_version: str
    model_deployment_configuration_schemas: SharedAndModelSpecificSchemas
    model_deployment_custom_resource_definition: DeploymentCustomResourceDefinition
    model_deployment_state_schemas: SharedAndModelSpecificSchemas
    model_deployment_supported_model_sources: list[ModelSource]
    model_deployment_type_configuration_schemas: DeploymentTypeSpecificSchemas
    model_deployment_type_state_schemas: DeploymentTypeSpecificSchemas
    resource_configuration_last_modified: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_plane_id = self.data_plane_id

        deployment_target_configuration = self.deployment_target_configuration.to_dict()

        deployment_target_last_modified = self.deployment_target_last_modified.isoformat()

        deployment_target_type_id = self.deployment_target_type_id

        deployment_target_type_name = self.deployment_target_type_name

        deployment_target_type_operator_version = self.deployment_target_type_operator_version

        model_deployment_configuration_schemas = self.model_deployment_configuration_schemas.to_dict()

        model_deployment_custom_resource_definition = self.model_deployment_custom_resource_definition.to_dict()

        model_deployment_state_schemas = self.model_deployment_state_schemas.to_dict()

        model_deployment_supported_model_sources = []
        for model_deployment_supported_model_sources_item_data in self.model_deployment_supported_model_sources:
            model_deployment_supported_model_sources_item = model_deployment_supported_model_sources_item_data.value
            model_deployment_supported_model_sources.append(model_deployment_supported_model_sources_item)

        model_deployment_type_configuration_schemas = self.model_deployment_type_configuration_schemas.to_dict()

        model_deployment_type_state_schemas = self.model_deployment_type_state_schemas.to_dict()

        resource_configuration_last_modified = self.resource_configuration_last_modified.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataPlaneId": data_plane_id,
                "deploymentTargetConfiguration": deployment_target_configuration,
                "deploymentTargetLastModified": deployment_target_last_modified,
                "deploymentTargetTypeId": deployment_target_type_id,
                "deploymentTargetTypeName": deployment_target_type_name,
                "deploymentTargetTypeOperatorVersion": deployment_target_type_operator_version,
                "modelDeploymentConfigurationSchemas": model_deployment_configuration_schemas,
                "modelDeploymentCustomResourceDefinition": model_deployment_custom_resource_definition,
                "modelDeploymentStateSchemas": model_deployment_state_schemas,
                "modelDeploymentSupportedModelSources": model_deployment_supported_model_sources,
                "modelDeploymentTypeConfigurationSchemas": model_deployment_type_configuration_schemas,
                "modelDeploymentTypeStateSchemas": model_deployment_type_state_schemas,
                "resourceConfigurationLastModified": resource_configuration_last_modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_custom_resource_definition import DeploymentCustomResourceDefinition
        from ..models.deployment_target_configuration import DeploymentTargetConfiguration
        from ..models.deployment_type_specific_schemas import DeploymentTypeSpecificSchemas
        from ..models.shared_and_model_specific_schemas import SharedAndModelSpecificSchemas

        d = dict(src_dict)
        data_plane_id = d.pop("dataPlaneId")

        deployment_target_configuration = DeploymentTargetConfiguration.from_dict(
            d.pop("deploymentTargetConfiguration")
        )

        deployment_target_last_modified = isoparse(d.pop("deploymentTargetLastModified"))

        deployment_target_type_id = d.pop("deploymentTargetTypeId")

        deployment_target_type_name = d.pop("deploymentTargetTypeName")

        deployment_target_type_operator_version = d.pop("deploymentTargetTypeOperatorVersion")

        model_deployment_configuration_schemas = SharedAndModelSpecificSchemas.from_dict(
            d.pop("modelDeploymentConfigurationSchemas")
        )

        model_deployment_custom_resource_definition = DeploymentCustomResourceDefinition.from_dict(
            d.pop("modelDeploymentCustomResourceDefinition")
        )

        model_deployment_state_schemas = SharedAndModelSpecificSchemas.from_dict(d.pop("modelDeploymentStateSchemas"))

        model_deployment_supported_model_sources = []
        _model_deployment_supported_model_sources = d.pop("modelDeploymentSupportedModelSources")
        for model_deployment_supported_model_sources_item_data in _model_deployment_supported_model_sources:
            model_deployment_supported_model_sources_item = ModelSource(
                model_deployment_supported_model_sources_item_data
            )

            model_deployment_supported_model_sources.append(model_deployment_supported_model_sources_item)

        model_deployment_type_configuration_schemas = DeploymentTypeSpecificSchemas.from_dict(
            d.pop("modelDeploymentTypeConfigurationSchemas")
        )

        model_deployment_type_state_schemas = DeploymentTypeSpecificSchemas.from_dict(
            d.pop("modelDeploymentTypeStateSchemas")
        )

        resource_configuration_last_modified = isoparse(d.pop("resourceConfigurationLastModified"))

        effective_model_deployment_schema = cls(
            data_plane_id=data_plane_id,
            deployment_target_configuration=deployment_target_configuration,
            deployment_target_last_modified=deployment_target_last_modified,
            deployment_target_type_id=deployment_target_type_id,
            deployment_target_type_name=deployment_target_type_name,
            deployment_target_type_operator_version=deployment_target_type_operator_version,
            model_deployment_configuration_schemas=model_deployment_configuration_schemas,
            model_deployment_custom_resource_definition=model_deployment_custom_resource_definition,
            model_deployment_state_schemas=model_deployment_state_schemas,
            model_deployment_supported_model_sources=model_deployment_supported_model_sources,
            model_deployment_type_configuration_schemas=model_deployment_type_configuration_schemas,
            model_deployment_type_state_schemas=model_deployment_type_state_schemas,
            resource_configuration_last_modified=resource_configuration_last_modified,
        )

        effective_model_deployment_schema.additional_properties = d
        return effective_model_deployment_schema

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
