from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_nucleus_modelproduct_models_model_product import DominoNucleusModelproductModelsModelProduct


T = TypeVar("T", bound="DominoNucleusModelproductModelsGrantAccessRequired")


@_attrs_define
class DominoNucleusModelproductModelsGrantAccessRequired:
    """
    Attributes:
        model_product (DominoNucleusModelproductModelsModelProduct):
    """

    model_product: DominoNucleusModelproductModelsModelProduct
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_product = self.model_product.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelProduct": model_product,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_modelproduct_models_model_product import (
            DominoNucleusModelproductModelsModelProduct,
        )

        d = dict(src_dict)
        model_product = DominoNucleusModelproductModelsModelProduct.from_dict(d.pop("modelProduct"))

        domino_nucleus_modelproduct_models_grant_access_required = cls(
            model_product=model_product,
        )

        domino_nucleus_modelproduct_models_grant_access_required.additional_properties = d
        return domino_nucleus_modelproduct_models_grant_access_required

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
