from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_quota_api_quota_type import DominoQuotaApiQuotaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_quota_api_quota_dto_action_metadata import DominoQuotaApiQuotaDtoActionMetadata
    from ..models.domino_quota_api_quota_dto_target_metadata import DominoQuotaApiQuotaDtoTargetMetadata


T = TypeVar("T", bound="DominoQuotaApiQuotaDto")


@_attrs_define
class DominoQuotaApiQuotaDto:
    """
    Attributes:
        id (str): quota Id
        quota_type (DominoQuotaApiQuotaType): type of quota
        limit (int | Unset): quota limit
        target_id (str | Unset): Id of user for quota
        action_metadata (DominoQuotaApiQuotaDtoActionMetadata | Unset):
        target_metadata (DominoQuotaApiQuotaDtoTargetMetadata | Unset):
    """

    id: str
    quota_type: DominoQuotaApiQuotaType
    limit: int | Unset = UNSET
    target_id: str | Unset = UNSET
    action_metadata: DominoQuotaApiQuotaDtoActionMetadata | Unset = UNSET
    target_metadata: DominoQuotaApiQuotaDtoTargetMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quota_type = self.quota_type.value

        limit = self.limit

        target_id = self.target_id

        action_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_metadata, Unset):
            action_metadata = self.action_metadata.to_dict()

        target_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_metadata, Unset):
            target_metadata = self.target_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quotaType": quota_type,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if action_metadata is not UNSET:
            field_dict["actionMetadata"] = action_metadata
        if target_metadata is not UNSET:
            field_dict["targetMetadata"] = target_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_quota_api_quota_dto_action_metadata import DominoQuotaApiQuotaDtoActionMetadata
        from ..models.domino_quota_api_quota_dto_target_metadata import DominoQuotaApiQuotaDtoTargetMetadata

        d = dict(src_dict)
        id = d.pop("id")

        quota_type = DominoQuotaApiQuotaType(d.pop("quotaType"))

        limit = d.pop("limit", UNSET)

        target_id = d.pop("targetId", UNSET)

        _action_metadata = d.pop("actionMetadata", UNSET)
        action_metadata: DominoQuotaApiQuotaDtoActionMetadata | Unset
        if isinstance(_action_metadata, Unset):
            action_metadata = UNSET
        else:
            action_metadata = DominoQuotaApiQuotaDtoActionMetadata.from_dict(_action_metadata)

        _target_metadata = d.pop("targetMetadata", UNSET)
        target_metadata: DominoQuotaApiQuotaDtoTargetMetadata | Unset
        if isinstance(_target_metadata, Unset):
            target_metadata = UNSET
        else:
            target_metadata = DominoQuotaApiQuotaDtoTargetMetadata.from_dict(_target_metadata)

        domino_quota_api_quota_dto = cls(
            id=id,
            quota_type=quota_type,
            limit=limit,
            target_id=target_id,
            action_metadata=action_metadata,
            target_metadata=target_metadata,
        )

        domino_quota_api_quota_dto.additional_properties = d
        return domino_quota_api_quota_dto

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
