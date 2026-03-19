from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.new_async_prediction_v1_parameters import NewAsyncPredictionV1Parameters


T = TypeVar("T", bound="NewAsyncPredictionV1")


@_attrs_define
class NewAsyncPredictionV1:
    """
    Attributes:
        parameters (NewAsyncPredictionV1Parameters): Parameters that will be passed to Async Model predict function
    """

    parameters: NewAsyncPredictionV1Parameters
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameters": parameters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_async_prediction_v1_parameters import NewAsyncPredictionV1Parameters

        d = dict(src_dict)
        parameters = NewAsyncPredictionV1Parameters.from_dict(d.pop("parameters"))

        new_async_prediction_v1 = cls(
            parameters=parameters,
        )

        new_async_prediction_v1.additional_properties = d
        return new_async_prediction_v1

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
