from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoJobsInterfaceOrchestratorExecutionMetadata")


@_attrs_define
class DominoJobsInterfaceOrchestratorExecutionMetadata:
    """
    Attributes:
        task_project_id (None | str | Unset):
        task_domain (None | str | Unset):
        task_execution_version (None | str | Unset):
        task_execution_name (None | str | Unset):
        node_id (None | str | Unset):
        node_project_id (None | str | Unset):
        node_domain (None | str | Unset):
        node_workflow_execution_name (None | str | Unset):
    """

    task_project_id: None | str | Unset = UNSET
    task_domain: None | str | Unset = UNSET
    task_execution_version: None | str | Unset = UNSET
    task_execution_name: None | str | Unset = UNSET
    node_id: None | str | Unset = UNSET
    node_project_id: None | str | Unset = UNSET
    node_domain: None | str | Unset = UNSET
    node_workflow_execution_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_project_id: None | str | Unset
        if isinstance(self.task_project_id, Unset):
            task_project_id = UNSET
        else:
            task_project_id = self.task_project_id

        task_domain: None | str | Unset
        if isinstance(self.task_domain, Unset):
            task_domain = UNSET
        else:
            task_domain = self.task_domain

        task_execution_version: None | str | Unset
        if isinstance(self.task_execution_version, Unset):
            task_execution_version = UNSET
        else:
            task_execution_version = self.task_execution_version

        task_execution_name: None | str | Unset
        if isinstance(self.task_execution_name, Unset):
            task_execution_name = UNSET
        else:
            task_execution_name = self.task_execution_name

        node_id: None | str | Unset
        if isinstance(self.node_id, Unset):
            node_id = UNSET
        else:
            node_id = self.node_id

        node_project_id: None | str | Unset
        if isinstance(self.node_project_id, Unset):
            node_project_id = UNSET
        else:
            node_project_id = self.node_project_id

        node_domain: None | str | Unset
        if isinstance(self.node_domain, Unset):
            node_domain = UNSET
        else:
            node_domain = self.node_domain

        node_workflow_execution_name: None | str | Unset
        if isinstance(self.node_workflow_execution_name, Unset):
            node_workflow_execution_name = UNSET
        else:
            node_workflow_execution_name = self.node_workflow_execution_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_project_id is not UNSET:
            field_dict["taskProjectId"] = task_project_id
        if task_domain is not UNSET:
            field_dict["taskDomain"] = task_domain
        if task_execution_version is not UNSET:
            field_dict["taskExecutionVersion"] = task_execution_version
        if task_execution_name is not UNSET:
            field_dict["taskExecutionName"] = task_execution_name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if node_project_id is not UNSET:
            field_dict["nodeProjectId"] = node_project_id
        if node_domain is not UNSET:
            field_dict["nodeDomain"] = node_domain
        if node_workflow_execution_name is not UNSET:
            field_dict["nodeWorkflowExecutionName"] = node_workflow_execution_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_task_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_project_id = _parse_task_project_id(d.pop("taskProjectId", UNSET))

        def _parse_task_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_domain = _parse_task_domain(d.pop("taskDomain", UNSET))

        def _parse_task_execution_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_execution_version = _parse_task_execution_version(d.pop("taskExecutionVersion", UNSET))

        def _parse_task_execution_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_execution_name = _parse_task_execution_name(d.pop("taskExecutionName", UNSET))

        def _parse_node_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_id = _parse_node_id(d.pop("nodeId", UNSET))

        def _parse_node_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_project_id = _parse_node_project_id(d.pop("nodeProjectId", UNSET))

        def _parse_node_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_domain = _parse_node_domain(d.pop("nodeDomain", UNSET))

        def _parse_node_workflow_execution_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_workflow_execution_name = _parse_node_workflow_execution_name(d.pop("nodeWorkflowExecutionName", UNSET))

        domino_jobs_interface_orchestrator_execution_metadata = cls(
            task_project_id=task_project_id,
            task_domain=task_domain,
            task_execution_version=task_execution_version,
            task_execution_name=task_execution_name,
            node_id=node_id,
            node_project_id=node_project_id,
            node_domain=node_domain,
            node_workflow_execution_name=node_workflow_execution_name,
        )

        domino_jobs_interface_orchestrator_execution_metadata.additional_properties = d
        return domino_jobs_interface_orchestrator_execution_metadata

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
