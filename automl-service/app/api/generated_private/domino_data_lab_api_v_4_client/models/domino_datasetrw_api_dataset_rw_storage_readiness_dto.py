from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_storage_readiness_dto_state import (
    DominoDatasetrwApiDatasetRwStorageReadinessDtoState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwStorageReadinessDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwStorageReadinessDto:
    """
    Attributes:
        state (DominoDatasetrwApiDatasetRwStorageReadinessDtoState):
        last_updated_at (int | None | Unset):
    """

    state: DominoDatasetrwApiDatasetRwStorageReadinessDtoState
    last_updated_at: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        last_updated_at: int | None | Unset
        if isinstance(self.last_updated_at, Unset):
            last_updated_at = UNSET
        else:
            last_updated_at = self.last_updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = DominoDatasetrwApiDatasetRwStorageReadinessDtoState(d.pop("state"))

        def _parse_last_updated_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_updated_at = _parse_last_updated_at(d.pop("lastUpdatedAt", UNSET))

        domino_datasetrw_api_dataset_rw_storage_readiness_dto = cls(
            state=state,
            last_updated_at=last_updated_at,
        )

        domino_datasetrw_api_dataset_rw_storage_readiness_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_storage_readiness_dto

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
