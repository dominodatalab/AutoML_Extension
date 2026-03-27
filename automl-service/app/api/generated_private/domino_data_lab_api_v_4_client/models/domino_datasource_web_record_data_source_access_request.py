from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasource_web_record_data_source_access_request_extra_info_type_0 import (
        DominoDatasourceWebRecordDataSourceAccessRequestExtraInfoType0,
    )


T = TypeVar("T", bound="DominoDatasourceWebRecordDataSourceAccessRequest")


@_attrs_define
class DominoDatasourceWebRecordDataSourceAccessRequest:
    """
    Attributes:
        client_source (None | str | Unset):
        data_plane_id (None | str | Unset):
        run_id (None | str | Unset):
        user_name (None | str | Unset):
        extra_info (DominoDatasourceWebRecordDataSourceAccessRequestExtraInfoType0 | None | Unset):
    """

    client_source: None | str | Unset = UNSET
    data_plane_id: None | str | Unset = UNSET
    run_id: None | str | Unset = UNSET
    user_name: None | str | Unset = UNSET
    extra_info: DominoDatasourceWebRecordDataSourceAccessRequestExtraInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_datasource_web_record_data_source_access_request_extra_info_type_0 import (
            DominoDatasourceWebRecordDataSourceAccessRequestExtraInfoType0,
        )

        client_source: None | str | Unset
        if isinstance(self.client_source, Unset):
            client_source = UNSET
        else:
            client_source = self.client_source

        data_plane_id: None | str | Unset
        if isinstance(self.data_plane_id, Unset):
            data_plane_id = UNSET
        else:
            data_plane_id = self.data_plane_id

        run_id: None | str | Unset
        if isinstance(self.run_id, Unset):
            run_id = UNSET
        else:
            run_id = self.run_id

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        extra_info: dict[str, Any] | None | Unset
        if isinstance(self.extra_info, Unset):
            extra_info = UNSET
        elif isinstance(self.extra_info, DominoDatasourceWebRecordDataSourceAccessRequestExtraInfoType0):
            extra_info = self.extra_info.to_dict()
        else:
            extra_info = self.extra_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_source is not UNSET:
            field_dict["clientSource"] = client_source
        if data_plane_id is not UNSET:
            field_dict["dataPlaneId"] = data_plane_id
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if extra_info is not UNSET:
            field_dict["extraInfo"] = extra_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_web_record_data_source_access_request_extra_info_type_0 import (
            DominoDatasourceWebRecordDataSourceAccessRequestExtraInfoType0,
        )

        d = dict(src_dict)

        def _parse_client_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_source = _parse_client_source(d.pop("clientSource", UNSET))

        def _parse_data_plane_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_plane_id = _parse_data_plane_id(d.pop("dataPlaneId", UNSET))

        def _parse_run_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_id = _parse_run_id(d.pop("runId", UNSET))

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_extra_info(
            data: object,
        ) -> DominoDatasourceWebRecordDataSourceAccessRequestExtraInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_info_type_0 = DominoDatasourceWebRecordDataSourceAccessRequestExtraInfoType0.from_dict(data)

                return extra_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoDatasourceWebRecordDataSourceAccessRequestExtraInfoType0 | None | Unset, data)

        extra_info = _parse_extra_info(d.pop("extraInfo", UNSET))

        domino_datasource_web_record_data_source_access_request = cls(
            client_source=client_source,
            data_plane_id=data_plane_id,
            run_id=run_id,
            user_name=user_name,
            extra_info=extra_info,
        )

        domino_datasource_web_record_data_source_access_request.additional_properties = d
        return domino_datasource_web_record_data_source_access_request

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
