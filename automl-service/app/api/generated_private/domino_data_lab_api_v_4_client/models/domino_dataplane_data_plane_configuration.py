from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDataplaneDataPlaneConfiguration")


@_attrs_define
class DominoDataplaneDataPlaneConfiguration:
    """
    Attributes:
        storage_class (None | str | Unset):
        address (None | str | Unset):
        file_sync_disabled (bool | None | Unset):
        domino_api_hostname (None | str | Unset):
        docker_registry_hostname (None | str | Unset):
        rabbit_mq_hostname (None | str | Unset):
        rabbit_mq_amqp_port (int | None | Unset):
        rabbit_mq_stream_port (int | None | Unset):
        istio_enabled (bool | None | Unset):
        s_3_endpoint_url (None | str | Unset):
        additional_storage_class (None | str | Unset):
    """

    storage_class: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    file_sync_disabled: bool | None | Unset = UNSET
    domino_api_hostname: None | str | Unset = UNSET
    docker_registry_hostname: None | str | Unset = UNSET
    rabbit_mq_hostname: None | str | Unset = UNSET
    rabbit_mq_amqp_port: int | None | Unset = UNSET
    rabbit_mq_stream_port: int | None | Unset = UNSET
    istio_enabled: bool | None | Unset = UNSET
    s_3_endpoint_url: None | str | Unset = UNSET
    additional_storage_class: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_class: None | str | Unset
        if isinstance(self.storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = self.storage_class

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        file_sync_disabled: bool | None | Unset
        if isinstance(self.file_sync_disabled, Unset):
            file_sync_disabled = UNSET
        else:
            file_sync_disabled = self.file_sync_disabled

        domino_api_hostname: None | str | Unset
        if isinstance(self.domino_api_hostname, Unset):
            domino_api_hostname = UNSET
        else:
            domino_api_hostname = self.domino_api_hostname

        docker_registry_hostname: None | str | Unset
        if isinstance(self.docker_registry_hostname, Unset):
            docker_registry_hostname = UNSET
        else:
            docker_registry_hostname = self.docker_registry_hostname

        rabbit_mq_hostname: None | str | Unset
        if isinstance(self.rabbit_mq_hostname, Unset):
            rabbit_mq_hostname = UNSET
        else:
            rabbit_mq_hostname = self.rabbit_mq_hostname

        rabbit_mq_amqp_port: int | None | Unset
        if isinstance(self.rabbit_mq_amqp_port, Unset):
            rabbit_mq_amqp_port = UNSET
        else:
            rabbit_mq_amqp_port = self.rabbit_mq_amqp_port

        rabbit_mq_stream_port: int | None | Unset
        if isinstance(self.rabbit_mq_stream_port, Unset):
            rabbit_mq_stream_port = UNSET
        else:
            rabbit_mq_stream_port = self.rabbit_mq_stream_port

        istio_enabled: bool | None | Unset
        if isinstance(self.istio_enabled, Unset):
            istio_enabled = UNSET
        else:
            istio_enabled = self.istio_enabled

        s_3_endpoint_url: None | str | Unset
        if isinstance(self.s_3_endpoint_url, Unset):
            s_3_endpoint_url = UNSET
        else:
            s_3_endpoint_url = self.s_3_endpoint_url

        additional_storage_class: None | str | Unset
        if isinstance(self.additional_storage_class, Unset):
            additional_storage_class = UNSET
        else:
            additional_storage_class = self.additional_storage_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if storage_class is not UNSET:
            field_dict["storageClass"] = storage_class
        if address is not UNSET:
            field_dict["address"] = address
        if file_sync_disabled is not UNSET:
            field_dict["fileSyncDisabled"] = file_sync_disabled
        if domino_api_hostname is not UNSET:
            field_dict["dominoApiHostname"] = domino_api_hostname
        if docker_registry_hostname is not UNSET:
            field_dict["dockerRegistryHostname"] = docker_registry_hostname
        if rabbit_mq_hostname is not UNSET:
            field_dict["rabbitMqHostname"] = rabbit_mq_hostname
        if rabbit_mq_amqp_port is not UNSET:
            field_dict["rabbitMqAmqpPort"] = rabbit_mq_amqp_port
        if rabbit_mq_stream_port is not UNSET:
            field_dict["rabbitMqStreamPort"] = rabbit_mq_stream_port
        if istio_enabled is not UNSET:
            field_dict["istioEnabled"] = istio_enabled
        if s_3_endpoint_url is not UNSET:
            field_dict["s3EndpointUrl"] = s_3_endpoint_url
        if additional_storage_class is not UNSET:
            field_dict["additionalStorageClass"] = additional_storage_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_storage_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_class = _parse_storage_class(d.pop("storageClass", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_file_sync_disabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        file_sync_disabled = _parse_file_sync_disabled(d.pop("fileSyncDisabled", UNSET))

        def _parse_domino_api_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domino_api_hostname = _parse_domino_api_hostname(d.pop("dominoApiHostname", UNSET))

        def _parse_docker_registry_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        docker_registry_hostname = _parse_docker_registry_hostname(d.pop("dockerRegistryHostname", UNSET))

        def _parse_rabbit_mq_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rabbit_mq_hostname = _parse_rabbit_mq_hostname(d.pop("rabbitMqHostname", UNSET))

        def _parse_rabbit_mq_amqp_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rabbit_mq_amqp_port = _parse_rabbit_mq_amqp_port(d.pop("rabbitMqAmqpPort", UNSET))

        def _parse_rabbit_mq_stream_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rabbit_mq_stream_port = _parse_rabbit_mq_stream_port(d.pop("rabbitMqStreamPort", UNSET))

        def _parse_istio_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        istio_enabled = _parse_istio_enabled(d.pop("istioEnabled", UNSET))

        def _parse_s_3_endpoint_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s_3_endpoint_url = _parse_s_3_endpoint_url(d.pop("s3EndpointUrl", UNSET))

        def _parse_additional_storage_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        additional_storage_class = _parse_additional_storage_class(d.pop("additionalStorageClass", UNSET))

        domino_dataplane_data_plane_configuration = cls(
            storage_class=storage_class,
            address=address,
            file_sync_disabled=file_sync_disabled,
            domino_api_hostname=domino_api_hostname,
            docker_registry_hostname=docker_registry_hostname,
            rabbit_mq_hostname=rabbit_mq_hostname,
            rabbit_mq_amqp_port=rabbit_mq_amqp_port,
            rabbit_mq_stream_port=rabbit_mq_stream_port,
            istio_enabled=istio_enabled,
            s_3_endpoint_url=s_3_endpoint_url,
            additional_storage_class=additional_storage_class,
        )

        domino_dataplane_data_plane_configuration.additional_properties = d
        return domino_dataplane_data_plane_configuration

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
