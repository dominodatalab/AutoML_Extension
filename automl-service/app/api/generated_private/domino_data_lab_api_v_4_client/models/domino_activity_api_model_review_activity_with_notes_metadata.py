from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoActivityApiModelReviewActivityWithNotesMetadata")


@_attrs_define
class DominoActivityApiModelReviewActivityWithNotesMetadata:
    """
    Attributes:
        model_version (int):
        initial_stage (str):
        target_stage (str):
        review_id (str):
        notes (str):
    """

    model_version: int
    initial_stage: str
    target_stage: str
    review_id: str
    notes: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_version = self.model_version

        initial_stage = self.initial_stage

        target_stage = self.target_stage

        review_id = self.review_id

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelVersion": model_version,
                "initialStage": initial_stage,
                "targetStage": target_stage,
                "reviewId": review_id,
                "notes": notes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_version = d.pop("modelVersion")

        initial_stage = d.pop("initialStage")

        target_stage = d.pop("targetStage")

        review_id = d.pop("reviewId")

        notes = d.pop("notes")

        domino_activity_api_model_review_activity_with_notes_metadata = cls(
            model_version=model_version,
            initial_stage=initial_stage,
            target_stage=target_stage,
            review_id=review_id,
            notes=notes,
        )

        domino_activity_api_model_review_activity_with_notes_metadata.additional_properties = d
        return domino_activity_api_model_review_activity_with_notes_metadata

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
