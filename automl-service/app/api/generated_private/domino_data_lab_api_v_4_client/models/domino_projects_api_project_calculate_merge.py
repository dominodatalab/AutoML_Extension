from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiProjectCalculateMerge")


@_attrs_define
class DominoProjectsApiProjectCalculateMerge:
    """
    Attributes:
        from_project_id (str):
        from_branch_name (str):
        into_project_id (str):
        into_branch_name (str):
        override_from_commit_id (None | str | Unset):
        override_into_commit_id (None | str | Unset):
    """

    from_project_id: str
    from_branch_name: str
    into_project_id: str
    into_branch_name: str
    override_from_commit_id: None | str | Unset = UNSET
    override_into_commit_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_project_id = self.from_project_id

        from_branch_name = self.from_branch_name

        into_project_id = self.into_project_id

        into_branch_name = self.into_branch_name

        override_from_commit_id: None | str | Unset
        if isinstance(self.override_from_commit_id, Unset):
            override_from_commit_id = UNSET
        else:
            override_from_commit_id = self.override_from_commit_id

        override_into_commit_id: None | str | Unset
        if isinstance(self.override_into_commit_id, Unset):
            override_into_commit_id = UNSET
        else:
            override_into_commit_id = self.override_into_commit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromProjectId": from_project_id,
                "fromBranchName": from_branch_name,
                "intoProjectId": into_project_id,
                "intoBranchName": into_branch_name,
            }
        )
        if override_from_commit_id is not UNSET:
            field_dict["overrideFromCommitId"] = override_from_commit_id
        if override_into_commit_id is not UNSET:
            field_dict["overrideIntoCommitId"] = override_into_commit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_project_id = d.pop("fromProjectId")

        from_branch_name = d.pop("fromBranchName")

        into_project_id = d.pop("intoProjectId")

        into_branch_name = d.pop("intoBranchName")

        def _parse_override_from_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_from_commit_id = _parse_override_from_commit_id(d.pop("overrideFromCommitId", UNSET))

        def _parse_override_into_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_into_commit_id = _parse_override_into_commit_id(d.pop("overrideIntoCommitId", UNSET))

        domino_projects_api_project_calculate_merge = cls(
            from_project_id=from_project_id,
            from_branch_name=from_branch_name,
            into_project_id=into_project_id,
            into_branch_name=into_branch_name,
            override_from_commit_id=override_from_commit_id,
            override_into_commit_id=override_into_commit_id,
        )

        domino_projects_api_project_calculate_merge.additional_properties = d
        return domino_projects_api_project_calculate_merge

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
