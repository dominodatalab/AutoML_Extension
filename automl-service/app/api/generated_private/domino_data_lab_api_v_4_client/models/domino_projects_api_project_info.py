from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_owner_info import DominoProjectsApiProjectOwnerInfo


T = TypeVar("T", bound="DominoProjectsApiProjectInfo")


@_attrs_define
class DominoProjectsApiProjectInfo:
    """
    Attributes:
        id (str):
        name (str):
        owner (DominoProjectsApiProjectOwnerInfo):
        is_archived (bool):
        has_project_access (bool | None | Unset):
    """

    id: str
    name: str
    owner: DominoProjectsApiProjectOwnerInfo
    is_archived: bool
    has_project_access: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        owner = self.owner.to_dict()

        is_archived = self.is_archived

        has_project_access: bool | None | Unset
        if isinstance(self.has_project_access, Unset):
            has_project_access = UNSET
        else:
            has_project_access = self.has_project_access

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "owner": owner,
                "isArchived": is_archived,
            }
        )
        if has_project_access is not UNSET:
            field_dict["hasProjectAccess"] = has_project_access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_owner_info import DominoProjectsApiProjectOwnerInfo

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        owner = DominoProjectsApiProjectOwnerInfo.from_dict(d.pop("owner"))

        is_archived = d.pop("isArchived")

        def _parse_has_project_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_project_access = _parse_has_project_access(d.pop("hasProjectAccess", UNSET))

        domino_projects_api_project_info = cls(
            id=id,
            name=name,
            owner=owner,
            is_archived=is_archived,
            has_project_access=has_project_access,
        )

        domino_projects_api_project_info.additional_properties = d
        return domino_projects_api_project_info

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
