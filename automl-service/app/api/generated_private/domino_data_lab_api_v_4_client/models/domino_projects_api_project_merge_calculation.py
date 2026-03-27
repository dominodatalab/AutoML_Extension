from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_file_diff_entry import DominoProjectsApiFileDiffEntry
    from ..models.domino_projects_api_project_hypothetical_merge_result import (
        DominoProjectsApiProjectHypotheticalMergeResult,
    )


T = TypeVar("T", bound="DominoProjectsApiProjectMergeCalculation")


@_attrs_define
class DominoProjectsApiProjectMergeCalculation:
    """
    Attributes:
        from_project_id (str):
        from_project_name (str):
        from_branch_name (str):
        from_commit_id (str):
        into_project_id (str):
        into_project_name (str):
        into_branch_name (str):
        into_commit_id (str):
        diffs (list[DominoProjectsApiFileDiffEntry]):
        commits_for_range (list[str]):
        hypothetical_merge_result (DominoProjectsApiProjectHypotheticalMergeResult):
    """

    from_project_id: str
    from_project_name: str
    from_branch_name: str
    from_commit_id: str
    into_project_id: str
    into_project_name: str
    into_branch_name: str
    into_commit_id: str
    diffs: list[DominoProjectsApiFileDiffEntry]
    commits_for_range: list[str]
    hypothetical_merge_result: DominoProjectsApiProjectHypotheticalMergeResult
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_project_id = self.from_project_id

        from_project_name = self.from_project_name

        from_branch_name = self.from_branch_name

        from_commit_id = self.from_commit_id

        into_project_id = self.into_project_id

        into_project_name = self.into_project_name

        into_branch_name = self.into_branch_name

        into_commit_id = self.into_commit_id

        diffs = []
        for diffs_item_data in self.diffs:
            diffs_item = diffs_item_data.to_dict()
            diffs.append(diffs_item)

        commits_for_range = self.commits_for_range

        hypothetical_merge_result = self.hypothetical_merge_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromProjectId": from_project_id,
                "fromProjectName": from_project_name,
                "fromBranchName": from_branch_name,
                "fromCommitId": from_commit_id,
                "intoProjectId": into_project_id,
                "intoProjectName": into_project_name,
                "intoBranchName": into_branch_name,
                "intoCommitId": into_commit_id,
                "diffs": diffs,
                "commitsForRange": commits_for_range,
                "hypotheticalMergeResult": hypothetical_merge_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_file_diff_entry import DominoProjectsApiFileDiffEntry
        from ..models.domino_projects_api_project_hypothetical_merge_result import (
            DominoProjectsApiProjectHypotheticalMergeResult,
        )

        d = dict(src_dict)
        from_project_id = d.pop("fromProjectId")

        from_project_name = d.pop("fromProjectName")

        from_branch_name = d.pop("fromBranchName")

        from_commit_id = d.pop("fromCommitId")

        into_project_id = d.pop("intoProjectId")

        into_project_name = d.pop("intoProjectName")

        into_branch_name = d.pop("intoBranchName")

        into_commit_id = d.pop("intoCommitId")

        diffs = []
        _diffs = d.pop("diffs")
        for diffs_item_data in _diffs:
            diffs_item = DominoProjectsApiFileDiffEntry.from_dict(diffs_item_data)

            diffs.append(diffs_item)

        commits_for_range = cast(list[str], d.pop("commitsForRange"))

        hypothetical_merge_result = DominoProjectsApiProjectHypotheticalMergeResult.from_dict(
            d.pop("hypotheticalMergeResult")
        )

        domino_projects_api_project_merge_calculation = cls(
            from_project_id=from_project_id,
            from_project_name=from_project_name,
            from_branch_name=from_branch_name,
            from_commit_id=from_commit_id,
            into_project_id=into_project_id,
            into_project_name=into_project_name,
            into_branch_name=into_branch_name,
            into_commit_id=into_commit_id,
            diffs=diffs,
            commits_for_range=commits_for_range,
            hypothetical_merge_result=hypothetical_merge_result,
        )

        domino_projects_api_project_merge_calculation.additional_properties = d
        return domino_projects_api_project_merge_calculation

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
