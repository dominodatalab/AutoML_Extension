from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_common_user_user_uiux_state_dto_state_map import DominoCommonUserUserUIUXStateDTOStateMap


T = TypeVar("T", bound="DominoCommonUserUserUIUXStateDTO")


@_attrs_define
class DominoCommonUserUserUIUXStateDTO:
    """
    Attributes:
        state_map (DominoCommonUserUserUIUXStateDTOStateMap):
    """

    state_map: DominoCommonUserUserUIUXStateDTOStateMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state_map = self.state_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stateMap": state_map,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_user_user_uiux_state_dto_state_map import DominoCommonUserUserUIUXStateDTOStateMap

        d = dict(src_dict)
        state_map = DominoCommonUserUserUIUXStateDTOStateMap.from_dict(d.pop("stateMap"))

        domino_common_user_user_uiux_state_dto = cls(
            state_map=state_map,
        )

        domino_common_user_user_uiux_state_dto.additional_properties = d
        return domino_common_user_user_uiux_state_dto

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
