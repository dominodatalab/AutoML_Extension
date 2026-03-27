from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_environments_api_paginated_revision_info import DominoEnvironmentsApiPaginatedRevisionInfo
    from ..models.domino_environments_api_revision_summary import DominoEnvironmentsApiRevisionSummary


T = TypeVar("T", bound="DominoEnvironmentsApiPaginatedRevisionData")


@_attrs_define
class DominoEnvironmentsApiPaginatedRevisionData:
    """
    Attributes:
        revisions (list[DominoEnvironmentsApiRevisionSummary]):
        page_info (DominoEnvironmentsApiPaginatedRevisionInfo):
    """

    revisions: list[DominoEnvironmentsApiRevisionSummary]
    page_info: DominoEnvironmentsApiPaginatedRevisionInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revisions = []
        for revisions_item_data in self.revisions:
            revisions_item = revisions_item_data.to_dict()
            revisions.append(revisions_item)

        page_info = self.page_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revisions": revisions,
                "pageInfo": page_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_paginated_revision_info import DominoEnvironmentsApiPaginatedRevisionInfo
        from ..models.domino_environments_api_revision_summary import DominoEnvironmentsApiRevisionSummary

        d = dict(src_dict)
        revisions = []
        _revisions = d.pop("revisions")
        for revisions_item_data in _revisions:
            revisions_item = DominoEnvironmentsApiRevisionSummary.from_dict(revisions_item_data)

            revisions.append(revisions_item)

        page_info = DominoEnvironmentsApiPaginatedRevisionInfo.from_dict(d.pop("pageInfo"))

        domino_environments_api_paginated_revision_data = cls(
            revisions=revisions,
            page_info=page_info,
        )

        domino_environments_api_paginated_revision_data.additional_properties = d
        return domino_environments_api_paginated_revision_data

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
