from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.project_template_template_type import ProjectTemplateTemplateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_template_access import ProjectTemplateAccess
    from ..models.project_template_definition import ProjectTemplateDefinition
    from ..models.project_template_owner import ProjectTemplateOwner
    from ..models.project_template_source_project import ProjectTemplateSourceProject


T = TypeVar("T", bound="CustomerTemplate")


@_attrs_define
class CustomerTemplate:
    """
    Attributes:
        access (ProjectTemplateAccess):
        categories (list[str]):
        created (datetime.datetime):
        id (str):
        name (str):
        owner (ProjectTemplateOwner):
        template_type (ProjectTemplateTemplateType):
        updated (datetime.datetime):
        is_company_official (bool): Whether or not this template is marked as official
        definition (ProjectTemplateDefinition):
        is_archived (bool):
        source_project (ProjectTemplateSourceProject):
        base_64_logo (str | Unset):
        description (str | Unset):
        license_ (str | Unset):
        recommended (bool | Unset):
        revision_id (str | Unset):
    """

    access: ProjectTemplateAccess
    categories: list[str]
    created: datetime.datetime
    id: str
    name: str
    owner: ProjectTemplateOwner
    template_type: ProjectTemplateTemplateType
    updated: datetime.datetime
    is_company_official: bool
    definition: ProjectTemplateDefinition
    is_archived: bool
    source_project: ProjectTemplateSourceProject
    base_64_logo: str | Unset = UNSET
    description: str | Unset = UNSET
    license_: str | Unset = UNSET
    recommended: bool | Unset = UNSET
    revision_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access.to_dict()

        categories = self.categories

        created = self.created.isoformat()

        id = self.id

        name = self.name

        owner = self.owner.to_dict()

        template_type = self.template_type.value

        updated = self.updated.isoformat()

        is_company_official = self.is_company_official

        definition = self.definition.to_dict()

        is_archived = self.is_archived

        source_project = self.source_project.to_dict()

        base_64_logo = self.base_64_logo

        description = self.description

        license_ = self.license_

        recommended = self.recommended

        revision_id = self.revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "categories": categories,
                "created": created,
                "id": id,
                "name": name,
                "owner": owner,
                "templateType": template_type,
                "updated": updated,
                "isCompanyOfficial": is_company_official,
                "definition": definition,
                "isArchived": is_archived,
                "sourceProject": source_project,
            }
        )
        if base_64_logo is not UNSET:
            field_dict["base64Logo"] = base_64_logo
        if description is not UNSET:
            field_dict["description"] = description
        if license_ is not UNSET:
            field_dict["license"] = license_
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_template_access import ProjectTemplateAccess
        from ..models.project_template_definition import ProjectTemplateDefinition
        from ..models.project_template_owner import ProjectTemplateOwner
        from ..models.project_template_source_project import ProjectTemplateSourceProject

        d = dict(src_dict)
        access = ProjectTemplateAccess.from_dict(d.pop("access"))

        categories = cast(list[str], d.pop("categories"))

        created = isoparse(d.pop("created"))

        id = d.pop("id")

        name = d.pop("name")

        owner = ProjectTemplateOwner.from_dict(d.pop("owner"))

        template_type = ProjectTemplateTemplateType(d.pop("templateType"))

        updated = isoparse(d.pop("updated"))

        is_company_official = d.pop("isCompanyOfficial")

        definition = ProjectTemplateDefinition.from_dict(d.pop("definition"))

        is_archived = d.pop("isArchived")

        source_project = ProjectTemplateSourceProject.from_dict(d.pop("sourceProject"))

        base_64_logo = d.pop("base64Logo", UNSET)

        description = d.pop("description", UNSET)

        license_ = d.pop("license", UNSET)

        recommended = d.pop("recommended", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        customer_template = cls(
            access=access,
            categories=categories,
            created=created,
            id=id,
            name=name,
            owner=owner,
            template_type=template_type,
            updated=updated,
            is_company_official=is_company_official,
            definition=definition,
            is_archived=is_archived,
            source_project=source_project,
            base_64_logo=base_64_logo,
            description=description,
            license_=license_,
            recommended=recommended,
            revision_id=revision_id,
        )

        customer_template.additional_properties = d
        return customer_template

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
