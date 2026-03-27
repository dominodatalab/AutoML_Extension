from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_computecluster_api_compute_cluster_config_response_dto import (
        DominoComputeclusterApiComputeClusterConfigResponseDto,
    )


T = TypeVar("T", bound="DominoComputeclusterApiComputeClusterDetails")


@_attrs_define
class DominoComputeclusterApiComputeClusterDetails:
    """
    Attributes:
        cluster_config (DominoComputeclusterApiComputeClusterConfigResponseDto):
        web_ui_path (None | str | Unset):
    """

    cluster_config: DominoComputeclusterApiComputeClusterConfigResponseDto
    web_ui_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_config = self.cluster_config.to_dict()

        web_ui_path: None | str | Unset
        if isinstance(self.web_ui_path, Unset):
            web_ui_path = UNSET
        else:
            web_ui_path = self.web_ui_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clusterConfig": cluster_config,
            }
        )
        if web_ui_path is not UNSET:
            field_dict["webUiPath"] = web_ui_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computecluster_api_compute_cluster_config_response_dto import (
            DominoComputeclusterApiComputeClusterConfigResponseDto,
        )

        d = dict(src_dict)
        cluster_config = DominoComputeclusterApiComputeClusterConfigResponseDto.from_dict(d.pop("clusterConfig"))

        def _parse_web_ui_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        web_ui_path = _parse_web_ui_path(d.pop("webUiPath", UNSET))

        domino_computecluster_api_compute_cluster_details = cls(
            cluster_config=cluster_config,
            web_ui_path=web_ui_path,
        )

        domino_computecluster_api_compute_cluster_details.additional_properties = d
        return domino_computecluster_api_compute_cluster_details

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
