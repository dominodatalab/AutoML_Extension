from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_layout_web_complete_workflow_request_workflow_id import (
    DominoLayoutWebCompleteWorkflowRequestWorkflowID,
)

if TYPE_CHECKING:
    from ..models.domino_layout_web_complete_workflow_request_data import DominoLayoutWebCompleteWorkflowRequestData


T = TypeVar("T", bound="DominoLayoutWebCompleteWorkflowRequest")


@_attrs_define
class DominoLayoutWebCompleteWorkflowRequest:
    """
    Attributes:
        workflow_id (DominoLayoutWebCompleteWorkflowRequestWorkflowID):
        data (DominoLayoutWebCompleteWorkflowRequestData):
    """

    workflow_id: DominoLayoutWebCompleteWorkflowRequestWorkflowID
    data: DominoLayoutWebCompleteWorkflowRequestData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id.value

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflowID": workflow_id,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_layout_web_complete_workflow_request_data import DominoLayoutWebCompleteWorkflowRequestData

        d = dict(src_dict)
        workflow_id = DominoLayoutWebCompleteWorkflowRequestWorkflowID(d.pop("workflowID"))

        data = DominoLayoutWebCompleteWorkflowRequestData.from_dict(d.pop("data"))

        domino_layout_web_complete_workflow_request = cls(
            workflow_id=workflow_id,
            data=data,
        )

        domino_layout_web_complete_workflow_request.additional_properties = d
        return domino_layout_web_complete_workflow_request

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
