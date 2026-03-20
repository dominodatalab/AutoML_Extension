from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_type_v1 import ClusterTypeV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_tool_v1 import EnvironmentToolV1
    from ..models.environment_variable_v1 import EnvironmentVariableV1


T = TypeVar("T", bound="NewEnvironmentRevisionV1")


@_attrs_define
class NewEnvironmentRevisionV1:
    """
    Attributes:
        dockerfile_instructions (str | Unset):
        environment_variables (list[EnvironmentVariableV1] | Unset):
        image (str | Unset): Environment revision image. Required for creating a new environment
        post_run_script (str | Unset):
        post_setup_script (str | Unset):
        pre_run_script (str | Unset):
        pre_setup_script (str | Unset):
        skip_cache (bool | Unset):
        summary (str | Unset):
        supported_clusters (list[ClusterTypeV1] | Unset):
        tags (list[str] | Unset):
        use_vpn (bool | Unset):
        workspace_tools (list[EnvironmentToolV1] | Unset):
    """

    dockerfile_instructions: str | Unset = UNSET
    environment_variables: list[EnvironmentVariableV1] | Unset = UNSET
    image: str | Unset = UNSET
    post_run_script: str | Unset = UNSET
    post_setup_script: str | Unset = UNSET
    pre_run_script: str | Unset = UNSET
    pre_setup_script: str | Unset = UNSET
    skip_cache: bool | Unset = UNSET
    summary: str | Unset = UNSET
    supported_clusters: list[ClusterTypeV1] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    use_vpn: bool | Unset = UNSET
    workspace_tools: list[EnvironmentToolV1] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dockerfile_instructions = self.dockerfile_instructions

        environment_variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.environment_variables, Unset):
            environment_variables = []
            for environment_variables_item_data in self.environment_variables:
                environment_variables_item = environment_variables_item_data.to_dict()
                environment_variables.append(environment_variables_item)

        image = self.image

        post_run_script = self.post_run_script

        post_setup_script = self.post_setup_script

        pre_run_script = self.pre_run_script

        pre_setup_script = self.pre_setup_script

        skip_cache = self.skip_cache

        summary = self.summary

        supported_clusters: list[str] | Unset = UNSET
        if not isinstance(self.supported_clusters, Unset):
            supported_clusters = []
            for supported_clusters_item_data in self.supported_clusters:
                supported_clusters_item = supported_clusters_item_data.value
                supported_clusters.append(supported_clusters_item)

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        use_vpn = self.use_vpn

        workspace_tools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workspace_tools, Unset):
            workspace_tools = []
            for workspace_tools_item_data in self.workspace_tools:
                workspace_tools_item = workspace_tools_item_data.to_dict()
                workspace_tools.append(workspace_tools_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dockerfile_instructions is not UNSET:
            field_dict["dockerfileInstructions"] = dockerfile_instructions
        if environment_variables is not UNSET:
            field_dict["environmentVariables"] = environment_variables
        if image is not UNSET:
            field_dict["image"] = image
        if post_run_script is not UNSET:
            field_dict["postRunScript"] = post_run_script
        if post_setup_script is not UNSET:
            field_dict["postSetupScript"] = post_setup_script
        if pre_run_script is not UNSET:
            field_dict["preRunScript"] = pre_run_script
        if pre_setup_script is not UNSET:
            field_dict["preSetupScript"] = pre_setup_script
        if skip_cache is not UNSET:
            field_dict["skipCache"] = skip_cache
        if summary is not UNSET:
            field_dict["summary"] = summary
        if supported_clusters is not UNSET:
            field_dict["supportedClusters"] = supported_clusters
        if tags is not UNSET:
            field_dict["tags"] = tags
        if use_vpn is not UNSET:
            field_dict["useVpn"] = use_vpn
        if workspace_tools is not UNSET:
            field_dict["workspaceTools"] = workspace_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_tool_v1 import EnvironmentToolV1
        from ..models.environment_variable_v1 import EnvironmentVariableV1

        d = dict(src_dict)
        dockerfile_instructions = d.pop("dockerfileInstructions", UNSET)

        _environment_variables = d.pop("environmentVariables", UNSET)
        environment_variables: list[EnvironmentVariableV1] | Unset = UNSET
        if _environment_variables is not UNSET:
            environment_variables = []
            for environment_variables_item_data in _environment_variables:
                environment_variables_item = EnvironmentVariableV1.from_dict(environment_variables_item_data)

                environment_variables.append(environment_variables_item)

        image = d.pop("image", UNSET)

        post_run_script = d.pop("postRunScript", UNSET)

        post_setup_script = d.pop("postSetupScript", UNSET)

        pre_run_script = d.pop("preRunScript", UNSET)

        pre_setup_script = d.pop("preSetupScript", UNSET)

        skip_cache = d.pop("skipCache", UNSET)

        summary = d.pop("summary", UNSET)

        _supported_clusters = d.pop("supportedClusters", UNSET)
        supported_clusters: list[ClusterTypeV1] | Unset = UNSET
        if _supported_clusters is not UNSET:
            supported_clusters = []
            for supported_clusters_item_data in _supported_clusters:
                supported_clusters_item = ClusterTypeV1(supported_clusters_item_data)

                supported_clusters.append(supported_clusters_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        use_vpn = d.pop("useVpn", UNSET)

        _workspace_tools = d.pop("workspaceTools", UNSET)
        workspace_tools: list[EnvironmentToolV1] | Unset = UNSET
        if _workspace_tools is not UNSET:
            workspace_tools = []
            for workspace_tools_item_data in _workspace_tools:
                workspace_tools_item = EnvironmentToolV1.from_dict(workspace_tools_item_data)

                workspace_tools.append(workspace_tools_item)

        new_environment_revision_v1 = cls(
            dockerfile_instructions=dockerfile_instructions,
            environment_variables=environment_variables,
            image=image,
            post_run_script=post_run_script,
            post_setup_script=post_setup_script,
            pre_run_script=pre_run_script,
            pre_setup_script=pre_setup_script,
            skip_cache=skip_cache,
            summary=summary,
            supported_clusters=supported_clusters,
            tags=tags,
            use_vpn=use_vpn,
            workspace_tools=workspace_tools,
        )

        new_environment_revision_v1.additional_properties = d
        return new_environment_revision_v1

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
