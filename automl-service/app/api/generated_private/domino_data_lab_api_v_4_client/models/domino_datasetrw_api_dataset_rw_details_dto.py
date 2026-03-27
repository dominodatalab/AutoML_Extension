from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_details_dto_lifecycle_status import (
    DominoDatasetrwApiDatasetRwDetailsDtoLifecycleStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_rw_details_dto_tags import DominoDatasetrwApiDatasetRwDetailsDtoTags
    from ..models.domino_datasetrw_api_dataset_rw_project_details_dto import (
        DominoDatasetrwApiDatasetRwProjectDetailsDto,
    )


T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwDetailsDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwDetailsDto:
    """
    Attributes:
        dataset_path (str):
        projects (DominoDatasetrwApiDatasetRwProjectDetailsDto):
        lifecycle_status (DominoDatasetrwApiDatasetRwDetailsDtoLifecycleStatus):
        snapshot_ids (list[str]):
        read_write_snapshot_id (str):
        name (str):
        id (str):
        tags (DominoDatasetrwApiDatasetRwDetailsDtoTags):
        author (None | str | Unset):
        description (None | str | Unset):
    """

    dataset_path: str
    projects: DominoDatasetrwApiDatasetRwProjectDetailsDto
    lifecycle_status: DominoDatasetrwApiDatasetRwDetailsDtoLifecycleStatus
    snapshot_ids: list[str]
    read_write_snapshot_id: str
    name: str
    id: str
    tags: DominoDatasetrwApiDatasetRwDetailsDtoTags
    author: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_path = self.dataset_path

        projects = self.projects.to_dict()

        lifecycle_status = self.lifecycle_status.value

        snapshot_ids = self.snapshot_ids

        read_write_snapshot_id = self.read_write_snapshot_id

        name = self.name

        id = self.id

        tags = self.tags.to_dict()

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetPath": dataset_path,
                "projects": projects,
                "lifecycleStatus": lifecycle_status,
                "snapshotIds": snapshot_ids,
                "readWriteSnapshotId": read_write_snapshot_id,
                "name": name,
                "id": id,
                "tags": tags,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_rw_details_dto_tags import DominoDatasetrwApiDatasetRwDetailsDtoTags
        from ..models.domino_datasetrw_api_dataset_rw_project_details_dto import (
            DominoDatasetrwApiDatasetRwProjectDetailsDto,
        )

        d = dict(src_dict)
        dataset_path = d.pop("datasetPath")

        projects = DominoDatasetrwApiDatasetRwProjectDetailsDto.from_dict(d.pop("projects"))

        lifecycle_status = DominoDatasetrwApiDatasetRwDetailsDtoLifecycleStatus(d.pop("lifecycleStatus"))

        snapshot_ids = cast(list[str], d.pop("snapshotIds"))

        read_write_snapshot_id = d.pop("readWriteSnapshotId")

        name = d.pop("name")

        id = d.pop("id")

        tags = DominoDatasetrwApiDatasetRwDetailsDtoTags.from_dict(d.pop("tags"))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        domino_datasetrw_api_dataset_rw_details_dto = cls(
            dataset_path=dataset_path,
            projects=projects,
            lifecycle_status=lifecycle_status,
            snapshot_ids=snapshot_ids,
            read_write_snapshot_id=read_write_snapshot_id,
            name=name,
            id=id,
            tags=tags,
            author=author,
            description=description,
        )

        domino_datasetrw_api_dataset_rw_details_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_details_dto

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
