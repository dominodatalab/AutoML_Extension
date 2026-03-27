from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_project_template_details_template_type import (
    DominoProjectsApiProjectTemplateDetailsTemplateType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiProjectTemplateDetails")


@_attrs_define
class DominoProjectsApiProjectTemplateDetails:
    """
    Attributes:
        name (str):
        template_id (str):
        template_type (DominoProjectsApiProjectTemplateDetailsTemplateType | Unset):
        template_revision_id (None | str | Unset):
        import_to_main_repo (bool | None | Unset):
        force_import (bool | None | Unset):
    """

    name: str
    template_id: str
    template_type: DominoProjectsApiProjectTemplateDetailsTemplateType | Unset = UNSET
    template_revision_id: None | str | Unset = UNSET
    import_to_main_repo: bool | None | Unset = UNSET
    force_import: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        template_id = self.template_id

        template_type: str | Unset = UNSET
        if not isinstance(self.template_type, Unset):
            template_type = self.template_type.value

        template_revision_id: None | str | Unset
        if isinstance(self.template_revision_id, Unset):
            template_revision_id = UNSET
        else:
            template_revision_id = self.template_revision_id

        import_to_main_repo: bool | None | Unset
        if isinstance(self.import_to_main_repo, Unset):
            import_to_main_repo = UNSET
        else:
            import_to_main_repo = self.import_to_main_repo

        force_import: bool | None | Unset
        if isinstance(self.force_import, Unset):
            force_import = UNSET
        else:
            force_import = self.force_import

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "templateId": template_id,
            }
        )
        if template_type is not UNSET:
            field_dict["templateType"] = template_type
        if template_revision_id is not UNSET:
            field_dict["templateRevisionId"] = template_revision_id
        if import_to_main_repo is not UNSET:
            field_dict["importToMainRepo"] = import_to_main_repo
        if force_import is not UNSET:
            field_dict["forceImport"] = force_import

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        template_id = d.pop("templateId")

        _template_type = d.pop("templateType", UNSET)
        template_type: DominoProjectsApiProjectTemplateDetailsTemplateType | Unset
        if isinstance(_template_type, Unset):
            template_type = UNSET
        else:
            template_type = DominoProjectsApiProjectTemplateDetailsTemplateType(_template_type)

        def _parse_template_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_revision_id = _parse_template_revision_id(d.pop("templateRevisionId", UNSET))

        def _parse_import_to_main_repo(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        import_to_main_repo = _parse_import_to_main_repo(d.pop("importToMainRepo", UNSET))

        def _parse_force_import(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force_import = _parse_force_import(d.pop("forceImport", UNSET))

        domino_projects_api_project_template_details = cls(
            name=name,
            template_id=template_id,
            template_type=template_type,
            template_revision_id=template_revision_id,
            import_to_main_repo=import_to_main_repo,
            force_import=force_import,
        )

        domino_projects_api_project_template_details.additional_properties = d
        return domino_projects_api_project_template_details

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
