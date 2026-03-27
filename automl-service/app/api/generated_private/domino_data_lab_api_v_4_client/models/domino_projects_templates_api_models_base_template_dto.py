from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_projects_templates_api_models_base_template_dto_type import (
    DominoProjectsTemplatesApiModelsBaseTemplateDtoType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_template_access_dto import (
        DominoProjectsTemplatesApiModelsTemplateAccessDto,
    )
    from ..models.domino_projects_templates_api_models_template_owner_dto import (
        DominoProjectsTemplatesApiModelsTemplateOwnerDto,
    )


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsBaseTemplateDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsBaseTemplateDto:
    """
    Attributes:
        type_ (DominoProjectsTemplatesApiModelsBaseTemplateDtoType):
        id (str):
        name (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        categories (list[str]):
        owner (DominoProjectsTemplatesApiModelsTemplateOwnerDto):
        access (DominoProjectsTemplatesApiModelsTemplateAccessDto):
        description (None | str | Unset):
        base_64_logo (None | str | Unset):
        license_ (None | str | Unset):
        revision_id (None | str | Unset):
        recommended (bool | None | Unset):
        is_company_official (bool | None | Unset):
    """

    type_: DominoProjectsTemplatesApiModelsBaseTemplateDtoType
    id: str
    name: str
    created: datetime.datetime
    updated: datetime.datetime
    categories: list[str]
    owner: DominoProjectsTemplatesApiModelsTemplateOwnerDto
    access: DominoProjectsTemplatesApiModelsTemplateAccessDto
    description: None | str | Unset = UNSET
    base_64_logo: None | str | Unset = UNSET
    license_: None | str | Unset = UNSET
    revision_id: None | str | Unset = UNSET
    recommended: bool | None | Unset = UNSET
    is_company_official: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id = self.id

        name = self.name

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        categories = self.categories

        owner = self.owner.to_dict()

        access = self.access.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        base_64_logo: None | str | Unset
        if isinstance(self.base_64_logo, Unset):
            base_64_logo = UNSET
        else:
            base_64_logo = self.base_64_logo

        license_: None | str | Unset
        if isinstance(self.license_, Unset):
            license_ = UNSET
        else:
            license_ = self.license_

        revision_id: None | str | Unset
        if isinstance(self.revision_id, Unset):
            revision_id = UNSET
        else:
            revision_id = self.revision_id

        recommended: bool | None | Unset
        if isinstance(self.recommended, Unset):
            recommended = UNSET
        else:
            recommended = self.recommended

        is_company_official: bool | None | Unset
        if isinstance(self.is_company_official, Unset):
            is_company_official = UNSET
        else:
            is_company_official = self.is_company_official

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "created": created,
                "updated": updated,
                "categories": categories,
                "owner": owner,
                "access": access,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if base_64_logo is not UNSET:
            field_dict["base64Logo"] = base_64_logo
        if license_ is not UNSET:
            field_dict["license"] = license_
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if is_company_official is not UNSET:
            field_dict["isCompanyOfficial"] = is_company_official

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_template_access_dto import (
            DominoProjectsTemplatesApiModelsTemplateAccessDto,
        )
        from ..models.domino_projects_templates_api_models_template_owner_dto import (
            DominoProjectsTemplatesApiModelsTemplateOwnerDto,
        )

        d = dict(src_dict)
        type_ = DominoProjectsTemplatesApiModelsBaseTemplateDtoType(d.pop("type"))

        id = d.pop("id")

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        categories = cast(list[str], d.pop("categories"))

        owner = DominoProjectsTemplatesApiModelsTemplateOwnerDto.from_dict(d.pop("owner"))

        access = DominoProjectsTemplatesApiModelsTemplateAccessDto.from_dict(d.pop("access"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_base_64_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_64_logo = _parse_base_64_logo(d.pop("base64Logo", UNSET))

        def _parse_license_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_ = _parse_license_(d.pop("license", UNSET))

        def _parse_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revision_id = _parse_revision_id(d.pop("revisionId", UNSET))

        def _parse_recommended(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        recommended = _parse_recommended(d.pop("recommended", UNSET))

        def _parse_is_company_official(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_company_official = _parse_is_company_official(d.pop("isCompanyOfficial", UNSET))

        domino_projects_templates_api_models_base_template_dto = cls(
            type_=type_,
            id=id,
            name=name,
            created=created,
            updated=updated,
            categories=categories,
            owner=owner,
            access=access,
            description=description,
            base_64_logo=base_64_logo,
            license_=license_,
            revision_id=revision_id,
            recommended=recommended,
            is_company_official=is_company_official,
        )

        domino_projects_templates_api_models_base_template_dto.additional_properties = d
        return domino_projects_templates_api_models_base_template_dto

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
