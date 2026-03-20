from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TagToAddV1")


@_attrs_define
class TagToAddV1:
    """
    Attributes:
        project_id (str): Id of project the resource belongs to. Example: 62313ce67a0af0281c01a6a5.
        tag_name (str): Name of tag to add to a job. Example: MyTag.
    """

    project_id: str
    tag_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        tag_name = self.tag_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "tagName": tag_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        tag_name = d.pop("tagName")

        tag_to_add_v1 = cls(
            project_id=project_id,
            tag_name=tag_name,
        )

        tag_to_add_v1.additional_properties = d
        return tag_to_add_v1

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
