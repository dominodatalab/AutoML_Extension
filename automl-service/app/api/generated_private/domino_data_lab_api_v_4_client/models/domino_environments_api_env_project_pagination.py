from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoEnvironmentsApiEnvProjectPagination")


@_attrs_define
class DominoEnvironmentsApiEnvProjectPagination:
    """
    Attributes:
        page_size (int):
        page_no (int):
    """

    page_size: int
    page_no: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        page_no = self.page_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageSize": page_size,
                "pageNo": page_no,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_size = d.pop("pageSize")

        page_no = d.pop("pageNo")

        domino_environments_api_env_project_pagination = cls(
            page_size=page_size,
            page_no=page_no,
        )

        domino_environments_api_env_project_pagination.additional_properties = d
        return domino_environments_api_env_project_pagination

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
