from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_environments_api_environment_details_rebuild_on_base_changes import (
    DominoEnvironmentsApiEnvironmentDetailsRebuildOnBaseChanges,
)
from ..models.domino_environments_api_environment_details_supported_clusters_item import (
    DominoEnvironmentsApiEnvironmentDetailsSupportedClustersItem,
)
from ..models.domino_environments_api_environment_details_visibility import (
    DominoEnvironmentsApiEnvironmentDetailsVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_base_drift import DominoEnvironmentsApiEnvironmentBaseDrift
    from ..models.domino_environments_api_environment_owner import DominoEnvironmentsApiEnvironmentOwner
    from ..models.domino_environments_api_environment_revision import DominoEnvironmentsApiEnvironmentRevision
    from ..models.domino_environments_api_environment_template_metadata import (
        DominoEnvironmentsApiEnvironmentTemplateMetadata,
    )
    from ..models.domino_environments_api_revision_overview import DominoEnvironmentsApiRevisionOverview


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentDetails")


@_attrs_define
class DominoEnvironmentsApiEnvironmentDetails:
    """
    Attributes:
        id (str):
        description (str):
        archived (bool):
        name (str):
        visibility (DominoEnvironmentsApiEnvironmentDetailsVisibility):
        supported_clusters (list[DominoEnvironmentsApiEnvironmentDetailsSupportedClustersItem]):
        owner (DominoEnvironmentsApiEnvironmentOwner | Unset):
        latest_revision (DominoEnvironmentsApiRevisionOverview | Unset):
        selected_revision (DominoEnvironmentsApiRevisionOverview | Unset):
        restricted_revision (DominoEnvironmentsApiRevisionOverview | Unset):
        base_dependencies_init_image (None | str | Unset):
        is_curated (bool | None | Unset):
        active_revision_tags (list[str] | None | Unset):
        internal_tags (list[str] | None | Unset):
        projects_count (int | None | Unset):
        last_updated (datetime.datetime | None | Unset):
        latest_revision_details (DominoEnvironmentsApiEnvironmentRevision | Unset):
        base (DominoEnvironmentsApiEnvironmentRevision | Unset):
        rebuild_on_base_changes (DominoEnvironmentsApiEnvironmentDetailsRebuildOnBaseChanges | Unset):
        assign_latest_revision_as_active (bool | None | Unset):
        template_metadata (DominoEnvironmentsApiEnvironmentTemplateMetadata | Unset):
        base_drift (DominoEnvironmentsApiEnvironmentBaseDrift | Unset):
    """

    id: str
    description: str
    archived: bool
    name: str
    visibility: DominoEnvironmentsApiEnvironmentDetailsVisibility
    supported_clusters: list[DominoEnvironmentsApiEnvironmentDetailsSupportedClustersItem]
    owner: DominoEnvironmentsApiEnvironmentOwner | Unset = UNSET
    latest_revision: DominoEnvironmentsApiRevisionOverview | Unset = UNSET
    selected_revision: DominoEnvironmentsApiRevisionOverview | Unset = UNSET
    restricted_revision: DominoEnvironmentsApiRevisionOverview | Unset = UNSET
    base_dependencies_init_image: None | str | Unset = UNSET
    is_curated: bool | None | Unset = UNSET
    active_revision_tags: list[str] | None | Unset = UNSET
    internal_tags: list[str] | None | Unset = UNSET
    projects_count: int | None | Unset = UNSET
    last_updated: datetime.datetime | None | Unset = UNSET
    latest_revision_details: DominoEnvironmentsApiEnvironmentRevision | Unset = UNSET
    base: DominoEnvironmentsApiEnvironmentRevision | Unset = UNSET
    rebuild_on_base_changes: DominoEnvironmentsApiEnvironmentDetailsRebuildOnBaseChanges | Unset = UNSET
    assign_latest_revision_as_active: bool | None | Unset = UNSET
    template_metadata: DominoEnvironmentsApiEnvironmentTemplateMetadata | Unset = UNSET
    base_drift: DominoEnvironmentsApiEnvironmentBaseDrift | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

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

        base_dependencies_init_image: None | str | Unset
        if isinstance(self.base_dependencies_init_image, Unset):
            base_dependencies_init_image = UNSET
        else:
            base_dependencies_init_image = self.base_dependencies_init_image

        is_curated: bool | None | Unset
        if isinstance(self.is_curated, Unset):
            is_curated = UNSET
        else:
            is_curated = self.is_curated

        active_revision_tags: list[str] | None | Unset
        if isinstance(self.active_revision_tags, Unset):
            active_revision_tags = UNSET
        elif isinstance(self.active_revision_tags, list):
            active_revision_tags = self.active_revision_tags

        else:
            active_revision_tags = self.active_revision_tags

        internal_tags: list[str] | None | Unset
        if isinstance(self.internal_tags, Unset):
            internal_tags = UNSET
        elif isinstance(self.internal_tags, list):
            internal_tags = self.internal_tags

        else:
            internal_tags = self.internal_tags

        projects_count: int | None | Unset
        if isinstance(self.projects_count, Unset):
            projects_count = UNSET
        else:
            projects_count = self.projects_count

        last_updated: None | str | Unset
        if isinstance(self.last_updated, Unset):
            last_updated = UNSET
        elif isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        latest_revision_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_revision_details, Unset):
            latest_revision_details = self.latest_revision_details.to_dict()

        base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base, Unset):
            base = self.base.to_dict()

        rebuild_on_base_changes: str | Unset = UNSET
        if not isinstance(self.rebuild_on_base_changes, Unset):
            rebuild_on_base_changes = self.rebuild_on_base_changes.value

        assign_latest_revision_as_active: bool | None | Unset
        if isinstance(self.assign_latest_revision_as_active, Unset):
            assign_latest_revision_as_active = UNSET
        else:
            assign_latest_revision_as_active = self.assign_latest_revision_as_active

        template_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_metadata, Unset):
            template_metadata = self.template_metadata.to_dict()

        base_drift: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_drift, Unset):
            base_drift = self.base_drift.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "description": description,
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
        if base_dependencies_init_image is not UNSET:
            field_dict["baseDependenciesInitImage"] = base_dependencies_init_image
        if is_curated is not UNSET:
            field_dict["isCurated"] = is_curated
        if active_revision_tags is not UNSET:
            field_dict["activeRevisionTags"] = active_revision_tags
        if internal_tags is not UNSET:
            field_dict["internalTags"] = internal_tags
        if projects_count is not UNSET:
            field_dict["projectsCount"] = projects_count
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if latest_revision_details is not UNSET:
            field_dict["latestRevisionDetails"] = latest_revision_details
        if base is not UNSET:
            field_dict["base"] = base
        if rebuild_on_base_changes is not UNSET:
            field_dict["rebuildOnBaseChanges"] = rebuild_on_base_changes
        if assign_latest_revision_as_active is not UNSET:
            field_dict["assignLatestRevisionAsActive"] = assign_latest_revision_as_active
        if template_metadata is not UNSET:
            field_dict["templateMetadata"] = template_metadata
        if base_drift is not UNSET:
            field_dict["baseDrift"] = base_drift

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_base_drift import DominoEnvironmentsApiEnvironmentBaseDrift
        from ..models.domino_environments_api_environment_owner import DominoEnvironmentsApiEnvironmentOwner
        from ..models.domino_environments_api_environment_revision import DominoEnvironmentsApiEnvironmentRevision
        from ..models.domino_environments_api_environment_template_metadata import (
            DominoEnvironmentsApiEnvironmentTemplateMetadata,
        )
        from ..models.domino_environments_api_revision_overview import DominoEnvironmentsApiRevisionOverview

        d = dict(src_dict)
        id = d.pop("id")

        description = d.pop("description")

        archived = d.pop("archived")

        name = d.pop("name")

        visibility = DominoEnvironmentsApiEnvironmentDetailsVisibility(d.pop("visibility"))

        supported_clusters = []
        _supported_clusters = d.pop("supportedClusters")
        for supported_clusters_item_data in _supported_clusters:
            supported_clusters_item = DominoEnvironmentsApiEnvironmentDetailsSupportedClustersItem(
                supported_clusters_item_data
            )

            supported_clusters.append(supported_clusters_item)

        _owner = d.pop("owner", UNSET)
        owner: DominoEnvironmentsApiEnvironmentOwner | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = DominoEnvironmentsApiEnvironmentOwner.from_dict(_owner)

        _latest_revision = d.pop("latestRevision", UNSET)
        latest_revision: DominoEnvironmentsApiRevisionOverview | Unset
        if isinstance(_latest_revision, Unset):
            latest_revision = UNSET
        else:
            latest_revision = DominoEnvironmentsApiRevisionOverview.from_dict(_latest_revision)

        _selected_revision = d.pop("selectedRevision", UNSET)
        selected_revision: DominoEnvironmentsApiRevisionOverview | Unset
        if isinstance(_selected_revision, Unset):
            selected_revision = UNSET
        else:
            selected_revision = DominoEnvironmentsApiRevisionOverview.from_dict(_selected_revision)

        _restricted_revision = d.pop("restrictedRevision", UNSET)
        restricted_revision: DominoEnvironmentsApiRevisionOverview | Unset
        if isinstance(_restricted_revision, Unset):
            restricted_revision = UNSET
        else:
            restricted_revision = DominoEnvironmentsApiRevisionOverview.from_dict(_restricted_revision)

        def _parse_base_dependencies_init_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_dependencies_init_image = _parse_base_dependencies_init_image(d.pop("baseDependenciesInitImage", UNSET))

        def _parse_is_curated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_curated = _parse_is_curated(d.pop("isCurated", UNSET))

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

        def _parse_internal_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                internal_tags_type_0 = cast(list[str], data)

                return internal_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        internal_tags = _parse_internal_tags(d.pop("internalTags", UNSET))

        def _parse_projects_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        projects_count = _parse_projects_count(d.pop("projectsCount", UNSET))

        def _parse_last_updated(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = isoparse(data)

                return last_updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_updated = _parse_last_updated(d.pop("lastUpdated", UNSET))

        _latest_revision_details = d.pop("latestRevisionDetails", UNSET)
        latest_revision_details: DominoEnvironmentsApiEnvironmentRevision | Unset
        if isinstance(_latest_revision_details, Unset):
            latest_revision_details = UNSET
        else:
            latest_revision_details = DominoEnvironmentsApiEnvironmentRevision.from_dict(_latest_revision_details)

        _base = d.pop("base", UNSET)
        base: DominoEnvironmentsApiEnvironmentRevision | Unset
        if isinstance(_base, Unset):
            base = UNSET
        else:
            base = DominoEnvironmentsApiEnvironmentRevision.from_dict(_base)

        _rebuild_on_base_changes = d.pop("rebuildOnBaseChanges", UNSET)
        rebuild_on_base_changes: DominoEnvironmentsApiEnvironmentDetailsRebuildOnBaseChanges | Unset
        if isinstance(_rebuild_on_base_changes, Unset):
            rebuild_on_base_changes = UNSET
        else:
            rebuild_on_base_changes = DominoEnvironmentsApiEnvironmentDetailsRebuildOnBaseChanges(
                _rebuild_on_base_changes
            )

        def _parse_assign_latest_revision_as_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        assign_latest_revision_as_active = _parse_assign_latest_revision_as_active(
            d.pop("assignLatestRevisionAsActive", UNSET)
        )

        _template_metadata = d.pop("templateMetadata", UNSET)
        template_metadata: DominoEnvironmentsApiEnvironmentTemplateMetadata | Unset
        if isinstance(_template_metadata, Unset):
            template_metadata = UNSET
        else:
            template_metadata = DominoEnvironmentsApiEnvironmentTemplateMetadata.from_dict(_template_metadata)

        _base_drift = d.pop("baseDrift", UNSET)
        base_drift: DominoEnvironmentsApiEnvironmentBaseDrift | Unset
        if isinstance(_base_drift, Unset):
            base_drift = UNSET
        else:
            base_drift = DominoEnvironmentsApiEnvironmentBaseDrift.from_dict(_base_drift)

        domino_environments_api_environment_details = cls(
            id=id,
            description=description,
            archived=archived,
            name=name,
            visibility=visibility,
            supported_clusters=supported_clusters,
            owner=owner,
            latest_revision=latest_revision,
            selected_revision=selected_revision,
            restricted_revision=restricted_revision,
            base_dependencies_init_image=base_dependencies_init_image,
            is_curated=is_curated,
            active_revision_tags=active_revision_tags,
            internal_tags=internal_tags,
            projects_count=projects_count,
            last_updated=last_updated,
            latest_revision_details=latest_revision_details,
            base=base,
            rebuild_on_base_changes=rebuild_on_base_changes,
            assign_latest_revision_as_active=assign_latest_revision_as_active,
            template_metadata=template_metadata,
            base_drift=base_drift,
        )

        domino_environments_api_environment_details.additional_properties = d
        return domino_environments_api_environment_details

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
