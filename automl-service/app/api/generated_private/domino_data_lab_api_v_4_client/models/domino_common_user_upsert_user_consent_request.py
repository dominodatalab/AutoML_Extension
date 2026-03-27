from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_user_upsert_user_consent_request_consent_details_type_0 import (
        DominoCommonUserUpsertUserConsentRequestConsentDetailsType0,
    )


T = TypeVar("T", bound="DominoCommonUserUpsertUserConsentRequest")


@_attrs_define
class DominoCommonUserUpsertUserConsentRequest:
    """
    Attributes:
        execution_type (str):
        execution_id (str):
        exp (int | None | Unset):
        consent_details (DominoCommonUserUpsertUserConsentRequestConsentDetailsType0 | None | Unset):
    """

    execution_type: str
    execution_id: str
    exp: int | None | Unset = UNSET
    consent_details: DominoCommonUserUpsertUserConsentRequestConsentDetailsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_common_user_upsert_user_consent_request_consent_details_type_0 import (
            DominoCommonUserUpsertUserConsentRequestConsentDetailsType0,
        )

        execution_type = self.execution_type

        execution_id = self.execution_id

        exp: int | None | Unset
        if isinstance(self.exp, Unset):
            exp = UNSET
        else:
            exp = self.exp

        consent_details: dict[str, Any] | None | Unset
        if isinstance(self.consent_details, Unset):
            consent_details = UNSET
        elif isinstance(self.consent_details, DominoCommonUserUpsertUserConsentRequestConsentDetailsType0):
            consent_details = self.consent_details.to_dict()
        else:
            consent_details = self.consent_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "executionType": execution_type,
                "executionId": execution_id,
            }
        )
        if exp is not UNSET:
            field_dict["exp"] = exp
        if consent_details is not UNSET:
            field_dict["consentDetails"] = consent_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_user_upsert_user_consent_request_consent_details_type_0 import (
            DominoCommonUserUpsertUserConsentRequestConsentDetailsType0,
        )

        d = dict(src_dict)
        execution_type = d.pop("executionType")

        execution_id = d.pop("executionId")

        def _parse_exp(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exp = _parse_exp(d.pop("exp", UNSET))

        def _parse_consent_details(
            data: object,
        ) -> DominoCommonUserUpsertUserConsentRequestConsentDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                consent_details_type_0 = DominoCommonUserUpsertUserConsentRequestConsentDetailsType0.from_dict(data)

                return consent_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoCommonUserUpsertUserConsentRequestConsentDetailsType0 | None | Unset, data)

        consent_details = _parse_consent_details(d.pop("consentDetails", UNSET))

        domino_common_user_upsert_user_consent_request = cls(
            execution_type=execution_type,
            execution_id=execution_id,
            exp=exp,
            consent_details=consent_details,
        )

        domino_common_user_upsert_user_consent_request.additional_properties = d
        return domino_common_user_upsert_user_consent_request

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
