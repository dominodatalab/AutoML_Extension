from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_modelmanager_api_model import DominoModelmanagerApiModel
    from ..models.domino_modelmanager_api_models_for_ui_api_response_model_access import (
        DominoModelmanagerApiModelsForUIApiResponseModelAccess,
    )


T = TypeVar("T", bound="DominoModelmanagerApiModelsForUIApiResponse")


@_attrs_define
class DominoModelmanagerApiModelsForUIApiResponse:
    """
    Attributes:
        current_item_count (int):
        start_index (int):
        items_per_page (int):
        total_items (int):
        models (list[DominoModelmanagerApiModel]):
        model_access (DominoModelmanagerApiModelsForUIApiResponseModelAccess):
    """

    current_item_count: int
    start_index: int
    items_per_page: int
    total_items: int
    models: list[DominoModelmanagerApiModel]
    model_access: DominoModelmanagerApiModelsForUIApiResponseModelAccess
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_item_count = self.current_item_count

        start_index = self.start_index

        items_per_page = self.items_per_page

        total_items = self.total_items

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        model_access = self.model_access.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentItemCount": current_item_count,
                "startIndex": start_index,
                "itemsPerPage": items_per_page,
                "totalItems": total_items,
                "models": models,
                "modelAccess": model_access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_modelmanager_api_model import DominoModelmanagerApiModel
        from ..models.domino_modelmanager_api_models_for_ui_api_response_model_access import (
            DominoModelmanagerApiModelsForUIApiResponseModelAccess,
        )

        d = dict(src_dict)
        current_item_count = d.pop("currentItemCount")

        start_index = d.pop("startIndex")

        items_per_page = d.pop("itemsPerPage")

        total_items = d.pop("totalItems")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = DominoModelmanagerApiModel.from_dict(models_item_data)

            models.append(models_item)

        model_access = DominoModelmanagerApiModelsForUIApiResponseModelAccess.from_dict(d.pop("modelAccess"))

        domino_modelmanager_api_models_for_ui_api_response = cls(
            current_item_count=current_item_count,
            start_index=start_index,
            items_per_page=items_per_page,
            total_items=total_items,
            models=models,
            model_access=model_access,
        )

        domino_modelmanager_api_models_for_ui_api_response.additional_properties = d
        return domino_modelmanager_api_models_for_ui_api_response

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
