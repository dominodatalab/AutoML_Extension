from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_api_environment_variable import ModelApiEnvironmentVariable
    from ..models.model_api_version_creation_request import ModelApiVersionCreationRequest


T = TypeVar("T", bound="ModelApiCreationRequest")


@_attrs_define
class ModelApiCreationRequest:
    """
    Attributes:
        description (str): The description of the Model API to create.
        environment_id (str): The id of the environment the Model API to create should be deployed to.
        environment_variables (list[ModelApiEnvironmentVariable]): The environment variables of the Model API to create.
        is_async (bool): Whether the Model API to create should be async.
        name (str): The name of the Model API to create.
        strict_node_anti_affinity (bool): Whether the Model API to create should have strict node anti affinity.
        version (ModelApiVersionCreationRequest):
        bundle_id (None | str | Unset): The ID of the bundle governing the model API to create.
        hardware_tier_id (None | str | Unset): The id of the hardware tier the Model API to create should be deployed
            with.
        replicas (int | Unset): The number of replicas of the Model API should be created with.
        resource_quota_id (None | str | Unset): The id of the resource quota the Model API to create should be deployed
            with.
    """

    description: str
    environment_id: str
    environment_variables: list[ModelApiEnvironmentVariable]
    is_async: bool
    name: str
    strict_node_anti_affinity: bool
    version: ModelApiVersionCreationRequest
    bundle_id: None | str | Unset = UNSET
    hardware_tier_id: None | str | Unset = UNSET
    replicas: int | Unset = UNSET
    resource_quota_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        environment_id = self.environment_id

        environment_variables = []
        for environment_variables_item_data in self.environment_variables:
            environment_variables_item = environment_variables_item_data.to_dict()
            environment_variables.append(environment_variables_item)

        is_async = self.is_async

        name = self.name

        strict_node_anti_affinity = self.strict_node_anti_affinity

        version = self.version.to_dict()

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

        replicas = self.replicas

        resource_quota_id: None | str | Unset
        if isinstance(self.resource_quota_id, Unset):
            resource_quota_id = UNSET
        else:
            resource_quota_id = self.resource_quota_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "environmentId": environment_id,
                "environmentVariables": environment_variables,
                "isAsync": is_async,
                "name": name,
                "strictNodeAntiAffinity": strict_node_anti_affinity,
                "version": version,
            }
        )
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id
        if replicas is not UNSET:
            field_dict["replicas"] = replicas
        if resource_quota_id is not UNSET:
            field_dict["resourceQuotaId"] = resource_quota_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_api_environment_variable import ModelApiEnvironmentVariable
        from ..models.model_api_version_creation_request import ModelApiVersionCreationRequest

        d = dict(src_dict)
        description = d.pop("description")

        environment_id = d.pop("environmentId")

        environment_variables = []
        _environment_variables = d.pop("environmentVariables")
        for environment_variables_item_data in _environment_variables:
            environment_variables_item = ModelApiEnvironmentVariable.from_dict(environment_variables_item_data)

            environment_variables.append(environment_variables_item)

        is_async = d.pop("isAsync")

        name = d.pop("name")

        strict_node_anti_affinity = d.pop("strictNodeAntiAffinity")

        version = ModelApiVersionCreationRequest.from_dict(d.pop("version"))

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

        replicas = d.pop("replicas", UNSET)

        def _parse_resource_quota_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_quota_id = _parse_resource_quota_id(d.pop("resourceQuotaId", UNSET))

        model_api_creation_request = cls(
            description=description,
            environment_id=environment_id,
            environment_variables=environment_variables,
            is_async=is_async,
            name=name,
            strict_node_anti_affinity=strict_node_anti_affinity,
            version=version,
            bundle_id=bundle_id,
            hardware_tier_id=hardware_tier_id,
            replicas=replicas,
            resource_quota_id=resource_quota_id,
        )

        model_api_creation_request.additional_properties = d
        return model_api_creation_request

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
