from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_file_change_activity_meta_data_action import (
    DominoActivityApiFileChangeActivityMetaDataAction,
)
from ..models.domino_activity_api_file_change_activity_meta_data_file_changed_due_to import (
    DominoActivityApiFileChangeActivityMetaDataFileChangedDueTo,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoActivityApiFileChangeActivityMetaData")


@_attrs_define
class DominoActivityApiFileChangeActivityMetaData:
    """
    Attributes:
        files_changed (list[str]):
        action (DominoActivityApiFileChangeActivityMetaDataAction):
        commit_id (str):
        file_changed_due_to_id (str):
        file_changed_due_to (DominoActivityApiFileChangeActivityMetaDataFileChangedDueTo):
        commit_message (None | str | Unset):
    """

    files_changed: list[str]
    action: DominoActivityApiFileChangeActivityMetaDataAction
    commit_id: str
    file_changed_due_to_id: str
    file_changed_due_to: DominoActivityApiFileChangeActivityMetaDataFileChangedDueTo
    commit_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files_changed = self.files_changed

        action = self.action.value

        commit_id = self.commit_id

        file_changed_due_to_id = self.file_changed_due_to_id

        file_changed_due_to = self.file_changed_due_to.value

        commit_message: None | str | Unset
        if isinstance(self.commit_message, Unset):
            commit_message = UNSET
        else:
            commit_message = self.commit_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filesChanged": files_changed,
                "action": action,
                "commitId": commit_id,
                "fileChangedDueToId": file_changed_due_to_id,
                "fileChangedDueTo": file_changed_due_to,
            }
        )
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        files_changed = cast(list[str], d.pop("filesChanged"))

        action = DominoActivityApiFileChangeActivityMetaDataAction(d.pop("action"))

        commit_id = d.pop("commitId")

        file_changed_due_to_id = d.pop("fileChangedDueToId")

        file_changed_due_to = DominoActivityApiFileChangeActivityMetaDataFileChangedDueTo(d.pop("fileChangedDueTo"))

        def _parse_commit_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_message = _parse_commit_message(d.pop("commitMessage", UNSET))

        domino_activity_api_file_change_activity_meta_data = cls(
            files_changed=files_changed,
            action=action,
            commit_id=commit_id,
            file_changed_due_to_id=file_changed_due_to_id,
            file_changed_due_to=file_changed_due_to,
            commit_message=commit_message,
        )

        domino_activity_api_file_change_activity_meta_data.additional_properties = d
        return domino_activity_api_file_change_activity_meta_data

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
