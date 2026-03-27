from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProvenanceApiProvenanceCommit")


@_attrs_define
class DominoProvenanceApiProvenanceCommit:
    """
    Attributes:
        commit_id (str):
        branch_name (str):
    """

    commit_id: str
    branch_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id = self.commit_id

        branch_name = self.branch_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitId": commit_id,
                "branchName": branch_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commit_id = d.pop("commitId")

        branch_name = d.pop("branchName")

        domino_provenance_api_provenance_commit = cls(
            commit_id=commit_id,
            branch_name=branch_name,
        )

        domino_provenance_api_provenance_commit.additional_properties = d
        return domino_provenance_api_provenance_commit

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
