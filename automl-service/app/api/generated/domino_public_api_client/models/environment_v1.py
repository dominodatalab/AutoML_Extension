from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_type_v1 import ClusterTypeV1
from ..models.environment_rebuild_on_base_changes_v1 import EnvironmentRebuildOnBaseChangesV1
from ..models.environment_visibility_v1 import EnvironmentVisibilityV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_owner_v1 import EnvironmentOwnerV1
    from ..models.environment_revision_v1 import EnvironmentRevisionV1


T = TypeVar("T", bound="EnvironmentV1")


@_attrs_define
class EnvironmentV1:
    """
    Attributes:
        archived (bool): Whether the environment is archived
        id (str): Id of environment Example: 623132867a0af0281c01a69c.
        name (str):  Example: MyOrg.
        rebuild_on_base_changes (EnvironmentRebuildOnBaseChangesV1): Whether to build a new revision when the base
            environment changes.
        supported_clusters (list[ClusterTypeV1]):
        visibility (EnvironmentVisibilityV1): Visibility of an environment. Private Environments are only visible to the
            creating user, whereas Organization owned Environments can be seen by all Org members.
        active_revision_tags (list[str] | Unset): The tags on the active revision for this environment
        internal_tags (list[str] | Unset): The internal tags specifying if this environment is restricted
        is_curated (bool | Unset): Whether or not the environment is curated for a deployment
        latest_revision (EnvironmentRevisionV1 | Unset):
        owner (EnvironmentOwnerV1 | Unset):
        restricted_revision (EnvironmentRevisionV1 | Unset):
        selected_revision (EnvironmentRevisionV1 | Unset):
    """

    archived: bool
    id: str
    name: str
    rebuild_on_base_changes: EnvironmentRebuildOnBaseChangesV1
    supported_clusters: list[ClusterTypeV1]
    visibility: EnvironmentVisibilityV1
    active_revision_tags: list[str] | Unset = UNSET
    internal_tags: list[str] | Unset = UNSET
    is_curated: bool | Unset = UNSET
    latest_revision: EnvironmentRevisionV1 | Unset = UNSET
    owner: EnvironmentOwnerV1 | Unset = UNSET
    restricted_revision: EnvironmentRevisionV1 | Unset = UNSET
    selected_revision: EnvironmentRevisionV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        id = self.id

        name = self.name

        rebuild_on_base_changes = self.rebuild_on_base_changes.value

        supported_clusters = []
        for supported_clusters_item_data in self.supported_clusters:
            supported_clusters_item = supported_clusters_item_data.value
            supported_clusters.append(supported_clusters_item)

        visibility = self.visibility.value

        active_revision_tags: list[str] | Unset = UNSET
        if not isinstance(self.active_revision_tags, Unset):
            active_revision_tags = self.active_revision_tags

        internal_tags: list[str] | Unset = UNSET
        if not isinstance(self.internal_tags, Unset):
            internal_tags = self.internal_tags

        is_curated = self.is_curated

        latest_revision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_revision, Unset):
            latest_revision = self.latest_revision.to_dict()

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        restricted_revision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restricted_revision, Unset):
            restricted_revision = self.restricted_revision.to_dict()

        selected_revision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_revision, Unset):
            selected_revision = self.selected_revision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archived": archived,
                "id": id,
                "name": name,
                "rebuildOnBaseChanges": rebuild_on_base_changes,
                "supportedClusters": supported_clusters,
                "visibility": visibility,
            }
        )
        if active_revision_tags is not UNSET:
            field_dict["activeRevisionTags"] = active_revision_tags
        if internal_tags is not UNSET:
            field_dict["internalTags"] = internal_tags
        if is_curated is not UNSET:
            field_dict["isCurated"] = is_curated
        if latest_revision is not UNSET:
            field_dict["latestRevision"] = latest_revision
        if owner is not UNSET:
            field_dict["owner"] = owner
        if restricted_revision is not UNSET:
            field_dict["restrictedRevision"] = restricted_revision
        if selected_revision is not UNSET:
            field_dict["selectedRevision"] = selected_revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_owner_v1 import EnvironmentOwnerV1
        from ..models.environment_revision_v1 import EnvironmentRevisionV1

        d = dict(src_dict)
        archived = d.pop("archived")

        id = d.pop("id")

        name = d.pop("name")

        rebuild_on_base_changes = EnvironmentRebuildOnBaseChangesV1(d.pop("rebuildOnBaseChanges"))

        supported_clusters = []
        _supported_clusters = d.pop("supportedClusters")
        for supported_clusters_item_data in _supported_clusters:
            supported_clusters_item = ClusterTypeV1(supported_clusters_item_data)

            supported_clusters.append(supported_clusters_item)

        visibility = EnvironmentVisibilityV1(d.pop("visibility"))

        active_revision_tags = cast(list[str], d.pop("activeRevisionTags", UNSET))

        internal_tags = cast(list[str], d.pop("internalTags", UNSET))

        is_curated = d.pop("isCurated", UNSET)

        _latest_revision = d.pop("latestRevision", UNSET)
        latest_revision: EnvironmentRevisionV1 | Unset
        if isinstance(_latest_revision, Unset):
            latest_revision = UNSET
        else:
            latest_revision = EnvironmentRevisionV1.from_dict(_latest_revision)

        _owner = d.pop("owner", UNSET)
        owner: EnvironmentOwnerV1 | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = EnvironmentOwnerV1.from_dict(_owner)

        _restricted_revision = d.pop("restrictedRevision", UNSET)
        restricted_revision: EnvironmentRevisionV1 | Unset
        if isinstance(_restricted_revision, Unset):
            restricted_revision = UNSET
        else:
            restricted_revision = EnvironmentRevisionV1.from_dict(_restricted_revision)

        _selected_revision = d.pop("selectedRevision", UNSET)
        selected_revision: EnvironmentRevisionV1 | Unset
        if isinstance(_selected_revision, Unset):
            selected_revision = UNSET
        else:
            selected_revision = EnvironmentRevisionV1.from_dict(_selected_revision)

        environment_v1 = cls(
            archived=archived,
            id=id,
            name=name,
            rebuild_on_base_changes=rebuild_on_base_changes,
            supported_clusters=supported_clusters,
            visibility=visibility,
            active_revision_tags=active_revision_tags,
            internal_tags=internal_tags,
            is_curated=is_curated,
            latest_revision=latest_revision,
            owner=owner,
            restricted_revision=restricted_revision,
            selected_revision=selected_revision,
        )

        environment_v1.additional_properties = d
        return environment_v1

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
