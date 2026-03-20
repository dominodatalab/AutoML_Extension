from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_autoscaling_specification import AppAutoscalingSpecification
    from ..models.app_instance_summary_response import AppInstanceSummaryResponse
    from ..models.app_user_response import AppUserResponse
    from ..models.app_version_tag import AppVersionTag
    from ..models.git_ref import GitRef


T = TypeVar("T", bound="AppVersionResponse")


@_attrs_define
class AppVersionResponse:
    """
    Attributes:
        created_at (float):
        environment_id (str):
        environment_revision_id (str):
        extended_identity_propagation_to_apps_enabled (bool):
        external_volume_mount_ids (list[str]):
        hardware_tier_id (str):
        id (str):
        net_app_volume_ids (list[str]):
        tags (list[AppVersionTag]):
        updated_at (float):
        autoscaling_specification (AppAutoscalingSpecification | Unset):
        bundle_id (str | Unset):
        bundle_name (str | Unset):
        current_instance (AppInstanceSummaryResponse | Unset):
        dfs_commit_id (str | Unset):
        entry_script (str | Unset): Optional inline script to execute instead of the app's entry point. If provided,
            this script will take precedence over the entry point.
        git_ref (GitRef | Unset):
        publisher (AppUserResponse | Unset):
        vanity_url (str | Unset):
    """

    created_at: float
    environment_id: str
    environment_revision_id: str
    extended_identity_propagation_to_apps_enabled: bool
    external_volume_mount_ids: list[str]
    hardware_tier_id: str
    id: str
    net_app_volume_ids: list[str]
    tags: list[AppVersionTag]
    updated_at: float
    autoscaling_specification: AppAutoscalingSpecification | Unset = UNSET
    bundle_id: str | Unset = UNSET
    bundle_name: str | Unset = UNSET
    current_instance: AppInstanceSummaryResponse | Unset = UNSET
    dfs_commit_id: str | Unset = UNSET
    entry_script: str | Unset = UNSET
    git_ref: GitRef | Unset = UNSET
    publisher: AppUserResponse | Unset = UNSET
    vanity_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        environment_id = self.environment_id

        environment_revision_id = self.environment_revision_id

        extended_identity_propagation_to_apps_enabled = self.extended_identity_propagation_to_apps_enabled

        external_volume_mount_ids = self.external_volume_mount_ids

        hardware_tier_id = self.hardware_tier_id

        id = self.id

        net_app_volume_ids = self.net_app_volume_ids

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        updated_at = self.updated_at

        autoscaling_specification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.autoscaling_specification, Unset):
            autoscaling_specification = self.autoscaling_specification.to_dict()

        bundle_id = self.bundle_id

        bundle_name = self.bundle_name

        current_instance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_instance, Unset):
            current_instance = self.current_instance.to_dict()

        dfs_commit_id = self.dfs_commit_id

        entry_script = self.entry_script

        git_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_ref, Unset):
            git_ref = self.git_ref.to_dict()

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        vanity_url = self.vanity_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "environmentId": environment_id,
                "environmentRevisionId": environment_revision_id,
                "extendedIdentityPropagationToAppsEnabled": extended_identity_propagation_to_apps_enabled,
                "externalVolumeMountIds": external_volume_mount_ids,
                "hardwareTierId": hardware_tier_id,
                "id": id,
                "netAppVolumeIds": net_app_volume_ids,
                "tags": tags,
                "updatedAt": updated_at,
            }
        )
        if autoscaling_specification is not UNSET:
            field_dict["autoscalingSpecification"] = autoscaling_specification
        if bundle_id is not UNSET:
            field_dict["bundleId"] = bundle_id
        if bundle_name is not UNSET:
            field_dict["bundleName"] = bundle_name
        if current_instance is not UNSET:
            field_dict["currentInstance"] = current_instance
        if dfs_commit_id is not UNSET:
            field_dict["dfsCommitId"] = dfs_commit_id
        if entry_script is not UNSET:
            field_dict["entryScript"] = entry_script
        if git_ref is not UNSET:
            field_dict["gitRef"] = git_ref
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if vanity_url is not UNSET:
            field_dict["vanityUrl"] = vanity_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_autoscaling_specification import AppAutoscalingSpecification
        from ..models.app_instance_summary_response import AppInstanceSummaryResponse
        from ..models.app_user_response import AppUserResponse
        from ..models.app_version_tag import AppVersionTag
        from ..models.git_ref import GitRef

        d = dict(src_dict)
        created_at = d.pop("createdAt")

        environment_id = d.pop("environmentId")

        environment_revision_id = d.pop("environmentRevisionId")

        extended_identity_propagation_to_apps_enabled = d.pop("extendedIdentityPropagationToAppsEnabled")

        external_volume_mount_ids = cast(list[str], d.pop("externalVolumeMountIds"))

        hardware_tier_id = d.pop("hardwareTierId")

        id = d.pop("id")

        net_app_volume_ids = cast(list[str], d.pop("netAppVolumeIds"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = AppVersionTag.from_dict(tags_item_data)

            tags.append(tags_item)

        updated_at = d.pop("updatedAt")

        _autoscaling_specification = d.pop("autoscalingSpecification", UNSET)
        autoscaling_specification: AppAutoscalingSpecification | Unset
        if isinstance(_autoscaling_specification, Unset):
            autoscaling_specification = UNSET
        else:
            autoscaling_specification = AppAutoscalingSpecification.from_dict(_autoscaling_specification)

        bundle_id = d.pop("bundleId", UNSET)

        bundle_name = d.pop("bundleName", UNSET)

        _current_instance = d.pop("currentInstance", UNSET)
        current_instance: AppInstanceSummaryResponse | Unset
        if isinstance(_current_instance, Unset):
            current_instance = UNSET
        else:
            current_instance = AppInstanceSummaryResponse.from_dict(_current_instance)

        dfs_commit_id = d.pop("dfsCommitId", UNSET)

        entry_script = d.pop("entryScript", UNSET)

        _git_ref = d.pop("gitRef", UNSET)
        git_ref: GitRef | Unset
        if isinstance(_git_ref, Unset):
            git_ref = UNSET
        else:
            git_ref = GitRef.from_dict(_git_ref)

        _publisher = d.pop("publisher", UNSET)
        publisher: AppUserResponse | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = AppUserResponse.from_dict(_publisher)

        vanity_url = d.pop("vanityUrl", UNSET)

        app_version_response = cls(
            created_at=created_at,
            environment_id=environment_id,
            environment_revision_id=environment_revision_id,
            extended_identity_propagation_to_apps_enabled=extended_identity_propagation_to_apps_enabled,
            external_volume_mount_ids=external_volume_mount_ids,
            hardware_tier_id=hardware_tier_id,
            id=id,
            net_app_volume_ids=net_app_volume_ids,
            tags=tags,
            updated_at=updated_at,
            autoscaling_specification=autoscaling_specification,
            bundle_id=bundle_id,
            bundle_name=bundle_name,
            current_instance=current_instance,
            dfs_commit_id=dfs_commit_id,
            entry_script=entry_script,
            git_ref=git_ref,
            publisher=publisher,
            vanity_url=vanity_url,
        )

        app_version_response.additional_properties = d
        return app_version_response

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
