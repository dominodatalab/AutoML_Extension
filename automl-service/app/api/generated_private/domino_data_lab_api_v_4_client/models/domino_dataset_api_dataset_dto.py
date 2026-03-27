from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_project_id import DominoCommonProjectId
    from ..models.domino_dataset_api_dataset_dto_tags import DominoDatasetApiDatasetDtoTags


T = TypeVar("T", bound="DominoDatasetApiDatasetDto")


@_attrs_define
class DominoDatasetApiDatasetDto:
    """
    Attributes:
        archived (bool):
        created (int):
        snapshot_ids (list[str]):
        name (str):
        id (str):
        tags (DominoDatasetApiDatasetDtoTags):
        description (None | str | Unset):
        project_id (None | str | Unset):
        stupid_project_id (DominoCommonProjectId | Unset):
    """

    archived: bool
    created: int
    snapshot_ids: list[str]
    name: str
    id: str
    tags: DominoDatasetApiDatasetDtoTags
    description: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    stupid_project_id: DominoCommonProjectId | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        created = self.created

        snapshot_ids = self.snapshot_ids

        name = self.name

        id = self.id

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

        stupid_project_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stupid_project_id, Unset):
            stupid_project_id = self.stupid_project_id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archived": archived,
                "created": created,
                "snapshotIds": snapshot_ids,
                "name": name,
                "id": id,
                "tags": tags,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if stupid_project_id is not UNSET:
            field_dict["stupidProjectId"] = stupid_project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_project_id import DominoCommonProjectId
        from ..models.domino_dataset_api_dataset_dto_tags import DominoDatasetApiDatasetDtoTags

        d = dict(src_dict)
        archived = d.pop("archived")

        created = d.pop("created")

        snapshot_ids = cast(list[str], d.pop("snapshotIds"))

        name = d.pop("name")

        id = d.pop("id")

        tags = DominoDatasetApiDatasetDtoTags.from_dict(d.pop("tags"))

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

        _stupid_project_id = d.pop("stupidProjectId", UNSET)
        stupid_project_id: DominoCommonProjectId | Unset
        if isinstance(_stupid_project_id, Unset):
            stupid_project_id = UNSET
        else:
            stupid_project_id = DominoCommonProjectId.from_dict(_stupid_project_id)

        domino_dataset_api_dataset_dto = cls(
            archived=archived,
            created=created,
            snapshot_ids=snapshot_ids,
            name=name,
            id=id,
            tags=tags,
            description=description,
            project_id=project_id,
            stupid_project_id=stupid_project_id,
        )

        domino_dataset_api_dataset_dto.additional_properties = d
        return domino_dataset_api_dataset_dto

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
