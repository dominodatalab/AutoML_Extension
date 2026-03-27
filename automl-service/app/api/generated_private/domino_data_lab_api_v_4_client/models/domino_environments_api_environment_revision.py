from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_environments_api_environment_revision_cluster_types_type_0_item import (
    DominoEnvironmentsApiEnvironmentRevisionClusterTypesType0Item,
)
from ..models.domino_environments_api_environment_revision_image_type import (
    DominoEnvironmentsApiEnvironmentRevisionImageType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_util_yaml_default_yaml_string import DominoCommonUtilYamlDefaultYamlString
    from ..models.domino_environments_api_environment_revision_build_environment_variables_item import (
        DominoEnvironmentsApiEnvironmentRevisionBuildEnvironmentVariablesItem,
    )
    from ..models.information import Information


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentRevision")


@_attrs_define
class DominoEnvironmentsApiEnvironmentRevision:
    """
    Attributes:
        id (str):
        environment_id (str):
        environment_name (str):
        image_type (DominoEnvironmentsApiEnvironmentRevisionImageType):
        is_restricted (bool):
        is_built (bool):
        docker_arguments (list[str]):
        should_use_vpn (bool):
        build_environment_variables (list[DominoEnvironmentsApiEnvironmentRevisionBuildEnvironmentVariablesItem]):
        supports_package_persistence (bool):
        number (int | None | Unset):
        cluster_types (list[DominoEnvironmentsApiEnvironmentRevisionClusterTypesType0Item] | None | Unset):
        summary (None | str | Unset):
        compressed_image_size (Information | Unset):
        docker_image (None | str | Unset):
        workspaces_properties (DominoCommonUtilYamlDefaultYamlString | Unset):
        dockerfile_instructions (None | str | Unset):
        pre_setup_script (None | str | Unset):
        post_setup_script (None | str | Unset):
        pre_run_script (None | str | Unset):
        post_run_script (None | str | Unset):
    """

    id: str
    environment_id: str
    environment_name: str
    image_type: DominoEnvironmentsApiEnvironmentRevisionImageType
    is_restricted: bool
    is_built: bool
    docker_arguments: list[str]
    should_use_vpn: bool
    build_environment_variables: list[DominoEnvironmentsApiEnvironmentRevisionBuildEnvironmentVariablesItem]
    supports_package_persistence: bool
    number: int | None | Unset = UNSET
    cluster_types: list[DominoEnvironmentsApiEnvironmentRevisionClusterTypesType0Item] | None | Unset = UNSET
    summary: None | str | Unset = UNSET
    compressed_image_size: Information | Unset = UNSET
    docker_image: None | str | Unset = UNSET
    workspaces_properties: DominoCommonUtilYamlDefaultYamlString | Unset = UNSET
    dockerfile_instructions: None | str | Unset = UNSET
    pre_setup_script: None | str | Unset = UNSET
    post_setup_script: None | str | Unset = UNSET
    pre_run_script: None | str | Unset = UNSET
    post_run_script: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        environment_id = self.environment_id

        environment_name = self.environment_name

        image_type = self.image_type.value

        is_restricted = self.is_restricted

        is_built = self.is_built

        docker_arguments = self.docker_arguments

        should_use_vpn = self.should_use_vpn

        build_environment_variables = []
        for build_environment_variables_item_data in self.build_environment_variables:
            build_environment_variables_item = build_environment_variables_item_data.to_dict()
            build_environment_variables.append(build_environment_variables_item)

        supports_package_persistence = self.supports_package_persistence

        number: int | None | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

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

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        compressed_image_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compressed_image_size, Unset):
            compressed_image_size = self.compressed_image_size.to_dict()

        docker_image: None | str | Unset
        if isinstance(self.docker_image, Unset):
            docker_image = UNSET
        else:
            docker_image = self.docker_image

        workspaces_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspaces_properties, Unset):
            workspaces_properties = self.workspaces_properties.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "environmentId": environment_id,
                "environmentName": environment_name,
                "imageType": image_type,
                "isRestricted": is_restricted,
                "isBuilt": is_built,
                "dockerArguments": docker_arguments,
                "shouldUseVPN": should_use_vpn,
                "buildEnvironmentVariables": build_environment_variables,
                "supportsPackagePersistence": supports_package_persistence,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number
        if cluster_types is not UNSET:
            field_dict["clusterTypes"] = cluster_types
        if summary is not UNSET:
            field_dict["summary"] = summary
        if compressed_image_size is not UNSET:
            field_dict["compressedImageSize"] = compressed_image_size
        if docker_image is not UNSET:
            field_dict["dockerImage"] = docker_image
        if workspaces_properties is not UNSET:
            field_dict["workspacesProperties"] = workspaces_properties
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_util_yaml_default_yaml_string import DominoCommonUtilYamlDefaultYamlString
        from ..models.domino_environments_api_environment_revision_build_environment_variables_item import (
            DominoEnvironmentsApiEnvironmentRevisionBuildEnvironmentVariablesItem,
        )
        from ..models.information import Information

        d = dict(src_dict)
        id = d.pop("id")

        environment_id = d.pop("environmentId")

        environment_name = d.pop("environmentName")

        image_type = DominoEnvironmentsApiEnvironmentRevisionImageType(d.pop("imageType"))

        is_restricted = d.pop("isRestricted")

        is_built = d.pop("isBuilt")

        docker_arguments = cast(list[str], d.pop("dockerArguments"))

        should_use_vpn = d.pop("shouldUseVPN")

        build_environment_variables = []
        _build_environment_variables = d.pop("buildEnvironmentVariables")
        for build_environment_variables_item_data in _build_environment_variables:
            build_environment_variables_item = (
                DominoEnvironmentsApiEnvironmentRevisionBuildEnvironmentVariablesItem.from_dict(
                    build_environment_variables_item_data
                )
            )

            build_environment_variables.append(build_environment_variables_item)

        supports_package_persistence = d.pop("supportsPackagePersistence")

        def _parse_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_cluster_types(
            data: object,
        ) -> list[DominoEnvironmentsApiEnvironmentRevisionClusterTypesType0Item] | None | Unset:
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
                    cluster_types_type_0_item = DominoEnvironmentsApiEnvironmentRevisionClusterTypesType0Item(
                        cluster_types_type_0_item_data
                    )

                    cluster_types_type_0.append(cluster_types_type_0_item)

                return cluster_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoEnvironmentsApiEnvironmentRevisionClusterTypesType0Item] | None | Unset, data)

        cluster_types = _parse_cluster_types(d.pop("clusterTypes", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        _compressed_image_size = d.pop("compressedImageSize", UNSET)
        compressed_image_size: Information | Unset
        if isinstance(_compressed_image_size, Unset):
            compressed_image_size = UNSET
        else:
            compressed_image_size = Information.from_dict(_compressed_image_size)

        def _parse_docker_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        docker_image = _parse_docker_image(d.pop("dockerImage", UNSET))

        _workspaces_properties = d.pop("workspacesProperties", UNSET)
        workspaces_properties: DominoCommonUtilYamlDefaultYamlString | Unset
        if isinstance(_workspaces_properties, Unset):
            workspaces_properties = UNSET
        else:
            workspaces_properties = DominoCommonUtilYamlDefaultYamlString.from_dict(_workspaces_properties)

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

        domino_environments_api_environment_revision = cls(
            id=id,
            environment_id=environment_id,
            environment_name=environment_name,
            image_type=image_type,
            is_restricted=is_restricted,
            is_built=is_built,
            docker_arguments=docker_arguments,
            should_use_vpn=should_use_vpn,
            build_environment_variables=build_environment_variables,
            supports_package_persistence=supports_package_persistence,
            number=number,
            cluster_types=cluster_types,
            summary=summary,
            compressed_image_size=compressed_image_size,
            docker_image=docker_image,
            workspaces_properties=workspaces_properties,
            dockerfile_instructions=dockerfile_instructions,
            pre_setup_script=pre_setup_script,
            post_setup_script=post_setup_script,
            pre_run_script=pre_run_script,
            post_run_script=post_run_script,
        )

        domino_environments_api_environment_revision.additional_properties = d
        return domino_environments_api_environment_revision

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
