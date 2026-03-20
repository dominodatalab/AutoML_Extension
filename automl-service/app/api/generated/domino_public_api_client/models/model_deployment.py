from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creator_info import CreatorInfo
    from ..models.deployment_target_info import DeploymentTargetInfo
    from ..models.model_deployment_collaborator import ModelDeploymentCollaborator
    from ..models.model_deployment_configuration import ModelDeploymentConfiguration
    from ..models.model_deployment_status import ModelDeploymentStatus
    from ..models.model_detail import ModelDetail
    from ..models.resource_configuration_info import ResourceConfigurationInfo


T = TypeVar("T", bound="ModelDeployment")


@_attrs_define
class ModelDeployment:
    """Model Deployment

    Attributes:
        collaborators (list[ModelDeploymentCollaborator]): List of collaborators, if any
        configuration (ModelDeploymentConfiguration): The Model Deployment configuration
        creation_timestamp (datetime.datetime):  Example: 2023-07-15T14:35:47.89Z.
        creator_info (CreatorInfo): Information about the creator of a Model Deployment
        deployment_target_info (DeploymentTargetInfo): Information about a Deployment Target and its corresponding
            Deployment Target Type
        description (str):  Example: This endpoint is designed to provide businesses with insights into their customer
            retention patterns..
        id (str): The id of the Model Deployment. Example: 614e40a7-0509-4cae-89af-55e2097b817d.
        is_globally_accessible (bool): Whether the Model Deployment is viewable by Domino Users who are not
            collaborators
        models (list[ModelDetail]): Models associated with this Model Deployment.
        name (str):  Example: Income Classifier Deployment.
        resource_configuration_info (ResourceConfigurationInfo): Information about a Resource Configuration
        version (int):  Example: 23.
        remote_update_timestamp (datetime.datetime | Unset):  Example: 2023-07-16T19:20:30.45Z.
        status (ModelDeploymentStatus | Unset): The Model Deployment status
    """

    collaborators: list[ModelDeploymentCollaborator]
    configuration: ModelDeploymentConfiguration
    creation_timestamp: datetime.datetime
    creator_info: CreatorInfo
    deployment_target_info: DeploymentTargetInfo
    description: str
    id: str
    is_globally_accessible: bool
    models: list[ModelDetail]
    name: str
    resource_configuration_info: ResourceConfigurationInfo
    version: int
    remote_update_timestamp: datetime.datetime | Unset = UNSET
    status: ModelDeploymentStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        configuration = self.configuration.to_dict()

        creation_timestamp = self.creation_timestamp.isoformat()

        creator_info = self.creator_info.to_dict()

        deployment_target_info = self.deployment_target_info.to_dict()

        description = self.description

        id = self.id

        is_globally_accessible = self.is_globally_accessible

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        name = self.name

        resource_configuration_info = self.resource_configuration_info.to_dict()

        version = self.version

        remote_update_timestamp: str | Unset = UNSET
        if not isinstance(self.remote_update_timestamp, Unset):
            remote_update_timestamp = self.remote_update_timestamp.isoformat()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collaborators": collaborators,
                "configuration": configuration,
                "creationTimestamp": creation_timestamp,
                "creatorInfo": creator_info,
                "deploymentTargetInfo": deployment_target_info,
                "description": description,
                "id": id,
                "isGloballyAccessible": is_globally_accessible,
                "models": models,
                "name": name,
                "resourceConfigurationInfo": resource_configuration_info,
                "version": version,
            }
        )
        if remote_update_timestamp is not UNSET:
            field_dict["remoteUpdateTimestamp"] = remote_update_timestamp
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator_info import CreatorInfo
        from ..models.deployment_target_info import DeploymentTargetInfo
        from ..models.model_deployment_collaborator import ModelDeploymentCollaborator
        from ..models.model_deployment_configuration import ModelDeploymentConfiguration
        from ..models.model_deployment_status import ModelDeploymentStatus
        from ..models.model_detail import ModelDetail
        from ..models.resource_configuration_info import ResourceConfigurationInfo

        d = dict(src_dict)
        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = ModelDeploymentCollaborator.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        configuration = ModelDeploymentConfiguration.from_dict(d.pop("configuration"))

        creation_timestamp = isoparse(d.pop("creationTimestamp"))

        creator_info = CreatorInfo.from_dict(d.pop("creatorInfo"))

        deployment_target_info = DeploymentTargetInfo.from_dict(d.pop("deploymentTargetInfo"))

        description = d.pop("description")

        id = d.pop("id")

        is_globally_accessible = d.pop("isGloballyAccessible")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = ModelDetail.from_dict(models_item_data)

            models.append(models_item)

        name = d.pop("name")

        resource_configuration_info = ResourceConfigurationInfo.from_dict(d.pop("resourceConfigurationInfo"))

        version = d.pop("version")

        _remote_update_timestamp = d.pop("remoteUpdateTimestamp", UNSET)
        remote_update_timestamp: datetime.datetime | Unset
        if isinstance(_remote_update_timestamp, Unset):
            remote_update_timestamp = UNSET
        else:
            remote_update_timestamp = isoparse(_remote_update_timestamp)

        _status = d.pop("status", UNSET)
        status: ModelDeploymentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ModelDeploymentStatus.from_dict(_status)

        model_deployment = cls(
            collaborators=collaborators,
            configuration=configuration,
            creation_timestamp=creation_timestamp,
            creator_info=creator_info,
            deployment_target_info=deployment_target_info,
            description=description,
            id=id,
            is_globally_accessible=is_globally_accessible,
            models=models,
            name=name,
            resource_configuration_info=resource_configuration_info,
            version=version,
            remote_update_timestamp=remote_update_timestamp,
            status=status,
        )

        model_deployment.additional_properties = d
        return model_deployment

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
