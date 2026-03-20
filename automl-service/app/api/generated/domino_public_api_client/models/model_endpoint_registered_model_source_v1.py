from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelEndpointRegisteredModelSourceV1")


@_attrs_define
class ModelEndpointRegisteredModelSourceV1:
    """
    Attributes:
        model_name (str): The name of the Registered Model Example: RandomForestRegression.
        model_version (int): The version of the Registered Model Example: 1.
    """

    model_name: str
    model_version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_name = self.model_name

        model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelName": model_name,
                "modelVersion": model_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_name = d.pop("modelName")

        model_version = d.pop("modelVersion")

        model_endpoint_registered_model_source_v1 = cls(
            model_name=model_name,
            model_version=model_version,
        )

        model_endpoint_registered_model_source_v1.additional_properties = d
        return model_endpoint_registered_model_source_v1

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
