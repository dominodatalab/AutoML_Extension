from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_autoscaling_specification import AppAutoscalingSpecification
    from ..models.app_version_tag import AppVersionTag
    from ..models.git_ref import GitRef


T = TypeVar("T", bound="AppVersionCreationRequest")


@_attrs_define
class AppVersionCreationRequest:
    """
    Attributes:
        autoscaling_specification (AppAutoscalingSpecification | Unset):
        bundle_id (str | Unset):
        dfs_commit_id (str | Unset):
        entry_script (str | Unset): Optional inline script to execute instead of the app's entry point. If provided,
            this script will take precedence over the entry point.
        environment_id (str | Unset):
        environment_revision_id (str | Unset):
        extended_identity_propagation_to_apps_enabled (bool | Unset):  Default: False.
        external_volume_mount_ids (list[str] | Unset):
        git_ref (GitRef | Unset):
        hardware_tier_id (str | Unset):
        net_app_volume_ids (list[str] | Unset):
        tags (list[AppVersionTag] | Unset):
        vanity_url (str | Unset):
    """

    autoscaling_specification: AppAutoscalingSpecification | Unset = UNSET
    bundle_id: str | Unset = UNSET
    dfs_commit_id: str | Unset = UNSET
    entry_script: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    environment_revision_id: str | Unset = UNSET
    extended_identity_propagation_to_apps_enabled: bool | Unset = False
    external_volume_mount_ids: list[str] | Unset = UNSET
    git_ref: GitRef | Unset = UNSET
    hardware_tier_id: str | Unset = UNSET
    net_app_volume_ids: list[str] | Unset = UNSET
    tags: list[AppVersionTag] | Unset = UNSET
    vanity_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        autoscaling_specification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.autoscaling_specification, Unset):
            autoscaling_specification = self.autoscaling_specification.to_dict()

        bundle_id = self.bundle_id

        dfs_commit_id = self.dfs_commit_id

        entry_script = self.entry_script

        environment_id = self.environment_id

        environment_revision_id = self.environment_revision_id

        extended_identity_propagation_to_apps_enabled = self.extended_identity_propagation_to_apps_enabled

        external_volume_mount_ids: list[str] | Unset = UNSET
        if not isinstance(self.external_volume_mount_ids, Unset):
            external_volume_mount_ids = self.external_volume_mount_ids

        git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_ref, Unset):
            git_ref = self.git_ref.to_dict()

        hardware_tier_id = self.hardware_tier_id

        net_app_volume_ids: list[str] | Unset = UNSET
        if not isinstance(self.net_app_volume_ids, Unset):
            net_app_volume_ids = self.net_app_volume_ids

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        vanity_url = self.vanity_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if autoscaling_specification is not UNSET:
            field_dict["autoscalingSpecification"] = autoscaling_specification
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if dfs_commit_id is not UNSET:
            field_dict["dfsCommitId"] = dfs_commit_id
        if entry_script is not UNSET:
            field_dict["entryScript"] = entry_script
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if environment_revision_id is not UNSET:
            field_dict["environmentRevisionId"] = environment_revision_id
        if extended_identity_propagation_to_apps_enabled is not UNSET:
            field_dict["extendedIdentityPropagationToAppsEnabled"] = extended_identity_propagation_to_apps_enabled
        if external_volume_mount_ids is not UNSET:
            field_dict["externalVolumeMountIds"] = external_volume_mount_ids
        if git_ref is not UNSET:
            field_dict["gitRef"] = git_ref
        if hardware_tier_id is not UNSET:
            field_dict["hardwareTierId"] = hardware_tier_id
        if net_app_volume_ids is not UNSET:
            field_dict["netAppVolumeIds"] = net_app_volume_ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if vanity_url is not UNSET:
            field_dict["vanityUrl"] = vanity_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_autoscaling_specification import AppAutoscalingSpecification
        from ..models.app_version_tag import AppVersionTag
        from ..models.git_ref import GitRef

        d = dict(src_dict)
        _autoscaling_specification = d.pop("autoscalingSpecification", UNSET)
        autoscaling_specification: AppAutoscalingSpecification | Unset
        if isinstance(_autoscaling_specification, Unset):
            autoscaling_specification = UNSET
        else:
            autoscaling_specification = AppAutoscalingSpecification.from_dict(_autoscaling_specification)

        bundle_id = d.pop("bundleId", UNSET)

        dfs_commit_id = d.pop("dfsCommitId", UNSET)

        entry_script = d.pop("entryScript", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        environment_revision_id = d.pop("environmentRevisionId", UNSET)

        extended_identity_propagation_to_apps_enabled = d.pop("extendedIdentityPropagationToAppsEnabled", UNSET)

        external_volume_mount_ids = cast(list[str], d.pop("externalVolumeMountIds", UNSET))

        _git_ref = d.pop("gitRef", UNSET)
        git_ref: GitRef | Unset
        if isinstance(_git_ref, Unset):
            git_ref = UNSET
        else:
            git_ref = GitRef.from_dict(_git_ref)

        hardware_tier_id = d.pop("hardwareTierId", UNSET)

        net_app_volume_ids = cast(list[str], d.pop("netAppVolumeIds", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: list[AppVersionTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = AppVersionTag.from_dict(tags_item_data)

                tags.append(tags_item)

        vanity_url = d.pop("vanityUrl", UNSET)

        app_version_creation_request = cls(
            autoscaling_specification=autoscaling_specification,
            bundle_id=bundle_id,
            dfs_commit_id=dfs_commit_id,
            entry_script=entry_script,
            environment_id=environment_id,
            environment_revision_id=environment_revision_id,
            extended_identity_propagation_to_apps_enabled=extended_identity_propagation_to_apps_enabled,
            external_volume_mount_ids=external_volume_mount_ids,
            git_ref=git_ref,
            hardware_tier_id=hardware_tier_id,
            net_app_volume_ids=net_app_volume_ids,
            tags=tags,
            vanity_url=vanity_url,
        )

        app_version_creation_request.additional_properties = d
        return app_version_creation_request

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
