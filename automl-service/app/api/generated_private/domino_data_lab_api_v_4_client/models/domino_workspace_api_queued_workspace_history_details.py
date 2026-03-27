from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoWorkspaceApiQueuedWorkspaceHistoryDetails")


@_attrs_define
class DominoWorkspaceApiQueuedWorkspaceHistoryDetails:
    """
    Attributes:
        expected_wait (str):
        explanation (str):
        help_text (str):
    """

    expected_wait: str
    explanation: str
    help_text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_wait = self.expected_wait

        explanation = self.explanation

        help_text = self.help_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expectedWait": expected_wait,
                "explanation": explanation,
                "helpText": help_text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_wait = d.pop("expectedWait")

        explanation = d.pop("explanation")

        help_text = d.pop("helpText")

        domino_workspace_api_queued_workspace_history_details = cls(
            expected_wait=expected_wait,
            explanation=explanation,
            help_text=help_text,
        )

        domino_workspace_api_queued_workspace_history_details.additional_properties = d
        return domino_workspace_api_queued_workspace_history_details

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
