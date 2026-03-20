from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelApiUpdateRequest")


@_attrs_define
class ModelApiUpdateRequest:
    """
    Attributes:
        description (str): The new description for the Model API.
        environment_id (str): The id of the new environment to deploy the Model API with.
        name (str): The new name for the Model API.
        replicas (int): The new number of replicas of the Model API.
        hardware_tier_id (None | str | Unset): The id of the new hardware tier to deploy the Model API with.
        resource_quota_id (None | str | Unset): The id of the new resource quota to deploy the Model API with.
    """

    description: str
    environment_id: str
    name: str
    replicas: int
    hardware_tier_id: None | str | Unset = UNSET
    resource_quota_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        environment_id = self.environment_id

        name = self.name

        replicas = self.replicas

        hardware_tier_id: None | str | Unset
        if isinstance(self.hardware_tier_id, Unset):
            hardware_tier_id = UNSET
        else:
            hardware_tier_id = self.hardware_tier_id

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
                "name": name,
                "replicas": replicas,
            }
        )
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id
        if resource_quota_id is not UNSET:
            field_dict["resourceQuotaId"] = resource_quota_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        environment_id = d.pop("environmentId")

        name = d.pop("name")

        replicas = d.pop("replicas")

        def _parse_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hardware_tier_id = _parse_hardware_tier_id(d.pop("hardwareTierId", UNSET))

        def _parse_resource_quota_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_quota_id = _parse_resource_quota_id(d.pop("resourceQuotaId", UNSET))

        model_api_update_request = cls(
            description=description,
            environment_id=environment_id,
            name=name,
            replicas=replicas,
            hardware_tier_id=hardware_tier_id,
            resource_quota_id=resource_quota_id,
        )

        model_api_update_request.additional_properties = d
        return model_api_update_request

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
