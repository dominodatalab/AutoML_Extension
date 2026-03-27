from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoAdminInterfaceGlobalBanner")


@_attrs_define
class DominoAdminInterfaceGlobalBanner:
    """
    Attributes:
        content (str):
        is_closable (bool):
        reappear_time_after_close_in_sec (int | None | Unset):
    """

    content: str
    is_closable: bool
    reappear_time_after_close_in_sec: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        is_closable = self.is_closable

        reappear_time_after_close_in_sec: int | None | Unset
        if isinstance(self.reappear_time_after_close_in_sec, Unset):
            reappear_time_after_close_in_sec = UNSET
        else:
            reappear_time_after_close_in_sec = self.reappear_time_after_close_in_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "isClosable": is_closable,
            }
        )
        if reappear_time_after_close_in_sec is not UNSET:
            field_dict["reappearTimeAfterCloseInSec"] = reappear_time_after_close_in_sec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        is_closable = d.pop("isClosable")

        def _parse_reappear_time_after_close_in_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reappear_time_after_close_in_sec = _parse_reappear_time_after_close_in_sec(
            d.pop("reappearTimeAfterCloseInSec", UNSET)
        )

        domino_admin_interface_global_banner = cls(
            content=content,
            is_closable=is_closable,
            reappear_time_after_close_in_sec=reappear_time_after_close_in_sec,
        )

        domino_admin_interface_global_banner.additional_properties = d
        return domino_admin_interface_global_banner

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
