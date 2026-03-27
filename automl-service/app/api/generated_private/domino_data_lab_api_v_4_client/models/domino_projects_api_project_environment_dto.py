from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compute_cluster_type import ComputeClusterType
from ..models.domino_projects_api_project_environment_dto_visibility import (
    DominoProjectsApiProjectEnvironmentDTOVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_environment_owner_dto import DominoProjectsApiProjectEnvironmentOwnerDTO


T = TypeVar("T", bound="DominoProjectsApiProjectEnvironmentDTO")


@_attrs_define
class DominoProjectsApiProjectEnvironmentDTO:
    """
    Attributes:
        id (str):
        archived (bool):
        name (str):
        version (int):
        visibility (DominoProjectsApiProjectEnvironmentDTOVisibility):
        supported_clusters (list[ComputeClusterType]):
        owner (DominoProjectsApiProjectEnvironmentOwnerDTO | Unset):
        active_revision_tags (list[str] | None | Unset):
        is_curated (bool | None | Unset):
        active_revision_number (int | None | Unset):
        active_revision_id (None | str | Unset):
        restricted_revision_number (int | None | Unset):
        restricted_revision_id (None | str | Unset):
    """

    id: str
    archived: bool
    name: str
    version: int
    visibility: DominoProjectsApiProjectEnvironmentDTOVisibility
    supported_clusters: list[ComputeClusterType]
    owner: DominoProjectsApiProjectEnvironmentOwnerDTO | Unset = UNSET
    active_revision_tags: list[str] | None | Unset = UNSET
    is_curated: bool | None | Unset = UNSET
    active_revision_number: int | None | Unset = UNSET
    active_revision_id: None | str | Unset = UNSET
    restricted_revision_number: int | None | Unset = UNSET
    restricted_revision_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        archived = self.archived

        name = self.name

        version = self.version

        visibility = self.visibility.value

        supported_clusters = []
        for supported_clusters_item_data in self.supported_clusters:
            supported_clusters_item = supported_clusters_item_data.value
            supported_clusters.append(supported_clusters_item)

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        active_revision_tags: list[str] | None | Unset
        if isinstance(self.active_revision_tags, Unset):
            active_revision_tags = UNSET
        elif isinstance(self.active_revision_tags, list):
            active_revision_tags = self.active_revision_tags

        else:
            active_revision_tags = self.active_revision_tags

        is_curated: bool | None | Unset
        if isinstance(self.is_curated, Unset):
            is_curated = UNSET
        else:
            is_curated = self.is_curated

        active_revision_number: int | None | Unset
        if isinstance(self.active_revision_number, Unset):
            active_revision_number = UNSET
        else:
            active_revision_number = self.active_revision_number

        active_revision_id: None | str | Unset
        if isinstance(self.active_revision_id, Unset):
            active_revision_id = UNSET
        else:
            active_revision_id = self.active_revision_id

        restricted_revision_number: int | None | Unset
        if isinstance(self.restricted_revision_number, Unset):
            restricted_revision_number = UNSET
        else:
            restricted_revision_number = self.restricted_revision_number

        restricted_revision_id: None | str | Unset
        if isinstance(self.restricted_revision_id, Unset):
            restricted_revision_id = UNSET
        else:
            restricted_revision_id = self.restricted_revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "archived": archived,
                "name": name,
                "version": version,
                "visibility": visibility,
                "supportedClusters": supported_clusters,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if active_revision_tags is not UNSET:
            field_dict["activeRevisionTags"] = active_revision_tags
        if is_curated is not UNSET:
            field_dict["isCurated"] = is_curated
        if active_revision_number is not UNSET:
            field_dict["activeRevisionNumber"] = active_revision_number
        if active_revision_id is not UNSET:
            field_dict["activeRevisionId"] = active_revision_id
        if restricted_revision_number is not UNSET:
            field_dict["restrictedRevisionNumber"] = restricted_revision_number
        if restricted_revision_id is not UNSET:
            field_dict["restrictedRevisionId"] = restricted_revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_environment_owner_dto import (
            DominoProjectsApiProjectEnvironmentOwnerDTO,
        )

        d = dict(src_dict)
        id = d.pop("id")

        archived = d.pop("archived")

        name = d.pop("name")

        version = d.pop("version")

        visibility = DominoProjectsApiProjectEnvironmentDTOVisibility(d.pop("visibility"))

        supported_clusters = []
        _supported_clusters = d.pop("supportedClusters")
        for supported_clusters_item_data in _supported_clusters:
            supported_clusters_item = ComputeClusterType(supported_clusters_item_data)

            supported_clusters.append(supported_clusters_item)

        _owner = d.pop("owner", UNSET)
        owner: DominoProjectsApiProjectEnvironmentOwnerDTO | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = DominoProjectsApiProjectEnvironmentOwnerDTO.from_dict(_owner)

        def _parse_active_revision_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                active_revision_tags_type_0 = cast(list[str], data)

                return active_revision_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        active_revision_tags = _parse_active_revision_tags(d.pop("activeRevisionTags", UNSET))

        def _parse_is_curated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_curated = _parse_is_curated(d.pop("isCurated", UNSET))

        def _parse_active_revision_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        active_revision_number = _parse_active_revision_number(d.pop("activeRevisionNumber", UNSET))

        def _parse_active_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        active_revision_id = _parse_active_revision_id(d.pop("activeRevisionId", UNSET))

        def _parse_restricted_revision_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        restricted_revision_number = _parse_restricted_revision_number(d.pop("restrictedRevisionNumber", UNSET))

        def _parse_restricted_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        restricted_revision_id = _parse_restricted_revision_id(d.pop("restrictedRevisionId", UNSET))

        domino_projects_api_project_environment_dto = cls(
            id=id,
            archived=archived,
            name=name,
            version=version,
            visibility=visibility,
            supported_clusters=supported_clusters,
            owner=owner,
            active_revision_tags=active_revision_tags,
            is_curated=is_curated,
            active_revision_number=active_revision_number,
            active_revision_id=active_revision_id,
            restricted_revision_number=restricted_revision_number,
            restricted_revision_id=restricted_revision_id,
        )

        domino_projects_api_project_environment_dto.additional_properties = d
        return domino_projects_api_project_environment_dto

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
