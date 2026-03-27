from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoModelmanagerWebExportImageForNvidiaApiRequest")


@_attrs_define
class DominoModelmanagerWebExportImageForNvidiaApiRequest:
    """
    Attributes:
        container_repository (str):
        helm_repository (str):
        helm_version (str):
        ngc_api_key (str):
        tag (None | str | Unset):
    """

    container_repository: str
    helm_repository: str
    helm_version: str
    ngc_api_key: str
    tag: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_repository = self.container_repository

        helm_repository = self.helm_repository

        helm_version = self.helm_version

        ngc_api_key = self.ngc_api_key

        tag: None | str | Unset
        if isinstance(self.tag, Unset):
            tag = UNSET
        else:
            tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "containerRepository": container_repository,
                "helmRepository": helm_repository,
                "helmVersion": helm_version,
                "ngcApiKey": ngc_api_key,
            }
        )
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        container_repository = d.pop("containerRepository")

        helm_repository = d.pop("helmRepository")

        helm_version = d.pop("helmVersion")

        ngc_api_key = d.pop("ngcApiKey")

        def _parse_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tag = _parse_tag(d.pop("tag", UNSET))

        domino_modelmanager_web_export_image_for_nvidia_api_request = cls(
            container_repository=container_repository,
            helm_repository=helm_repository,
            helm_version=helm_version,
            ngc_api_key=ngc_api_key,
            tag=tag,
        )

        domino_modelmanager_web_export_image_for_nvidia_api_request.additional_properties = d
        return domino_modelmanager_web_export_image_for_nvidia_api_request

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
