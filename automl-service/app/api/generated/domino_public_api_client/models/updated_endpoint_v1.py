from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_config_v1 import ModelConfigV1


T = TypeVar("T", bound="UpdatedEndpointV1")


@_attrs_define
class UpdatedEndpointV1:
    """
    Attributes:
        endpoint_name (str | Unset): Valid name of the endpoint Example: completions-1.
        endpoint_type (str | Unset): Type of the endpoint Example: llm/v1/completions.
        model_config (ModelConfigV1 | Unset): Configuration for the model Example: {'openai_api_key':
            '58utu49034093nc9cc9n'}.
        model_name (str | Unset): Name of the model Example: gpt-3.5.
        model_provider (str | Unset): Provider of the model Example: openai.
    """

    endpoint_name: str | Unset = UNSET
    endpoint_type: str | Unset = UNSET
    model_config: ModelConfigV1 | Unset = UNSET
    model_name: str | Unset = UNSET
    model_provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoint_name = self.endpoint_name

        endpoint_type = self.endpoint_type

        model_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_config, Unset):
            model_config = self.model_config.to_dict()

        model_name = self.model_name

        model_provider = self.model_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoint_name is not UNSET:
            field_dict["endpointName"] = endpoint_name
        if endpoint_type is not UNSET:
            field_dict["endpointType"] = endpoint_type
        if model_config is not UNSET:
            field_dict["modelConfig"] = model_config
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if model_provider is not UNSET:
            field_dict["modelProvider"] = model_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_config_v1 import ModelConfigV1

        d = dict(src_dict)
        endpoint_name = d.pop("endpointName", UNSET)

        endpoint_type = d.pop("endpointType", UNSET)

        _model_config = d.pop("modelConfig", UNSET)
        model_config: ModelConfigV1 | Unset
        if isinstance(_model_config, Unset):
            model_config = UNSET
        else:
            model_config = ModelConfigV1.from_dict(_model_config)

        model_name = d.pop("modelName", UNSET)

        model_provider = d.pop("modelProvider", UNSET)

        updated_endpoint_v1 = cls(
            endpoint_name=endpoint_name,
            endpoint_type=endpoint_type,
            model_config=model_config,
            model_name=model_name,
            model_provider=model_provider,
        )

        updated_endpoint_v1.additional_properties = d
        return updated_endpoint_v1

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
