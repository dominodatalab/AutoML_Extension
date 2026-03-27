from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_named_link import DominoProjectsTemplatesApiModelsNamedLink


T = TypeVar("T", bound="DominoProjectsApiProjectHubTemplatesResult")


@_attrs_define
class DominoProjectsApiProjectHubTemplatesResult:
    """
    Attributes:
        template_id (str):
        title (str):
        categories (list[str]):
        created (datetime.datetime):
        updated (datetime.datetime):
        owner (DominoProjectsTemplatesApiModelsNamedLink):
        revision_id (str):
        description (None | str | Unset):
        base_64_logo (None | str | Unset):
        license_ (DominoProjectsTemplatesApiModelsNamedLink | Unset):
        data_format (None | str | Unset):
        recommended (bool | None | Unset):
        supported_domino_versions (list[str] | None | Unset):
    """

    template_id: str
    title: str
    categories: list[str]
    created: datetime.datetime
    updated: datetime.datetime
    owner: DominoProjectsTemplatesApiModelsNamedLink
    revision_id: str
    description: None | str | Unset = UNSET
    base_64_logo: None | str | Unset = UNSET
    license_: DominoProjectsTemplatesApiModelsNamedLink | Unset = UNSET
    data_format: None | str | Unset = UNSET
    recommended: bool | None | Unset = UNSET
    supported_domino_versions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        title = self.title

        categories = self.categories

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        owner = self.owner.to_dict()

        revision_id = self.revision_id

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

        license_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        data_format: None | str | Unset
        if isinstance(self.data_format, Unset):
            data_format = UNSET
        else:
            data_format = self.data_format

        recommended: bool | None | Unset
        if isinstance(self.recommended, Unset):
            recommended = UNSET
        else:
            recommended = self.recommended

        supported_domino_versions: list[str] | None | Unset
        if isinstance(self.supported_domino_versions, Unset):
            supported_domino_versions = UNSET
        elif isinstance(self.supported_domino_versions, list):
            supported_domino_versions = self.supported_domino_versions

        else:
            supported_domino_versions = self.supported_domino_versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateId": template_id,
                "title": title,
                "categories": categories,
                "created": created,
                "updated": updated,
                "owner": owner,
                "revisionId": revision_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if base_64_logo is not UNSET:
            field_dict["base64Logo"] = base_64_logo
        if license_ is not UNSET:
            field_dict["license"] = license_
        if data_format is not UNSET:
            field_dict["dataFormat"] = data_format
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if supported_domino_versions is not UNSET:
            field_dict["supportedDominoVersions"] = supported_domino_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_named_link import DominoProjectsTemplatesApiModelsNamedLink

        d = dict(src_dict)
        template_id = d.pop("templateId")

        title = d.pop("title")

        categories = cast(list[str], d.pop("categories"))

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        owner = DominoProjectsTemplatesApiModelsNamedLink.from_dict(d.pop("owner"))

        revision_id = d.pop("revisionId")

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

        _license_ = d.pop("license", UNSET)
        license_: DominoProjectsTemplatesApiModelsNamedLink | Unset
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = DominoProjectsTemplatesApiModelsNamedLink.from_dict(_license_)

        def _parse_data_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_format = _parse_data_format(d.pop("dataFormat", UNSET))

        def _parse_recommended(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        recommended = _parse_recommended(d.pop("recommended", UNSET))

        def _parse_supported_domino_versions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_domino_versions_type_0 = cast(list[str], data)

                return supported_domino_versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        supported_domino_versions = _parse_supported_domino_versions(d.pop("supportedDominoVersions", UNSET))

        domino_projects_api_project_hub_templates_result = cls(
            template_id=template_id,
            title=title,
            categories=categories,
            created=created,
            updated=updated,
            owner=owner,
            revision_id=revision_id,
            description=description,
            base_64_logo=base_64_logo,
            license_=license_,
            data_format=data_format,
            recommended=recommended,
            supported_domino_versions=supported_domino_versions,
        )

        domino_projects_api_project_hub_templates_result.additional_properties = d
        return domino_projects_api_project_hub_templates_result

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
