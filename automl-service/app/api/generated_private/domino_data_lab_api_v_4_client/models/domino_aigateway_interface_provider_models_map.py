from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_aigateway_interface_provider_models_map_models_map import (
        DominoAigatewayInterfaceProviderModelsMapModelsMap,
    )


T = TypeVar("T", bound="DominoAigatewayInterfaceProviderModelsMap")


@_attrs_define
class DominoAigatewayInterfaceProviderModelsMap:
    """
    Attributes:
        models_map (DominoAigatewayInterfaceProviderModelsMapModelsMap):
    """

    models_map: DominoAigatewayInterfaceProviderModelsMapModelsMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        models_map = self.models_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelsMap": models_map,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_aigateway_interface_provider_models_map_models_map import (
            DominoAigatewayInterfaceProviderModelsMapModelsMap,
        )

        d = dict(src_dict)
        models_map = DominoAigatewayInterfaceProviderModelsMapModelsMap.from_dict(d.pop("modelsMap"))

        domino_aigateway_interface_provider_models_map = cls(
            models_map=models_map,
        )

        domino_aigateway_interface_provider_models_map.additional_properties = d
        return domino_aigateway_interface_provider_models_map

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
