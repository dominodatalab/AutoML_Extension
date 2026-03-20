from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_customer_template_visibility import UpdateCustomerTemplateVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_template_collaborator import ProjectTemplateCollaborator


T = TypeVar("T", bound="UpdateCustomerTemplate")


@_attrs_define
class UpdateCustomerTemplate:
    """
    Attributes:
        collaborators (list[ProjectTemplateCollaborator] | Unset): The updated list of collaborators for the template.
            Will overwrite the existing list.
        description (str | Unset): The new description for the template
        is_company_official (bool | Unset): Whether or not to mark this template as official, indicating that it has
            been vetted by your company.
        name (str | Unset): The new name for the template
        tag_names (list[str] | Unset): The updated list of tags for the template. Will overwrite the existing list.
        visibility (UpdateCustomerTemplateVisibility | Unset): The new visibility for the template
    """

    collaborators: list[ProjectTemplateCollaborator] | Unset = UNSET
    description: str | Unset = UNSET
    is_company_official: bool | Unset = UNSET
    name: str | Unset = UNSET
    tag_names: list[str] | Unset = UNSET
    visibility: UpdateCustomerTemplateVisibility | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collaborators, Unset):
            collaborators = []
            for collaborators_item_data in self.collaborators:
                collaborators_item = collaborators_item_data.to_dict()
                collaborators.append(collaborators_item)

        description = self.description

        is_company_official = self.is_company_official

        name = self.name

        tag_names: list[str] | Unset = UNSET
        if not isinstance(self.tag_names, Unset):
            tag_names = self.tag_names

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if description is not UNSET:
            field_dict["description"] = description
        if is_company_official is not UNSET:
            field_dict["isCompanyOfficial"] = is_company_official
        if name is not UNSET:
            field_dict["name"] = name
        if tag_names is not UNSET:
            field_dict["tagNames"] = tag_names
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_template_collaborator import ProjectTemplateCollaborator

        d = dict(src_dict)
        _collaborators = d.pop("collaborators", UNSET)
        collaborators: list[ProjectTemplateCollaborator] | Unset = UNSET
        if _collaborators is not UNSET:
            collaborators = []
            for collaborators_item_data in _collaborators:
                collaborators_item = ProjectTemplateCollaborator.from_dict(collaborators_item_data)

                collaborators.append(collaborators_item)

        description = d.pop("description", UNSET)

        is_company_official = d.pop("isCompanyOfficial", UNSET)

        name = d.pop("name", UNSET)

        tag_names = cast(list[str], d.pop("tagNames", UNSET))

        _visibility = d.pop("visibility", UNSET)
        visibility: UpdateCustomerTemplateVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = UpdateCustomerTemplateVisibility(_visibility)

        update_customer_template = cls(
            collaborators=collaborators,
            description=description,
            is_company_official=is_company_official,
            name=name,
            tag_names=tag_names,
            visibility=visibility,
        )

        update_customer_template.additional_properties = d
        return update_customer_template

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
