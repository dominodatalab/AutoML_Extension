from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_detail_source_registered_model_type import ModelDetailSourceRegisteredModelType

T = TypeVar("T", bound="ModelDetailSource")


@_attrs_define
class ModelDetailSource:
    """Model Deployment Model Detail Source

    Attributes:
        registered_model_name (str): The name of the registered model served by this source. Example: Growth Forecasting
            Model.
        registered_model_type (ModelDetailSourceRegisteredModelType): The type of this model source. Example:
            MODELREGISTRY.
        registered_model_version (int): The version of the registered model served by this source. Example: 3.
    """

    registered_model_name: str
    registered_model_type: ModelDetailSourceRegisteredModelType
    registered_model_version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registered_model_name = self.registered_model_name

        registered_model_type = self.registered_model_type.value

        registered_model_version = self.registered_model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registeredModelName": registered_model_name,
                "registeredModelType": registered_model_type,
                "registeredModelVersion": registered_model_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        registered_model_name = d.pop("registeredModelName")

        registered_model_type = ModelDetailSourceRegisteredModelType(d.pop("registeredModelType"))

        registered_model_version = d.pop("registeredModelVersion")

        model_detail_source = cls(
            registered_model_name=registered_model_name,
            registered_model_type=registered_model_type,
            registered_model_version=registered_model_version,
        )

        model_detail_source.additional_properties = d
        return model_detail_source

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
