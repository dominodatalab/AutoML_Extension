from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_endpoint_general_access_v1 import ModelEndpointGeneralAccessV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_endpoint_collaborator_v1 import ModelEndpointCollaboratorV1
    from ..models.model_endpoint_configuration_v1 import ModelEndpointConfigurationV1
    from ..models.model_endpoint_model_source_v1 import ModelEndpointModelSourceV1
    from ..models.new_model_endpoint_environment_info_v1 import NewModelEndpointEnvironmentInfoV1


T = TypeVar("T", bound="NewModelEndpointV1")


@_attrs_define
class NewModelEndpointV1:
    """
    Attributes:
        collaborators (list[ModelEndpointCollaboratorV1]):
        configuration (ModelEndpointConfigurationV1):
        environment (NewModelEndpointEnvironmentInfoV1):
        general_access (ModelEndpointGeneralAccessV1):
        hardware_tier_id (str): The hardware tier ID of the endpoint Example: 62313ce67a0af0281c01a6a5.
        model_source (ModelEndpointModelSourceV1):
        name (str): The name of the endpoint Example: My Endpoint.
        project_id (str): The project ID of the endpoint Example: 62313ce67a0af0281c01a6a5.
        description (str | Unset): The description of the endpoint Example: My Endpoint Description.
        vanity_url (str | Unset): The optional Vanity url for the Gen AI Endpoint. This will default to https://{domino-
            instance}/endpoints/{endpointName} Example: https://cloud-dogfood.domino.tech/endpoints/my-endpoint.
        version_description (str | Unset): The description of the initial version of the endpoint Example: My Endpoint
            Version Description.
        version_label (str | Unset): The label of the initial version of the endpoint Example: 1.0.
    """

    collaborators: list[ModelEndpointCollaboratorV1]
    configuration: ModelEndpointConfigurationV1
    environment: NewModelEndpointEnvironmentInfoV1
    general_access: ModelEndpointGeneralAccessV1
    hardware_tier_id: str
    model_source: ModelEndpointModelSourceV1
    name: str
    project_id: str
    description: str | Unset = UNSET
    vanity_url: str | Unset = UNSET
    version_description: str | Unset = UNSET
    version_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        configuration = self.configuration.to_dict()

        environment = self.environment.to_dict()

        general_access = self.general_access.value

        hardware_tier_id = self.hardware_tier_id

        model_source = self.model_source.to_dict()

        name = self.name

        project_id = self.project_id

        description = self.description

        vanity_url = self.vanity_url

        version_description = self.version_description

        version_label = self.version_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collaborators": collaborators,
                "configuration": configuration,
                "environment": environment,
                "generalAccess": general_access,
                "hardwareTierId": hardware_tier_id,
                "modelSource": model_source,
                "name": name,
                "projectId": project_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if vanity_url is not UNSET:
            field_dict["vanityUrl"] = vanity_url
        if version_description is not UNSET:
            field_dict["versionDescription"] = version_description
        if version_label is not UNSET:
            field_dict["versionLabel"] = version_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_endpoint_collaborator_v1 import ModelEndpointCollaboratorV1
        from ..models.model_endpoint_configuration_v1 import ModelEndpointConfigurationV1
        from ..models.model_endpoint_model_source_v1 import ModelEndpointModelSourceV1
        from ..models.new_model_endpoint_environment_info_v1 import NewModelEndpointEnvironmentInfoV1

        d = dict(src_dict)
        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = ModelEndpointCollaboratorV1.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        configuration = ModelEndpointConfigurationV1.from_dict(d.pop("configuration"))

        environment = NewModelEndpointEnvironmentInfoV1.from_dict(d.pop("environment"))

        general_access = ModelEndpointGeneralAccessV1(d.pop("generalAccess"))

        hardware_tier_id = d.pop("hardwareTierId")

        model_source = ModelEndpointModelSourceV1.from_dict(d.pop("modelSource"))

        name = d.pop("name")

        project_id = d.pop("projectId")

        description = d.pop("description", UNSET)

        vanity_url = d.pop("vanityUrl", UNSET)

        version_description = d.pop("versionDescription", UNSET)

        version_label = d.pop("versionLabel", UNSET)

        new_model_endpoint_v1 = cls(
            collaborators=collaborators,
            configuration=configuration,
            environment=environment,
            general_access=general_access,
            hardware_tier_id=hardware_tier_id,
            model_source=model_source,
            name=name,
            project_id=project_id,
            description=description,
            vanity_url=vanity_url,
            version_description=version_description,
            version_label=version_label,
        )

        new_model_endpoint_v1.additional_properties = d
        return new_model_endpoint_v1

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
