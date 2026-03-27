from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_environments_api_environment_rebuild_on_base_changes import (
    DominoEnvironmentsApiEnvironmentRebuildOnBaseChanges,
)
from ..models.domino_environments_api_environment_supported_clusters_item import (
    DominoEnvironmentsApiEnvironmentSupportedClustersItem,
)
from ..models.domino_environments_api_environment_visibility import DominoEnvironmentsApiEnvironmentVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_owner import DominoEnvironmentsApiEnvironmentOwner


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironment")


@_attrs_define
class DominoEnvironmentsApiEnvironment:
    """
    Attributes:
        id (str):
        description (str):
        archived (bool):
        name (str):
        visibility (DominoEnvironmentsApiEnvironmentVisibility):
        supported_clusters (list[DominoEnvironmentsApiEnvironmentSupportedClustersItem]):
        is_curated (bool):
        rebuild_on_base_changes (DominoEnvironmentsApiEnvironmentRebuildOnBaseChanges | Unset):
        assign_latest_revision_as_active (bool | None | Unset):
        owner (DominoEnvironmentsApiEnvironmentOwner | Unset):
        active_revision_tags (list[str] | None | Unset):
        internal_tags (list[str] | None | Unset):
    """

    id: str
    description: str
    archived: bool
    name: str
    visibility: DominoEnvironmentsApiEnvironmentVisibility
    supported_clusters: list[DominoEnvironmentsApiEnvironmentSupportedClustersItem]
    is_curated: bool
    rebuild_on_base_changes: DominoEnvironmentsApiEnvironmentRebuildOnBaseChanges | Unset = UNSET
    assign_latest_revision_as_active: bool | None | Unset = UNSET
    owner: DominoEnvironmentsApiEnvironmentOwner | Unset = UNSET
    active_revision_tags: list[str] | None | Unset = UNSET
    internal_tags: list[str] | None | Unset = UNSET
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

        is_curated = self.is_curated

        rebuild_on_base_changes: str | Unset = UNSET
        if not isinstance(self.rebuild_on_base_changes, Unset):
            rebuild_on_base_changes = self.rebuild_on_base_changes.value

        assign_latest_revision_as_active: bool | None | Unset
        if isinstance(self.assign_latest_revision_as_active, Unset):
            assign_latest_revision_as_active = UNSET
        else:
            assign_latest_revision_as_active = self.assign_latest_revision_as_active

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

        internal_tags: list[str] | None | Unset
        if isinstance(self.internal_tags, Unset):
            internal_tags = UNSET
        elif isinstance(self.internal_tags, list):
            internal_tags = self.internal_tags

        else:
            internal_tags = self.internal_tags

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
                "isCurated": is_curated,
            }
        )
        if rebuild_on_base_changes is not UNSET:
            field_dict["rebuildOnBaseChanges"] = rebuild_on_base_changes
        if assign_latest_revision_as_active is not UNSET:
            field_dict["assignLatestRevisionAsActive"] = assign_latest_revision_as_active
        if owner is not UNSET:
            field_dict["owner"] = owner
        if active_revision_tags is not UNSET:
            field_dict["activeRevisionTags"] = active_revision_tags
        if internal_tags is not UNSET:
            field_dict["internalTags"] = internal_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_owner import DominoEnvironmentsApiEnvironmentOwner

        d = dict(src_dict)
        id = d.pop("id")

        description = d.pop("description")

        archived = d.pop("archived")

        name = d.pop("name")

        visibility = DominoEnvironmentsApiEnvironmentVisibility(d.pop("visibility"))

        supported_clusters = []
        _supported_clusters = d.pop("supportedClusters")
        for supported_clusters_item_data in _supported_clusters:
            supported_clusters_item = DominoEnvironmentsApiEnvironmentSupportedClustersItem(
                supported_clusters_item_data
            )

            supported_clusters.append(supported_clusters_item)

        is_curated = d.pop("isCurated")

        _rebuild_on_base_changes = d.pop("rebuildOnBaseChanges", UNSET)
        rebuild_on_base_changes: DominoEnvironmentsApiEnvironmentRebuildOnBaseChanges | Unset
        if isinstance(_rebuild_on_base_changes, Unset):
            rebuild_on_base_changes = UNSET
        else:
            rebuild_on_base_changes = DominoEnvironmentsApiEnvironmentRebuildOnBaseChanges(_rebuild_on_base_changes)

        def _parse_assign_latest_revision_as_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        assign_latest_revision_as_active = _parse_assign_latest_revision_as_active(
            d.pop("assignLatestRevisionAsActive", UNSET)
        )

        _owner = d.pop("owner", UNSET)
        owner: DominoEnvironmentsApiEnvironmentOwner | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = DominoEnvironmentsApiEnvironmentOwner.from_dict(_owner)

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

        domino_environments_api_environment = cls(
            id=id,
            description=description,
            archived=archived,
            name=name,
            visibility=visibility,
            supported_clusters=supported_clusters,
            is_curated=is_curated,
            rebuild_on_base_changes=rebuild_on_base_changes,
            assign_latest_revision_as_active=assign_latest_revision_as_active,
            owner=owner,
            active_revision_tags=active_revision_tags,
            internal_tags=internal_tags,
        )

        domino_environments_api_environment.additional_properties = d
        return domino_environments_api_environment

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
