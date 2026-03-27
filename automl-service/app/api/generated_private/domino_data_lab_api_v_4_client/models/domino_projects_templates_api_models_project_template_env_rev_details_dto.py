from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsProjectTemplateEnvRevDetailsDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsProjectTemplateEnvRevDetailsDto:
    """
    Attributes:
        environment_id (str):
        revision_number (int):
        link (str):
    """

    environment_id: str
    revision_number: int
    link: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_id = self.environment_id

        revision_number = self.revision_number

        link = self.link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environmentId": environment_id,
                "revisionNumber": revision_number,
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        environment_id = d.pop("environmentId")

        revision_number = d.pop("revisionNumber")

        link = d.pop("link")

        domino_projects_templates_api_models_project_template_env_rev_details_dto = cls(
            environment_id=environment_id,
            revision_number=revision_number,
            link=link,
        )

        domino_projects_templates_api_models_project_template_env_rev_details_dto.additional_properties = d
        return domino_projects_templates_api_models_project_template_env_rev_details_dto

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
