from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_source import ModelSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_custom_resource_definition import DeploymentCustomResourceDefinition
    from ..models.deployment_target_configuration_schemas import DeploymentTargetConfigurationSchemas
    from ..models.deployment_type_specific_schemas import DeploymentTypeSpecificSchemas
    from ..models.shared_and_model_specific_schemas import SharedAndModelSpecificSchemas


T = TypeVar("T", bound="DeploymentTargetType")


@_attrs_define
class DeploymentTargetType:
    """Deployment Target Type.  Each specific schema can have properties that are direct children or one layer deep.  Two
    or more layers of nesting is not supported.

        Example:
            {'dataPlaneId': 0, 'deploymentTargetConfigurationSchemas': {'defaultResourceConfigs': {'Cheap': {'instanceType':
                'ml.t2.medium'}, 'Expensive': {'instanceType': 'ml.c5.2xlarge'}}, 'resourceConfigSchema': {'properties':
                {'instanceType': {'description': 'AWS compute instance type', 'title': 'Instance Type', 'type': 'string'}},
                'required': ['instanceType'], 'type': 'object'}, 'targetConfigSchema': {'properties': {'credentials':
                {'properties': {'account': {'description': 'AWS Account ID', 'title': 'Account', 'type': 'string'},
                'credentials': {'description': 'AWS Credentials File', 'format': 'password', 'title': 'Credentials', 'type':
                'string'}}, 'required': ['account', 'credentials'], 'type': 'object'}, 'sagemaker': {'properties': {'ecrUrl':
                {'description': 'Amazon Elastic Container Registry URL for model images', 'title': 'ECR URL', 'type': 'string'},
                'executionRoleArn': {'description': 'The Amazon Resource Name (ARN) of the task execution role that grants the
                Amazon ECS container agent permission to make AWS API calls on your behalf.', 'title': 'Execution Role ARN',
                'type': 'string'}, 'region': {'description': 'AWS Region', 'title': 'Region', 'type': 'string'},
                'sagemakerS3ModelsBucket': {'description': 'S3 bucket for storing model artifacts', 'title': 'Sagemaker S3
                Models Bucket', 'type': 'string'}}, 'required': ['region', 'executionRoleArn'], 'type': 'object'}}, 'type':
                'object'}}, 'id': 0, 'modelDeploymentConfigurationSchemas': {'modelSpecificSchema': {'properties':
                {'autoscaling': {'properties': {'enabled': {'default': False, 'description': 'Enable autoscaling', 'title':
                'Autoscaling Enabled', 'type': 'Boolean'}, 'maxInstances': {'default': 4, 'description': 'Maximum number of
                instances running at any time', 'minimum': 0, 'title': 'Max Instances', 'type': 'Integer'}, 'minInstances':
                {'default': 0, 'description': 'Minimum number of instances running at any time', 'minimum': 0, 'title': 'Min
                Instances', 'type': 'Integer'}}, 'type': 'object'}}, 'type': 'object'}, 'sharedSchema': {'properties':
                {'enableExplanations': {'default': False, 'description': 'Turn on Explainer', 'title': 'Enable Explanations',
                'type': 'Boolean'}}, 'type': 'object'}}, 'modelDeploymentCustomResourceDefinition': {'group':
                'modelserving.dominodatalab.com', 'kind': 'SagemakerModelDeployment', 'version': 'v1alpha1'},
                'modelDeploymentStateSchemas': {'modelSpecificSchema': {}, 'sharedSchema': {}},
                'modelDeploymentSupportedModelSources': ['MODELREGISTRY'], 'modelDeploymentTypeConfigurationSchemas':
                {'ASYNC_ENDPOINT': {'modelSpecificSchema': {'properties': {'requestTimeoutSeconds': {'default': 60, 'maximum':
                1800, 'minimum': 1, 'title': 'Request Timeout', 'type': 'Integer'}}, 'type': 'object'}, 'sharedSchema':
                {'properties': {'maximumQueuedRequests': {'default': 1000, 'maximum': 10000, 'minimum': 100, 'title': 'Maximum
                queued requests', 'type': 'Integer'}}, 'type': 'object'}}, 'SYNC_ENDPOINT': {'modelSpecificSchema':
                {'properties': {'serverless': {'default': False, 'title': 'Serverless', 'type': 'Boolean'}}, 'type': 'object'},
                'sharedSchema': {'properties': {'healthcheck': {'properties': {'failureThresholdCount': {'default': 3,
                'description': '(count)', 'minimum': 1, 'title': 'Failure Threshold', 'type': 'Integer'}, 'initialDelaySeconds':
                {'default': 60, 'description': '(seconds)', 'minimum': 0, 'title': 'Initial Delay', 'type': 'Integer'},
                'periodSeconds': {'default': 60, 'description': '(seconds)', 'minimum': 5, 'title': 'Health check period',
                'type': 'Integer'}, 'timeoutSeconds': {'default': 300, 'description': '(seconds)', 'minimum': 1, 'title':
                'Health check timeout', 'type': 'Integer'}}, 'title': 'HealthCheck Fields', 'type': 'object'}}, 'type':
                'object'}}}, 'modelDeploymentTypeStateSchemas': {'ASYNC_ENDPOINT': {'modelSpecificSchema': {}, 'sharedSchema':
                {}}, 'SYNC_ENDPOINT': {'modelSpecificSchema': {}, 'sharedSchema': {}}}, 'name': 'SagemakerModelDeployment',
                'operatorVersion': 1}

        Attributes:
            data_plane_id (str): ID of the data plane where the operator is deployed
            deployment_target_configuration_schemas (DeploymentTargetConfigurationSchemas): The Deployment Target
                configuration schemas.  Each configuration can have properties that are direct children or one layer deep.  Two
                or more layers of nesting is not supported.
            id (str): UUID for the Deployment Target Type
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
            name (str): Internal name for the Deployment Target Type Example: aws.
            operator_version (str): Version of the operator Example: 1.0.2.
            logo_url (str | Unset): Url to pull logo image from
    """

    data_plane_id: str
    deployment_target_configuration_schemas: DeploymentTargetConfigurationSchemas
    id: str
    model_deployment_configuration_schemas: SharedAndModelSpecificSchemas
    model_deployment_custom_resource_definition: DeploymentCustomResourceDefinition
    model_deployment_state_schemas: SharedAndModelSpecificSchemas
    model_deployment_supported_model_sources: list[ModelSource]
    model_deployment_type_configuration_schemas: DeploymentTypeSpecificSchemas
    model_deployment_type_state_schemas: DeploymentTypeSpecificSchemas
    name: str
    operator_version: str
    logo_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_plane_id = self.data_plane_id

        deployment_target_configuration_schemas = self.deployment_target_configuration_schemas.to_dict()

        id = self.id

        model_deployment_configuration_schemas = self.model_deployment_configuration_schemas.to_dict()

        model_deployment_custom_resource_definition = self.model_deployment_custom_resource_definition.to_dict()

        model_deployment_state_schemas = self.model_deployment_state_schemas.to_dict()

        model_deployment_supported_model_sources = []
        for model_deployment_supported_model_sources_item_data in self.model_deployment_supported_model_sources:
            model_deployment_supported_model_sources_item = model_deployment_supported_model_sources_item_data.value
            model_deployment_supported_model_sources.append(model_deployment_supported_model_sources_item)

        model_deployment_type_configuration_schemas = self.model_deployment_type_configuration_schemas.to_dict()

        model_deployment_type_state_schemas = self.model_deployment_type_state_schemas.to_dict()

        name = self.name

        operator_version = self.operator_version

        logo_url = self.logo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataPlaneId": data_plane_id,
                "deploymentTargetConfigurationSchemas": deployment_target_configuration_schemas,
                "id": id,
                "modelDeploymentConfigurationSchemas": model_deployment_configuration_schemas,
                "modelDeploymentCustomResourceDefinition": model_deployment_custom_resource_definition,
                "modelDeploymentStateSchemas": model_deployment_state_schemas,
                "modelDeploymentSupportedModelSources": model_deployment_supported_model_sources,
                "modelDeploymentTypeConfigurationSchemas": model_deployment_type_configuration_schemas,
                "modelDeploymentTypeStateSchemas": model_deployment_type_state_schemas,
                "name": name,
                "operatorVersion": operator_version,
            }
        )
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_custom_resource_definition import DeploymentCustomResourceDefinition
        from ..models.deployment_target_configuration_schemas import DeploymentTargetConfigurationSchemas
        from ..models.deployment_type_specific_schemas import DeploymentTypeSpecificSchemas
        from ..models.shared_and_model_specific_schemas import SharedAndModelSpecificSchemas

        d = dict(src_dict)
        data_plane_id = d.pop("dataPlaneId")

        deployment_target_configuration_schemas = DeploymentTargetConfigurationSchemas.from_dict(
            d.pop("deploymentTargetConfigurationSchemas")
        )

        id = d.pop("id")

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

        name = d.pop("name")

        operator_version = d.pop("operatorVersion")

        logo_url = d.pop("logoUrl", UNSET)

        deployment_target_type = cls(
            data_plane_id=data_plane_id,
            deployment_target_configuration_schemas=deployment_target_configuration_schemas,
            id=id,
            model_deployment_configuration_schemas=model_deployment_configuration_schemas,
            model_deployment_custom_resource_definition=model_deployment_custom_resource_definition,
            model_deployment_state_schemas=model_deployment_state_schemas,
            model_deployment_supported_model_sources=model_deployment_supported_model_sources,
            model_deployment_type_configuration_schemas=model_deployment_type_configuration_schemas,
            model_deployment_type_state_schemas=model_deployment_type_state_schemas,
            name=name,
            operator_version=operator_version,
            logo_url=logo_url,
        )

        deployment_target_type.additional_properties = d
        return deployment_target_type

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
