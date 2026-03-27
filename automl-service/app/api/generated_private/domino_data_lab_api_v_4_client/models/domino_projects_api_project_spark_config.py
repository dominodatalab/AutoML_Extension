from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiProjectSparkConfig")


@_attrs_define
class DominoProjectsApiProjectSparkConfig:
    """
    Attributes:
        spark_mode (str):
        spark_legacy_proxiable (bool | None | Unset):
        master_host (None | str | Unset):
        master_port (int | None | Unset):
        free_form_config (None | str | Unset):
        yarn_free_form_config (None | str | Unset):
        on_demand_free_form_config (None | str | Unset):
        hostname_mappings (None | str | Unset):
        hadoop_user_name (None | str | Unset):
    """

    spark_mode: str
    spark_legacy_proxiable: bool | None | Unset = UNSET
    master_host: None | str | Unset = UNSET
    master_port: int | None | Unset = UNSET
    free_form_config: None | str | Unset = UNSET
    yarn_free_form_config: None | str | Unset = UNSET
    on_demand_free_form_config: None | str | Unset = UNSET
    hostname_mappings: None | str | Unset = UNSET
    hadoop_user_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spark_mode = self.spark_mode

        spark_legacy_proxiable: bool | None | Unset
        if isinstance(self.spark_legacy_proxiable, Unset):
            spark_legacy_proxiable = UNSET
        else:
            spark_legacy_proxiable = self.spark_legacy_proxiable

        master_host: None | str | Unset
        if isinstance(self.master_host, Unset):
            master_host = UNSET
        else:
            master_host = self.master_host

        master_port: int | None | Unset
        if isinstance(self.master_port, Unset):
            master_port = UNSET
        else:
            master_port = self.master_port

        free_form_config: None | str | Unset
        if isinstance(self.free_form_config, Unset):
            free_form_config = UNSET
        else:
            free_form_config = self.free_form_config

        yarn_free_form_config: None | str | Unset
        if isinstance(self.yarn_free_form_config, Unset):
            yarn_free_form_config = UNSET
        else:
            yarn_free_form_config = self.yarn_free_form_config

        on_demand_free_form_config: None | str | Unset
        if isinstance(self.on_demand_free_form_config, Unset):
            on_demand_free_form_config = UNSET
        else:
            on_demand_free_form_config = self.on_demand_free_form_config

        hostname_mappings: None | str | Unset
        if isinstance(self.hostname_mappings, Unset):
            hostname_mappings = UNSET
        else:
            hostname_mappings = self.hostname_mappings

        hadoop_user_name: None | str | Unset
        if isinstance(self.hadoop_user_name, Unset):
            hadoop_user_name = UNSET
        else:
            hadoop_user_name = self.hadoop_user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sparkMode": spark_mode,
            }
        )
        if spark_legacy_proxiable is not UNSET:
            field_dict["sparkLegacyProxiable"] = spark_legacy_proxiable
        if master_host is not UNSET:
            field_dict["masterHost"] = master_host
        if master_port is not UNSET:
            field_dict["masterPort"] = master_port
        if free_form_config is not UNSET:
            field_dict["freeFormConfig"] = free_form_config
        if yarn_free_form_config is not UNSET:
            field_dict["yarnFreeFormConfig"] = yarn_free_form_config
        if on_demand_free_form_config is not UNSET:
            field_dict["onDemandFreeFormConfig"] = on_demand_free_form_config
        if hostname_mappings is not UNSET:
            field_dict["hostnameMappings"] = hostname_mappings
        if hadoop_user_name is not UNSET:
            field_dict["hadoopUserName"] = hadoop_user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        spark_mode = d.pop("sparkMode")

        def _parse_spark_legacy_proxiable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        spark_legacy_proxiable = _parse_spark_legacy_proxiable(d.pop("sparkLegacyProxiable", UNSET))

        def _parse_master_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        master_host = _parse_master_host(d.pop("masterHost", UNSET))

        def _parse_master_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        master_port = _parse_master_port(d.pop("masterPort", UNSET))

        def _parse_free_form_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        free_form_config = _parse_free_form_config(d.pop("freeFormConfig", UNSET))

        def _parse_yarn_free_form_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yarn_free_form_config = _parse_yarn_free_form_config(d.pop("yarnFreeFormConfig", UNSET))

        def _parse_on_demand_free_form_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        on_demand_free_form_config = _parse_on_demand_free_form_config(d.pop("onDemandFreeFormConfig", UNSET))

        def _parse_hostname_mappings(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname_mappings = _parse_hostname_mappings(d.pop("hostnameMappings", UNSET))

        def _parse_hadoop_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hadoop_user_name = _parse_hadoop_user_name(d.pop("hadoopUserName", UNSET))

        domino_projects_api_project_spark_config = cls(
            spark_mode=spark_mode,
            spark_legacy_proxiable=spark_legacy_proxiable,
            master_host=master_host,
            master_port=master_port,
            free_form_config=free_form_config,
            yarn_free_form_config=yarn_free_form_config,
            on_demand_free_form_config=on_demand_free_form_config,
            hostname_mappings=hostname_mappings,
            hadoop_user_name=hadoop_user_name,
        )

        domino_projects_api_project_spark_config.additional_properties = d
        return domino_projects_api_project_spark_config

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
