from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectTemplateDetailsV1")


@_attrs_define
class ProjectTemplateDetailsV1:
    """
    Attributes:
        name (str): name of the template Example: ImageNet Classifier.
        template_id (str): id of the template Example: templateId.
        force_import (bool | Unset): optional flag to force import the template code into the main repo, overwriting all
            git history
        import_to_main_repo (bool | Unset): optional flag to import the template code to the main repo, Github only
        template_revision_id (str | Unset): optional id of the revision of the template
        template_type (str | Unset): Specifying "ecosystem" or "customer" template type
    """

    name: str
    template_id: str
    force_import: bool | Unset = UNSET
    import_to_main_repo: bool | Unset = UNSET
    template_revision_id: str | Unset = UNSET
    template_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        template_id = self.template_id

        force_import = self.force_import

        import_to_main_repo = self.import_to_main_repo

        template_revision_id = self.template_revision_id

        template_type = self.template_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "templateId": template_id,
            }
        )
        if force_import is not UNSET:
            field_dict["forceImport"] = force_import
        if import_to_main_repo is not UNSET:
            field_dict["importToMainRepo"] = import_to_main_repo
        if template_revision_id is not UNSET:
            field_dict["templateRevisionId"] = template_revision_id
        if template_type is not UNSET:
            field_dict["templateType"] = template_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        template_id = d.pop("templateId")

        force_import = d.pop("forceImport", UNSET)

        import_to_main_repo = d.pop("importToMainRepo", UNSET)

        template_revision_id = d.pop("templateRevisionId", UNSET)

        template_type = d.pop("templateType", UNSET)

        project_template_details_v1 = cls(
            name=name,
            template_id=template_id,
            force_import=force_import,
            import_to_main_repo=import_to_main_repo,
            template_revision_id=template_revision_id,
            template_type=template_type,
        )

        project_template_details_v1.additional_properties = d
        return project_template_details_v1

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
