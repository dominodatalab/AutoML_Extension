from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoAdminWebMenuItemDto")


@_attrs_define
class DominoAdminWebMenuItemDto:
    """
    Attributes:
        type_ (str | Unset):
        code (str | Unset):
        text (str | Unset):
        url (str | Unset):
        allowed (bool | Unset):
        items (list[DominoAdminWebMenuItemDto] | Unset):
    """

    type_: str | Unset = UNSET
    code: str | Unset = UNSET
    text: str | Unset = UNSET
    url: str | Unset = UNSET
    allowed: bool | Unset = UNSET
    items: list[DominoAdminWebMenuItemDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        code = self.code

        text = self.text

        url = self.url

        allowed = self.allowed

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if code is not UNSET:
            field_dict["code"] = code
        if text is not UNSET:
            field_dict["text"] = text
        if url is not UNSET:
            field_dict["url"] = url
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        code = d.pop("code", UNSET)

        text = d.pop("text", UNSET)

        url = d.pop("url", UNSET)

        allowed = d.pop("allowed", UNSET)

        _items = d.pop("items", UNSET)
        items: list[DominoAdminWebMenuItemDto] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = DominoAdminWebMenuItemDto.from_dict(items_item_data)

                items.append(items_item)

        domino_admin_web_menu_item_dto = cls(
            type_=type_,
            code=code,
            text=text,
            url=url,
            allowed=allowed,
            items=items,
        )

        domino_admin_web_menu_item_dto.additional_properties = d
        return domino_admin_web_menu_item_dto

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
