from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwWebCalculateSnapshotSizeRequest")


@_attrs_define
class DominoDatasetrwWebCalculateSnapshotSizeRequest:
    """
    Attributes:
        force_recalculate (bool | None | Unset):
    """

    force_recalculate: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        force_recalculate: bool | None | Unset
        if isinstance(self.force_recalculate, Unset):
            force_recalculate = UNSET
        else:
            force_recalculate = self.force_recalculate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force_recalculate is not UNSET:
            field_dict["forceRecalculate"] = force_recalculate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_force_recalculate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force_recalculate = _parse_force_recalculate(d.pop("forceRecalculate", UNSET))

        domino_datasetrw_web_calculate_snapshot_size_request = cls(
            force_recalculate=force_recalculate,
        )

        domino_datasetrw_web_calculate_snapshot_size_request.additional_properties = d
        return domino_datasetrw_web_calculate_snapshot_size_request

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
