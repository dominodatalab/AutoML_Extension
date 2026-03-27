from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_layout_web_owner_info_dto import DominoLayoutWebOwnerInfoDto


T = TypeVar("T", bound="DominoLayoutWebCompleteWorkflowResponse")


@_attrs_define
class DominoLayoutWebCompleteWorkflowResponse:
    """
    Attributes:
        errors (list[str]):
        success (bool):
        id (None | str | Unset):
        name (None | str | Unset):
        owner_info (DominoLayoutWebOwnerInfoDto | Unset):
    """

    errors: list[str]
    success: bool
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    owner_info: DominoLayoutWebOwnerInfoDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = self.errors

        success = self.success

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        owner_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner_info, Unset):
            owner_info = self.owner_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "success": success,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if owner_info is not UNSET:
            field_dict["ownerInfo"] = owner_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_layout_web_owner_info_dto import DominoLayoutWebOwnerInfoDto

        d = dict(src_dict)
        errors = cast(list[str], d.pop("errors"))

        success = d.pop("success")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _owner_info = d.pop("ownerInfo", UNSET)
        owner_info: DominoLayoutWebOwnerInfoDto | Unset
        if isinstance(_owner_info, Unset):
            owner_info = UNSET
        else:
            owner_info = DominoLayoutWebOwnerInfoDto.from_dict(_owner_info)

        domino_layout_web_complete_workflow_response = cls(
            errors=errors,
            success=success,
            id=id,
            name=name,
            owner_info=owner_info,
        )

        domino_layout_web_complete_workflow_response.additional_properties = d
        return domino_layout_web_complete_workflow_response

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
