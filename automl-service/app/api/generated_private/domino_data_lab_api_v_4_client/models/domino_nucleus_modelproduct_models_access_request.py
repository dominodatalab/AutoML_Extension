from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoNucleusModelproductModelsAccessRequest")


@_attrs_define
class DominoNucleusModelproductModelsAccessRequest:
    """
    Attributes:
        user_id (str):
        redirect (bool | None | Unset):
    """

    user_id: str
    redirect: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        redirect: bool | None | Unset
        if isinstance(self.redirect, Unset):
            redirect = UNSET
        else:
            redirect = self.redirect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
            }
        )
        if redirect is not UNSET:
            field_dict["redirect"] = redirect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        def _parse_redirect(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        redirect = _parse_redirect(d.pop("redirect", UNSET))

        domino_nucleus_modelproduct_models_access_request = cls(
            user_id=user_id,
            redirect=redirect,
        )

        domino_nucleus_modelproduct_models_access_request.additional_properties = d
        return domino_nucleus_modelproduct_models_access_request

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
