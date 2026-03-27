from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_environments_api_new_environment_cluster_types_type_0_item import (
    DominoEnvironmentsApiNewEnvironmentClusterTypesType0Item,
)
from ..models.domino_environments_api_new_environment_rebuild_on_base_changes import (
    DominoEnvironmentsApiNewEnvironmentRebuildOnBaseChanges,
)
from ..models.domino_environments_api_new_environment_visibility import DominoEnvironmentsApiNewEnvironmentVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_template_metadata import (
        DominoEnvironmentsApiEnvironmentTemplateMetadata,
    )


T = TypeVar("T", bound="DominoEnvironmentsApiNewEnvironment")


@_attrs_define
class DominoEnvironmentsApiNewEnvironment:
    """
    Attributes:
        name (str):
        description (str):
        visibility (DominoEnvironmentsApiNewEnvironmentVisibility):
        add_base_dependencies (bool):
        is_curated (bool):
        skip_first_build (bool):
        rebuild_on_base_changes (DominoEnvironmentsApiNewEnvironmentRebuildOnBaseChanges | Unset):
        assign_latest_revision_as_active (bool | None | Unset):
        owner_id (None | str | Unset):
        cluster_types (list[DominoEnvironmentsApiNewEnvironmentClusterTypesType0Item] | None | Unset):
        is_restricted (bool | None | Unset):
        projects_count (int | None | Unset):
        last_updated (datetime.datetime | None | Unset):
        template_metadata (DominoEnvironmentsApiEnvironmentTemplateMetadata | Unset):
    """

    name: str
    description: str
    visibility: DominoEnvironmentsApiNewEnvironmentVisibility
    add_base_dependencies: bool
    is_curated: bool
    skip_first_build: bool
    rebuild_on_base_changes: DominoEnvironmentsApiNewEnvironmentRebuildOnBaseChanges | Unset = UNSET
    assign_latest_revision_as_active: bool | None | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    cluster_types: list[DominoEnvironmentsApiNewEnvironmentClusterTypesType0Item] | None | Unset = UNSET
    is_restricted: bool | None | Unset = UNSET
    projects_count: int | None | Unset = UNSET
    last_updated: datetime.datetime | None | Unset = UNSET
    template_metadata: DominoEnvironmentsApiEnvironmentTemplateMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        visibility = self.visibility.value

        add_base_dependencies = self.add_base_dependencies

        is_curated = self.is_curated

        skip_first_build = self.skip_first_build

        rebuild_on_base_changes: str | Unset = UNSET
        if not isinstance(self.rebuild_on_base_changes, Unset):
            rebuild_on_base_changes = self.rebuild_on_base_changes.value

        assign_latest_revision_as_active: bool | None | Unset
        if isinstance(self.assign_latest_revision_as_active, Unset):
            assign_latest_revision_as_active = UNSET
        else:
            assign_latest_revision_as_active = self.assign_latest_revision_as_active

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        cluster_types: list[str] | None | Unset
        if isinstance(self.cluster_types, Unset):
            cluster_types = UNSET
        elif isinstance(self.cluster_types, list):
            cluster_types = []
            for cluster_types_type_0_item_data in self.cluster_types:
                cluster_types_type_0_item = cluster_types_type_0_item_data.value
                cluster_types.append(cluster_types_type_0_item)

        else:
            cluster_types = self.cluster_types

        is_restricted: bool | None | Unset
        if isinstance(self.is_restricted, Unset):
            is_restricted = UNSET
        else:
            is_restricted = self.is_restricted

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

        template_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_metadata, Unset):
            template_metadata = self.template_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "visibility": visibility,
                "addBaseDependencies": add_base_dependencies,
                "isCurated": is_curated,
                "skipFirstBuild": skip_first_build,
            }
        )
        if rebuild_on_base_changes is not UNSET:
            field_dict["rebuildOnBaseChanges"] = rebuild_on_base_changes
        if assign_latest_revision_as_active is not UNSET:
            field_dict["assignLatestRevisionAsActive"] = assign_latest_revision_as_active
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if cluster_types is not UNSET:
            field_dict["clusterTypes"] = cluster_types
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if projects_count is not UNSET:
            field_dict["projectsCount"] = projects_count
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if template_metadata is not UNSET:
            field_dict["templateMetadata"] = template_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_template_metadata import (
            DominoEnvironmentsApiEnvironmentTemplateMetadata,
        )

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        visibility = DominoEnvironmentsApiNewEnvironmentVisibility(d.pop("visibility"))

        add_base_dependencies = d.pop("addBaseDependencies")

        is_curated = d.pop("isCurated")

        skip_first_build = d.pop("skipFirstBuild")

        _rebuild_on_base_changes = d.pop("rebuildOnBaseChanges", UNSET)
        rebuild_on_base_changes: DominoEnvironmentsApiNewEnvironmentRebuildOnBaseChanges | Unset
        if isinstance(_rebuild_on_base_changes, Unset):
            rebuild_on_base_changes = UNSET
        else:
            rebuild_on_base_changes = DominoEnvironmentsApiNewEnvironmentRebuildOnBaseChanges(_rebuild_on_base_changes)

        def _parse_assign_latest_revision_as_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        assign_latest_revision_as_active = _parse_assign_latest_revision_as_active(
            d.pop("assignLatestRevisionAsActive", UNSET)
        )

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))

        def _parse_cluster_types(
            data: object,
        ) -> list[DominoEnvironmentsApiNewEnvironmentClusterTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cluster_types_type_0 = []
                _cluster_types_type_0 = data
                for cluster_types_type_0_item_data in _cluster_types_type_0:
                    cluster_types_type_0_item = DominoEnvironmentsApiNewEnvironmentClusterTypesType0Item(
                        cluster_types_type_0_item_data
                    )

                    cluster_types_type_0.append(cluster_types_type_0_item)

                return cluster_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoEnvironmentsApiNewEnvironmentClusterTypesType0Item] | None | Unset, data)

        cluster_types = _parse_cluster_types(d.pop("clusterTypes", UNSET))

        def _parse_is_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_restricted = _parse_is_restricted(d.pop("isRestricted", UNSET))

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

        _template_metadata = d.pop("templateMetadata", UNSET)
        template_metadata: DominoEnvironmentsApiEnvironmentTemplateMetadata | Unset
        if isinstance(_template_metadata, Unset):
            template_metadata = UNSET
        else:
            template_metadata = DominoEnvironmentsApiEnvironmentTemplateMetadata.from_dict(_template_metadata)

        domino_environments_api_new_environment = cls(
            name=name,
            description=description,
            visibility=visibility,
            add_base_dependencies=add_base_dependencies,
            is_curated=is_curated,
            skip_first_build=skip_first_build,
            rebuild_on_base_changes=rebuild_on_base_changes,
            assign_latest_revision_as_active=assign_latest_revision_as_active,
            owner_id=owner_id,
            cluster_types=cluster_types,
            is_restricted=is_restricted,
            projects_count=projects_count,
            last_updated=last_updated,
            template_metadata=template_metadata,
        )

        domino_environments_api_new_environment.additional_properties = d
        return domino_environments_api_new_environment

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
