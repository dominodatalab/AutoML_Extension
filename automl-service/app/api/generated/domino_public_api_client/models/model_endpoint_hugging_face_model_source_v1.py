from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_endpoint_model_type_v1 import ModelEndpointModelTypeV1
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelEndpointHuggingFaceModelSourceV1")


@_attrs_define
class ModelEndpointHuggingFaceModelSourceV1:
    """
    Attributes:
        commit (str): The commit of the model Example: 62313ce67a0af0281c01a6a5.
        model_type (ModelEndpointModelTypeV1):
        path (str): The path to the model Example: my-model.
        api_token (str | Unset): The API token for the model Example: 62313ce67a0af0281c01a6a5.
    """

    commit: str
    model_type: ModelEndpointModelTypeV1
    path: str
    api_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit = self.commit

        model_type = self.model_type.value

        path = self.path

        api_token = self.api_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commit": commit,
                "modelType": model_type,
                "path": path,
            }
        )
        if api_token is not UNSET:
            field_dict["apiToken"] = api_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commit = d.pop("commit")

        model_type = ModelEndpointModelTypeV1(d.pop("modelType"))

        path = d.pop("path")

        api_token = d.pop("apiToken", UNSET)

        model_endpoint_hugging_face_model_source_v1 = cls(
            commit=commit,
            model_type=model_type,
            path=path,
            api_token=api_token,
        )

        model_endpoint_hugging_face_model_source_v1.additional_properties = d
        return model_endpoint_hugging_face_model_source_v1

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
