from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitDetailsV1")


@_attrs_define
class CommitDetailsV1:
    """
    Attributes:
        input_commit_id (str): CommitId at execution start. Example: f1dafe322c7d4a6720f652c330fe33b014720e46.
        output_commit_id (str | Unset): CommitId at execution end. May be empty if execution caused no new commits.
            Example: e1f06e5f64cfc26c2b70e405f70b7c8300d8a4ed.
    """

    input_commit_id: str
    output_commit_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_commit_id = self.input_commit_id

        output_commit_id = self.output_commit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputCommitId": input_commit_id,
            }
        )
        if output_commit_id is not UNSET:
            field_dict["outputCommitId"] = output_commit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_commit_id = d.pop("inputCommitId")

        output_commit_id = d.pop("outputCommitId", UNSET)

        commit_details_v1 = cls(
            input_commit_id=input_commit_id,
            output_commit_id=output_commit_id,
        )

        commit_details_v1.additional_properties = d
        return commit_details_v1

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
