from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.endpoint_permissions_dto_v1 import EndpointPermissionsDtoV1
    from ..models.model_config_v1 import ModelConfigV1


T = TypeVar("T", bound="NewEndpointV1")


@_attrs_define
class NewEndpointV1:
    """
    Attributes:
        endpoint_name (str): Valid name of the endpoint Example: completions.
        endpoint_permissions (EndpointPermissionsDtoV1):
        endpoint_type (str): Type of the endpoint Example: llm/v1/completions.
        model_config (ModelConfigV1): Configuration for the model Example: {'openai_api_key': '58utu49034093nc9cc9n'}.
        model_name (str): Name of the model Example: gpt-4.
        model_provider (str): Provider of the model Example: openai.
    """

    endpoint_name: str
    endpoint_permissions: EndpointPermissionsDtoV1
    endpoint_type: str
    model_config: ModelConfigV1
    model_name: str
    model_provider: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_name = self.endpoint_name

        endpoint_permissions = self.endpoint_permissions.to_dict()

        endpoint_type = self.endpoint_type

        model_config = self.model_config.to_dict()

        model_name = self.model_name

        model_provider = self.model_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpointName": endpoint_name,
                "endpointPermissions": endpoint_permissions,
                "endpointType": endpoint_type,
                "modelConfig": model_config,
                "modelName": model_name,
                "modelProvider": model_provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_permissions_dto_v1 import EndpointPermissionsDtoV1
        from ..models.model_config_v1 import ModelConfigV1

        d = dict(src_dict)
        endpoint_name = d.pop("endpointName")

        endpoint_permissions = EndpointPermissionsDtoV1.from_dict(d.pop("endpointPermissions"))

        endpoint_type = d.pop("endpointType")

        model_config = ModelConfigV1.from_dict(d.pop("modelConfig"))

        model_name = d.pop("modelName")

        model_provider = d.pop("modelProvider")

        new_endpoint_v1 = cls(
            endpoint_name=endpoint_name,
            endpoint_permissions=endpoint_permissions,
            endpoint_type=endpoint_type,
            model_config=model_config,
            model_name=model_name,
            model_provider=model_provider,
        )

        new_endpoint_v1.additional_properties = d
        return new_endpoint_v1

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
