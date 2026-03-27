from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoNucleusLibAuthGlobalBannerSettings")


@_attrs_define
class DominoNucleusLibAuthGlobalBannerSettings:
    """
    Attributes:
        is_closable (bool):
        reappear_time_after_close_in_sec (int | None | Unset):
        content (None | str | Unset):
    """

    is_closable: bool
    reappear_time_after_close_in_sec: int | None | Unset = UNSET
    content: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_closable = self.is_closable

        reappear_time_after_close_in_sec: int | None | Unset
        if isinstance(self.reappear_time_after_close_in_sec, Unset):
            reappear_time_after_close_in_sec = UNSET
        else:
            reappear_time_after_close_in_sec = self.reappear_time_after_close_in_sec

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isClosable": is_closable,
            }
        )
        if reappear_time_after_close_in_sec is not UNSET:
            field_dict["reappearTimeAfterCloseInSec"] = reappear_time_after_close_in_sec
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        domino_nucleus_lib_auth_global_banner_settings = cls(
            is_closable=is_closable,
            reappear_time_after_close_in_sec=reappear_time_after_close_in_sec,
            content=content,
        )

        domino_nucleus_lib_auth_global_banner_settings.additional_properties = d
        return domino_nucleus_lib_auth_global_banner_settings

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
