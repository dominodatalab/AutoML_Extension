from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_api_access_configuration import ModelApiAccessConfiguration
    from ..models.model_api_collaborator_role import ModelApiCollaboratorRole
    from ..models.model_api_health_check_configuration import ModelApiHealthCheckConfiguration
    from ..models.model_api_metadata import ModelApiMetadata
    from ..models.model_api_version_summary import ModelApiVersionSummary
    from ..models.model_api_volume import ModelApiVolume


T = TypeVar("T", bound="ModelApi")


@_attrs_define
class ModelApi:
    """
    Attributes:
        access (ModelApiAccessConfiguration):
        collaborators (list[ModelApiCollaboratorRole]): The collaborators of the Model API.
        description (str): The description of the Model API.
        environment_id (str): The id of the environment the Model API is deployed to.
        health_check (ModelApiHealthCheckConfiguration):
        id (str): The id of the Model API.
        is_archived (bool): Whether the Model API is archived.
        is_async (bool): Whether the Model API is async.
        metadata (ModelApiMetadata):
        name (str): The name of the Model API.
        replicas (int): The number of replicas of the Model API.
        routing_mode (str): The routing mode of the Model API.
        strict_node_anti_affinity (bool): Whether the Model API has strict node anti affinity.
        volumes (list[ModelApiVolume]): The volumes of the Model API.
        active_version (ModelApiVersionSummary | Unset):
        bundle_id (None | str | Unset): The ID of the bundle governing the model API to create.
        hardware_tier_id (None | str | Unset): The id of the hardware tier the Model API is deployed with.
        override_request_timeout_secs (int | None | Unset): The request timeout configuration of the Model API.
        resource_quota_id (None | str | Unset): The id of the resource quota the Model API is deployed with.
    """

    access: ModelApiAccessConfiguration
    collaborators: list[ModelApiCollaboratorRole]
    description: str
    environment_id: str
    health_check: ModelApiHealthCheckConfiguration
    id: str
    is_archived: bool
    is_async: bool
    metadata: ModelApiMetadata
    name: str
    replicas: int
    routing_mode: str
    strict_node_anti_affinity: bool
    volumes: list[ModelApiVolume]
    active_version: ModelApiVersionSummary | Unset = UNSET
    bundle_id: None | str | Unset = UNSET
    hardware_tier_id: None | str | Unset = UNSET
    override_request_timeout_secs: int | None | Unset = UNSET
    resource_quota_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access.to_dict()

        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        description = self.description

        environment_id = self.environment_id

        health_check = self.health_check.to_dict()

        id = self.id

        is_archived = self.is_archived

        is_async = self.is_async

        metadata = self.metadata.to_dict()

        name = self.name

        replicas = self.replicas

        routing_mode = self.routing_mode

        strict_node_anti_affinity = self.strict_node_anti_affinity

        volumes = []
        for volumes_item_data in self.volumes:
            volumes_item = volumes_item_data.to_dict()
            volumes.append(volumes_item)

        active_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.active_version, Unset):
            active_version = self.active_version.to_dict()

        bundle_id: None | str | Unset
        if isinstance(self.bundle_id, Unset):
            bundle_id = UNSET
        else:
            bundle_id = self.bundle_id

        hardware_tier_id: None | str | Unset
        if isinstance(self.hardware_tier_id, Unset):
            hardware_tier_id = UNSET
        else:
            hardware_tier_id = self.hardware_tier_id

        override_request_timeout_secs: int | None | Unset
        if isinstance(self.override_request_timeout_secs, Unset):
            override_request_timeout_secs = UNSET
        else:
            override_request_timeout_secs = self.override_request_timeout_secs

        resource_quota_id: None | str | Unset
        if isinstance(self.resource_quota_id, Unset):
            resource_quota_id = UNSET
        else:
            resource_quota_id = self.resource_quota_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "collaborators": collaborators,
                "description": description,
                "environmentId": environment_id,
                "healthCheck": health_check,
                "id": id,
                "isArchived": is_archived,
                "isAsync": is_async,
                "metadata": metadata,
                "name": name,
                "replicas": replicas,
                "routingMode": routing_mode,
                "strictNodeAntiAffinity": strict_node_anti_affinity,
                "volumes": volumes,
            }
        )
        if active_version is not UNSET:
            field_dict["activeVersion"] = active_version
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id
        if override_request_timeout_secs is not UNSET:
            field_dict["overrideRequestTimeoutSecs"] = override_request_timeout_secs
        if resource_quota_id is not UNSET:
            field_dict["resourceQuotaId"] = resource_quota_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_api_access_configuration import ModelApiAccessConfiguration
        from ..models.model_api_collaborator_role import ModelApiCollaboratorRole
        from ..models.model_api_health_check_configuration import ModelApiHealthCheckConfiguration
        from ..models.model_api_metadata import ModelApiMetadata
        from ..models.model_api_version_summary import ModelApiVersionSummary
        from ..models.model_api_volume import ModelApiVolume

        d = dict(src_dict)
        access = ModelApiAccessConfiguration.from_dict(d.pop("access"))

        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = ModelApiCollaboratorRole.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        description = d.pop("description")

        environment_id = d.pop("environmentId")

        health_check = ModelApiHealthCheckConfiguration.from_dict(d.pop("healthCheck"))

        id = d.pop("id")

        is_archived = d.pop("isArchived")

        is_async = d.pop("isAsync")

        metadata = ModelApiMetadata.from_dict(d.pop("metadata"))

        name = d.pop("name")

        replicas = d.pop("replicas")

        routing_mode = d.pop("routingMode")

        strict_node_anti_affinity = d.pop("strictNodeAntiAffinity")

        volumes = []
        _volumes = d.pop("volumes")
        for volumes_item_data in _volumes:
            volumes_item = ModelApiVolume.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        _active_version = d.pop("activeVersion", UNSET)
        active_version: ModelApiVersionSummary | Unset
        if isinstance(_active_version, Unset):
            active_version = UNSET
        else:
            active_version = ModelApiVersionSummary.from_dict(_active_version)

        def _parse_bundle_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bundle_id = _parse_bundle_id(d.pop("bundleId", UNSET))

        def _parse_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hardware_tier_id = _parse_hardware_tier_id(d.pop("hardwareTierId", UNSET))

        def _parse_override_request_timeout_secs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        override_request_timeout_secs = _parse_override_request_timeout_secs(d.pop("overrideRequestTimeoutSecs", UNSET))

        def _parse_resource_quota_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_quota_id = _parse_resource_quota_id(d.pop("resourceQuotaId", UNSET))

        model_api = cls(
            access=access,
            collaborators=collaborators,
            description=description,
            environment_id=environment_id,
            health_check=health_check,
            id=id,
            is_archived=is_archived,
            is_async=is_async,
            metadata=metadata,
            name=name,
            replicas=replicas,
            routing_mode=routing_mode,
            strict_node_anti_affinity=strict_node_anti_affinity,
            volumes=volumes,
            active_version=active_version,
            bundle_id=bundle_id,
            hardware_tier_id=hardware_tier_id,
            override_request_timeout_secs=override_request_timeout_secs,
            resource_quota_id=resource_quota_id,
        )

        model_api.additional_properties = d
        return model_api

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
