from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_endpoint_hugging_face_model_source_v1 import ModelEndpointHuggingFaceModelSourceV1
    from ..models.model_endpoint_registered_model_source_v1 import ModelEndpointRegisteredModelSourceV1


T = TypeVar("T", bound="NewModelEndpointModelSourceV1")


@_attrs_define
class NewModelEndpointModelSourceV1:
    """
    Attributes:
        hugging_face (ModelEndpointHuggingFaceModelSourceV1 | Unset):
        registered_model (ModelEndpointRegisteredModelSourceV1 | Unset):
    """

    hugging_face: ModelEndpointHuggingFaceModelSourceV1 | Unset = UNSET
    registered_model: ModelEndpointRegisteredModelSourceV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hugging_face: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hugging_face, Unset):
            hugging_face = self.hugging_face.to_dict()

        registered_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registered_model, Unset):
            registered_model = self.registered_model.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hugging_face is not UNSET:
            field_dict["huggingFace"] = hugging_face
        if registered_model is not UNSET:
            field_dict["registeredModel"] = registered_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_endpoint_hugging_face_model_source_v1 import ModelEndpointHuggingFaceModelSourceV1
        from ..models.model_endpoint_registered_model_source_v1 import ModelEndpointRegisteredModelSourceV1

        d = dict(src_dict)
        _hugging_face = d.pop("huggingFace", UNSET)
        hugging_face: ModelEndpointHuggingFaceModelSourceV1 | Unset
        if isinstance(_hugging_face, Unset):
            hugging_face = UNSET
        else:
            hugging_face = ModelEndpointHuggingFaceModelSourceV1.from_dict(_hugging_face)

        _registered_model = d.pop("registeredModel", UNSET)
        registered_model: ModelEndpointRegisteredModelSourceV1 | Unset
        if isinstance(_registered_model, Unset):
            registered_model = UNSET
        else:
            registered_model = ModelEndpointRegisteredModelSourceV1.from_dict(_registered_model)

        new_model_endpoint_model_source_v1 = cls(
            hugging_face=hugging_face,
            registered_model=registered_model,
        )

        new_model_endpoint_model_source_v1.additional_properties = d
        return new_model_endpoint_model_source_v1

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
