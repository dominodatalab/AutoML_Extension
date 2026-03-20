from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_registered_models_api_model_source_v1_source_type import (
    DominoRegisteredModelsApiModelSourceV1SourceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_registered_models_api_hugging_face_model_source_v1 import (
        DominoRegisteredModelsApiHuggingFaceModelSourceV1,
    )
    from ..models.domino_registered_models_api_mlflow_model_source_v1 import (
        DominoRegisteredModelsApiMlflowModelSourceV1,
    )


T = TypeVar("T", bound="DominoRegisteredModelsApiModelSourceV1")


@_attrs_define
class DominoRegisteredModelsApiModelSourceV1:
    """
    Attributes:
        source_type (DominoRegisteredModelsApiModelSourceV1SourceType): Type of model source Example: huggingface.
        hugging_face_source (DominoRegisteredModelsApiHuggingFaceModelSourceV1 | Unset):
        mlflow_source (DominoRegisteredModelsApiMlflowModelSourceV1 | Unset):
    """

    source_type: DominoRegisteredModelsApiModelSourceV1SourceType
    hugging_face_source: DominoRegisteredModelsApiHuggingFaceModelSourceV1 | Unset = UNSET
    mlflow_source: DominoRegisteredModelsApiMlflowModelSourceV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type.value

        hugging_face_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hugging_face_source, Unset):
            hugging_face_source = self.hugging_face_source.to_dict()

        mlflow_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlflow_source, Unset):
            mlflow_source = self.mlflow_source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceType": source_type,
            }
        )
        if hugging_face_source is not UNSET:
            field_dict["huggingFaceSource"] = hugging_face_source
        if mlflow_source is not UNSET:
            field_dict["mlflowSource"] = mlflow_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_registered_models_api_hugging_face_model_source_v1 import (
            DominoRegisteredModelsApiHuggingFaceModelSourceV1,
        )
        from ..models.domino_registered_models_api_mlflow_model_source_v1 import (
            DominoRegisteredModelsApiMlflowModelSourceV1,
        )

        d = dict(src_dict)
        source_type = DominoRegisteredModelsApiModelSourceV1SourceType(d.pop("sourceType"))

        _hugging_face_source = d.pop("huggingFaceSource", UNSET)
        hugging_face_source: DominoRegisteredModelsApiHuggingFaceModelSourceV1 | Unset
        if isinstance(_hugging_face_source, Unset):
            hugging_face_source = UNSET
        else:
            hugging_face_source = DominoRegisteredModelsApiHuggingFaceModelSourceV1.from_dict(_hugging_face_source)

        _mlflow_source = d.pop("mlflowSource", UNSET)
        mlflow_source: DominoRegisteredModelsApiMlflowModelSourceV1 | Unset
        if isinstance(_mlflow_source, Unset):
            mlflow_source = UNSET
        else:
            mlflow_source = DominoRegisteredModelsApiMlflowModelSourceV1.from_dict(_mlflow_source)

        domino_registered_models_api_model_source_v1 = cls(
            source_type=source_type,
            hugging_face_source=hugging_face_source,
            mlflow_source=mlflow_source,
        )

        domino_registered_models_api_model_source_v1.additional_properties = d
        return domino_registered_models_api_model_source_v1

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
