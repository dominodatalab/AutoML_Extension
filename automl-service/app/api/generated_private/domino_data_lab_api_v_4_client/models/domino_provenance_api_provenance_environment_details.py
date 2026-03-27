from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProvenanceApiProvenanceEnvironmentDetails")


@_attrs_define
class DominoProvenanceApiProvenanceEnvironmentDetails:
    """
    Attributes:
        environment_id (str):
        environment_revision_id (str):
        environment_name (str):
        environment_revision_number (int):
    """

    environment_id: str
    environment_revision_id: str
    environment_name: str
    environment_revision_number: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_id = self.environment_id

        environment_revision_id = self.environment_revision_id

        environment_name = self.environment_name

        environment_revision_number = self.environment_revision_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environmentId": environment_id,
                "environmentRevisionId": environment_revision_id,
                "environmentName": environment_name,
                "environmentRevisionNumber": environment_revision_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        environment_id = d.pop("environmentId")

        environment_revision_id = d.pop("environmentRevisionId")

        environment_name = d.pop("environmentName")

        environment_revision_number = d.pop("environmentRevisionNumber")

        domino_provenance_api_provenance_environment_details = cls(
            environment_id=environment_id,
            environment_revision_id=environment_revision_id,
            environment_name=environment_name,
            environment_revision_number=environment_revision_number,
        )

        domino_provenance_api_provenance_environment_details.additional_properties = d
        return domino_provenance_api_provenance_environment_details

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
