from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_orchestrator_execution_metadata import (
        DominoJobsInterfaceOrchestratorExecutionMetadata,
    )


T = TypeVar("T", bound="DominoJobsInterfaceWorkflowConfig")


@_attrs_define
class DominoJobsInterfaceWorkflowConfig:
    """
    Attributes:
        workflow_orchestrator (str):
        execution_metadata (DominoJobsInterfaceOrchestratorExecutionMetadata | Unset):
        input_interface (None | str | Unset):
        input_output_interface (None | str | Unset):
        input_metadata_prefix (None | str | Unset):
        output_metadata_prefix (None | str | Unset):
        raw_output_prefix (None | str | Unset):
    """

    workflow_orchestrator: str
    execution_metadata: DominoJobsInterfaceOrchestratorExecutionMetadata | Unset = UNSET
    input_interface: None | str | Unset = UNSET
    input_output_interface: None | str | Unset = UNSET
    input_metadata_prefix: None | str | Unset = UNSET
    output_metadata_prefix: None | str | Unset = UNSET
    raw_output_prefix: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_orchestrator = self.workflow_orchestrator

        execution_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_metadata, Unset):
            execution_metadata = self.execution_metadata.to_dict()

        input_interface: None | str | Unset
        if isinstance(self.input_interface, Unset):
            input_interface = UNSET
        else:
            input_interface = self.input_interface

        input_output_interface: None | str | Unset
        if isinstance(self.input_output_interface, Unset):
            input_output_interface = UNSET
        else:
            input_output_interface = self.input_output_interface

        input_metadata_prefix: None | str | Unset
        if isinstance(self.input_metadata_prefix, Unset):
            input_metadata_prefix = UNSET
        else:
            input_metadata_prefix = self.input_metadata_prefix

        output_metadata_prefix: None | str | Unset
        if isinstance(self.output_metadata_prefix, Unset):
            output_metadata_prefix = UNSET
        else:
            output_metadata_prefix = self.output_metadata_prefix

        raw_output_prefix: None | str | Unset
        if isinstance(self.raw_output_prefix, Unset):
            raw_output_prefix = UNSET
        else:
            raw_output_prefix = self.raw_output_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflowOrchestrator": workflow_orchestrator,
            }
        )
        if execution_metadata is not UNSET:
            field_dict["executionMetadata"] = execution_metadata
        if input_interface is not UNSET:
            field_dict["inputInterface"] = input_interface
        if input_output_interface is not UNSET:
            field_dict["inputOutputInterface"] = input_output_interface
        if input_metadata_prefix is not UNSET:
            field_dict["inputMetadataPrefix"] = input_metadata_prefix
        if output_metadata_prefix is not UNSET:
            field_dict["outputMetadataPrefix"] = output_metadata_prefix
        if raw_output_prefix is not UNSET:
            field_dict["rawOutputPrefix"] = raw_output_prefix

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

        def _parse_input_interface(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_interface = _parse_input_interface(d.pop("inputInterface", UNSET))

        def _parse_input_output_interface(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_output_interface = _parse_input_output_interface(d.pop("inputOutputInterface", UNSET))

        def _parse_input_metadata_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        input_metadata_prefix = _parse_input_metadata_prefix(d.pop("inputMetadataPrefix", UNSET))

        def _parse_output_metadata_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output_metadata_prefix = _parse_output_metadata_prefix(d.pop("outputMetadataPrefix", UNSET))

        def _parse_raw_output_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        raw_output_prefix = _parse_raw_output_prefix(d.pop("rawOutputPrefix", UNSET))

        domino_jobs_interface_workflow_config = cls(
            workflow_orchestrator=workflow_orchestrator,
            execution_metadata=execution_metadata,
            input_interface=input_interface,
            input_output_interface=input_output_interface,
            input_metadata_prefix=input_metadata_prefix,
            output_metadata_prefix=output_metadata_prefix,
            raw_output_prefix=raw_output_prefix,
        )

        domino_jobs_interface_workflow_config.additional_properties = d
        return domino_jobs_interface_workflow_config

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
