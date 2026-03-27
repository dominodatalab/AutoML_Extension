from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsApiUpdateProjectAnonymousRunExecutionSettings")


@_attrs_define
class DominoProjectsApiUpdateProjectAnonymousRunExecutionSettings:
    """
    Attributes:
        allow_public_run_execution (bool):
    """

    allow_public_run_execution: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_public_run_execution = self.allow_public_run_execution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowPublicRunExecution": allow_public_run_execution,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_public_run_execution = d.pop("allowPublicRunExecution")

        domino_projects_api_update_project_anonymous_run_execution_settings = cls(
            allow_public_run_execution=allow_public_run_execution,
        )

        domino_projects_api_update_project_anonymous_run_execution_settings.additional_properties = d
        return domino_projects_api_update_project_anonymous_run_execution_settings

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
