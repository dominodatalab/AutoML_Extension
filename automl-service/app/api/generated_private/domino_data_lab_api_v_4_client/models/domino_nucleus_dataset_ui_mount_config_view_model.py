from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoNucleusDatasetUiMountConfigViewModel")


@_attrs_define
class DominoNucleusDatasetUiMountConfigViewModel:
    """
    Attributes:
        dataset_id (str):
        use_latest (bool):
        path (str):
        use_tag (None | str | Unset):
        use_id (None | str | Unset):
    """

    dataset_id: str
    use_latest: bool
    path: str
    use_tag: None | str | Unset = UNSET
    use_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        use_latest = self.use_latest

        path = self.path

        use_tag: None | str | Unset
        if isinstance(self.use_tag, Unset):
            use_tag = UNSET
        else:
            use_tag = self.use_tag

        use_id: None | str | Unset
        if isinstance(self.use_id, Unset):
            use_id = UNSET
        else:
            use_id = self.use_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "useLatest": use_latest,
                "path": path,
            }
        )
        if use_tag is not UNSET:
            field_dict["useTag"] = use_tag
        if use_id is not UNSET:
            field_dict["useId"] = use_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        use_latest = d.pop("useLatest")

        path = d.pop("path")

        def _parse_use_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        use_tag = _parse_use_tag(d.pop("useTag", UNSET))

        def _parse_use_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        use_id = _parse_use_id(d.pop("useId", UNSET))

        domino_nucleus_dataset_ui_mount_config_view_model = cls(
            dataset_id=dataset_id,
            use_latest=use_latest,
            path=path,
            use_tag=use_tag,
            use_id=use_id,
        )

        domino_nucleus_dataset_ui_mount_config_view_model.additional_properties = d
        return domino_nucleus_dataset_ui_mount_config_view_model

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
