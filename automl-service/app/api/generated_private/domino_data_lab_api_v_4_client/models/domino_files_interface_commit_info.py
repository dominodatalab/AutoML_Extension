from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_files_interface_commit_source_info import DominoFilesInterfaceCommitSourceInfo


T = TypeVar("T", bound="DominoFilesInterfaceCommitInfo")


@_attrs_define
class DominoFilesInterfaceCommitInfo:
    """
    Attributes:
        commit_id (str):
        commit_short_message (str):
        commit_full_message (str):
        commit_time (int):
        committed_by (str):
        is_latest_commit (bool):
        commit_source_info (DominoFilesInterfaceCommitSourceInfo | Unset):
    """

    commit_id: str
    commit_short_message: str
    commit_full_message: str
    commit_time: int
    committed_by: str
    is_latest_commit: bool
    commit_source_info: DominoFilesInterfaceCommitSourceInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id = self.commit_id

        commit_short_message = self.commit_short_message

        commit_full_message = self.commit_full_message

        commit_time = self.commit_time

        committed_by = self.committed_by

        is_latest_commit = self.is_latest_commit

        commit_source_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit_source_info, Unset):
            commit_source_info = self.commit_source_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitId": commit_id,
                "commitShortMessage": commit_short_message,
                "commitFullMessage": commit_full_message,
                "commitTime": commit_time,
                "committedBy": committed_by,
                "isLatestCommit": is_latest_commit,
            }
        )
        if commit_source_info is not UNSET:
            field_dict["commitSourceInfo"] = commit_source_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_commit_source_info import DominoFilesInterfaceCommitSourceInfo

        d = dict(src_dict)
        commit_id = d.pop("commitId")

        commit_short_message = d.pop("commitShortMessage")

        commit_full_message = d.pop("commitFullMessage")

        commit_time = d.pop("commitTime")

        committed_by = d.pop("committedBy")

        is_latest_commit = d.pop("isLatestCommit")

        _commit_source_info = d.pop("commitSourceInfo", UNSET)
        commit_source_info: DominoFilesInterfaceCommitSourceInfo | Unset
        if isinstance(_commit_source_info, Unset):
            commit_source_info = UNSET
        else:
            commit_source_info = DominoFilesInterfaceCommitSourceInfo.from_dict(_commit_source_info)

        domino_files_interface_commit_info = cls(
            commit_id=commit_id,
            commit_short_message=commit_short_message,
            commit_full_message=commit_full_message,
            commit_time=commit_time,
            committed_by=committed_by,
            is_latest_commit=is_latest_commit,
            commit_source_info=commit_source_info,
        )

        domino_files_interface_commit_info.additional_properties = d
        return domino_files_interface_commit_info

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
