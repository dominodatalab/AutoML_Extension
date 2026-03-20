from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.model_config_v1 import ModelConfigV1


T = TypeVar("T", bound="EndpointEnvelopeV1")


@_attrs_define
class EndpointEnvelopeV1:
    """
    Attributes:
        creation_date (datetime.datetime): ISO 8601 formatted time of when the Endpoint was created Example:
            2022-04-23T18:25:43.511Z.
        endpoint_id (str): ID of the endpoint Example: 62604702b7e5d347dbe7a909.
        endpoint_name (str): Valid name of the endpoint Example: completions.
        endpoint_type (str): Type of the endpoint Example: llm/v1/completions.
        model_config (ModelConfigV1): Configuration for the model Example: {'openai_api_key': '58utu49034093nc9cc9n'}.
        model_name (str): Name of the model Example: gpt-4.
        model_provider (str): Provider of the model Example: openai.
    """

    creation_date: datetime.datetime
    endpoint_id: str
    endpoint_name: str
    endpoint_type: str
    model_config: ModelConfigV1
    model_name: str
    model_provider: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creation_date = self.creation_date.isoformat()

        endpoint_id = self.endpoint_id

        endpoint_name = self.endpoint_name

        endpoint_type = self.endpoint_type

        model_config = self.model_config.to_dict()

        model_name = self.model_name

        model_provider = self.model_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creationDate": creation_date,
                "endpointId": endpoint_id,
                "endpointName": endpoint_name,
                "endpointType": endpoint_type,
                "modelConfig": model_config,
                "modelName": model_name,
                "modelProvider": model_provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_config_v1 import ModelConfigV1

        d = dict(src_dict)
        creation_date = isoparse(d.pop("creationDate"))

        endpoint_id = d.pop("endpointId")

        endpoint_name = d.pop("endpointName")

        endpoint_type = d.pop("endpointType")

        model_config = ModelConfigV1.from_dict(d.pop("modelConfig"))

        model_name = d.pop("modelName")

        model_provider = d.pop("modelProvider")

        endpoint_envelope_v1 = cls(
            creation_date=creation_date,
            endpoint_id=endpoint_id,
            endpoint_name=endpoint_name,
            endpoint_type=endpoint_type,
            model_config=model_config,
            model_name=model_name,
            model_provider=model_provider,
        )

        endpoint_envelope_v1.additional_properties = d
        return endpoint_envelope_v1

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
