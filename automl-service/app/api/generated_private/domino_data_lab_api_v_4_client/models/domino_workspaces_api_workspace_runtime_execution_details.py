from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspaces_api_environment import DominoWorkspacesApiEnvironment
    from ..models.domino_workspaces_api_executor_info import DominoWorkspacesApiExecutorInfo
    from ..models.domino_workspaces_api_hardware_tier_details import DominoWorkspacesApiHardwareTierDetails


T = TypeVar("T", bound="DominoWorkspacesApiWorkspaceRuntimeExecutionDetails")


@_attrs_define
class DominoWorkspacesApiWorkspaceRuntimeExecutionDetails:
    """
    Attributes:
        environment (DominoWorkspacesApiEnvironment):
        hardware_tier (DominoWorkspacesApiHardwareTierDetails):
        executor_info (DominoWorkspacesApiExecutorInfo | Unset):
    """

    environment: DominoWorkspacesApiEnvironment
    hardware_tier: DominoWorkspacesApiHardwareTierDetails
    executor_info: DominoWorkspacesApiExecutorInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment = self.environment.to_dict()

        hardware_tier = self.hardware_tier.to_dict()

        executor_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executor_info, Unset):
            executor_info = self.executor_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment": environment,
                "hardwareTier": hardware_tier,
            }
        )
        if executor_info is not UNSET:
            field_dict["executorInfo"] = executor_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspaces_api_environment import DominoWorkspacesApiEnvironment
        from ..models.domino_workspaces_api_executor_info import DominoWorkspacesApiExecutorInfo
        from ..models.domino_workspaces_api_hardware_tier_details import DominoWorkspacesApiHardwareTierDetails

        d = dict(src_dict)
        environment = DominoWorkspacesApiEnvironment.from_dict(d.pop("environment"))

        hardware_tier = DominoWorkspacesApiHardwareTierDetails.from_dict(d.pop("hardwareTier"))

        _executor_info = d.pop("executorInfo", UNSET)
        executor_info: DominoWorkspacesApiExecutorInfo | Unset
        if isinstance(_executor_info, Unset):
            executor_info = UNSET
        else:
            executor_info = DominoWorkspacesApiExecutorInfo.from_dict(_executor_info)

        domino_workspaces_api_workspace_runtime_execution_details = cls(
            environment=environment,
            hardware_tier=hardware_tier,
            executor_info=executor_info,
        )

        domino_workspaces_api_workspace_runtime_execution_details.additional_properties = d
        return domino_workspaces_api_workspace_runtime_execution_details

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
