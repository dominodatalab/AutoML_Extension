from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspaceApiGitMergeConflictResolutionResponseDto")


@_attrs_define
class DominoWorkspaceApiGitMergeConflictResolutionResponseDto:
    """
    Attributes:
        succeeded_repo_ids (list[str]):
        failed_repo_ids (list[str]):
        failed_reason (None | str | Unset):
    """

    succeeded_repo_ids: list[str]
    failed_repo_ids: list[str]
    failed_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        succeeded_repo_ids = self.succeeded_repo_ids

        failed_repo_ids = self.failed_repo_ids

        failed_reason: None | str | Unset
        if isinstance(self.failed_reason, Unset):
            failed_reason = UNSET
        else:
            failed_reason = self.failed_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "succeededRepoIds": succeeded_repo_ids,
                "failedRepoIds": failed_repo_ids,
            }
        )
        if failed_reason is not UNSET:
            field_dict["failedReason"] = failed_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        succeeded_repo_ids = cast(list[str], d.pop("succeededRepoIds"))

        failed_repo_ids = cast(list[str], d.pop("failedRepoIds"))

        def _parse_failed_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failed_reason = _parse_failed_reason(d.pop("failedReason", UNSET))

        domino_workspace_api_git_merge_conflict_resolution_response_dto = cls(
            succeeded_repo_ids=succeeded_repo_ids,
            failed_repo_ids=failed_repo_ids,
            failed_reason=failed_reason,
        )

        domino_workspace_api_git_merge_conflict_resolution_response_dto.additional_properties = d
        return domino_workspace_api_git_merge_conflict_resolution_response_dto

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
