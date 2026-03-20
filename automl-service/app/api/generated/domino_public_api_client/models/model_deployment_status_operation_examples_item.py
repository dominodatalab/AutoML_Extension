from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelDeploymentStatusOperationExamplesItem")


@_attrs_define
class ModelDeploymentStatusOperationExamplesItem:
    """
    Attributes:
        code (str | Unset):
        format_ (str | Unset):
        language (str | Unset):
        request (str | Unset):
    """

    code: str | Unset = UNSET
    format_: str | Unset = UNSET
    language: str | Unset = UNSET
    request: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        format_ = self.format_

        language = self.language

        request = self.request

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if format_ is not UNSET:
            field_dict["format"] = format_
        if language is not UNSET:
            field_dict["language"] = language
        if request is not UNSET:
            field_dict["request"] = request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        format_ = d.pop("format", UNSET)

        language = d.pop("language", UNSET)

        request = d.pop("request", UNSET)

        model_deployment_status_operation_examples_item = cls(
            code=code,
            format_=format_,
            language=language,
            request=request,
        )

        model_deployment_status_operation_examples_item.additional_properties = d
        return model_deployment_status_operation_examples_item

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
