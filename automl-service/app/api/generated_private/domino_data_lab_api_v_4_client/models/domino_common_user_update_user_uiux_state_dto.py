from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_user_update_user_uiux_state_dto_state_map import (
        DominoCommonUserUpdateUserUIUXStateDTOStateMap,
    )


T = TypeVar("T", bound="DominoCommonUserUpdateUserUIUXStateDTO")


@_attrs_define
class DominoCommonUserUpdateUserUIUXStateDTO:
    """
    Attributes:
        state_map (DominoCommonUserUpdateUserUIUXStateDTOStateMap):
        replace (bool | None | Unset):
    """

    state_map: DominoCommonUserUpdateUserUIUXStateDTOStateMap
    replace: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state_map = self.state_map.to_dict()

        replace: bool | None | Unset
        if isinstance(self.replace, Unset):
            replace = UNSET
        else:
            replace = self.replace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stateMap": state_map,
            }
        )
        if replace is not UNSET:
            field_dict["replace"] = replace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_user_update_user_uiux_state_dto_state_map import (
            DominoCommonUserUpdateUserUIUXStateDTOStateMap,
        )

        d = dict(src_dict)
        state_map = DominoCommonUserUpdateUserUIUXStateDTOStateMap.from_dict(d.pop("stateMap"))

        def _parse_replace(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        replace = _parse_replace(d.pop("replace", UNSET))

        domino_common_user_update_user_uiux_state_dto = cls(
            state_map=state_map,
            replace=replace,
        )

        domino_common_user_update_user_uiux_state_dto.additional_properties = d
        return domino_common_user_update_user_uiux_state_dto

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
