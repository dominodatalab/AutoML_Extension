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
    from ..models.model_endpoint_environment_update_v1 import ModelEndpointEnvironmentUpdateV1
    from ..models.model_endpoint_model_source_v1 import ModelEndpointModelSourceV1


T = TypeVar("T", bound="ModelEndpointVersionPatchV1")


@_attrs_define
class ModelEndpointVersionPatchV1:
    """
    Attributes:
        collaborators (list[ModelEndpointCollaboratorV1] | Unset):
        configuration (ModelEndpointConfigurationV1 | Unset):
        description (str | Unset): The description of the endpoint Example: My Endpoint Description.
        environment (ModelEndpointEnvironmentUpdateV1 | Unset):
        general_access (ModelEndpointGeneralAccessV1 | Unset):
        hardware_tier_id (str | Unset): The hardware tier ID of the endpoint Example: 62313ce67a0af0281c01a6a5.
        instructions (str | Unset): The instructions for using the endpoint Example: Use the endpoint to generate text.
        model_source (ModelEndpointModelSourceV1 | Unset):
        name (str | Unset): The name of the endpoint Example: My Endpoint.
        vanity_url (str | Unset): The vanity URL of the endpoint Example: my-endpoint-url.
        version_description (str | Unset): The description of the initial version of the endpoint Example: My Endpoint
            Version Description.
        version_label (str | Unset): The label of the initial version of the endpoint Example: 1.0.
    """

    collaborators: list[ModelEndpointCollaboratorV1] | Unset = UNSET
    configuration: ModelEndpointConfigurationV1 | Unset = UNSET
    description: str | Unset = UNSET
    environment: ModelEndpointEnvironmentUpdateV1 | Unset = UNSET
    general_access: ModelEndpointGeneralAccessV1 | Unset = UNSET
    hardware_tier_id: str | Unset = UNSET
    instructions: str | Unset = UNSET
    model_source: ModelEndpointModelSourceV1 | Unset = UNSET
    name: str | Unset = UNSET
    vanity_url: str | Unset = UNSET
    version_description: str | Unset = UNSET
    version_label: str | Unset = UNSET
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

        description = self.description

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        general_access: str | Unset = UNSET
        if not isinstance(self.general_access, Unset):
            general_access = self.general_access.value

        hardware_tier_id = self.hardware_tier_id

        instructions = self.instructions

        model_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_source, Unset):
            model_source = self.model_source.to_dict()

        name = self.name

        vanity_url = self.vanity_url

        version_description = self.version_description

        version_label = self.version_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if description is not UNSET:
            field_dict["description"] = description
        if environment is not UNSET:
            field_dict["environment"] = environment
        if general_access is not UNSET:
            field_dict["generalAccess"] = general_access
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if model_source is not UNSET:
            field_dict["modelSource"] = model_source
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.model_endpoint_environment_update_v1 import ModelEndpointEnvironmentUpdateV1
        from ..models.model_endpoint_model_source_v1 import ModelEndpointModelSourceV1

        d = dict(src_dict)
        _collaborators = d.pop("collaborators", UNSET)
        collaborators: list[ModelEndpointCollaboratorV1] | Unset = UNSET
        if _collaborators is not UNSET:
            collaborators = []
            for collaborators_item_data in _collaborators:
                collaborators_item = ModelEndpointCollaboratorV1.from_dict(collaborators_item_data)

                collaborators.append(collaborators_item)

        _configuration = d.pop("configuration", UNSET)
        configuration: ModelEndpointConfigurationV1 | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = ModelEndpointConfigurationV1.from_dict(_configuration)

        description = d.pop("description", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: ModelEndpointEnvironmentUpdateV1 | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = ModelEndpointEnvironmentUpdateV1.from_dict(_environment)

        _general_access = d.pop("generalAccess", UNSET)
        general_access: ModelEndpointGeneralAccessV1 | Unset
        if isinstance(_general_access, Unset):
            general_access = UNSET
        else:
            general_access = ModelEndpointGeneralAccessV1(_general_access)

        hardware_tier_id = d.pop("hardwareTierId", UNSET)

        instructions = d.pop("instructions", UNSET)

        _model_source = d.pop("modelSource", UNSET)
        model_source: ModelEndpointModelSourceV1 | Unset
        if isinstance(_model_source, Unset):
            model_source = UNSET
        else:
            model_source = ModelEndpointModelSourceV1.from_dict(_model_source)

        name = d.pop("name", UNSET)

        vanity_url = d.pop("vanityUrl", UNSET)

        version_description = d.pop("versionDescription", UNSET)

        version_label = d.pop("versionLabel", UNSET)

        model_endpoint_version_patch_v1 = cls(
            collaborators=collaborators,
            configuration=configuration,
            description=description,
            environment=environment,
            general_access=general_access,
            hardware_tier_id=hardware_tier_id,
            instructions=instructions,
            model_source=model_source,
            name=name,
            vanity_url=vanity_url,
            version_description=version_description,
            version_label=version_label,
        )

        model_endpoint_version_patch_v1.additional_properties = d
        return model_endpoint_version_patch_v1

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
