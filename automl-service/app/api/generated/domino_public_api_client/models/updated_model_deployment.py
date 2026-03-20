from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_deployment_collaborator import ModelDeploymentCollaborator
    from ..models.model_deployment_configuration import ModelDeploymentConfiguration
    from ..models.new_or_updated_model_detail import NewOrUpdatedModelDetail


T = TypeVar("T", bound="UpdatedModelDeployment")


@_attrs_define
class UpdatedModelDeployment:
    """Model Deployment

    Attributes:
        collaborators (list[ModelDeploymentCollaborator] | Unset): List of collaborators, if any
        configuration (ModelDeploymentConfiguration | Unset): The Model Deployment configuration
        deployment_target_id (str | Unset): Id of the deployment target
        description (str | Unset):  Example: This endpoint is designed to provide businesses with insights into their
            customer retention patterns..
        is_globally_accessible (bool | Unset): Whether the Model Deployment is viewable by Domino Users who are not
            collaborators.
        models (list[NewOrUpdatedModelDetail] | Unset): A list of models associated with this Model Deployment.
        name (str | Unset): The Model Deployment name. Example: Income Classifier Deployment.
        resource_configuration_id (str | Unset): Id of the resource configuration
    """

    collaborators: list[ModelDeploymentCollaborator] | Unset = UNSET
    configuration: ModelDeploymentConfiguration | Unset = UNSET
    deployment_target_id: str | Unset = UNSET
    description: str | Unset = UNSET
    is_globally_accessible: bool | Unset = UNSET
    models: list[NewOrUpdatedModelDetail] | Unset = UNSET
    name: str | Unset = UNSET
    resource_configuration_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collaborators, Unset):
            collaborators = []
            for collaborators_item_data in self.collaborators:
                collaborators_item = collaborators_item_data.to_dict()
                collaborators.append(collaborators_item)

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        deployment_target_id = self.deployment_target_id

        description = self.description

        is_globally_accessible = self.is_globally_accessible

        models: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = []
            for models_item_data in self.models:
                models_item = models_item_data.to_dict()
                models.append(models_item)

        name = self.name

        resource_configuration_id = self.resource_configuration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if deployment_target_id is not UNSET:
            field_dict["deploymentTargetId"] = deployment_target_id
        if description is not UNSET:
            field_dict["description"] = description
        if is_globally_accessible is not UNSET:
            field_dict["isGloballyAccessible"] = is_globally_accessible
        if models is not UNSET:
            field_dict["models"] = models
        if name is not UNSET:
            field_dict["name"] = name
        if resource_configuration_id is not UNSET:
            field_dict["resourceConfigurationId"] = resource_configuration_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_deployment_collaborator import ModelDeploymentCollaborator
        from ..models.model_deployment_configuration import ModelDeploymentConfiguration
        from ..models.new_or_updated_model_detail import NewOrUpdatedModelDetail

        d = dict(src_dict)
        _collaborators = d.pop("collaborators", UNSET)
        collaborators: list[ModelDeploymentCollaborator] | Unset = UNSET
        if _collaborators is not UNSET:
            collaborators = []
            for collaborators_item_data in _collaborators:
                collaborators_item = ModelDeploymentCollaborator.from_dict(collaborators_item_data)

                collaborators.append(collaborators_item)

        _configuration = d.pop("configuration", UNSET)
        configuration: ModelDeploymentConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = ModelDeploymentConfiguration.from_dict(_configuration)

        deployment_target_id = d.pop("deploymentTargetId", UNSET)

        description = d.pop("description", UNSET)

        is_globally_accessible = d.pop("isGloballyAccessible", UNSET)

        _models = d.pop("models", UNSET)
        models: list[NewOrUpdatedModelDetail] | Unset = UNSET
        if _models is not UNSET:
            models = []
            for models_item_data in _models:
                models_item = NewOrUpdatedModelDetail.from_dict(models_item_data)

                models.append(models_item)

        name = d.pop("name", UNSET)

        resource_configuration_id = d.pop("resourceConfigurationId", UNSET)

        updated_model_deployment = cls(
            collaborators=collaborators,
            configuration=configuration,
            deployment_target_id=deployment_target_id,
            description=description,
            is_globally_accessible=is_globally_accessible,
            models=models,
            name=name,
            resource_configuration_id=resource_configuration_id,
        )

        updated_model_deployment.additional_properties = d
        return updated_model_deployment

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
