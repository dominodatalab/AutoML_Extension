from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoNucleusProjectModelsUpdateESignatureWorkflowSetting")


@_attrs_define
class DominoNucleusProjectModelsUpdateESignatureWorkflowSetting:
    """
    Attributes:
        require_e_signature_workflow (bool):
    """

    require_e_signature_workflow: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        require_e_signature_workflow = self.require_e_signature_workflow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requireESignatureWorkflow": require_e_signature_workflow,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        require_e_signature_workflow = d.pop("requireESignatureWorkflow")

        domino_nucleus_project_models_update_e_signature_workflow_setting = cls(
            require_e_signature_workflow=require_e_signature_workflow,
        )

        domino_nucleus_project_models_update_e_signature_workflow_setting.additional_properties = d
        return domino_nucleus_project_models_update_e_signature_workflow_setting

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
