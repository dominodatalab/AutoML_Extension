from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_rw_view_dto_tags import DominoDatasetrwApiDatasetRwViewDtoTags


T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwViewDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwViewDto:
    """
    Attributes:
        snapshot_ids (list[str]):
        name (str):
        created_time (int):
        project_owner (str):
        id (str):
        project_name (str):
        tags (DominoDatasetrwApiDatasetRwViewDtoTags):
        description (None | str | Unset):
        project_id (None | str | Unset):
    """

    snapshot_ids: list[str]
    name: str
    created_time: int
    project_owner: str
    id: str
    project_name: str
    tags: DominoDatasetrwApiDatasetRwViewDtoTags
    description: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_ids = self.snapshot_ids

        name = self.name

        created_time = self.created_time

        project_owner = self.project_owner

        id = self.id

        project_name = self.project_name

        tags = self.tags.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshotIds": snapshot_ids,
                "name": name,
                "createdTime": created_time,
                "projectOwner": project_owner,
                "id": id,
                "projectName": project_name,
                "tags": tags,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_rw_view_dto_tags import DominoDatasetrwApiDatasetRwViewDtoTags

        d = dict(src_dict)
        snapshot_ids = cast(list[str], d.pop("snapshotIds"))

        name = d.pop("name")

        created_time = d.pop("createdTime")

        project_owner = d.pop("projectOwner")

        id = d.pop("id")

        project_name = d.pop("projectName")

        tags = DominoDatasetrwApiDatasetRwViewDtoTags.from_dict(d.pop("tags"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        domino_datasetrw_api_dataset_rw_view_dto = cls(
            snapshot_ids=snapshot_ids,
            name=name,
            created_time=created_time,
            project_owner=project_owner,
            id=id,
            project_name=project_name,
            tags=tags,
            description=description,
            project_id=project_id,
        )

        domino_datasetrw_api_dataset_rw_view_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_view_dto

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
