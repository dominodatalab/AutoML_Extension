from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_registered_models_api_model_source_v1 import DominoRegisteredModelsApiModelSourceV1


T = TypeVar("T", bound="NewRegisteredModelV2")


@_attrs_define
class NewRegisteredModelV2:
    """
    Attributes:
        create (bool): Indicates whether to create or update the registered model.
        model_name (str): The name of the registered model Example: churn-prediction-model.
        model_source (DominoRegisteredModelsApiModelSourceV1):
        description (str | Unset): Optional description of the registered model Example: Customer churn prediction model
            trained on historical data.
        discoverable (bool | Unset): Indicates whether this model is publicly discoverable. If true, users who are not
            project members will see this model in search results and can view basic model details.
             Default: False.
        model_category (str | Unset): Category of the model (e.g., "genai", "ml"). Example: genai.
        model_type (str | Unset): Type of the model (e.g., "llm", "embedding", "other-genai", "ml"). Example: llm.
        project_id (str | Unset): Project ID of the registered model. Required for Hugging Face models only. For MLflow
            models, this is ignored as the project is determined from the experiment run id.
    """

    create: bool
    model_name: str
    model_source: DominoRegisteredModelsApiModelSourceV1
    description: str | Unset = UNSET
    discoverable: bool | Unset = False
    model_category: str | Unset = UNSET
    model_type: str | Unset = UNSET
    project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create = self.create

        model_name = self.model_name

        model_source = self.model_source.to_dict()

        description = self.description

        discoverable = self.discoverable

        model_category = self.model_category

        model_type = self.model_type

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create": create,
                "modelName": model_name,
                "modelSource": model_source,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if discoverable is not UNSET:
            field_dict["discoverable"] = discoverable
        if model_category is not UNSET:
            field_dict["modelCategory"] = model_category
        if model_type is not UNSET:
            field_dict["modelType"] = model_type
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_registered_models_api_model_source_v1 import DominoRegisteredModelsApiModelSourceV1

        d = dict(src_dict)
        create = d.pop("create")

        model_name = d.pop("modelName")

        model_source = DominoRegisteredModelsApiModelSourceV1.from_dict(d.pop("modelSource"))

        description = d.pop("description", UNSET)

        discoverable = d.pop("discoverable", UNSET)

        model_category = d.pop("modelCategory", UNSET)

        model_type = d.pop("modelType", UNSET)

        project_id = d.pop("projectId", UNSET)

        new_registered_model_v2 = cls(
            create=create,
            model_name=model_name,
            model_source=model_source,
            description=description,
            discoverable=discoverable,
            model_category=model_category,
            model_type=model_type,
            project_id=project_id,
        )

        new_registered_model_v2.additional_properties = d
        return new_registered_model_v2

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
