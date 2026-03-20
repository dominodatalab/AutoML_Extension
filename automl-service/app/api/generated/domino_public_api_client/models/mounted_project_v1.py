from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MountedProjectV1")


@_attrs_define
class MountedProjectV1:
    """
    Attributes:
        commit_id (str): CommitId to use for project being mounted. Example: 7f8e3908f129c0ca6529028618e6f10b3d2f315a.
        project_id (str): Id of project to mount. Example: 623138c87a0af0281c01a6a3.
    """

    commit_id: str
    project_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id = self.commit_id

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitId": commit_id,
                "projectId": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commit_id = d.pop("commitId")

        project_id = d.pop("projectId")

        mounted_project_v1 = cls(
            commit_id=commit_id,
            project_id=project_id,
        )

        mounted_project_v1.additional_properties = d
        return mounted_project_v1

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
