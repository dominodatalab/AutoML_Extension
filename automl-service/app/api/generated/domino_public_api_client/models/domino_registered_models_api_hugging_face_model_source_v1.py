from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoRegisteredModelsApiHuggingFaceModelSourceV1")


@_attrs_define
class DominoRegisteredModelsApiHuggingFaceModelSourceV1:
    """
    Attributes:
        model_id (str): Hugging Face model ID Example: microsoft/DialoGPT-medium.
        hugging_face_token (str | Unset): Optional Hugging Face token for private models Example:
            hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
        model_revision (str | Unset): Optional model revision Example: fe8a4ea1ffedaf415f4da2f062534de366a451e6.
    """

    model_id: str
    hugging_face_token: str | Unset = UNSET
    model_revision: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        hugging_face_token = self.hugging_face_token

        model_revision = self.model_revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
            }
        )
        if hugging_face_token is not UNSET:
            field_dict["huggingFaceToken"] = hugging_face_token
        if model_revision is not UNSET:
            field_dict["modelRevision"] = model_revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_id = d.pop("modelId")

        hugging_face_token = d.pop("huggingFaceToken", UNSET)

        model_revision = d.pop("modelRevision", UNSET)

        domino_registered_models_api_hugging_face_model_source_v1 = cls(
            model_id=model_id,
            hugging_face_token=hugging_face_token,
            model_revision=model_revision,
        )

        domino_registered_models_api_hugging_face_model_source_v1.additional_properties = d
        return domino_registered_models_api_hugging_face_model_source_v1

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
