from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_environments_api_environment_revision_summary_revision_type import (
    DominoEnvironmentsApiEnvironmentRevisionSummaryRevisionType,
)

T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentRevisionSummary")


@_attrs_define
class DominoEnvironmentsApiEnvironmentRevisionSummary:
    """
    Attributes:
        id (str):
        name (str):
        revision_id (str):
        revision_number (int):
        revision_type (DominoEnvironmentsApiEnvironmentRevisionSummaryRevisionType):
        is_restricted (bool):
    """

    id: str
    name: str
    revision_id: str
    revision_number: int
    revision_type: DominoEnvironmentsApiEnvironmentRevisionSummaryRevisionType
    is_restricted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        revision_id = self.revision_id

        revision_number = self.revision_number

        revision_type = self.revision_type.value

        is_restricted = self.is_restricted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "revisionId": revision_id,
                "revisionNumber": revision_number,
                "revisionType": revision_type,
                "isRestricted": is_restricted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        revision_id = d.pop("revisionId")

        revision_number = d.pop("revisionNumber")

        revision_type = DominoEnvironmentsApiEnvironmentRevisionSummaryRevisionType(d.pop("revisionType"))

        is_restricted = d.pop("isRestricted")

        domino_environments_api_environment_revision_summary = cls(
            id=id,
            name=name,
            revision_id=revision_id,
            revision_number=revision_number,
            revision_type=revision_type,
            is_restricted=is_restricted,
        )

        domino_environments_api_environment_revision_summary.additional_properties = d
        return domino_environments_api_environment_revision_summary

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
