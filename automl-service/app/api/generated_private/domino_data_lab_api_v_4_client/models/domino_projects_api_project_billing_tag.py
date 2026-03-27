from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag


T = TypeVar("T", bound="DominoProjectsApiProjectBillingTag")


@_attrs_define
class DominoProjectsApiProjectBillingTag:
    """
    Attributes:
        project_id (str):
        billing_tag (DominoProjectsApiBillingTag | Unset):
    """

    project_id: str
    billing_tag: DominoProjectsApiBillingTag | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        billing_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_tag, Unset):
            billing_tag = self.billing_tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
            }
        )
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag

        d = dict(src_dict)
        project_id = d.pop("projectId")

        _billing_tag = d.pop("billingTag", UNSET)
        billing_tag: DominoProjectsApiBillingTag | Unset
        if isinstance(_billing_tag, Unset):
            billing_tag = UNSET
        else:
            billing_tag = DominoProjectsApiBillingTag.from_dict(_billing_tag)

        domino_projects_api_project_billing_tag = cls(
            project_id=project_id,
            billing_tag=billing_tag,
        )

        domino_projects_api_project_billing_tag.additional_properties = d
        return domino_projects_api_project_billing_tag

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
