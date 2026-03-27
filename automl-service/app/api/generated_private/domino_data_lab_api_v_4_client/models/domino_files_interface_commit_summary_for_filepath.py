from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_files_interface_commit_info import DominoFilesInterfaceCommitInfo


T = TypeVar("T", bound="DominoFilesInterfaceCommitSummaryForFilepath")


@_attrs_define
class DominoFilesInterfaceCommitSummaryForFilepath:
    """
    Attributes:
        requested_or_newest_commit (DominoFilesInterfaceCommitInfo):
        all_commits_for_path (list[DominoFilesInterfaceCommitInfo]):
        last_commit_of_file (DominoFilesInterfaceCommitInfo | Unset):
    """

    requested_or_newest_commit: DominoFilesInterfaceCommitInfo
    all_commits_for_path: list[DominoFilesInterfaceCommitInfo]
    last_commit_of_file: DominoFilesInterfaceCommitInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested_or_newest_commit = self.requested_or_newest_commit.to_dict()

        all_commits_for_path = []
        for all_commits_for_path_item_data in self.all_commits_for_path:
            all_commits_for_path_item = all_commits_for_path_item_data.to_dict()
            all_commits_for_path.append(all_commits_for_path_item)

        last_commit_of_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_commit_of_file, Unset):
            last_commit_of_file = self.last_commit_of_file.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestedOrNewestCommit": requested_or_newest_commit,
                "allCommitsForPath": all_commits_for_path,
            }
        )
        if last_commit_of_file is not UNSET:
            field_dict["lastCommitOfFile"] = last_commit_of_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_commit_info import DominoFilesInterfaceCommitInfo

        d = dict(src_dict)
        requested_or_newest_commit = DominoFilesInterfaceCommitInfo.from_dict(d.pop("requestedOrNewestCommit"))

        all_commits_for_path = []
        _all_commits_for_path = d.pop("allCommitsForPath")
        for all_commits_for_path_item_data in _all_commits_for_path:
            all_commits_for_path_item = DominoFilesInterfaceCommitInfo.from_dict(all_commits_for_path_item_data)

            all_commits_for_path.append(all_commits_for_path_item)

        _last_commit_of_file = d.pop("lastCommitOfFile", UNSET)
        last_commit_of_file: DominoFilesInterfaceCommitInfo | Unset
        if isinstance(_last_commit_of_file, Unset):
            last_commit_of_file = UNSET
        else:
            last_commit_of_file = DominoFilesInterfaceCommitInfo.from_dict(_last_commit_of_file)

        domino_files_interface_commit_summary_for_filepath = cls(
            requested_or_newest_commit=requested_or_newest_commit,
            all_commits_for_path=all_commits_for_path,
            last_commit_of_file=last_commit_of_file,
        )

        domino_files_interface_commit_summary_for_filepath.additional_properties = d
        return domino_files_interface_commit_summary_for_filepath

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
