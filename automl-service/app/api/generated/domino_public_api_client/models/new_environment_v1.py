from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_type_v1 import ClusterTypeV1
from ..models.environment_rebuild_on_base_changes_v1 import EnvironmentRebuildOnBaseChangesV1
from ..models.new_environment_visibility_v1 import NewEnvironmentVisibilityV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_tool_v1 import EnvironmentToolV1
    from ..models.environment_variable_v1 import EnvironmentVariableV1


T = TypeVar("T", bound="NewEnvironmentV1")


@_attrs_define
class NewEnvironmentV1:
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
        add_base_dependencies (bool | Unset): Required for creating a new environment
        description (str | Unset):
        duplicate_from_environment_id (str | Unset): The id of the environment to duplicate. When specifying this
            property, no other properties in the payload must be set.
        is_curated (bool | Unset):
        is_restricted (bool | Unset): Specifies if an environment is restricted. Only users with ClassifyEnvironments
            permission can set this to true
        name (str | Unset): Environment name. Required for creating a new environment
        org_owner_id (str | Unset): Sets an Organization as the Environment owner. Only used if visibility is 'Private',
            as 'Global' environments don't have owners.
        rebuild_on_base_changes (EnvironmentRebuildOnBaseChangesV1 | Unset): Whether to build a new revision when the
            base environment changes.
        visibility (NewEnvironmentVisibilityV1 | Unset): Environment visibility. Required for creating a new environment
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
    add_base_dependencies: bool | Unset = UNSET
    description: str | Unset = UNSET
    duplicate_from_environment_id: str | Unset = UNSET
    is_curated: bool | Unset = UNSET
    is_restricted: bool | Unset = UNSET
    name: str | Unset = UNSET
    org_owner_id: str | Unset = UNSET
    rebuild_on_base_changes: EnvironmentRebuildOnBaseChangesV1 | Unset = UNSET
    visibility: NewEnvironmentVisibilityV1 | Unset = UNSET
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

        add_base_dependencies = self.add_base_dependencies

        description = self.description

        duplicate_from_environment_id = self.duplicate_from_environment_id

        is_curated = self.is_curated

        is_restricted = self.is_restricted

        name = self.name

        org_owner_id = self.org_owner_id

        rebuild_on_base_changes: str | Unset = UNSET
        if not isinstance(self.rebuild_on_base_changes, Unset):
            rebuild_on_base_changes = self.rebuild_on_base_changes.value

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

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
        if add_base_dependencies is not UNSET:
            field_dict["addBaseDependencies"] = add_base_dependencies
        if description is not UNSET:
            field_dict["description"] = description
        if duplicate_from_environment_id is not UNSET:
            field_dict["duplicateFromEnvironmentId"] = duplicate_from_environment_id
        if is_curated is not UNSET:
            field_dict["isCurated"] = is_curated
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if name is not UNSET:
            field_dict["name"] = name
        if org_owner_id is not UNSET:
            field_dict["orgOwnerId"] = org_owner_id
        if rebuild_on_base_changes is not UNSET:
            field_dict["rebuildOnBaseChanges"] = rebuild_on_base_changes
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

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

        add_base_dependencies = d.pop("addBaseDependencies", UNSET)

        description = d.pop("description", UNSET)

        duplicate_from_environment_id = d.pop("duplicateFromEnvironmentId", UNSET)

        is_curated = d.pop("isCurated", UNSET)

        is_restricted = d.pop("isRestricted", UNSET)

        name = d.pop("name", UNSET)

        org_owner_id = d.pop("orgOwnerId", UNSET)

        _rebuild_on_base_changes = d.pop("rebuildOnBaseChanges", UNSET)
        rebuild_on_base_changes: EnvironmentRebuildOnBaseChangesV1 | Unset
        if isinstance(_rebuild_on_base_changes, Unset):
            rebuild_on_base_changes = UNSET
        else:
            rebuild_on_base_changes = EnvironmentRebuildOnBaseChangesV1(_rebuild_on_base_changes)

        _visibility = d.pop("visibility", UNSET)
        visibility: NewEnvironmentVisibilityV1 | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = NewEnvironmentVisibilityV1(_visibility)

        new_environment_v1 = cls(
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
            add_base_dependencies=add_base_dependencies,
            description=description,
            duplicate_from_environment_id=duplicate_from_environment_id,
            is_curated=is_curated,
            is_restricted=is_restricted,
            name=name,
            org_owner_id=org_owner_id,
            rebuild_on_base_changes=rebuild_on_base_changes,
            visibility=visibility,
        )

        new_environment_v1.additional_properties = d
        return new_environment_v1

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
