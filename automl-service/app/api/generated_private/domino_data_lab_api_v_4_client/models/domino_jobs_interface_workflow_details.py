from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_orchestrator_execution_metadata import (
        DominoJobsInterfaceOrchestratorExecutionMetadata,
    )


T = TypeVar("T", bound="DominoJobsInterfaceWorkflowDetails")


@_attrs_define
class DominoJobsInterfaceWorkflowDetails:
    """
    Attributes:
        workflow_orchestrator (str):
        execution_metadata (DominoJobsInterfaceOrchestratorExecutionMetadata | Unset):
    """

    workflow_orchestrator: str
    execution_metadata: DominoJobsInterfaceOrchestratorExecutionMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_orchestrator = self.workflow_orchestrator

        execution_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_metadata, Unset):
            execution_metadata = self.execution_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflowOrchestrator": workflow_orchestrator,
            }
        )
        if execution_metadata is not UNSET:
            field_dict["executionMetadata"] = execution_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_orchestrator_execution_metadata import (
            DominoJobsInterfaceOrchestratorExecutionMetadata,
        )

        d = dict(src_dict)
        workflow_orchestrator = d.pop("workflowOrchestrator")

        _execution_metadata = d.pop("executionMetadata", UNSET)
        execution_metadata: DominoJobsInterfaceOrchestratorExecutionMetadata | Unset
        if isinstance(_execution_metadata, Unset):
            execution_metadata = UNSET
        else:
            execution_metadata = DominoJobsInterfaceOrchestratorExecutionMetadata.from_dict(_execution_metadata)

        domino_jobs_interface_workflow_details = cls(
            workflow_orchestrator=workflow_orchestrator,
            execution_metadata=execution_metadata,
        )

        domino_jobs_interface_workflow_details.additional_properties = d
        return domino_jobs_interface_workflow_details

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
