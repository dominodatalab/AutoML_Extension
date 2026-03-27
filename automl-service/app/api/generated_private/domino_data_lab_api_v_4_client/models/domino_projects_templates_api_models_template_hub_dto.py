from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_projects_templates_api_models_template_hub_dto_kind import (
    DominoProjectsTemplatesApiModelsTemplateHubDtoKind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsTemplateHubDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsTemplateHubDto:
    """
    Attributes:
        name (str):
        kind (DominoProjectsTemplatesApiModelsTemplateHubDtoKind):
        total_templates (int):
        updated (datetime.datetime | None | Unset):
    """

    name: str
    kind: DominoProjectsTemplatesApiModelsTemplateHubDtoKind
    total_templates: int
    updated: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind = self.kind.value

        total_templates = self.total_templates

        updated: None | str | Unset
        if isinstance(self.updated, Unset):
            updated = UNSET
        elif isinstance(self.updated, datetime.datetime):
            updated = self.updated.isoformat()
        else:
            updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "totalTemplates": total_templates,
            }
        )
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        kind = DominoProjectsTemplatesApiModelsTemplateHubDtoKind(d.pop("kind"))

        total_templates = d.pop("totalTemplates")

        def _parse_updated(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_type_0 = isoparse(data)

                return updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated = _parse_updated(d.pop("updated", UNSET))

        domino_projects_templates_api_models_template_hub_dto = cls(
            name=name,
            kind=kind,
            total_templates=total_templates,
            updated=updated,
        )

        domino_projects_templates_api_models_template_hub_dto.additional_properties = d
        return domino_projects_templates_api_models_template_hub_dto

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
