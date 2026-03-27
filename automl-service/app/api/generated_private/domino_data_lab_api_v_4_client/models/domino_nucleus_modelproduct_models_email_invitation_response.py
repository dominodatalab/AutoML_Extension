from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_nucleus_modelproduct_models_email_invitation_failure import (
        DominoNucleusModelproductModelsEmailInvitationFailure,
    )


T = TypeVar("T", bound="DominoNucleusModelproductModelsEmailInvitationResponse")


@_attrs_define
class DominoNucleusModelproductModelsEmailInvitationResponse:
    """
    Attributes:
        succeeded (list[str]):
        failed (list[DominoNucleusModelproductModelsEmailInvitationFailure]):
    """

    succeeded: list[str]
    failed: list[DominoNucleusModelproductModelsEmailInvitationFailure]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        succeeded = self.succeeded

        failed = []
        for failed_item_data in self.failed:
            failed_item = failed_item_data.to_dict()
            failed.append(failed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "succeeded": succeeded,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_nucleus_modelproduct_models_email_invitation_failure import (
            DominoNucleusModelproductModelsEmailInvitationFailure,
        )

        d = dict(src_dict)
        succeeded = cast(list[str], d.pop("succeeded"))

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = DominoNucleusModelproductModelsEmailInvitationFailure.from_dict(failed_item_data)

            failed.append(failed_item)

        domino_nucleus_modelproduct_models_email_invitation_response = cls(
            succeeded=succeeded,
            failed=failed,
        )

        domino_nucleus_modelproduct_models_email_invitation_response.additional_properties = d
        return domino_nucleus_modelproduct_models_email_invitation_response

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
