from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasource_api_data_source_proxy_config_dto_data_source_type import (
    DominoDatasourceApiDataSourceProxyConfigDtoDataSourceType,
)
from ..models.domino_datasource_api_data_source_proxy_config_dto_engine_type import (
    DominoDatasourceApiDataSourceProxyConfigDtoEngineType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasource_api_data_source_proxy_config_dto_config import (
        DominoDatasourceApiDataSourceProxyConfigDtoConfig,
    )
    from ..models.domino_datasource_api_engine_config import DominoDatasourceApiEngineConfig


T = TypeVar("T", bound="DominoDatasourceApiDataSourceProxyConfigDto")


@_attrs_define
class DominoDatasourceApiDataSourceProxyConfigDto:
    """
    Attributes:
        config (DominoDatasourceApiDataSourceProxyConfigDtoConfig):
        data_source_type (DominoDatasourceApiDataSourceProxyConfigDtoDataSourceType):
        engine_type (DominoDatasourceApiDataSourceProxyConfigDtoEngineType):
        data_plane_ids (list[str]):
        available_hardware_tiers (list[str]):
        data_source_name (str):
        data_source_id (str):
        engine_config (DominoDatasourceApiEngineConfig | Unset):
    """

    config: DominoDatasourceApiDataSourceProxyConfigDtoConfig
    data_source_type: DominoDatasourceApiDataSourceProxyConfigDtoDataSourceType
    engine_type: DominoDatasourceApiDataSourceProxyConfigDtoEngineType
    data_plane_ids: list[str]
    available_hardware_tiers: list[str]
    data_source_name: str
    data_source_id: str
    engine_config: DominoDatasourceApiEngineConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        data_source_type = self.data_source_type.value

        engine_type = self.engine_type.value

        data_plane_ids = self.data_plane_ids

        available_hardware_tiers = self.available_hardware_tiers

        data_source_name = self.data_source_name

        data_source_id = self.data_source_id

        engine_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.engine_config, Unset):
            engine_config = self.engine_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "dataSourceType": data_source_type,
                "engineType": engine_type,
                "dataPlaneIds": data_plane_ids,
                "availableHardwareTiers": available_hardware_tiers,
                "dataSourceName": data_source_name,
                "dataSourceId": data_source_id,
            }
        )
        if engine_config is not UNSET:
            field_dict["engineConfig"] = engine_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_api_data_source_proxy_config_dto_config import (
            DominoDatasourceApiDataSourceProxyConfigDtoConfig,
        )
        from ..models.domino_datasource_api_engine_config import DominoDatasourceApiEngineConfig

        d = dict(src_dict)
        config = DominoDatasourceApiDataSourceProxyConfigDtoConfig.from_dict(d.pop("config"))

        data_source_type = DominoDatasourceApiDataSourceProxyConfigDtoDataSourceType(d.pop("dataSourceType"))

        engine_type = DominoDatasourceApiDataSourceProxyConfigDtoEngineType(d.pop("engineType"))

        data_plane_ids = cast(list[str], d.pop("dataPlaneIds"))

        available_hardware_tiers = cast(list[str], d.pop("availableHardwareTiers"))

        data_source_name = d.pop("dataSourceName")

        data_source_id = d.pop("dataSourceId")

        _engine_config = d.pop("engineConfig", UNSET)
        engine_config: DominoDatasourceApiEngineConfig | Unset
        if isinstance(_engine_config, Unset):
            engine_config = UNSET
        else:
            engine_config = DominoDatasourceApiEngineConfig.from_dict(_engine_config)

        domino_datasource_api_data_source_proxy_config_dto = cls(
            config=config,
            data_source_type=data_source_type,
            engine_type=engine_type,
            data_plane_ids=data_plane_ids,
            available_hardware_tiers=available_hardware_tiers,
            data_source_name=data_source_name,
            data_source_id=data_source_id,
            engine_config=engine_config,
        )

        domino_datasource_api_data_source_proxy_config_dto.additional_properties = d
        return domino_datasource_api_data_source_proxy_config_dto

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
