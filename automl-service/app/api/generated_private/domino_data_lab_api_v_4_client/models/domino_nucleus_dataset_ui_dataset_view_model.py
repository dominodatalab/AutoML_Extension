from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_nucleus_dataset_ui_dataset_view_model_tags import DominoNucleusDatasetUiDatasetViewModelTags


T = TypeVar("T", bound="DominoNucleusDatasetUiDatasetViewModel")


@_attrs_define
class DominoNucleusDatasetUiDatasetViewModel:
    """
    Attributes:
        snapshot_ids (list[str]):
        name (str):
        id (str):
        tags (DominoNucleusDatasetUiDatasetViewModelTags):
        description (None | str | Unset):
        project_owner (None | str | Unset):
        project_name (None | str | Unset):
    """

    snapshot_ids: list[str]
    name: str
    id: str
    tags: DominoNucleusDatasetUiDatasetViewModelTags
    description: None | str | Unset = UNSET
    project_owner: None | str | Unset = UNSET
    project_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_ids = self.snapshot_ids

        name = self.name

        id = self.id

        tags = self.tags.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        project_owner: None | str | Unset
        if isinstance(self.project_owner, Unset):
            project_owner = UNSET
        else:
            project_owner = self.project_owner

        project_name: None | str | Unset
        if isinstance(self.project_name, Unset):
            project_name = UNSET
        else:
            project_name = self.project_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshotIds": snapshot_ids,
                "name": name,
                "id": id,
                "tags": tags,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if project_owner is not UNSET:
            field_dict["projectOwner"] = project_owner
        if project_name is not UNSET:
            field_dict["projectName"] = project_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_dataset_ui_dataset_view_model_tags import (
            DominoNucleusDatasetUiDatasetViewModelTags,
        )

        d = dict(src_dict)
        snapshot_ids = cast(list[str], d.pop("snapshotIds"))

        name = d.pop("name")

        id = d.pop("id")

        tags = DominoNucleusDatasetUiDatasetViewModelTags.from_dict(d.pop("tags"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_project_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_owner = _parse_project_owner(d.pop("projectOwner", UNSET))

        def _parse_project_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_name = _parse_project_name(d.pop("projectName", UNSET))

        domino_nucleus_dataset_ui_dataset_view_model = cls(
            snapshot_ids=snapshot_ids,
            name=name,
            id=id,
            tags=tags,
            description=description,
            project_owner=project_owner,
            project_name=project_name,
        )

        domino_nucleus_dataset_ui_dataset_view_model.additional_properties = d
        return domino_nucleus_dataset_ui_dataset_view_model

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
