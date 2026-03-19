from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.billing_tag_v1 import BillingTagV1


T = TypeVar("T", bound="BillingTagsEnvelopeV1")


@_attrs_define
class BillingTagsEnvelopeV1:
    """
    Attributes:
        billing_tags (list[BillingTagV1]):
    """

    billing_tags: list[BillingTagV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_tags = []
        for billing_tags_item_data in self.billing_tags:
            billing_tags_item = billing_tags_item_data.to_dict()
            billing_tags.append(billing_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billingTags": billing_tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_tag_v1 import BillingTagV1

        d = dict(src_dict)
        billing_tags = []
        _billing_tags = d.pop("billingTags")
        for billing_tags_item_data in _billing_tags:
            billing_tags_item = BillingTagV1.from_dict(billing_tags_item_data)

            billing_tags.append(billing_tags_item)

        billing_tags_envelope_v1 = cls(
            billing_tags=billing_tags,
        )

        billing_tags_envelope_v1.additional_properties = d
        return billing_tags_envelope_v1

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
