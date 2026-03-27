from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_environments_api_new_environment_revision_supported_clusters_item import (
    DominoEnvironmentsApiNewEnvironmentRevisionSupportedClustersItem,
)
from ..models.domino_environments_api_new_environment_revision_trigger import (
    DominoEnvironmentsApiNewEnvironmentRevisionTrigger,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_new_environment_revision_base import (
        DominoEnvironmentsApiNewEnvironmentRevisionBase,
    )
    from ..models.domino_environments_api_new_environment_revision_environment_variables import (
        DominoEnvironmentsApiNewEnvironmentRevisionEnvironmentVariables,
    )


T = TypeVar("T", bound="DominoEnvironmentsApiNewEnvironmentRevision")


@_attrs_define
class DominoEnvironmentsApiNewEnvironmentRevision:
    """
    Attributes:
        base_revision (DominoEnvironmentsApiNewEnvironmentRevisionBase):
        supported_clusters (list[DominoEnvironmentsApiNewEnvironmentRevisionSupportedClustersItem]):
        environment_variables (DominoEnvironmentsApiNewEnvironmentRevisionEnvironmentVariables):
        docker_arguments (list[str]):
        skip_cache (bool):
        should_use_vpn (bool):
        workspace_tools (None | str | Unset):
        dockerfile_instructions (None | str | Unset):
        pre_setup_script (None | str | Unset):
        post_setup_script (None | str | Unset):
        pre_run_script (None | str | Unset):
        post_run_script (None | str | Unset):
        summary (None | str | Unset):
        tags (list[str] | None | Unset):
        is_restricted (bool | None | Unset):
        trigger (DominoEnvironmentsApiNewEnvironmentRevisionTrigger | Unset):
        supports_package_persistence (bool | None | Unset):
    """

    base_revision: DominoEnvironmentsApiNewEnvironmentRevisionBase
    supported_clusters: list[DominoEnvironmentsApiNewEnvironmentRevisionSupportedClustersItem]
    environment_variables: DominoEnvironmentsApiNewEnvironmentRevisionEnvironmentVariables
    docker_arguments: list[str]
    skip_cache: bool
    should_use_vpn: bool
    workspace_tools: None | str | Unset = UNSET
    dockerfile_instructions: None | str | Unset = UNSET
    pre_setup_script: None | str | Unset = UNSET
    post_setup_script: None | str | Unset = UNSET
    pre_run_script: None | str | Unset = UNSET
    post_run_script: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    is_restricted: bool | None | Unset = UNSET
    trigger: DominoEnvironmentsApiNewEnvironmentRevisionTrigger | Unset = UNSET
    supports_package_persistence: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_revision = self.base_revision.to_dict()

        supported_clusters = []
        for supported_clusters_item_data in self.supported_clusters:
            supported_clusters_item = supported_clusters_item_data.value
            supported_clusters.append(supported_clusters_item)

        environment_variables = self.environment_variables.to_dict()

        docker_arguments = self.docker_arguments

        skip_cache = self.skip_cache

        should_use_vpn = self.should_use_vpn

        workspace_tools: None | str | Unset
        if isinstance(self.workspace_tools, Unset):
            workspace_tools = UNSET
        else:
            workspace_tools = self.workspace_tools

        dockerfile_instructions: None | str | Unset
        if isinstance(self.dockerfile_instructions, Unset):
            dockerfile_instructions = UNSET
        else:
            dockerfile_instructions = self.dockerfile_instructions

        pre_setup_script: None | str | Unset
        if isinstance(self.pre_setup_script, Unset):
            pre_setup_script = UNSET
        else:
            pre_setup_script = self.pre_setup_script

        post_setup_script: None | str | Unset
        if isinstance(self.post_setup_script, Unset):
            post_setup_script = UNSET
        else:
            post_setup_script = self.post_setup_script

        pre_run_script: None | str | Unset
        if isinstance(self.pre_run_script, Unset):
            pre_run_script = UNSET
        else:
            pre_run_script = self.pre_run_script

        post_run_script: None | str | Unset
        if isinstance(self.post_run_script, Unset):
            post_run_script = UNSET
        else:
            post_run_script = self.post_run_script

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        is_restricted: bool | None | Unset
        if isinstance(self.is_restricted, Unset):
            is_restricted = UNSET
        else:
            is_restricted = self.is_restricted

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        supports_package_persistence: bool | None | Unset
        if isinstance(self.supports_package_persistence, Unset):
            supports_package_persistence = UNSET
        else:
            supports_package_persistence = self.supports_package_persistence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseRevision": base_revision,
                "supportedClusters": supported_clusters,
                "environmentVariables": environment_variables,
                "dockerArguments": docker_arguments,
                "skipCache": skip_cache,
                "shouldUseVpn": should_use_vpn,
            }
        )
        if workspace_tools is not UNSET:
            field_dict["workspaceTools"] = workspace_tools
        if dockerfile_instructions is not UNSET:
            field_dict["dockerfileInstructions"] = dockerfile_instructions
        if pre_setup_script is not UNSET:
            field_dict["preSetupScript"] = pre_setup_script
        if post_setup_script is not UNSET:
            field_dict["postSetupScript"] = post_setup_script
        if pre_run_script is not UNSET:
            field_dict["preRunScript"] = pre_run_script
        if post_run_script is not UNSET:
            field_dict["postRunScript"] = post_run_script
        if summary is not UNSET:
            field_dict["summary"] = summary
        if tags is not UNSET:
            field_dict["tags"] = tags
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if supports_package_persistence is not UNSET:
            field_dict["supportsPackagePersistence"] = supports_package_persistence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_new_environment_revision_base import (
            DominoEnvironmentsApiNewEnvironmentRevisionBase,
        )
        from ..models.domino_environments_api_new_environment_revision_environment_variables import (
            DominoEnvironmentsApiNewEnvironmentRevisionEnvironmentVariables,
        )

        d = dict(src_dict)
        base_revision = DominoEnvironmentsApiNewEnvironmentRevisionBase.from_dict(d.pop("baseRevision"))

        supported_clusters = []
        _supported_clusters = d.pop("supportedClusters")
        for supported_clusters_item_data in _supported_clusters:
            supported_clusters_item = DominoEnvironmentsApiNewEnvironmentRevisionSupportedClustersItem(
                supported_clusters_item_data
            )

            supported_clusters.append(supported_clusters_item)

        environment_variables = DominoEnvironmentsApiNewEnvironmentRevisionEnvironmentVariables.from_dict(
            d.pop("environmentVariables")
        )

        docker_arguments = cast(list[str], d.pop("dockerArguments"))

        skip_cache = d.pop("skipCache")

        should_use_vpn = d.pop("shouldUseVpn")

        def _parse_workspace_tools(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_tools = _parse_workspace_tools(d.pop("workspaceTools", UNSET))

        def _parse_dockerfile_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dockerfile_instructions = _parse_dockerfile_instructions(d.pop("dockerfileInstructions", UNSET))

        def _parse_pre_setup_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pre_setup_script = _parse_pre_setup_script(d.pop("preSetupScript", UNSET))

        def _parse_post_setup_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_setup_script = _parse_post_setup_script(d.pop("postSetupScript", UNSET))

        def _parse_pre_run_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pre_run_script = _parse_pre_run_script(d.pop("preRunScript", UNSET))

        def _parse_post_run_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_run_script = _parse_post_run_script(d.pop("postRunScript", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_is_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_restricted = _parse_is_restricted(d.pop("isRestricted", UNSET))

        _trigger = d.pop("trigger", UNSET)
        trigger: DominoEnvironmentsApiNewEnvironmentRevisionTrigger | Unset
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = DominoEnvironmentsApiNewEnvironmentRevisionTrigger(_trigger)

        def _parse_supports_package_persistence(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_package_persistence = _parse_supports_package_persistence(d.pop("supportsPackagePersistence", UNSET))

        domino_environments_api_new_environment_revision = cls(
            base_revision=base_revision,
            supported_clusters=supported_clusters,
            environment_variables=environment_variables,
            docker_arguments=docker_arguments,
            skip_cache=skip_cache,
            should_use_vpn=should_use_vpn,
            workspace_tools=workspace_tools,
            dockerfile_instructions=dockerfile_instructions,
            pre_setup_script=pre_setup_script,
            post_setup_script=post_setup_script,
            pre_run_script=pre_run_script,
            post_run_script=post_run_script,
            summary=summary,
            tags=tags,
            is_restricted=is_restricted,
            trigger=trigger,
            supports_package_persistence=supports_package_persistence,
        )

        domino_environments_api_new_environment_revision.additional_properties = d
        return domino_environments_api_new_environment_revision

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
