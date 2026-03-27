from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compute_cluster_type import ComputeClusterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_selected_v2_environment_details_dto import (
        DominoProjectsApiSelectedV2EnvironmentDetailsDTO,
    )


T = TypeVar("T", bound="DominoProjectsApiSelectedEnvironmentDTO")


@_attrs_define
class DominoProjectsApiSelectedEnvironmentDTO:
    """
    Attributes:
        id (str):
        name (str):
        supported_clusters (list[ComputeClusterType]):
        v_2_environment_details (DominoProjectsApiSelectedV2EnvironmentDetailsDTO | Unset):
        active_revision_tags (list[str] | None | Unset):
        is_curated (bool | None | Unset):
    """

    id: str
    name: str
    supported_clusters: list[ComputeClusterType]
    v_2_environment_details: DominoProjectsApiSelectedV2EnvironmentDetailsDTO | Unset = UNSET
    active_revision_tags: list[str] | None | Unset = UNSET
    is_curated: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        supported_clusters = []
        for supported_clusters_item_data in self.supported_clusters:
            supported_clusters_item = supported_clusters_item_data.value
            supported_clusters.append(supported_clusters_item)

        v_2_environment_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.v_2_environment_details, Unset):
            v_2_environment_details = self.v_2_environment_details.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "supportedClusters": supported_clusters,
            }
        )
        if v_2_environment_details is not UNSET:
            field_dict["v2EnvironmentDetails"] = v_2_environment_details
        if active_revision_tags is not UNSET:
            field_dict["activeRevisionTags"] = active_revision_tags
        if is_curated is not UNSET:
            field_dict["isCurated"] = is_curated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_selected_v2_environment_details_dto import (
            DominoProjectsApiSelectedV2EnvironmentDetailsDTO,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        supported_clusters = []
        _supported_clusters = d.pop("supportedClusters")
        for supported_clusters_item_data in _supported_clusters:
            supported_clusters_item = ComputeClusterType(supported_clusters_item_data)

            supported_clusters.append(supported_clusters_item)

        _v_2_environment_details = d.pop("v2EnvironmentDetails", UNSET)
        v_2_environment_details: DominoProjectsApiSelectedV2EnvironmentDetailsDTO | Unset
        if isinstance(_v_2_environment_details, Unset):
            v_2_environment_details = UNSET
        else:
            v_2_environment_details = DominoProjectsApiSelectedV2EnvironmentDetailsDTO.from_dict(
                _v_2_environment_details
            )

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

        domino_projects_api_selected_environment_dto = cls(
            id=id,
            name=name,
            supported_clusters=supported_clusters,
            v_2_environment_details=v_2_environment_details,
            active_revision_tags=active_revision_tags,
            is_curated=is_curated,
        )

        domino_projects_api_selected_environment_dto.additional_properties = d
        return domino_projects_api_selected_environment_dto

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
