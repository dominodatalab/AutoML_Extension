from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_api_access_token import ModelApiAccessToken


T = TypeVar("T", bound="ModelApiAccessConfiguration")


@_attrs_define
class ModelApiAccessConfiguration:
    """
    Attributes:
        access_tokens (list[ModelApiAccessToken]): The access tokens of the Model API.
        is_public (bool): Whether the Model API is public.
    """

    access_tokens: list[ModelApiAccessToken]
    is_public: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_tokens = []
        for access_tokens_item_data in self.access_tokens:
            access_tokens_item = access_tokens_item_data.to_dict()
            access_tokens.append(access_tokens_item)

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessTokens": access_tokens,
                "isPublic": is_public,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_api_access_token import ModelApiAccessToken

        d = dict(src_dict)
        access_tokens = []
        _access_tokens = d.pop("accessTokens")
        for access_tokens_item_data in _access_tokens:
            access_tokens_item = ModelApiAccessToken.from_dict(access_tokens_item_data)

            access_tokens.append(access_tokens_item)

        is_public = d.pop("isPublic")

        model_api_access_configuration = cls(
            access_tokens=access_tokens,
            is_public=is_public,
        )

        model_api_access_configuration.additional_properties = d
        return model_api_access_configuration

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
