from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoGruzApiRunMemoryLimit")


@_attrs_define
class DominoGruzApiRunMemoryLimit:
    """
    Attributes:
        memory_limit_megabytes (int | None | Unset):
        memory_swap_limit_megabytes (int | None | Unset):
    """

    memory_limit_megabytes: int | None | Unset = UNSET
    memory_swap_limit_megabytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory_limit_megabytes: int | None | Unset
        if isinstance(self.memory_limit_megabytes, Unset):
            memory_limit_megabytes = UNSET
        else:
            memory_limit_megabytes = self.memory_limit_megabytes

        memory_swap_limit_megabytes: int | None | Unset
        if isinstance(self.memory_swap_limit_megabytes, Unset):
            memory_swap_limit_megabytes = UNSET
        else:
            memory_swap_limit_megabytes = self.memory_swap_limit_megabytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memory_limit_megabytes is not UNSET:
            field_dict["memoryLimitMegabytes"] = memory_limit_megabytes
        if memory_swap_limit_megabytes is not UNSET:
            field_dict["memorySwapLimitMegabytes"] = memory_swap_limit_megabytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_memory_limit_megabytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_limit_megabytes = _parse_memory_limit_megabytes(d.pop("memoryLimitMegabytes", UNSET))

        def _parse_memory_swap_limit_megabytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_swap_limit_megabytes = _parse_memory_swap_limit_megabytes(d.pop("memorySwapLimitMegabytes", UNSET))

        domino_gruz_api_run_memory_limit = cls(
            memory_limit_megabytes=memory_limit_megabytes,
            memory_swap_limit_megabytes=memory_swap_limit_megabytes,
        )

        domino_gruz_api_run_memory_limit.additional_properties = d
        return domino_gruz_api_run_memory_limit

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
