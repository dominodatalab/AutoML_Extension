from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_template_source_project_component import ProjectTemplateSourceProjectComponent

if TYPE_CHECKING:
    from ..models.template_backing_git_code_spec import TemplateBackingGitCodeSpec


T = TypeVar("T", bound="NewProjectTemplateSourceProject")


@_attrs_define
class NewProjectTemplateSourceProject:
    """
    Attributes:
        git_provider_code_spec (TemplateBackingGitCodeSpec):
        id (str):
        included (list[ProjectTemplateSourceProjectComponent]):
    """

    git_provider_code_spec: TemplateBackingGitCodeSpec
    id: str
    included: list[ProjectTemplateSourceProjectComponent]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git_provider_code_spec = self.git_provider_code_spec.to_dict()

        id = self.id

        included = []
        for included_item_data in self.included:
            included_item = included_item_data.value
            included.append(included_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gitProviderCodeSpec": git_provider_code_spec,
                "id": id,
                "included": included,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_backing_git_code_spec import TemplateBackingGitCodeSpec

        d = dict(src_dict)
        git_provider_code_spec = TemplateBackingGitCodeSpec.from_dict(d.pop("gitProviderCodeSpec"))

        id = d.pop("id")

        included = []
        _included = d.pop("included")
        for included_item_data in _included:
            included_item = ProjectTemplateSourceProjectComponent(included_item_data)

            included.append(included_item)

        new_project_template_source_project = cls(
            git_provider_code_spec=git_provider_code_spec,
            id=id,
            included=included,
        )

        new_project_template_source_project.additional_properties = d
        return new_project_template_source_project

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
