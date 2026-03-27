from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_layout_web_validate_step_request_step_id import DominoLayoutWebValidateStepRequestStepID
from ..models.domino_layout_web_validate_step_request_workflow_id import DominoLayoutWebValidateStepRequestWorkflowID

if TYPE_CHECKING:
    from ..models.domino_layout_web_validate_step_request_data import DominoLayoutWebValidateStepRequestData


T = TypeVar("T", bound="DominoLayoutWebValidateStepRequest")


@_attrs_define
class DominoLayoutWebValidateStepRequest:
    """
    Attributes:
        workflow_id (DominoLayoutWebValidateStepRequestWorkflowID):
        step_id (DominoLayoutWebValidateStepRequestStepID):
        data (DominoLayoutWebValidateStepRequestData):
    """

    workflow_id: DominoLayoutWebValidateStepRequestWorkflowID
    step_id: DominoLayoutWebValidateStepRequestStepID
    data: DominoLayoutWebValidateStepRequestData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id.value

        step_id = self.step_id.value

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflowID": workflow_id,
                "stepID": step_id,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_layout_web_validate_step_request_data import DominoLayoutWebValidateStepRequestData

        d = dict(src_dict)
        workflow_id = DominoLayoutWebValidateStepRequestWorkflowID(d.pop("workflowID"))

        step_id = DominoLayoutWebValidateStepRequestStepID(d.pop("stepID"))

        data = DominoLayoutWebValidateStepRequestData.from_dict(d.pop("data"))

        domino_layout_web_validate_step_request = cls(
            workflow_id=workflow_id,
            step_id=step_id,
            data=data,
        )

        domino_layout_web_validate_step_request.additional_properties = d
        return domino_layout_web_validate_step_request

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
