from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compute_cluster_type import ComputeClusterType
from ..models.domino_projects_api_environment_details_visibility import DominoProjectsApiEnvironmentDetailsVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_template_metadata import (
        DominoEnvironmentsApiEnvironmentTemplateMetadata,
    )
    from ..models.domino_projects_api_environment_owner import DominoProjectsApiEnvironmentOwner
    from ..models.domino_projects_api_revision_overview import DominoProjectsApiRevisionOverview


T = TypeVar("T", bound="DominoProjectsApiEnvironmentDetails")


@_attrs_define
class DominoProjectsApiEnvironmentDetails:
    """
    Attributes:
        id (str):
        archived (bool):
        name (str):
        visibility (DominoProjectsApiEnvironmentDetailsVisibility):
        supported_clusters (list[ComputeClusterType]):
        owner (DominoProjectsApiEnvironmentOwner | Unset):
        latest_revision (DominoProjectsApiRevisionOverview | Unset):
        selected_revision (DominoProjectsApiRevisionOverview | Unset):
        restricted_revision (DominoProjectsApiRevisionOverview | Unset):
        is_curated (bool | None | Unset):
        template_metadata (DominoEnvironmentsApiEnvironmentTemplateMetadata | Unset):
    """

    id: str
    archived: bool
    name: str
    visibility: DominoProjectsApiEnvironmentDetailsVisibility
    supported_clusters: list[ComputeClusterType]
    owner: DominoProjectsApiEnvironmentOwner | Unset = UNSET
    latest_revision: DominoProjectsApiRevisionOverview | Unset = UNSET
    selected_revision: DominoProjectsApiRevisionOverview | Unset = UNSET
    restricted_revision: DominoProjectsApiRevisionOverview | Unset = UNSET
    is_curated: bool | None | Unset = UNSET
    template_metadata: DominoEnvironmentsApiEnvironmentTemplateMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        archived = self.archived

        name = self.name

        visibility = self.visibility.value

        supported_clusters = []
        for supported_clusters_item_data in self.supported_clusters:
            supported_clusters_item = supported_clusters_item_data.value
            supported_clusters.append(supported_clusters_item)

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        latest_revision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_revision, Unset):
            latest_revision = self.latest_revision.to_dict()

        selected_revision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_revision, Unset):
            selected_revision = self.selected_revision.to_dict()

        restricted_revision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restricted_revision, Unset):
            restricted_revision = self.restricted_revision.to_dict()

        is_curated: bool | None | Unset
        if isinstance(self.is_curated, Unset):
            is_curated = UNSET
        else:
            is_curated = self.is_curated

        template_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_metadata, Unset):
            template_metadata = self.template_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "archived": archived,
                "name": name,
                "visibility": visibility,
                "supportedClusters": supported_clusters,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if latest_revision is not UNSET:
            field_dict["latestRevision"] = latest_revision
        if selected_revision is not UNSET:
            field_dict["selectedRevision"] = selected_revision
        if restricted_revision is not UNSET:
            field_dict["restrictedRevision"] = restricted_revision
        if is_curated is not UNSET:
            field_dict["isCurated"] = is_curated
        if template_metadata is not UNSET:
            field_dict["templateMetadata"] = template_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_template_metadata import (
            DominoEnvironmentsApiEnvironmentTemplateMetadata,
        )
        from ..models.domino_projects_api_environment_owner import DominoProjectsApiEnvironmentOwner
        from ..models.domino_projects_api_revision_overview import DominoProjectsApiRevisionOverview

        d = dict(src_dict)
        id = d.pop("id")

        archived = d.pop("archived")

        name = d.pop("name")

        visibility = DominoProjectsApiEnvironmentDetailsVisibility(d.pop("visibility"))

        supported_clusters = []
        _supported_clusters = d.pop("supportedClusters")
        for supported_clusters_item_data in _supported_clusters:
            supported_clusters_item = ComputeClusterType(supported_clusters_item_data)

            supported_clusters.append(supported_clusters_item)

        _owner = d.pop("owner", UNSET)
        owner: DominoProjectsApiEnvironmentOwner | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = DominoProjectsApiEnvironmentOwner.from_dict(_owner)

        _latest_revision = d.pop("latestRevision", UNSET)
        latest_revision: DominoProjectsApiRevisionOverview | Unset
        if isinstance(_latest_revision, Unset):
            latest_revision = UNSET
        else:
            latest_revision = DominoProjectsApiRevisionOverview.from_dict(_latest_revision)

        _selected_revision = d.pop("selectedRevision", UNSET)
        selected_revision: DominoProjectsApiRevisionOverview | Unset
        if isinstance(_selected_revision, Unset):
            selected_revision = UNSET
        else:
            selected_revision = DominoProjectsApiRevisionOverview.from_dict(_selected_revision)

        _restricted_revision = d.pop("restrictedRevision", UNSET)
        restricted_revision: DominoProjectsApiRevisionOverview | Unset
        if isinstance(_restricted_revision, Unset):
            restricted_revision = UNSET
        else:
            restricted_revision = DominoProjectsApiRevisionOverview.from_dict(_restricted_revision)

        def _parse_is_curated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_curated = _parse_is_curated(d.pop("isCurated", UNSET))

        _template_metadata = d.pop("templateMetadata", UNSET)
        template_metadata: DominoEnvironmentsApiEnvironmentTemplateMetadata | Unset
        if isinstance(_template_metadata, Unset):
            template_metadata = UNSET
        else:
            template_metadata = DominoEnvironmentsApiEnvironmentTemplateMetadata.from_dict(_template_metadata)

        domino_projects_api_environment_details = cls(
            id=id,
            archived=archived,
            name=name,
            visibility=visibility,
            supported_clusters=supported_clusters,
            owner=owner,
            latest_revision=latest_revision,
            selected_revision=selected_revision,
            restricted_revision=restricted_revision,
            is_curated=is_curated,
            template_metadata=template_metadata,
        )

        domino_projects_api_environment_details.additional_properties = d
        return domino_projects_api_environment_details

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
