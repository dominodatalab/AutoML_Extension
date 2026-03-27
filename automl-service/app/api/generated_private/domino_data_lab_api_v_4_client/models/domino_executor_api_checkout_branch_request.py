from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoExecutorApiCheckoutBranchRequest")


@_attrs_define
class DominoExecutorApiCheckoutBranchRequest:
    """
    Attributes:
        branch_name (str):
        repo_id (str):
    """

    branch_name: str
    repo_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch_name = self.branch_name

        repo_id = self.repo_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branchName": branch_name,
                "repoId": repo_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch_name = d.pop("branchName")

        repo_id = d.pop("repoId")

        domino_executor_api_checkout_branch_request = cls(
            branch_name=branch_name,
            repo_id=repo_id,
        )

        domino_executor_api_checkout_branch_request.additional_properties = d
        return domino_executor_api_checkout_branch_request

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
