from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_tag_v1 import BillingTagV1
    from ..models.new_project_template_definition import NewProjectTemplateDefinition
    from ..models.new_project_template_source_project import NewProjectTemplateSourceProject
    from ..models.project_template_access import ProjectTemplateAccess


T = TypeVar("T", bound="NewCustomerTemplate")


@_attrs_define
class NewCustomerTemplate:
    """
    Attributes:
        access (ProjectTemplateAccess):
        definition (NewProjectTemplateDefinition):
        name (str):
        source_project (NewProjectTemplateSourceProject):
        billing_tag (BillingTagV1 | Unset): Billing Tag to assign to projects for cost aggregation
        description (str | Unset):
    """

    access: ProjectTemplateAccess
    definition: NewProjectTemplateDefinition
    name: str
    source_project: NewProjectTemplateSourceProject
    billing_tag: BillingTagV1 | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access.to_dict()

        definition = self.definition.to_dict()

        name = self.name

        source_project = self.source_project.to_dict()

        billing_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_tag, Unset):
            billing_tag = self.billing_tag.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "definition": definition,
                "name": name,
                "sourceProject": source_project,
            }
        )
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_tag_v1 import BillingTagV1
        from ..models.new_project_template_definition import NewProjectTemplateDefinition
        from ..models.new_project_template_source_project import NewProjectTemplateSourceProject
        from ..models.project_template_access import ProjectTemplateAccess

        d = dict(src_dict)
        access = ProjectTemplateAccess.from_dict(d.pop("access"))

        definition = NewProjectTemplateDefinition.from_dict(d.pop("definition"))

        name = d.pop("name")

        source_project = NewProjectTemplateSourceProject.from_dict(d.pop("sourceProject"))

        _billing_tag = d.pop("billingTag", UNSET)
        billing_tag: BillingTagV1 | Unset
        if isinstance(_billing_tag, Unset):
            billing_tag = UNSET
        else:
            billing_tag = BillingTagV1.from_dict(_billing_tag)

        description = d.pop("description", UNSET)

        new_customer_template = cls(
            access=access,
            definition=definition,
            name=name,
            source_project=source_project,
            billing_tag=billing_tag,
            description=description,
        )

        new_customer_template.additional_properties = d
        return new_customer_template

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
