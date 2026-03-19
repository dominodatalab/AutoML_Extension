from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AsyncPredictionRequestEnvelopeV1")


@_attrs_define
class AsyncPredictionRequestEnvelopeV1:
    """
    Attributes:
        async_prediction_id (str): Id of the created Async Prediction
    """

    async_prediction_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        async_prediction_id = self.async_prediction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asyncPredictionId": async_prediction_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        async_prediction_id = d.pop("asyncPredictionId")

        async_prediction_request_envelope_v1 = cls(
            async_prediction_id=async_prediction_id,
        )

        async_prediction_request_envelope_v1.additional_properties = d
        return async_prediction_request_envelope_v1

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
