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


T = TypeVar("T", bound="NewModelDeployment")


@_attrs_define
class NewModelDeployment:
    """Model Deployment

    Attributes:
        configuration (ModelDeploymentConfiguration): The Model Deployment configuration
        deployment_target_id (str):  Example: ABC-123.
        models (list[NewOrUpdatedModelDetail]): A list of models associated with this Model Deployment.
        name (str): The Model Deployment name. Example: Income Classifier Deployment.
        resource_configuration_id (str):  Example: DEF-123.
        collaborators (list[ModelDeploymentCollaborator] | Unset): List of collaborators, if any. Will default to empty
            list if not provided
        description (str | Unset):  Example: This endpoint is designed to provide businesses with insights into their
            customer retention patterns..
        is_globally_accessible (bool | Unset): Whether the Model Deployment is viewable by Domino Users who are not
            collaborators. Will default to false if not provided
    """

    configuration: ModelDeploymentConfiguration
    deployment_target_id: str
    models: list[NewOrUpdatedModelDetail]
    name: str
    resource_configuration_id: str
    collaborators: list[ModelDeploymentCollaborator] | Unset = UNSET
    description: str | Unset = UNSET
    is_globally_accessible: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        deployment_target_id = self.deployment_target_id

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        name = self.name

        resource_configuration_id = self.resource_configuration_id

        collaborators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collaborators, Unset):
            collaborators = []
            for collaborators_item_data in self.collaborators:
                collaborators_item = collaborators_item_data.to_dict()
                collaborators.append(collaborators_item)

        description = self.description

        is_globally_accessible = self.is_globally_accessible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "deploymentTargetId": deployment_target_id,
                "models": models,
                "name": name,
                "resourceConfigurationId": resource_configuration_id,
            }
        )
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if description is not UNSET:
            field_dict["description"] = description
        if is_globally_accessible is not UNSET:
            field_dict["isGloballyAccessible"] = is_globally_accessible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_deployment_collaborator import ModelDeploymentCollaborator
        from ..models.model_deployment_configuration import ModelDeploymentConfiguration
        from ..models.new_or_updated_model_detail import NewOrUpdatedModelDetail

        d = dict(src_dict)
        configuration = ModelDeploymentConfiguration.from_dict(d.pop("configuration"))

        deployment_target_id = d.pop("deploymentTargetId")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = NewOrUpdatedModelDetail.from_dict(models_item_data)

            models.append(models_item)

        name = d.pop("name")

        resource_configuration_id = d.pop("resourceConfigurationId")

        _collaborators = d.pop("collaborators", UNSET)
        collaborators: list[ModelDeploymentCollaborator] | Unset = UNSET
        if _collaborators is not UNSET:
            collaborators = []
            for collaborators_item_data in _collaborators:
                collaborators_item = ModelDeploymentCollaborator.from_dict(collaborators_item_data)

                collaborators.append(collaborators_item)

        description = d.pop("description", UNSET)

        is_globally_accessible = d.pop("isGloballyAccessible", UNSET)

        new_model_deployment = cls(
            configuration=configuration,
            deployment_target_id=deployment_target_id,
            models=models,
            name=name,
            resource_configuration_id=resource_configuration_id,
            collaborators=collaborators,
            description=description,
            is_globally_accessible=is_globally_accessible,
        )

        new_model_deployment.additional_properties = d
        return new_model_deployment

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
