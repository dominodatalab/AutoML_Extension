from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoGruzApiRunPostProcessingControl")


@_attrs_define
class DominoGruzApiRunPostProcessingControl:
    """
    Attributes:
        publish_api_endpoint (bool):
        publish_model_id (None | str | Unset):
    """

    publish_api_endpoint: bool
    publish_model_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        publish_api_endpoint = self.publish_api_endpoint

        publish_model_id: None | str | Unset
        if isinstance(self.publish_model_id, Unset):
            publish_model_id = UNSET
        else:
            publish_model_id = self.publish_model_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publishApiEndpoint": publish_api_endpoint,
            }
        )
        if publish_model_id is not UNSET:
            field_dict["publishModelId"] = publish_model_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        publish_api_endpoint = d.pop("publishApiEndpoint")

        def _parse_publish_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publish_model_id = _parse_publish_model_id(d.pop("publishModelId", UNSET))

        domino_gruz_api_run_post_processing_control = cls(
            publish_api_endpoint=publish_api_endpoint,
            publish_model_id=publish_model_id,
        )

        domino_gruz_api_run_post_processing_control.additional_properties = d
        return domino_gruz_api_run_post_processing_control

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
