from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_comment_activity_meta_data_commented_on import (
    DominoActivityApiCommentActivityMetaDataCommentedOn,
)
from ..models.domino_activity_api_comment_activity_meta_data_operation import (
    DominoActivityApiCommentActivityMetaDataOperation,
)

T = TypeVar("T", bound="DominoActivityApiCommentActivityMetaData")


@_attrs_define
class DominoActivityApiCommentActivityMetaData:
    """
    Attributes:
        commented_on (DominoActivityApiCommentActivityMetaDataCommentedOn):
        commented_on_meta_data (Any):
        operation (DominoActivityApiCommentActivityMetaDataOperation):
        comment_data (str):
    """

    commented_on: DominoActivityApiCommentActivityMetaDataCommentedOn
    commented_on_meta_data: Any
    operation: DominoActivityApiCommentActivityMetaDataOperation
    comment_data: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commented_on = self.commented_on.value

        commented_on_meta_data = self.commented_on_meta_data

        operation = self.operation.value

        comment_data = self.comment_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentedOn": commented_on,
                "commentedOnMetaData": commented_on_meta_data,
                "operation": operation,
                "commentData": comment_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commented_on = DominoActivityApiCommentActivityMetaDataCommentedOn(d.pop("commentedOn"))

        commented_on_meta_data = d.pop("commentedOnMetaData")

        operation = DominoActivityApiCommentActivityMetaDataOperation(d.pop("operation"))

        comment_data = d.pop("commentData")

        domino_activity_api_comment_activity_meta_data = cls(
            commented_on=commented_on,
            commented_on_meta_data=commented_on_meta_data,
            operation=operation,
            comment_data=comment_data,
        )

        domino_activity_api_comment_activity_meta_data.additional_properties = d
        return domino_activity_api_comment_activity_meta_data

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
